#Author: Chandresh Maurya
# Contact: ckm.jnu@gmail.com
import sys

import sys

if(len(sys.argv) < 3):
    print("usage: ./python convertToSVM.py inputfilename outputfilename")
#print sys.argv[1]

inputfilename = sys.argv[1]
fin = open(inputfilename,'r')
lines = fin.readlines()
fin.close()
outputfilename = sys.argv[2]
fout = open(outputfilename,'w')

beginToRead = False
for line in lines:
   #  print(line)
     if beginToRead:
        # print("reading")
         if line.strip(): # not an empty line
              #read this line
              dataList = line.split(',')
              resultLine = ''
              resultLine += dataList[-1].strip()
              resultLine += ' '
              for i in range(0,len(dataList)-1):
                  resultLine += str(i+1)
                  resultLine += (":"+dataList[i].strip()+" ")
#==============================================================================
#               print(resultLine)
#==============================================================================
              fout.write(resultLine+"\n")
     if line.find('@DATA') >=0 or line.find('@data') >=0 :
         beginToRead = True
#==============================================================================
#==============================================================================


