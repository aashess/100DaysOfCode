### OOPs (Object Oriented Programming Language)






### OOPs (Object Oriented Programming Language)


### Packages 


In Python, a package is a way of organizing related code by grouping multiple Python modules (individual code files) into a directory structure. The package directory contains an `__init__.py` file, signaling that it should be treated as a package. Packages can have subpackages and form a hierarchical structure.

Some Popular Packages:-
1. Numpy
2. Pandas
3. Matplotlib
4. TensorFlow
5. PyTorch
6. Django


### Why Packages Matter:


### Organization:
Packages help structure code logically, making it easier to manage and locate specific functionalities.


### Namespace Management:
 Prevents naming conflicts and provides a clear hierarchy for modules.


### Modularity:
 Encourages the development of reusable and interchangeable components.


### Distribution:
 Simplifies code distribution by bundling related modules together.


### How to Use Packages:

### Create a Package:
 Organize code into a directory hierarchy, including an `__init__.py` file.

### Import Modules:
 Use the `import` statement to bring modules into your code.
   ```python
   from mypackage import mymodule
   ```


### Utilize Subpackages:
Extend organization with subpackages and nested modules.
   ```python
   from mypackage.subpackage import submodule
   ```


### Initialization Tasks: 
 Code in the `__init__.py` file runs when the package is imported, allowing for initialization.



### Installation:
 Install packages using tools like `pip`.
   ```bash
   pip install package-name
   ```


### Example:
Suppose you have a package named `mypackage` with a module `mymodule`:
```
mypackage/
|-- __init__.py
|-- mymodule.py
```
You can import and use `mymodule` within your code.

Packages provide a structured and organized approach to managing and sharing Python code.

### PrettyTable Packages
PrettyTable is a Python library that provides a simple way to create and display tabular data in a visually appealing ASCII table format. It is useful for presenting data in a human-readable form, especially when working with text-based interfaces or command-line applications

studentName.add_row(["Hari","K256JY","20000"])

<!-- This is used to add row -->

studentName.add_column("Name",["K256JY","20000"])studentName.add_column("Id",["Ram","Married"])

<!-- This is to add column -->