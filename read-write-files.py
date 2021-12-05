import os

sampleFileRead=open(os.path.abspath('./data/sample0.txt'))

print(sampleFileRead.read())

sampleFileRead.close()

sampleFileWrite=open(os.path.abspath('./data/sample1.txt'), 'w')
sampleFileWrite.write('hey dude')
sampleFileWrite.close()

sampleFileAppend=open(os.path.abspath('./data/sample2.txt'), 'a')
sampleFileAppend.write('hey hey dude')
sampleFileAppend.close()