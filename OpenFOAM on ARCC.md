# Folder: project/turbmodel/OpenFOAM/arcc/OpenFOAM-v2306
[lli16@blog1 /project/turbmodel/OpenFOAM/arcc/OpenFOAM-v2306]$salloc -A turbmodel -t 12:00:00 --exclusive

# Notice, also loading: boost/1.80.0 fftw/3.3.10-ompi

  [lli16@t461 /project/turbmodel/OpenFOAM/arcc/OpenFOAM-v2306]$module load gcc/12.2.0 openmpi/4.1.4 boost/1.80.0 fftw/3.3.10-ompi
  [lli16@t461 /project/turbmodel/OpenFOAM/arcc/OpenFOAM-v2306]$source etc/bashrc
  No completions for /project/turbmodel/OpenFOAM/arcc/OpenFOAM-v2306/platforms/linux64GccDPInt32Opt/bin
  [ignore if OpenFOAM is not yet compiled]
  
  [lli16@t461 /project/turbmodel/OpenFOAM/arcc/OpenFOAM-v2306]$./Allwmake -l -j
  Logging wmake -all output to 'log.linux64GccDPInt32Opt'

    Compiling enabled on 32 cores
    gcc=/apps/u/spack/gcc/8.5.0/gcc/12.2.0-orvuxnl/bin/gcc
    clang=
    mpirun=/apps/u/opt/gcc/12.2.0/openmpi/4.1.4/bin/mpirun
    make=/usr/bin/make
    cmake=/usr/bin/cmake
    wmake=/project/turbmodel/OpenFOAM/arcc/OpenFOAM-v2306/wmake/wmake
    m4=/usr/bin/m4
    flex=/usr/bin/flex
    compiler=/apps/u/spack/gcc/8.5.0/gcc/12.2.0-orvuxnl/bin/g++
    g++ (Spack GCC) 12.2.0
    ========================================
    2023-12-12 09:05:06 -0700
    Starting compile OpenFOAM-v2306 Allwmake
      Gcc system compiler []
      linux64GccDPInt32Opt, with SYSTEMOPENMPI sys-openmpi
    ========================================
    gcc -m64 -DOPENFOAM=2306 -DWM_DP -DWM_LABEL_SIZE=32 -Wall -O3    -fPIC lemon.c -o /project/turbmodel/OpenFOAM/arcc/OpenFOAM-v2306/platforms/tools/linux64Gcc/lemon
    g++ -std=c++11 -m64 -pthread -DOPENFOAM=2306 -DWM_DP -DWM_LABEL_SIZE=32 -Wall -Wextra -Wold-style-cast -Wnon-virtual-dtor -Wno-unused-parameter -Wno-invalid-offsetof -Wno-attributes -Wno-unknown-pragmas -O3  -DNoRepository -ftemplate-depth-100   -fPIC wmkdepend.cc -o /project/turbmodel/OpenFOAM/arcc/OpenFOAM-v2306/platforms/tools/linux64Gcc/wmkdepend
    ...
    2023-12-12 10:43:06 -0700
    ========================================
    Finished compile of visualization with OpenFOAM-v2306
      Gcc system compiler
      linux64GccDPInt32Opt, with SYSTEMOPENMPI sys-openmpi

    2023-12-12 10:43:06 -0700
    ========================================
      OpenFOAM-v2306
      Gcc system compiler
      linux64GccDPInt32Opt, with SYSTEMOPENMPI sys-openmpi
      api = 2306
      patch = 0
      bin = 316 entries
      lib = 154 entries
========================================
Done logging to 'log.linux64GccDPInt32Opt'
