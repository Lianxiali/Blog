
# file name: paraview.samrai.series

## windows: use \\ for path

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
