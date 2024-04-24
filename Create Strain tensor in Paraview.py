#from paraview.vtk.numpy_interface import dataset_adapter as dsa
#from paraview.vtk.numpy_interface import algorithms as algs
#import numpy
# Need to merge block filter first for multiblock (exodus file)
# programmerable filter
# FF gradient of displacement

xx = inputs[0].PointData['FF'][:,0,0]
xy = inputs[0].PointData['FF'][:,1,0]
xz = inputs[0].PointData['FF'][:,2,0]
yx = inputs[0].PointData['FF'][:,0,1]
yy = inputs[0].PointData['FF'][:,1,1]
yz = inputs[0].PointData['FF'][:,2,1]
zx = inputs[0].PointData['FF'][:,0,2]
zy = inputs[0].PointData['FF'][:,1,2]
zz = inputs[0].PointData['FF'][:,2,2]

data = numpy.zeros((inputs[0].PointData["U_0"].size, 9))
data[:,0] = 0.5*(xx+xx) + 0.5*(xx*xx + yx*yx + zx*zx)
data[:,1] = 0.5*(xy+yx) + 0.5*(xx*xy + yx*yy + zx*zy)
data[:,2] = 0.5*(xz+zx) + 0.5*(xx*xz + yx*yz + zx*zz)

data[:,3] = 0.5*(yx+xy) + 0.5*(xy*xx + yy*yx + zy*zx)
data[:,4] = 0.5*(yy+yy) + 0.5*(xy*xy + yy*yy + zy*zy)
data[:,5] = 0.5*(yz+zy) + 0.5*(xy*xz + yy*yz + zy*zz)

data[:,6] = 0.5*(zx+xz) + 0.5*(xz*xx + yz*yx + zz*zx)
data[:,7] = 0.5*(zy+yz) + 0.5*(xz*xy + yz*yy + zz*zy)
data[:,8] = 0.5*(zz+zz) + 0.5*(xz*xz + yz*yz + zz*zz)
output.PointData.append(data, "strain")
