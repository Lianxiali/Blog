
# file name: paraview.samrai.series

## windows: use double slash \\\ for path

  {
    "file-series-version" : "1.0",
    "files" : [
      { "name" : "viz_IB2d\\visit_dump.00000\\summary.samrai", "time" : 0 },
      { "name" : "viz_IB2d\\visit_dump.00001\\summary.samrai", "time" : 2 },
    ]
  }

## linux: use / for path
 
  {
    "file-series-version" : "1.0",
    "files" : [
      { "name" : "viz_IB2d/visit_dump.00000/summary.samrai", "time" : 0 },
      { "name" : "viz_IB2d/visit_dump.00200/summary.samrai", "time" : 2 },
      { "name" : "viz_IB2d/visit_dump.00400/summary.samrai", "time" : 4 },
      { "name" : "viz_IB2d/visit_dump.00600/summary.samrai", "time" : 6 },
      { "name" : "viz_IB2d/visit_dump.00800/summary.samrai", "time" : 8 },
      { "name" : "viz_IB2d/visit_dump.01000/summary.samrai", "time" : 10 },
    ]
  }

# Python code
```
import os
import glob
import re

# Define variables
case = "viz_IB_3"  # Base folder name
viz_path = f"./{case}/visit*/"  # Data folder path
out_file_name = f"./{case}/paraview.samrai.series"  # Output file name

# Initialize data arrays
arrfolder = []  # Array to store folder names

# Get folder names from VizPath
arrfolder = glob.glob(viz_path)

# Check if the output file already exists and delete it
if os.path.isfile(out_file_name):
    os.remove(out_file_name)

# Sort the folders in natural order
arrfolder.sort(key=lambda x: [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', x)])

# Write the JSON content to the output file
with open(out_file_name, 'w') as outfile:
    outfile.write("{\n")
    outfile.write('  "file-series-version" : "1.0",\n')
    outfile.write('  "files" : [\n')

    count = 0  # Counter for time steps
    for i in arrfolder:
        # Reformat the folder name and replace '/' with '\\'
        var = '\\\\'.join(re.split(r'/', os.path.normpath(i))[-2:])
        print(var)  # Debug print to check the reformatted path
        
        # Create the file path string
        var2 = f"{var}summary.samrai"
        # Write the entry to the JSON series file
        outfile.write(f'    {{ "name" : "{case}\\\\{var2}", "time" : {count} }},\n')
        count += 1

    # Close the JSON structure
    outfile.write("  ]\n")
    outfile.write("}\n")

```
