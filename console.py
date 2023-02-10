#!/usr/bin/python3
"""Module HBNBCommand
   Defines the HBNB command intepreter

   Inherits from Cmd class
"""
import cmd
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review
from models.state import State
from models import storage


def parse(cline):
    """Method to parse command and arguments"""
    return tuple(cline.split())


class HBNBCommand(cmd.Cmd):
    """Defines HBNBCommand class
       Attributes:
       prompt (str): command line prompt
       classes (str): all classes to use in cmd
    """
    prompt = "(hbnb)"
    classes = {"BaseModel", "City", "User", "Amenity", "Place",
               "Review", "State"}

    def default(self, cline):
        """Default behaviour of cmd"""
        args = cline.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(cline))
            return
        try:
            args = args[1].split('(')
            cmnd = args[0]
            if cmnd == 'all':
                HBNBCommand.do_all(self, class_arg)
            elif cmnd == 'count':
                HBNBCommand.do_count(self, class_arg)
            elif cmnd == 'destroy':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg)
            elif cmnd == 'show':
                args = args[1].split('')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_show(self, arg)
            elif cmnd == 'update':
                args = args[1].split(',')
                id_arg = args[0].strip("'")
                id_arg = id_arg.strip('"')
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(cline))
        except IndexError:
            print("*** Unknown syntax: {}".format(cline))

    def do_EOF(self, cline):
        """Handles  Ctrl + D, exits"""
        print("")
        return True

    def emptyline(self):
        """Handles empty line prompt"""
        pass

    def do_all(self, cline):
        """Displays all objects, or all objects of a class
        Usage: all or all <class> or <class>.all()
        """
        args = parse(cline)
        list_obj = []
        if len(cline) == 0:
            for obj in storage.all().values():
                list_obj.append(obj)
            print(list_obj)
        elif args[0] in HBNBCommand.classes:
            for key, obj in storage.all().items():
                if args[0] in key:
                    list_obj.append(obj)
            print(list_obj)
        else:
            print("** class doesn't exist **")

    def do_create(self, cline):
        """Creates class instance and saves to file storage
        Usage: create <class>
        """
        args = parse(cline)
        if len(cline) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_quit(self):
        """Exit The program, quit the command
        """
        return True

    def do_show(self, cline):
        """Displays string representation of name and id
        Usage: show <class> <id> or <class>.show(<id>)
        """
        args = parse(cline)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, cline):
        """Destroys an instance with given id
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        """
        args = parse(cline)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_update(self, cline):
        """Updates an instance of a given id
        Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        """
        args = parse(cline)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = val_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            for key, val in eval(args[2]).items():
                obj_val = obj.__class__.__dict__[key]
                if (key in obj.__class__.__dict__.keys() and
                        type(obj_val) in {str, int, float}):
                    val_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(val)
                else:
                    obj.__dict__[key] = val
        storage.save()

    def do_count(self, cline):
        """Usage: count <class> or <class>.count()
        Counts number of number of instances of a certain class"""
        args = parse(cline)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
