from pathlib import Path
#from module import Class


path1 = Path("ecommerce")
print(path1.exists())


# path = Path("emails")
# path.mkdir() for creating directories
# path.rmdir() for removing the directories

path2 = Path()
for file in path2.glob('*.py'):
    print(file)