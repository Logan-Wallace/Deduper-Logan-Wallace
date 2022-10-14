# Unit test folder

## Purpose
The purpose of this folder is to host test files and expected output files for when we run on code on the test files.

## What do we need to test for in the unit test?
Case 1. The mapping positions are not a match
Case 2. The UMI's do not match
Case 3. The CIGAR string asks us to move the mapping position 2 bases so that the new read does match
Case 4. The CIGAR string asks us to move the mapping position such that the new read does not match
Case 5. The read is matching otherwise, but is not on the same strand.
Case 6. The read is fully matching and should be ommitted (not written out)

## More basics being tested;
Does our code loop through the file as expected and write out each line in the proper format?
Can the code read and adjust for the CIGAR string?


## Structure of the test file
The file will have 7 lines of reads. The first will be a 'canonical read' to which all else will be compared and the remaining 6 will each represent one of the test cases above. 


## ELSE
I have omitted the lines of the header that correspond to chromosome locations within the genome as this is not an important part of our test and makes the expected output easier to read. 