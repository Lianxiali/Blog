The Slice Along PolyLine filter is similar to the Slice Filter except that it slices along a surface 
that is defined by sweeping the input polyline parallel to the z-axis. 
Explained another way: take a laser cutter and move it so that it hits every point on the input polyline while keeping it parallel to the z-axis. 
The surface cut from the input dataset is the result.

**The key is to create a polyline from a point set.**

If the number of points is small, you can use the filter Polyline source to input the coordinates manually, otherwise use csv file to import the points.

1. Create a .csv file of the XYZ points that defines the curve
2. Import .csv file into Paraview
3. Apply Filter "Table to Points" to the .csv file
4. Create a polyline of the points: Apply Filter "Programmable Filter".

Code: https://www.youtube.com/watch?v=uhyWkb2decA
```
output.Points = inputs[0].Points
numPoints = len(output.Points)

pointIds = vtk.vtkIdList()
pointIds.SetNumberOfIds(numPoints)
for i in range(numPoints):
    pointIds.SetId(i, i)

output.Allocate(1, 1)
output.InsertNextCell(vtk.VTK_POLY_LINE, pointIds)
```
5. Then use Filter "Slice Along Polyline" using the newly created polyline from step 4.


**Plot over point set**

https://www.paraview.org/pipermail/paraview/2016-October/038277.html
1. Load your CFD results as normal.
2. Load your x,y,z dataset with the appropriate settings, demiliter,
header, etc.
3. Use the Table to Points filter on the x,y,z dataset, again selecting the
correct fields for the x, y and z data.
4. Select your CFD dataset and choose the Resample with Dataset filter.
    - The CFD dataset will be the Input and the Table to Points will the
Input
    - Now your data should be extracted at the selected points.
5. To plot the data, use the Plot Data filter.  You may need to first run a
Calculator filter to extract a coordinate component (x, y, or z) if you
want to use that as the abscissa.
