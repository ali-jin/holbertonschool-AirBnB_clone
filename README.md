# Project AirBnB clone - The console

![img](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230222%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230222T140234Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c3554c6ee8d5266896e0555bd009993b6fbeffb8a52a5697f9d05c415cfd6c17)

## Description
The console is the first step to the project of AirBnB clone, it will manipulate a powerful storage system. The console can create a data modele, manage objects via a console / command interpreter and store and persist objects to a file (JSON file).

# Commands

## Available commands
|Command| Explanation |
|--|--|
| create | Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`  |
| show | Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234` |
| all | Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel` |
| update | Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"` |

## Normal command input

|Command| Example|
|--|--|
|create| create [class name] |
|show| show [class name] [id] |
|all| create [class name] [id]|
|update| create [class name] [id] [arg_name] [arg_value]|

# To start the console
To start the console:
```
$ ./console.py
```
When you see `(hbnb)` it means that you are in the console

# Usage
You can for example create a model of User and give you the id:
```
(hbnb) create User
808803c5-de3b-4371-8e4d-f6e0e84c39f5
````
And with the command show:
```
(hbnb) show User 808803c5-de3b-4371-8e4d-f6e0e84c39f5
[User] (808803c5-de3b-4371-8e4d-f6e0e84c39f5) {'id': '808803c5-de3b-4371-8e4d-f6e0e84c39f5', 'created_at': datetime.datetime(2023, 2, 22, 15, 29, 12, 516394), 'updated_at': datetime.datetime(2023, 2, 22, 15, 29, 12, 516462)}
```
It will give you all the attributes of the created model.

If you want know all the commands, use the command `help`
