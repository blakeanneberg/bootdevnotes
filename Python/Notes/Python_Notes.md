## Function Definition Terms:

- Function name - The identifier you use to call the function (e.g., get_max_health)

- Parameters - The variable names listed in the function definition that receive values (e.g., modifier and level in your function definition)

- Arguments - The actual values you pass when calling the function (e.g., my_modifier and my_level when you call get_max_health(my_modifier, my_level))

- Return value - The result that gets sent back to the caller using the return keyword (e.g., modifier * level)

- Function body - The indented code block that runs when the function is called (e.g., return modifier * level)

- Function signature - The first line of the function definition, including the name and parameters (e.g., def get_max_health(modifier, level):)

- Scope - Where variables are accessible (which you just learned about!)

- Function call - When you actually execute the function by using its name with parentheses (e.g., get_max_health(my_modifier, my_level))

- A helpful way to remember parameters vs arguments: Parameters are the placeholders, arguments are the actual values!


## Variables vs Paramaters
- A parameter is a type of variable, but not all variables are parameters.

- Here's the distinction:

- Parameters are variables that are defined in a function's definition and receive values when the function is called. In your code: `def total_xp(level, xp_to_add):  # level and xp_to_add are parameters`

- Variables are any named containers for values. In your code: 
```python
current_xp = level * 100  # current_xp is a variable
final_xp = current_xp + xp_to_add  # final_xp is a variable
```
So the relationship is:

- All parameters are variables (they store values)
- Not all variables are parameters (only the ones in the function definition are)
- Think of it like this: parameters are variables that come into your function from the outside, while other variables are ones you create inside your function to help you do your work.


## Code

- Looping over a list to call a function - for item in list: do_something(item) is a fundamental pattern you'll use constantly.

- Using index-based loops when you need the position - for i in range(0, len(list)) gives you both the index i and access to the item via list[i]. Use this when the index itself matters.

Copying a list before mutating it - list.copy() creates an independent copy so you can safely del from it without destroying the original. If you'd skipped the copy, your dragons list would have shrunk each iteration and broken everything.


### filter-and-collect loop:
````
results = []
for item in collection:
    if some_condition(item):
        results.append(item)
return results
````

You'll use this pattern constantly - any time you need to filter a list down to a subset based on some condition. It's so common that Python even has a built-in shorthand for it called a list comprehension:
````
return [unit for unit in units if unit.in_area(...)]
````
Both are equivalent. The explicit loop is easier to read when starting out; the list comprehension is more idiomatic Python once you're comfortable with it.

## Inheritance 
1. Why super().__init__() and what does it do?

When a child class has its own constructor, it replaces the parent's constructor entirely. That means the parent's setup code won't run unless you explicitly call it. super().__init__() is just you saying "run the parent's constructor first, then I'll add my own stuff."
```
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed, num_doors):
        super().__init__(speed)   # sets self.speed
        self.num_doors = num_doors  # car-only variable
```
2. When does a child need its own constructor?

Only when it has extra instance variables the parent doesn't know about. If a child has no new variables, it can skip the constructor entirely and just inherit the parent's.
```
class SportsCar(Vehicle):
    pass  # inherits Vehicle's __init__ as-is
````
3. Method overriding

A child can redefine any parent method. When called on the child, Python uses the child's version. You can still reach the parent's version with super() if you need it as a base.
````
class Car(Vehicle):
    def describe(self):
        base = super().describe()   # parent's version
        return base + ", has doors"  # extend it
````
