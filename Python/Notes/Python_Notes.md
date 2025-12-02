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

