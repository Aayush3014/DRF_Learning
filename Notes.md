# Django Rest Framework Tutorials

## 1. Serializers and Serializations

### Python Json : Python has a built-in package called json, which can be used to work with JSON data.

Python Json has 2 methods: dumps() and loads() for serialization and deserialization respectively.

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