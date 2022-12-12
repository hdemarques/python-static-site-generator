from pathlib import Path

#In this module we'll build up a Site Class that will set configuration values and create the root structure of our static site.
#  We'll also create a command line tool using the Typer library.
#Since we are going to be working with paths, let's import pathlib, which is part of the standard library.
#Open the site.py located in the ssg directory. At the top, import Path from pathlib.

#Create a class
#Below the import you just wrote, create a class called Site. Next, create a Site class constructor 
# that accepts three arguments self, source, and dest.
#In the constructor, convert source to a Path object. This can be done by passing it to a call to Path().
#  Save the result to an instance attribute with the same name. Hint: instance attributes are prefixed with self.
#Repeat these steps for dest.

class Site():
    
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
    
#Still in the Site class, create a method called create_dir() that accepts two parameters, self and path.
    def create_dir(self, path):
#In the body of the create_dir method, create a variable called directory. 
# This variable will need to contain the full path to the destination folder.
#The first part of the path is self.dest. The second part of the path needs to be relative to self.source. 
# So after a / operator call relative_to() on path passing in self.source. Hint:  destination / relative_to().
        directory = self.dest / path.relative_to(self.source)
#On a new line in the create_dir() method, call the mkdir() method on directory. 
# For our scenario we want directory to be replaced if it exists. 
# Pass the following keyword arguments to mkdir():
#   parents set to True
#   exist_ok set to True
        directory.mkdir(parents=True, exist_ok=True)
#Create a new method called build() in the Site class. 
# Call the mkdir() method on self.dest. As with the previous mkdir() call, pass the following keyword arguments to mkdir():
#parents set to True
#exist_ok set to True
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
