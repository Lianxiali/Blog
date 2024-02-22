1. https://www.openfoam.com/documentation/guides/latest/api/classFoam_1_1functionObjects_1_1timeActivatedFileUpdate.html#details
2. Performs a file copy/replacement once a specified time has been reached.


Usage
Example usage to update the fvSolution dictionary at various times throughout the calculation:
```
fileUpdate1
{
    type              timeActivatedFileUpdate;
    libs              (utilityFunctionObjects);
    writeControl      timeStep;
    writeInterval     1;
    fileToUpdate      "<system>/fvSolution";
    timeVsFile
    (
        (-1   "<system>/fvSolution.0")
        (0.10 "<system>/fvSolution.10")
        (0.20 "<system>/fvSolution.20")
        (0.35 "<system>/fvSolution.35")
    );
    ...
}
```

2. Use systemCall to update file on-the-fly
https://www.cfd-online.com/Forums/openfoam/217350-write-data-specific-times-not-intervals.html
https://openfoamwiki.net/index.php/Tip_Function_Object_systemCall
```
functions
{
  writeCalls
  (
    type systemCall;
    functionObjectLibs ( "libsystemCall.so" );
    executeCalls 2("echo Execute system call before time iteration is done" "cp system/newControlDict system/controlDict");
    endCalls 1("echo Finishing up with a system call, which is seems to be before the write call...");
    writeCalls 2("echo Writing to file call" "ls -l");
    outputControl outputTime;  
  );
}
```
3. Use coded functionObject
   https://www.cfd-online.com/Forums/openfoam-programming-development/238065-table-format-writeinterval-controldict.html#post810828
```
/*--------------------------------*- C++ -*----------------------------------*\
  | =========                 |                                                 |
  | \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
  |  \\    /   O peration     | Version:  v2006                                 |
  |   \\  /    A nd           | Website:  www.openfoam.com                      |
  |    \\/     M anipulation  |                                                 |
  \*---------------------------------------------------------------------------*/
  FoamFile
  {
      version     2.0;
      format      ascii;
      class       dictionary;
      location    "system";
      object      controlDict;
  }
  // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

  application     simpleFoam;

  startFrom       startTime;

  startTime       0;

  stopAt          endTime;

  endTime         2000;

  deltaT          1;

  writeControl    timeStep;

  writeInterval   100000; // <------ big number

  purgeWrite      0;

  writeFormat     ascii;

  writePrecision  6;

  writeCompression off;

  timeFormat      general;

  timePrecision   6;

  runTimeModifiable true;

  functions
  {
      userWriteInterval
      {
          type coded;
          libs            ("libutilityFunctionObjects.so");
          name writeInterval;

          code
          #{
          #};

          codeExecute
          #{
              const Time& runTime = mesh().time();
              scalar myWriteInterval(1);

              // better logic here:
              // for example with a function1
              if (runTime.value() > 10)
              {
                  myWriteInterval = 10;
              }
              if (runTime.value() > 50)
              {
                  myWriteInterval = 50;
              }

              if (!(runTime.timeIndex() % label(myWriteInterval)))
              {
                  const_cast<Time&>(runTime).writeNow();
              }
          #};
      }

  }
```
