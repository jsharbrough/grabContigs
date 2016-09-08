# grabContigs
Takes a sequence list file (one sequence per line) and an assembly in fasta format as input and outputs a fasta file containing only the sequences present in the list file.


Make sure that the contig list, the input fasta file, and the 
grabContigs_v2.py file are all in the same directory. 

To run this in a unix environment move into the working directory containing 
your sequence list, the assembly file in fasta format, and the 
grabContigs_v2.py program. Then type the following:
    
    python grabContigs_v2.py <fastaFile> <testFile>

To run this in a python environment, start python, and then type import 
grabContigs, if using this script on more than one file in one sitting, need to 
type reload(grabContigs) in between each file, after it is edited. To run type:
    
    import grabContigs
    grabContigs.makeFastaFile(<fastaFile>,<textFile>)
    
***Note: You will receive an error when importing this module into python. 
Disregard that error message, the module loaded properly.

This program is provided as is and will not be updated to reflect different 
input formats. If you would like some help getting it to work, or if you would 
like a program that accepts more flexible inputs, please contact Joel 
Sharbrough at jsharbro@rams.colostate.edu

Copyright 2016 All Rights Reserved
This program is not intended for commercial use and no profit may be made as a 
result of its use. Sharing, editing, and free use are heartily encouraged.
