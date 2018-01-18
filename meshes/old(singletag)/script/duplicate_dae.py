import os
import sys
import fileinput
import shutil 

# Make sure tag0.dae is in this folder, then we will create 15 copies.
print ("Copying all instances of 'tag0' into 'tag#', 15 times.")

textToSearch = "tag0"
fileToSearch = 'tag0.dae'

for num in range(1,16):
  textToReplace = 'tag' + str(num)
  fileToProduce = 'tag' + str(num) + '.dae'
  shutil.copy2(fileToSearch, fileToProduce)

  tempFile = open( fileToProduce, 'r+' )
  for line in fileinput.input( fileToProduce ):
      tempFile.write( line.replace( textToSearch, textToReplace ) )
  tempFile.close()



