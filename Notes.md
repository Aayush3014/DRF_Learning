# Django Rest Framework Tutorials


## Python Json : Python has a built-in package called json, which can be used to work with JSON data.

#### Python Json has 2 methods: dumps() and loads() for serialization and deserialization respectively.

##### dumps() : Take a Python object, and convert it to a JSON string

##### Python ---> Json

```python
import json
python_dict = {"name": "David", "age": 6, "class": "I"}
json_string = json.dumps(python_dict)
print(json_string)

# String values in Json should be in double quotes.
Output: {"name": "David", "age": 6, "class": "I"}

```


##### loads() : Take a JSON string, and convert it to a Python object 

or 

##### It is used to parse the JSON string. It deserializes the JSON to a Python object.

##### Json ---> Python

```python
import json
json_string = '{"name": "David", "age": 6, "class": "I"}'
python_dict = json.loads(json_string)
print(python_dict)

Output: {'name': 'David', 'age': 6, 'class': 'I'}
```


### Serializers : In DRF, serializers are used to convert complex data such as QuerySets and model instances to native Python DataTypes that can then be easily rendered into JSON, XML or other content types which is understandable by the Frontend.

#### Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.


#### Serialization
##### Serializer Class: A serializer class is very similar to a Django Form and ModelForm, and includes similar validation flags on the various fields, such as required, max_length and default.
##### DRF provides a Serializer class which gives you a powerful, generic way to control the output of your responses.


#### How to create a Serializer Class?

##### 1. Create a serializers.py file to write all serializers.

##### 2. Import serializers from rest_framework.

```python
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
 

```
