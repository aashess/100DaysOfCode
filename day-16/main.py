from prettytable import PrettyTable

# # Columen Creation 
# mytable = PrettyTable(["Student Name","Class", "RollNo."])
# studentName = PrettyTable(["Teacher Name", "ID", "Salary"])
# # Row Creation 
# studentName.add_row(["Hari","K256JY","20000"])
# studentName.add_row(["Shayam","G783H","28000"])
# mytable.add_row(["Aashish Jha","10","24"])
# mytable.add_row(["Virat Kholi", "11", "08"])


# print(studentName)
# print(mytable)
# ------------------------------------------------------
# studentName = PrettyTable(["Student", "Due Date"])
# studentName.add_row(["Ram Chahal", "2022/6"])

# print(studentName)
# ------------------------------------------------------


x = PrettyTable()
x.align="l" 


x.add_column("Pokemon",["Pikachu","Squrite","Charmander"])
x.add_column("Type",["Electric","Water","Fire"])

print(x)