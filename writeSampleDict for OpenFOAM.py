import numpy
from stl import mesh
from stl import stl
import glob
import re
from pathlib import Path

# convert from m to mm
scale = 0.001 
files = glob.glob('../crossSectionSTL/Section*.stl')
print(files)
# sort file name numerically, 1,2,3,...,11,12,...
files = sorted(files, key=lambda x:float(re.findall("(\d+)",x)[0]))

section_sample_file = open(r"120/system/sampledata.txt", "w")
section_average_file = open(r"120/system/section_average_dict.txt", "w")

str = """
    type            surfaceFieldValue;
    libs            (fieldFunctionObjects);
    log             on;
    enabled         true;

    writeControl    timeStep;
    writeInterval   1;

    writeFields     false;
    surfaceFormat   raw;

    operation       areaAverage;
    fields          ( p U );
    // writeArea       true;

    // resetOnStartUp  true;
    // resetOnOutput   false;
    // periodicRestart true;
    // restartPeriod   0.0005;
"""


for file in files:
    print(file)
    your_mesh = mesh.Mesh.from_file(file)
    unit_normals = your_mesh.get_unit_normals()
    # The normal calculated by this tool has small numbers, we use the orginal normal vector 
    your_mesh.normals = unit_normals
    # convert to ASCII format, note that the STL is not scaled.
    fname = Path(file).stem
    # In slicer 3d, when saving stl, do not select compress, then it will be in ASCII
    # your_mesh.save(file, mode=stl.ASCII, update_normals =False)

    # dump sampleDict for OpenFOAM
    section_sample_file.write(f"{fname}\n")
    section_sample_file.write("{\n")
    section_sample_file.write("\ttype\tplane;\n")
    section_sample_file.write(f"\tpoint\t({your_mesh.v0[0][0]*scale}\t{your_mesh.v0[0][1]*scale}\t{your_mesh.v0[0][2]*scale});\n")
    section_sample_file.write(f"\tnormal\t({unit_normals[0][0]}\t{unit_normals[0][1]}\t{unit_normals[0][2]});\n")
    section_sample_file.write("\tinterpolate\ttrue;\n")
    section_sample_file.write("}\n")

    section_sample_file.write("\n")

    
    section_average_file.write(f"{fname}_average\n")
    section_average_file.write("{\n")
    section_average_file.write(str)
    section_average_file.write("\tenabled         true;\n")
    section_average_file.write("\tregionType      sampledSurface;\n")
    section_average_file.write(f"\tname            {fname};\n")
    section_average_file.write("\tsampledSurfaceDict\n")
    section_average_file.write("\t{\n")
    section_average_file.write("\t\ttype\tplane;\n")
    section_average_file.write(f"\t\tpoint\t({your_mesh.v0[0][0]*scale}\t{your_mesh.v0[0][1]*scale}\t{your_mesh.v0[0][2]*scale});\n")
    section_average_file.write(f"\t\tnormal\t({unit_normals[0][0]}\t{unit_normals[0][1]}\t{unit_normals[0][2]});\n")
    section_average_file.write("\t\tinterpolate\ttrue;\n")
    section_average_file.write("\t}\n")
    section_average_file.write("}\n")

    section_average_file.write("\n")


section_sample_file.close()
section_average_file.close()



