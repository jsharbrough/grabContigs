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


#grabBLASTHits
Takes a BLAST hit file (either xml or txt, format is automatically detected) and 
a fasta file from which the BLASTdb was constructedas input and outputs a fasta 
file containing only the sequences present in the hit file. The number of hits 
extracted can be toggled as well

Make sure that the BLAST result file, the database fasta file, and the 
BLASTHits.py file are all in the same directory. 
To run this in a unix environment move into the working directory containing 
your sequence list, the assembly file in fasta format, and the 
grabBLASTHits.py program. Then type the following:
    
    python grabBLASTHits.py <fastaFile> <hitFile> numHits
Where the <fastaFile> is the name of your database fasta file, the <hitFile> is 
the name of your BLAST result file, and numHits is the number of hits that you 
wish to extract from the database (if no number is included for this option, 
all hits will be extracted).
To run this in a python environment, start python, and type:
    
    import grabBLASTHits
    grabBLASTHits.makeFastaFile(<fastaFile>,<textFile>,numHits)
    
***Note: You will receive an error when importing this module into python. 
Disregard that error message, the module loaded properly.

These programs are provided as is and will not be updated to reflect different 
input formats. If you would like some help getting them to work, or if you would 
like a program that accepts more flexible inputs, please contact Joel 
Sharbrough at jsharbro@rams.colostate.edu

Copyright 2016 All Rights Reserved
These programs are not intended for commercial use and no profit may be made as a 
result of their use. Sharing, editing, and free use are heartily encouraged.
