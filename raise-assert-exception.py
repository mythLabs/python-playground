import traceback,os

try:
    if 1 == 1:
        raise('This is custom exception')
except:
    sampleFileAppend=open(os.path.abspath('./data/sample2.txt'), 'a')
    sampleFileAppend.write(traceback.format_exc())
    sampleFileAppend.close()

assert False, 'This is assertion error message'