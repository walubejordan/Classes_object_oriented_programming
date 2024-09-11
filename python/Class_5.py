class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount")

# Example
employee1 = Employee("John Doe", 50000)
print(employee1.name) 
print(employee1.get_salary()) 

employee1.set_salary(55000)
print(employee1.get_salary())