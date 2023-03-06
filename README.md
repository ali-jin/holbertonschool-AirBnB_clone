![img](https://www.tabbykatz.com/hbnb.png)

# <p align="center">Project AirBnB clone - The console</p>

## Description
The console is the first step to the project of AirBnB clone, it will manipulate a powerful storage system. The console can create a data modele, manage objects via a console / command interpreter and store and persist objects to a file (JSON file).

## Installation

```bash
  git clone https://github.com/ali-jin/holbertonschool-AirBnB_clone.git
  cd holbertonschool-AirBnB_clone
```
    

and then to use this command interpreter

```bash
  ./console.py
```

you should see the prompt running like this, and now you are able to write and use it as much as you want.

```bash
  (hbtn)
```

## Classes

● BaseModel (Init Class (ID))

● Amenity (attribute : name)

● City (attribute: state_id, name)

● Place (attribute: city_id, user_id, name, description, number_rooms, number_bathrooms, max_guests, price_by_night, latitude, longitude, amenity_ids)

● Review (attribute: place_id, user_id, text)

● State (attribute: name)

● User (attribute: email, password, first_name, last_name)


## Commands

| Command     | Description                                                                                                            | Usage                  | Exemple   | Output |
|-------------|------------------------------------------------------------------------------------------------------------------------|--------------------------|----------|-------|
| `create`        | Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`.                                                                                         | create <classes>       | `$ create BaseModel`         |  49faff9a-6318-451f-87b6-910505c55907 |
| `show`        | Prints the string representation of an instance based on the class name and `id`. | show <classes> <id>                                                                                         | `$ show BaseModel 1234-1234-1234` | [BaseModel] (1234-1234-1234) {'id': '1234-1234-1234'}|
| `destroy`        | Deletes an instance based on the class name and `id` (save it to json so be carefull)                                                                                   | destroy <classes> <id>          | `$ destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907  `       | No Output
| `all`        | Prints all string representation of all instances based or not on the class name.                                                                                      | all <classes>          | `$ all BaseModel`       | ["[BaseModel] (2dd6e...|
| `update`        | Updates an instance based on the class name and `id` by adding or updating attribute                                                                                            | update <classes> <id> <attribute> <"value">          | `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`      | No output|
| `exit`        | Quit the prompt                                                                                            | quit         |         | No ouput, just close the console!


### Normal command input

|Command| Example|
|--|--|
|create| create [class name] |
|show| show [class name] [id] |
|all| all [class name] [id]|
|update| update [class name] [id] [arg_name] [arg_value]|


## Usage
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

## Authors

- Alina JIN
- Caroline CHOCHOY
