import os

print(os.path.join('folder1','folder2','file.png'))

print(os.getcwd()) # current working directory

print(os.path.abspath('spam.png'))

print(os.path.dirname('/home/amit/python-playground/spam.png'))

print(os.path.basename('/home/amit/python-playground/spam.png'))

print(os.path.exists('/home/amit/python-playground/spam.pnggg'))

print(os.listdir('/home/amit/python-playground/'))