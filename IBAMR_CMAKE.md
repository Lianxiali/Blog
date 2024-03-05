
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
