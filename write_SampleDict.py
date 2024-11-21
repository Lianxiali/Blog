#region import packages
import numpy as np
import glob
import sys
import re
from pathlib import Path


#endregion

#----------------------------------------------------------------------------
#region read centerline information and get distance
## Need to remesh these sections (STL) in meshmixer
stl_files = glob.glob('../cross_section_data/STL/Section*.stl')
# sort file name numerically, 1,2,3,...,11,12,...
stl_files = sorted(stl_files, key=lambda x:float(re.findall("(\d+)",x)[0]))
n_sections = len(stl_files)

centerline_file = '../cross_section_data/section_data.txt'
centerline_data = np.loadtxt(centerline_file, skiprows=1)

# convert from mm to m
scale = 0.001 
d = centerline_data[:,1]
cx = centerline_data[:,2]*scale
cy = centerline_data[:,3]*scale
cz = centerline_data[:,4]*scale
nx = centerline_data[:,5]
ny = centerline_data[:,6]
nz = centerline_data[:,7]

# transform from [0, 1] to [1, 0] switch the start section from the outflow to the inflow
d = d*(-1) + (d[-1] + d[0]) 
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
#endregion

#----------------------------------------------------------------------------
#region dump sampleDict for OpenFOAM
casename = "/not_backed_up/lianxia/simulation/openfoam_run/KIDNEY/AVF/MediumMesh/D21C1"
section_sample_file = open(f"{casename}/system/sampleSurfaceDict", "w")

str ="""
type surfaces;
setFormat raw;
surfaceFormat vtk;
interpolationScheme cellPointFace;
fields (p U);
operation       areaAverage;

surfaces
{
"""
section_sample_file.write(str)

# for i in range(n_sections):
#     fname = Path(stl_files[i]).stem

for file in stl_files:
    p = Path(file)
    fname = p.stem  # STL files must be in constant\triSurface folder
    section_sample_file.write(f"\t{fname}\n")
    section_sample_file.write("\t{\n")
    # section_sample_file.write("\t\ttype\tplane;\n")
    # section_sample_file.write(f"\t\tpoint\t({cx[i]}\t{cy[i]}\t{cz[i]});\n")
    # section_sample_file.write(f"\t\tnormal\t({nx[i]}\t{ny[i]}\t{nz[i]});\n")
    section_sample_file.write("\t\t type    \t sampledTriSurfaceMesh;\n")    
    section_sample_file.write(f"\t\tsurface \t {p.name};\n") 
    section_sample_file.write("\t\t source\t cells;\n")   
    section_sample_file.write("\t\tinterpolate\ttrue;\n")
    section_sample_file.write("\t}\n")

    section_sample_file.write("\n")

section_sample_file.write("}\n")

section_sample_file.close()
#endregion 

#----------------------------------------------------------------------------
#region dump sectionAverageFuncDict for OpenFOAM

section_average_file = open(f"{casename}/system/sectionAverageFuncDict", "w")
header ="""
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      sectionAverageFuncDict;
}\n\n"""
section_average_file.write(header)
section_average_file.write("functions\n{\n")

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
	enabled         true;
	regionType      sampledSurface;
"""

# for i in range(n_sections):
#     fname = Path(stl_files[i]).stem
for file in stl_files: 
    p = Path(file)
    fname = p.stem  # STL files must be in constant\triSurface folder
    section_average_file.write(f"{fname}_average\n")
    section_average_file.write("{")
    section_average_file.write(str)    
    section_average_file.write(f"\tname            {fname};\n")
    section_average_file.write("\tsampledSurfaceDict\n")
    section_average_file.write("\t{\n")
    # section_average_file.write("\t\ttype\tplane;\n")
    # section_average_file.write(f"\t\tpoint\t({cx[i]}\t{cy[i]}\t{cz[i]});\n")
    # section_average_file.write(f"\t\tnormal\t({nx[i]}\t{ny[i]}\t{nz[i]});\n")
    section_average_file.write("\t\ttype    \t sampledTriSurfaceMesh;\n")    
    section_average_file.write(f"\t\tsurface \t {p.name};\n") 
    section_average_file.write("\t\t source\t cells;\n")

    section_average_file.write("\t\tinterpolate\ttrue;\n")
    section_average_file.write("\t}\n")
    section_average_file.write("}\n")

    section_average_file.write("\n")
section_average_file.write("}\n")
section_average_file.close()
#endregion 




