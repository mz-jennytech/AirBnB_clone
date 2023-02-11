			AirBnB Clone Project

## Description
AirBnB is a web app with a full development of back-end and front-end API
integrating also SQL storage
This project is the part 1 of 4 in which the back-end console is created
and deployed.
This is an educational purposes clone from [AirBnB](https://www.airbnb.com/)

## Classes

This projects uses the following classes:

|     | BaseModel | FileStorage | User | Amenity | City | Place | Review | State |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| Public instance attributes | id<br>created_at<br>updated_at | | Inherits BaseModel | Inherits BaseModel | Inherits BaseModel | Inherits BaseModel | Inherits BaseModel | Inherits BaseModel |
| Public instance methods | save<br>to_dict | all<br>new<br>save<br>reload |  |  |  |  |  |  |
| Public class attributes | | | email<br>password<br>first_name<br>last_name| name | _id<br>name | name | city_id<br>user_id<br>name<br>description<br>_rooms<br>_bathrooms<br>max_guest<br>price<br>latitude<br>longitude<br>amenity_id | place_id<br>user_id<br>text |
| Private class attributes | | file_path<br>objects | | | | | | |

## Storage

The presented classes are stored in [FileStorage](./models/engine/file_storage.py) class file.
When the console is initialized, the console redirects an instance of
FileStorage named storage.
#Storage object is loaded or reloaded from any class instances stored in the
JSON file file.json.
Class instances are created, updated, or deleted and storage object registers
changes intofile.json.

## Console
The console is a CLI that allows the use of data as backend tool.
It can be used to handle all classes predefined  previously called into
`storage` object.

### How to Use the CLI non-interactive
To run the console in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
### How to Use the CLI interactive
To run the console in interactive mode:

run the file console.py:

```
$ ./console.py

```

Running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```
```

## How to Test:
Unittests for the CLI AirBnB project are defined in the [tests](./tests)
folder. To run the entire test suite simultaneously, execute the following
command:

```
$ python3 unittest -m discover tests
```

Also, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Authors:
**Adava Onimisi** <[Adava Onimisi](https://github.com/Nomynameisjames)>
**Nnodim Obinna** <[Nnodim](https://github.com/Nnodim)>

