import numpy as np
import matplotlib.pyplot as plt
from stl import mesh
from stl import stl
import glob
import re
from pathlib import Path

import scienceplots
plt.style.use(["science"])

# convert from m to mm
scale = 0.001 
stl_files = glob.glob('../crossSectionData/STL/Section*.stl')

print(stl_files)
# sort file name numerically, 1,2,3,...,11,12,...
stl_files = sorted(stl_files, key=lambda x:float(re.findall("(\d+)",x)[0]))

section_sample_file = open(r"120/system/sampledata.txt", "w")
section_average_file = open(r"120/system/section_average_dict.txt", "w")

centerline_file = '../crossSectionData/section_data.txt'
centerline_data = np.loadtxt(centerline_file, skiprows=1)

cx = centerline_data[:,1]*scale
cy = centerline_data[:,2]*scale
cz = centerline_data[:,3]*scale
nx = centerline_data[:,4]
ny = centerline_data[:,5]
nz = centerline_data[:,6]
area = centerline_data[:,7] 
diameter = centerline_data[:,8] 

d = np.zeros(len(cx))  
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


for i, file in enumerate(stl_files):
    print(file)
    # your_mesh = mesh.Mesh.from_file(file)
    # unit_normals = your_mesh.get_unit_normals()
    # The normal calculated by this tool has small numbers, we use the orginal normal vector 
    # your_mesh.normals = unit_normals
    # convert to ASCII format, note that the STL is not scaled.
    fname = Path(file).stem
    # In slicer 3d, when saving stl, do not select compress, then it will be in ASCII
    # your_mesh.save(file, mode=stl.ASCII, update_normals =False)

    if (i==0):
        d[i]=0
    else:
        dx = cx[i]-cx[i-1]
        dy = cy[i]-cy[i-1]
        dz = cz[i]-cz[i-1]
        d[i] = d[i-1] + np.sqrt(dx*dx + dy*dy + dz*dz)
 
    # dump sampleDict for OpenFOAM
    section_sample_file.write(f"{fname}\n")
    section_sample_file.write("{\n")
    section_sample_file.write("\ttype\tplane;\n")
    section_sample_file.write(f"\tpoint\t({cx[i]}\t{cy[i]}\t{cz[i]});\n")
    section_sample_file.write(f"\tnormal\t({nx[i]}\t{ny[i]}\t{nz[i]});\n")
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
    section_average_file.write(f"\t\tpoint\t({cx[i]}\t{cy[i]}\t{cz[i]});\n")
    section_average_file.write(f"\t\tnormal\t({nz[i]}\t{ny[i]}\t{nz[i]});\n")
    section_average_file.write("\t\tinterpolate\ttrue;\n")
    section_average_file.write("\t}\n")
    section_average_file.write("}\n")

    section_average_file.write("\n")


section_sample_file.close()
section_average_file.close()


print("itme\tmin\tmax\taverage")
print(f"diameter\t{np.min(diameter)}\t{np.max(diameter)}\t{np.average(diameter)}\t")
print(f"area\t{np.min(area)}\t{np.max(area)}\t{np.average(area)}\t")

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
d = d/scale # m to mm
d = d*(-1) + (d[-1] + d[0]) # transform from [0, 1] to [1, 0]
ax1.plot(d, diameter, "r-", label = "Diameter")
ax2.plot(d, area, 'b--', label = "Area")

ax1.set_xlabel(r"Distance (mm)")
ax1.set_ylabel(r"Diamater (mm)")
ax2.set_ylabel(r"Area (mm$^2$)")
plt.tight_layout()
fig.legend(bbox_to_anchor=(0.6,0.95), ncol=1) # Note: fig, not plt, otherwise only show the last one
# fig.legend(loc='best') # Automatic legend placement (loc='best') not implemented for figure legend
plt.show()


