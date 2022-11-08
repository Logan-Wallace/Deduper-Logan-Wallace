#!/bin/bash
#SBATCH --account=bgmp                 
#SBATCH --partition=bgmp               
#SBATCH --job-name=Deduper_LW                           
#SBATCH --nodes=1                      
#SBATCH --cpus-per-task=8
#SBATCH --output=Deduper.output

python Deduper.py -f "C1_SE_uniqAlign.sorted.sam" -u "STL96.txt" -o "Output_test.sam"