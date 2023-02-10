PROJECT DESCRIPTION

In this project ( AirBnB clone), we implemented a console application with the help of the cmd module in python and also worked on the backend. json file was used to store data generated and could be accessed with the help of the json module in python.

DESCRIPTION OF THE COMMAND LINE INTERPRETER:

The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website. The command line interpreter serves as the frontend of the web application where users can interact with the backend which was developed with python OOP programming.

HOW TO INSTALL

The repository of the project should be cloned from Github. This will contain the simple shell program and all of its dependencies. After the repo has been cloned, a folder called AirBnB_clone will be available where there will be several files that will allow the program to work which includes:

/console.py : The min executable of the project; the command interpreter.

models/engine/file_storage.py : Class that serializes instances to a JSON file a                                nd deserializes JSON file to instances.

models/base_model.py : Class that defines all common attributes/methods for 
                        other classes.

models/user.py : User class that inherits from Basemodel.

models/_init_.py : A unique file storage instance for the application.

models/amenity.py : Amenity class that inherits from Basemodel.

models/place.py : Place class that inherits from Basemodel.

models/state.py : State class that inherits from Baemodel.

models/city.py : City class that inherits from Basemodel.

models/review.py : Review class that inherits from Basemodel.

USAGE:

It can be used in Interactive and Non-interactive modes.

In Interactive mode,the console will display a prompt(hbnb) indicating that the user can wite and execute a command.After the command is run,the prompt will appear again awaiting a new command and this can go on indefinitely as long as the user does not exit the program.

In Non-interactive mode,the shell will need to be run with a command input pipedinto its execution so that the command is run as soon as the shell starts. In this mode,no prompt will appear and no further input will be expected from the user.

AVAILABLE COMMANDS AND WHAT THEY DO

* quit/EOF :Exits the program.

* create : creates a new instance of a class and saves it to JSON file.

* show : Prints the string representation of an instance based on the class name and id.

* help : Provides a text describing how to use a command.

* update : Updates an instance based on the class name and id by adding or updating attribute.

* all : Prints all string representation of all instances based or not on the class name.

* destroy : Deletes an instance based on the class name and id.
