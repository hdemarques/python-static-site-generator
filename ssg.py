import typer
from ssg.site import Site

#Import typer
#Let's set up the command line interface (CLI). Open the ssg.py file in the root directory of the project.
#At the top, import typer. Also, import the Site class from ssg.site.



#Configuration options

# The Typer library requires a function that captures command line arguments.
#We'll call this function main. It should accept two keyword arguments: source with a default value of "content", 
# and dest with a default value of "dist".
#In the body of the main function, create a dictionary called config. 
# Add two key value pairs to config: "source" set to source, and "dest" set to dest.

#create an instance of the Site class. The Site class requires that you provide two attributes source and dest when creating an instance.
#These are currently stored in the config dictionary as key value pairs. Unpack these dictionary values with ** and pass it to the Site instance. Finally, chain a call to the build() method on this instance.
def main(source="content", dest="dist"):
    config = {"source": source, 
              "dest": dest
              }
    
    Site(**config).build()

typer.run(main)
