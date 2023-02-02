"""
Das Skript enthält Lösungen zu Aufgabe 5
"""

# Part I: About PUBLIC and _PROTECTED members of a class

""" All members in a Python class are PUBLIC by default. Any member can be accessed from outside the class environment.
Python prescribes a convention of prefixing the name of the variable/method with a _single or __double underscore to 
emulate the behavior of protected and private access specifiers.

PROTECTED members are supposed to be only accessible from within the class and also to its sub-classes. No other 
environment is permitted access to it. This enables specific resources of the parent class to be inherited by the child 
class."""


class Employer:

    country = 'Germany'  # PUBLIC class attribute

    _company = 'SMS group'  # PROTECTED class attribute (convented to be declared using SINGLE PREFIX).

    def __init__(self, name, age, salary):
        self.name = name  # PUBLIC instance attribute
        self._age = age  # PROTECTED instance attribute. DOESN'T prevent instance variables from accessing or modifying
        # the instance (f.e., with obj._age = 30)

        self._salary = salary
        # To make a property fully protected, it can be defined using @property-decorators of the property() function
        # More @ https://www.tutorialsteacher.com/python/property-decorator and
        # @ https://www.tutorialsteacher.com/python/property-function and
        # @ https://www.tutorialsteacher.com/python/decorators . Decorators are recommended for use over property()!!!
        """decorator is a design pattern that adds additional responsibilities to an object dynamically. In Python, 
        a function is the first-order object. So, a decorator in Python adds additional 
        responsibilities/functionalities to a function dynamically without modifying a function. A decorator in 
        Python is a function that receives another function as an argument. The behavior of the argument function is 
        extended by the decorator without actually modifying it """

    @property  # makes SALARY()-method a getter method for a protected property
    def salary(self):
        return self._salary

    @salary.setter  # overloads the SALARY()-method as a setter method for a protected property
    def salary(self, new_salary):
        self._salary = new_salary

    @salary.deleter  # overloads the SALARY()-method as a deleter method for a protected property
    def salary(self):
        del self._salary
        print("The protected property has been deleted")


ilia = Employer("Ilia", 29, 950)

print(ilia.name)

# Protected properties are still accessible from the outside in Python.
print(ilia._age)  # Returns 29. INSECURE!
print(ilia._salary)  # Returns 950. INSECURE!
# i.e. a good code should contain NO references to the protected props from outside of the class!

print(ilia.salary)  # returns 950 (calls a getter method SALARY() ). SECURE! (i.e. a protected instance is kept hidden)

ilia._age = 30  # setting a protected property directly with no setter. INSECURE
print(ilia._age)

ilia.salary = 2000  # setting a protected property with a setter. SECURE! However ilia._salary = X is also possible.
print(ilia.salary)  # Returns 2000 (calls a getter method SALARY() again). SECURE!

del ilia.salary  # deletes a protected property from the objet. SECURE!
# print(ilia.salary)  # AttributeError: 'Employer' object has no attribute '_salary'


# Part II: About __PRIVATE members of a class

""" Python doesn't have any mechanism that effectively restricts access to any instance variable or method.
It gives a strong suggestion not to touch a private member from outside the class. Any attempt to do so will result in 
an AttributeError: 'obj_name' object has no attribute '__private_member_name'.

However, Python performs name mangling of private variables. Every member with a double underscore will be changed to 
_object._class__variable. So, it CAN still be accessed from outside the class, BUT the practice should be refrained. """


class Employer2:

    country = 'Germany'
    _company = 'SMS group'
    __contract_number = 12345  # PRIVATE class attribute (convented to be declared using DOUBLE PREFIX).

    def __init__(self, name: str, age: int, salary: float, pass_no: int):  # INIT is also a PRIVATE METHOD of a class instance!
        self.name = name
        self.age = age
        self._salary = salary
        self.__passport_number = pass_no  # PRIVATE instance attribute

    def __tell_secret(self):  # PRIVATE instance method
        print("I'm telling you a private secret!")


# Thus, Python provides conceptual implementation of public, protected, and private access modifiers, but not like
# other languages like C#, Java, C++.

