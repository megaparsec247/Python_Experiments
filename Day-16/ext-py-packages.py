#users can use PYPI to find external packages to use in python
#to install external packages use pip install (package name)
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name" , ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type" , ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
