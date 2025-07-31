
PROJECT(main2d)

CMAKE_MINIMUM_REQUIRED(VERSION 3.15.0)

SET(IBAMR_ROOT /home/michael/software/IBAMR/debug-implicit-boyce)

# change the path of the executable 
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR})

# List your source files here - this example has just one.
SET(SOURCE_FILES CartGridBodyForce.cpp  ForceProjector.cpp  Kinematics.cpp  main.cpp)
ADD_EXECUTABLE(${PROJECT_NAME} ${SOURCE_FILES})

FIND_PACKAGE(IBAMR 0.13.0 REQUIRED)
TARGET_LINK_LIBRARIES(${PROJECT_NAME} IBAMR::IBAMR2d)
# IBAMR saves the flags it used to compile - you can reuse them if you want to
SET(CMAKE_CXX_FLAGS ${IBAMR_CXX_FLAGS})


# SET(IBAMR_DIR $HOME/software/IBAMR/debug-implicit-boyce)

SET(CMAKE_BUILD_TYPE "Debug")
# SET(CMAKE_LIBRARY_PATH /home/michael/software/IBAMR/lib)



# Compile IBAMR
cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=$HOME/autoibamr/packages/ibamr-0.13.0 \
  -DBOOST_ROOT=$HOME/autoibamr/packages/boost_1_83_0 \
  -DPETSC_ROOT=/home/michael/autoibamr/packages/petsc-3.17.5 \
  -DMPI_ROOT=/usr/bin \
  -DHYPRE_ROOT=/home/michael/autoibamr/packages/petsc-3.17.5 \
  -DSAMRAI_ROOT=/home/michael/autoibamr/packages/SAMRAI-2.4.4 \
  -DHDF5_ROOT=/home/michael/autoibamr/packages/hdf5-1.12.2 \
  -DSILO_ROOTi=/home/michael/autoibamr/packages/silo-4.11-bsd \
  -DLIBMESH_ROOT=/home/michael/autoibamr/packages/libmesh-1.6.2 \
  -DLIBMESH_METHOD=OPT \
  ../
make -j4

# Compile log
[] July 30, 2025: autoibamr compile on longleaf (mpi version rhel8 -> rhel9: /nas/longleaf/rhel9/apps/openmpi/5.0.6/gcc12/bin/mpicc)

  ```
  pwd
  /nas/longleaf/home/llianxia/autoibamr
  ls packages
  cmake-3.30.6  exodusii-2024-04-03  hdf5-1.12.2  IBAMR-0.16.0  IBSAMRAI2-2025.01.09  libmesh-1.7.8  netcdf-c-4.9.2  numdiff-5.9.0  petsc-3.23.3  silo-4.11-bsd
```
[] July 30, 2025: IBAMR v16.0 compile on longleaf (mpi version rhel8 -> rhel9: /nas/longleaf/rhel9/apps/openmpi/5.0.6/gcc12/bin/mpicc)
```
pwd
/nas/longleaf/home/llianxia/IBAMR/v16.0
vi build/michael_build.sh
export PETSC_DIR=/nas/longleaf/home/llianxia/autoibamr/packages/petsc-3.23.3
cmake \
  -DCMAKE_BUILD_TYPE=Release  \
  -DCMAKE_C_COMPILER="$(which mpicc)" \
  -DCMAKE_CXX_COMPILER="$(which mpicxx)" \
  -DCMAKE_Fortran_COMPILER="$(which mpif90)" \
  -DSAMRAI_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/IBSAMRAI2-2025.01.09 \
  -DLIBMESH_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/libmesh-1.7.8 \
  -DLIBMESH_METHOD=OPT \
  -DPETSC_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/petsc-3.23.3 \
  -DHDF5_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/hdf5-1.12.2  \
  -DSILO_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/silo-4.11-bsd  \
  -DHYPRE_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/petsc-3.23.3 \
  -DCMAKE_INSTALL_PREFIX=/nas/longleaf/home/llianxia/IIM/build \
  -DIBAMR_FORCE_BUNDLED_BOOST=ON \
  -DIBAMR_FORCE_BUNDLED_EIGEN3=ON \
  -DIBAMR_FORCE_BUNDLED_MUPARSER=ON \
  ../
make
```
[] July 30, 2025: IIM compile on longleaf (replaced IIMMethod.cpp/h from IBMAMR_QI) (mpi version rhel8 -> rhel9: /nas/longleaf/rhel9/apps/openmpi/5.0.6/gcc12/bin/mpicc)
```
pwd
/nas/longleaf/home/llianxia/IIM/IBAMR
vi build/michael_build.sh

export PETSC_DIR=/nas/longleaf/home/llianxia/autoibamr/packages/petsc-3.21.2
cmake \
  -DCMAKE_BUILD_TYPE=Release  \
  -DCMAKE_C_COMPILER="$(which mpicc)" \
  -DCMAKE_CXX_COMPILER="$(which mpicxx)" \
  -DCMAKE_Fortran_COMPILER="$(which mpif90)" \
  -DSAMRAI_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/IBSAMRAI2-2025.01.09 \
  -DLIBMESH_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/libmesh-1.7.8 \
  -DLIBMESH_METHOD=OPT \
  -DPETSC_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/petsc-3.23.3 \
  -DHDF5_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/hdf5-1.12.2  \
  -DSILO_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/silo-4.11-bsd  \
  -DHYPRE_ROOT=/nas/longleaf/home/llianxia/autoibamr/packages/petsc-3.23.3 \
  -DCMAKE_INSTALL_PREFIX=/nas/longleaf/home/llianxia/IIM/build \
  -DIBAMR_FORCE_BUNDLED_BOOST=ON \
  -DIBAMR_FORCE_BUNDLED_EIGEN3=ON \
  -DIBAMR_FORCE_BUNDLED_MUPARSER=ON \
  ../
make
```

