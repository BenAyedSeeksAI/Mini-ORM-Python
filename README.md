# Mini-ORM-Python
A simple ORM to migrate data models into an Sqlite3 database, I used sqlite3 python library. 
# Notice 
This project is still under development. So further changes will come up Insha2allah.
# Usage
All you need to do is to define a base model class in the [base.py](https://github.com/BenAyedSeeksAI/Mini-ORM-Python/blob/main/base.py) file. of course you need to specify the
table name of the model and its fields. the class inherits from baseModel.
```python
class Model(baseModel):
    base_model = base
    tablename = "Model"
    fields = ("field_1", "field_2")
```

In the same file you need to add the model into your the python list model_list:

```python
model_list = [Model,
              ]
```
To make a migration you need to execute this following command:
```bash
python migrate_manager.py migrate
```
The following output in the command prompt will show up to confirm the successful migration:
```bash
Begin database Migration ...

Model Migration
Connection started ...
Model: created successfully!
2022-01-04 02:29:53.402991: Commit is successful!!
Connection ended ...
```
