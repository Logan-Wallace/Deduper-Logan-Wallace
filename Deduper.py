#! usr/env/bin python

# Logan Wallace 
# 10/26/22
# Deduper Assignment

'''The purpose of this script is to remove PCR duplicates from 
a sorted SAM file. It will take as input both a SAM file as 
well as a text file of unique molecular indexes (here titled 
'STL96.txt')'''

#Import neccessary modules
import argparse
import re

#Arrange argparse arguments as needed
parser = argparse.ArgumentParser(description = "Arguments for Deduper.py")
parser.add_argument("-u", "--UMI", help = "Filename for the UMI", type =str, default = "STL96.txt")
parser.add_argument("-s", "--SAM", help = "Filename for the SAM file", type =str, default = "test.sam")
args = parser.parse_args()

#Variable Initialization
UMI_set = set()
UMI_filename: str = args.UMI
SAM_filename: str = args.SAM
plus_strand: bool = True
record_set = set()

#Functions
def cigar_parser(CIGAR, plus_strand):
    '''This function will take a CIGAR string and strand argument as input and return the 
    amount to which a mapping position needs to be adjusted'''
    #We first need to know which strand we are on as this will inform how we adjust the mapping position
    char_list = re.split("\d+", CIGAR)[1:]
    num_list = re.split("\D", CIGAR)[:-1]
    adjustment = 0
    if plus_strand == True:
        #Check to see if there is soft clipping at the beginning, if so, adjust for it
        if char_list[0] == "S":
            adjustment += num_list[0]
    elif plus_strand == False:
        #If there is soft clipping at the front, remove the leading number
        if char_list[0] == "S":
            adjustment -= num_list[0]
            i = 0 
            #Sum all digits associated with S, D, M or N
            for char in char_list:
                if char == "S" or char == "D" or char == "M" or char == "N":
                    adjustment += num_list[i]
                    i += 1
        #If there is not soft clipping at the front
        else:
            adjustment = sum(num_list)
            i = 0 
            #Sum all digits associated with S, D, M or N
            for char in char_list:
                if char == "S" or char == "D" or char == "M" or char == "N":
                    adjustment += num_list[i]
                    i += 1
    return(adjustment)

#Open and read in our UMI file
with open(UMI_filename) as UMI_file:
    for u in UMI_file:
        u = u.strip("\n")
        UMI_set.add(u)

#Just making sure we got the UMI file
print(UMI_set)
print("Length of UMI list: ", len(UMI_set))

#Open and read our SAM file
with open (SAM_filename) as SAM_file:
    for f in SAM_file:
        #Given we aren't at a header line
        if f[0] != "@":
            print(f)
            f = f.split("\t")
            #Grab the chomosome, the third field   
            chrom = f[2]
            print("Chrom: ", chrom)
            #Get the strandedness, the second field
            strand = int(f[1])
            print("strand: ", strand)
            #If the flag is set then we are on the minus strand
            if((strand & 16) == 16):
                plus_strand == False
                print("plus_strand: ", plus_strand)
            else: 
                plus_strand == True
            #Collect our UMI, first field
            UMI = f[0][-8:]
            print(UMI)
            #Capture our CIGAR, sixth field
            CIGAR = f[5]
            #Run the cigar through CIGAR parser
            adjustment = cigar_parser(CIGAR, plus_strand)
            #Store the mapping position
            mapping_pos = int(f[3]) + adjustment
        #Now we have the whole record, store it as a tuple inside a list of records
        

#1 Is the UMI matching? 
#2 Is the chromosome matching? 
#3 Does the strandedness match?
#4 Adjust the mapping position
#5 Does the mapping position match?
#6 If Yes to all above, PCR duplicate. Don't write out. If else, write out. 
