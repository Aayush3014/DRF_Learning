# Django Rest Framework Tutorials

## 1. Serializers and Serializations

### Python Json : Python has a built-in package called json, which can be used to work with JSON data.

Python Json has 2 methods: dumps() and loads()

dumps() : Take a Python object, and convert it to a JSON string

```python
import json
python_dict = {"name": "David", "age": 6, "class": "I"}
json_string = json.dumps(python_dict)
print(json_string)```

loads() : Take a JSON string, and convert it to a Python object

