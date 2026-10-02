// doing it with the html is cool and all
// but needing to *open a webpage* then *open inspect element* just to see *one* (1) result
// is not cool

console.log("hi");

//const randomString = "Dog";
const randomString = "Do";
var parities = [];
// 2d array
// i think
var currentRow = 0;
var currentColumn = 0;

var finalBits = "";

for (var i = 0; i < randomString.length; i++)
{
    const asciiVal = randomString.charCodeAt(i);
    
    // base 2 (binary)
    // https://stackoverflow.com/questions/9939760/how-do-i-convert-an-integer-to-binary-in-javascript
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString
    
    // then padding so its 1 byte long
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padStart
    const binaryVer = asciiVal.toString(2).padStart(8, "0");
    console.log( randomString[i] + " " + asciiVal + " " + binaryVer );
    //console.log( binaryVer );
    
    var firstFour = binaryVer.substring(0, 4);
    var finalFour = binaryVer.substring(4, 8);
    //console.log("hi " + firstFour);
    finalBits = finalBits + binaryVer;
    //finalBits = finalBits + firstFour + "_" + finalFour + "_";
    
    parities.push( firstFour.split(""), finalFour.split("") );
    
}
//finalBits = finalBits + "_";

console.log(parities);

// okay, got the bytes
// now to go and calculate parity
for (var row = 0; row < 4; row++)
{
    
    // starting with row 1
    var rowParity = 0;
    for (var col = 0; col < 4; col++)
    {
        rowParity = rowParity + parseInt( parities[row][col] );
    }
    rowParity = rowParity % 2;
    //console.log("row " + row + " parity: " + rowParity);
    finalBits = finalBits + rowParity;
    
}
//finalBits = finalBits + "_";

// okay, now columns
for (var col = 0; col < 4; col++)
{
    
    // start at row 1, column 1
    // then row 2, column 1
    // then row 3, column 1
    // and row 4, column 1
    var colParity = 0;
    for (var row = 0; row < 4; row++)
    {
        colParity = colParity + parseInt( parities[row][col] );
    }
    colParity = colParity % 2;
    //console.log("col " + col + " parity: " + colParity);
    finalBits = finalBits + colParity;
    
}

console.log("result: " + finalBits);

/*

OOOHHHH
I UNDERSTAND IT NOW
lets say you want to do a parity check with 3 bytes
obviously you cant fit that all in a 4x4 table
so instead you make two and pair the second byte with null (0000_0000)
that makes so much more sense
i thought i somehow had to fit in the 3 labels

okay i got this

*/


const addOnToParityArray = (someBinary, existingArray) => existingArray.concat( [someBinary.substring(0, 4).split("")], [someBinary.substring(4, 8).split("")] )

const getBinaryAndArray = (someString) => {
    // here goes
    
    // convert the string into the 3-byte binary
    var result = "";
    var binArray = [];

    for (var i = 0; i < someString.length; i++)
    {
        const asciiVal = someString.charCodeAt(i);
        
        // base 2 (binary)
        // https://stackoverflow.com/questions/9939760/how-do-i-convert-an-integer-to-binary-in-javascript
        // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString
        
        // then padding the ascii so its 1 byte long
        // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padStart
        const binaryVer = asciiVal.toString(2).padStart(8, "0");
        //console.log( someString[i] + " " + asciiVal + " " + binaryVer );
        //console.log( binaryVer );
        
        //var firstFour = binaryVer.substring(0, 4);
        //var finalFour = binaryVer.substring(4, 8);
        //console.log("hi " + firstFour);
        // update the result
        result = result + binaryVer;
        //finalBits = finalBits + firstFour + "_" + finalFour + "_";
        
        //parityArray.push( firstFour.split(""), finalFour.split("") );
        
        // add the new row to the 4x4 array
        binArray = addOnToParityArray(binaryVer, binArray);
        
    }
    // okay
    // i have the 4x4 array
    // (the parity bits arent included)
    
    
    // now to calculate parity
    
    // rows
    for (var row = 0; row < 4; row++)
    {
        
        // starting with row 1
        var rowParity = 0;
        for (var col = 0; col < 4; col++)
        {
            // string -> number
            rowParity = rowParity + parseInt( binArray[row][col] );
        }
        rowParity = rowParity % 2;
        //console.log("row " + row + " parity: " + rowParity);
        
        // then add it to the final bit sequence
        // (as a string)
        result = result + rowParity;
        
    }
    
    // okay, now columns
    // pretty similar
    for (var col = 0; col < 4; col++)
    {
        
        // start at row 1, column 1
        // then row 2, column 1
        // then row 3, column 1
        // and row 4, column 1
        var colParity = 0;
        for (var row = 0; row < 4; row++)
        {
            colParity = colParity + parseInt( binArray[row][col] );
        }
        colParity = colParity % 2;
        //console.log("col " + col + " parity: " + colParity);
        result = result + colParity;
        
    }
    
    // result is the final string of bits
    // binArray is the 4x4 array
    
    return [result, binArray];
    
}

const getArrayFromBinary = (binaryString) => {
    
    var result = [];
    
    for (var row = 0; row < 4; row++)
    {
        
        var newRow = [];
        for (var col = 0; col < 4; col++)
        {
            const index = (row * 4) + col;
            newRow.push( binaryString[index] );
        }
        result.push(newRow);
        
    }
    
    return result;
    
}

// takes in the 4x4 array and calculates parity
// 0-4 is horizontal
// 4-8 is vertical
const getParityStringFromArray = (inputArray) => {
    
    var result = "";
    
    for (var row = 0; row < 4; row++)
    {
        
        // starting with row 1
        var rowParity = 0;
        for (var col = 0; col < 4; col++)
        {
            // string -> number
            rowParity = rowParity + parseInt( inputArray[row][col] );
        }
        rowParity = rowParity % 2;
        //console.log("row " + row + " parity: " + rowParity);
        
        // then add it to the final bit sequence
        // (as a string)
        result = result + rowParity;
        
    }
    
    // okay, now columns
    // pretty similar
    for (var col = 0; col < 4; col++)
    {
        
        // start at row 1, column 1
        // then row 2, column 1
        // then row 3, column 1
        // and row 4, column 1
        var colParity = 0;
        for (var row = 0; row < 4; row++)
        {
            colParity = colParity + parseInt( inputArray[row][col] );
        }
        colParity = colParity % 2;
        //console.log("col " + col + " parity: " + colParity);
        result = result + colParity;
        
    }
    
    return result;
    
}

console.log("wait is it clean");
console.log(getBinaryAndArray("Do"));



// okay, i got the final bit sequence
// now i try to find the difference between 2 parities
/*
const compareParities = (parity1, parity2) => {
    // this assumes these are the full strings
    // (horizontal + vertical)
    
    
    var horizontalDiffs = [];
    
    for (var i = 0; i < 4; i++)
    {
        if ( !(parity1[i] === parity2[i]) )
        {
            // different
            horizontalDiffs.append(i);
        }
    }
    
    
    // the above works
    // (at least it would if i finished it)
    // but apparently the below follows functional programming better? allegedly?
    // https://stackoverflow.com/questions/1966476/how-can-i-process-each-letter-of-text-using-javascript
    // this feels really ugly though
    // taking a string, turning it into an array, then calling reduce()
    // is that a crazy thing to think that this is a little ugly
    // am i crazy here
    // is it just how i coded it
    
    return parity1.split("").reduce(
        (accumulator, item, index) => {
            
            if ( !(parity1[index] == parity2[index]) )
            {
                // theyre different
                //console.log(accumulator);
                //console.log(index);
                return accumulator.concat(index);
                *
                if (index < 4)
                {
                    // horizontal difference
                    
                }
                else
                {
                    // vertical difference
                }
                *
            }
            else
            {
                // no difference, just return the table on its own
                return accumulator;
            }
            
        },
        []
    );
    
    
    
}
*/

// okay this brings it down to one line
// thank you tenary operators
// still feels weird to split the string first
// this takes in the final byte (horizontal + vertical parity)
const compareParities = (parity1, parity2) => parity1.split("").reduce( (acc, item, index) => (item == parity2[index])? acc : acc.concat(index), [] );



const diff = compareParities("11000000", "01000001");
//console.log(diff);


// takes in 2 3 byte sequences
// returns [horizontal difference, vertical difference]
const getBitDifference = (obtainedSequence, expectedSequence) => {
    //const hello = compareParities(parity1, parity2);
    
    //const obtainedParity = obtainedSequence.substring(16);
    // vvv the sequence we should have
    const expectedParity = expectedSequence.substring(16);
    
    // calculate the parity the obtained sequence really has
    const obtainedParity = getParityStringFromArray( getArrayFromBinary(obtainedSequence) );
    
    console.log(obtainedParity);
    console.log(expectedParity);
    
    
    const diffLocations = compareParities(obtainedParity, expectedParity);
    console.log("HELLO");
    console.log(diffLocations);
    
    /*
    for (var i = 0; i < obtainedParity.length; i++)
    {
        if ( !(obtainedParity[i] == expectedParity[i]) )
        {
            console.log(obtainedParity[i] + ", " + expectedParity[i]);
            console.log("???? " + i);
        }
    }
    */
    
    // get the difference
    const numDifferences = diffLocations.reduce( (accumulator, item) => {
        if (item < 4)
        {
            // horizontal
            accumulator[0] += 1;
        }
        else
        {
            // vertical
            accumulator[1] += 1;
        }
        
        return accumulator;
        
    }, [0, 0] );
    
    return [numDifferences, diffLocations];
    
}

// okay
// i can now tell which bits are different
// hooray
/*
diff.forEach( (item) => {
    var result = "bit " + (item + 1) + " is different ";
    if (item < 4)
    {
        result = result + "(horizontal)";
    }
    else
    {
        result = result + "(vertical)";
    }
    console.log(result)
} );
*/



// now comes the maybe hard part
// error handling


// [horizontal, vertical]
/*
const bitDiffs = diff.reduce( (accumulator, item) => {
    
    if (item < 4)
    {
        // horizontal
        accumulator[0] += 1;
    }
    else
    {
        // vertical
        accumulator[1] += 1;
    }
    
    return accumulator;
    
}, [0, 0] );


console.log(bitDiffs);
*/

/*
if (bitDiffs[0] == 0 && bitDiffs[1] == 0)
{
    // no difference
    console.log("fine :)");
}
else if (bitDiffs[0] == 1 && bitDiffs[1] == 1)
{
    // 1 off on both (a fixable error)
    console.log("there is an error but it can be fixed");
    console.log("row " + bitDiffs[0] + ", col " + bitDiffs[1]);
    const whereToFlip = (bitDiffs[0] * 4) + bitDiffs[1];
    console.log("update index " + whereToFlip);
}
else
{
    // everything else
    // 1 off on the horizontal but 0 off on the vertical and vice versa
    // or more than 2 off on either
    console.log("unfixable (?)");
    
    // wait isnt 1 off on the horizontal + 0 off on the vertical (and vice versa) fixable
    // pretty sure it is
}
*/

// takes in a bitstring (the 3 bytes)
// also takes in the horizontal + vertical diffs
const updateBitString = (bitString, diffs, diffLocations) => {
    
    // okay this feels weird
    // this is meant to duplicate a string
    var duplicateString = bitString.substring(0);
    console.log(diffs);
    console.log(diffLocations);
    
    if (diffs[0] == 0 && diffs[1] == 0)
    {
        // no difference
        console.log("fine :)");
    }
    else if (diffs[0] == 1 && diffs[1] == 1)
    {
        // 1 off on both (a fixable error)
        
        var whatRow = 0;
        var whatCol = 0;
        
        if (diffLocations[0] < 4)
        {
            whatRow = diffLocations[0];
            whatCol = diffLocations[1];
        }
        else
        {
            whatRow = diffLocations[1];
            whatCol = diffLocations[0];
        }
        
        console.log("there is an error but it can be fixed");
        console.log("row " + whatRow + ", col " + whatCol);
        const whereToFlip = (whatRow * 4) + (whatCol - 4);
        console.log("update index " + whereToFlip);
        
        if (duplicateString[whereToFlip] == "0")
        {
            //duplicateString[whereToFlip] = "1";
            return bitString.substring(0, whereToFlip) + "1" + bitString.substring(whereToFlip);
        }
        else
        {
            //duplicateString[whereToFlip] = "0";
            return bitString.substring(0, whereToFlip) + "0" + bitString.substring(whereToFlip);
        }
        
    }
    else
    {
        // everything else
        // 1 off on the horizontal but 0 off on the vertical and vice versa
        // or more than 2 off on either
        console.log("unfixable (?)");
        throw new ValueError("no thanks");
        
        // wait isnt 1 off on the horizontal + 0 off on the vertical (and vice versa) fixable
        // pretty sure it is
    }
    
    // returns the fixed string
    //return duplicateString;
    
}

/*

possible conditions
perfectly fine (h = 0, v = 0)
a data error thats fixable (h = 1, v = 1)
unfixable by this program (everything else)

*/


const normalBinaryPlusArray = getBinaryAndArray("Do");
const expectedString = normalBinaryPlusArray[0];
const slightCorruption = "010001000110111111001001";
const someDiff = getBitDifference( slightCorruption, expectedString );
const diffLocations = someDiff[1];
//console.log(someDiff);
console.log(expectedString + " vs " + slightCorruption);
console.log( updateBitString(slightCorruption, someDiff[0], diffLocations) );



/*

okay
i got lost
what am i doing

i get 2 binary strings
i need to be able to (re)calculate parity with just binary
then i can get the difference in bits

*/







