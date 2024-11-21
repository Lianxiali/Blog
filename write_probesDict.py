import numpy as np
import sys

# convert from mm to m
scale = 0.001 

casename = "/not_backed_up/lianxia/simulation/openfoam_run/KIDNEY/AVF/MediumMesh/D21C1"
section_probe_file = open(f"{casename}/system/probes", "w")

centerline_file = '../cross_section_data/section_data.txt'
centerline_data = np.loadtxt(centerline_file, skiprows=1)

cx = centerline_data[:,2]*scale
cy = centerline_data[:,3]*scale
cz = centerline_data[:,4]*scale

str = """
probes
{
    type            probes;
    libs            (sampling);

    // Name of the directory for probe data
    name            probes;

    // Write at same frequency as fields
    writeControl    outputTime;
    writeInterval   1;
    setFormat raw;
    surfaceFormat raw;

    // Fields to be probed
    fields          (U "p.*");

    // Optional: do not recalculate cells if mesh moves
    // Only cell interpolation can be applied when not using fixedLocations. 
    // InterpolationScheme entry will be ignored
    fixedLocations  true;

    // Optional: interpolation scheme to use (default is cell)
    interpolationScheme cellPoint;

    probeLocations
    (
"""
section_probe_file.write(str)
for x, y, z in zip(cx, cy, cz):
        section_probe_file.write(f"\t\t({x}\t{y}\t{z})\n")

section_probe_file.write("\t);\n")
section_probe_file.write("\t// Optional: filter out points that haven't been found. Default")
section_probe_file.write("\tis to include them (with value -VGREAT)\n")
section_probe_file.write("\tincludeOutOfBounds  true;\n")
section_probe_file.write("}\n")

section_probe_file.close()




