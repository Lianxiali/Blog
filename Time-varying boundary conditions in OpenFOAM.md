Excerpted from https://doc.cfd.direct/openfoam/user-guide-v9/boundaries

There are several boundary conditions for which some input parameters are speciﬁed by a function of time (using Function1 functionality) class. They can be searched by the following command.

    find $FOAM_SRC/finiteVolume/fields/fvPatchFields -type f -name "*.H" |\
        xargs grep -l Function1 | xargs dirname | sort
They include conditions such as uniformFixedValue, which is a ﬁxedValue condition which applies a single value which is a function of time through a uniformValue keyword entry.
The Function1 is speciﬁed by a keyword following the uniformValue entry, followed by parameters that relate to the particular function. The Function1 options are list below.

constant: constant value.
table: inline list of (time value) pairs; interpolates values linearly between times.
tableFile: as above, but with data supplied in a separate ﬁle.
square: square-wave function.
squarePulse: single square pulse.
sine: sine function.
one and zero: constant one and zero values.
polynomial: polynomial function using a list (coeff exponent) pairs.
coded: function speciﬁed by user coding.
scale: scales a given value function by a scalar scale function; both entries can be themselves Function1; scale function is often a ramp function (below), with value controlling the ramp value.
linearRamp, quadraticRamp, halfCosineRamp, quarterCosineRamp and quarterSineRamp: monotonic ramp functions which ramp from 0 to 1 over speciﬁed duration.
reverseRamp: reverses the values of a ramp function, e.g. from 1 to 0.
Examples or a time-varying inlet for a scalar are shown below.
```
inlet
{
    type         uniformFixedValue;
    uniformValue constant 2;
}

inlet
{
    type         uniformFixedValue;
    uniformValue table ((0 0) (10 2));
}

inlet
{
    type         uniformFixedValue;
    uniformValue polynomial ((1 0) (2 2)); // = 1*t^0 + 2*t^2
}

inlet
{
    type         uniformFixedValue;
    uniformValue
    {
        type             tableFile;
        format           csv;
        nHeaderLine      4;              // number of header lines
        refColumn        0;              // time column index
        componentColumns (1);            // data column index
        separator        ",";            // optional (defaults to ",")
        mergeSeparators  no;             // merge multiple separators
        file             "dataTable.csv";
   }
}

inlet
{
    type         uniformFixedValue;
    uniformValue
    {
        type             square;
        frequency        10;
        amplitude        1;
        scale            2;  // Scale factor for wave
        level            1;  // Offset
    }
}

inlet
{
    type         uniformFixedValue;
    uniformValue
    {
        type             sine;
        frequency        10;
        amplitude        1;
        scale            2;  // Scale factor for wave
        level            1;  // Offset
    }
}

input  // ramp from 0 -> 2, from t = 0 -> 0.4
{
    type         uniformFixedValue;
    uniformValue
    {
        type             scale;
        scale            linearRamp;
        start            0;
        duration         0.4;
        value            2;
    }
}

input  // ramp from 2 -> 0, from t = 0 -> 0.4
{
    type         uniformFixedValue;
    uniformValue
    {
        type             scale;
        scale            reverseRamp;
ramp             linearRamp;
        start            0;
        duration         0.4;
        value            2;
    }
}

inlet  // pulse with value 2, from t = 0 -> 0.4
{
    type         uniformFixedValue;
    uniformValue
    {
        type             scale;
scale            squarePulse
        start            0;
        duration         0.4;
        value            2;
    }
}

inlet
{
    type            uniformFixedValue;
    uniformValue    coded;
    name            pulse;
    codeInclude
    #{
        #include "mathematicalConstants.H"
    #};

    code
    #{
        return scalar
        (
            0.5*(1 - cos(constant::mathematical::twoPi*min(x/0.3, 1)))
        );
    #};
}
```
