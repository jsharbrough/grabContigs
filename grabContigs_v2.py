'''Make sure that the contig list, the input fasta file, and the 
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
result of its use. Sharing, editing, and free use are heartily encouraged.'''
    
import sys

def makeSeqList(Infile):
    #Takes a text file as input and returns a list of contigs
    infile = open(Infile,'r')
    seqList = []
    for line in infile:
        seqName = '>' + line
        while seqName[len(seqName)-1] == '\r' or  seqName[len(seqName)-1] == '\n' or seqName[len(seqName)-1] == '\t':
                seqName = seqName[0:-1]
        seqList.append(seqName)
    infile.close()
    return seqList
    
def makeFastaFile(fastaFile,textFile):
    '''Text file should be a list of sequence names from the assembly file with 
    one sequence name per line. Do not include '>' symbol in sequence header 
    (i.e., text file should not have fasta formatted sequence headers)'''
    seqList = makeSeqList(textFile)
    infile = open(fastaFile,'r') # Put the name of your input fasta file in this line
    fileName = textFile.split('.')
    newFileName = ''
    for item in fileName[0:-1]:
        newFileName += item + '.'
    outfile = open(newFileName + 'fasta','w')  # Put the name of your output fasta file here
    seqDict = {}
    seqName = ''
    currSeq = ''
    for line in infile:
        if line[0] == '>':
            if currSeq != '':
                seqDict[seqName] = currSeq
            seqName = line
            while seqName[-1] == '\n' or seqName[-1] == '\t' or seqName[-1] == '\r':
                seqName = seqName[0:-1]
            currSeq = ''
        else:
            currSeq += line
            while currSeq[-1] == '\r' or currSeq[-1] == '\n' or currSeq[-1] == '\t':
                currSeq = currSeq[0:-1]
    seqDict[seqName] = currSeq
    for item in seqList:
        outfile.write(item + '\n')
        outfile.write(seqDict[item] + '\n')
    infile.close()
    outfile.close()


makeFastaFile(sys.argv[1],sys.argv[2])
        
