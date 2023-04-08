# Your code goes here:
def render_person(name, age, gender, birthdate, eye_color, ):
    # param = name + str(birthdate) + fav_color + str(age) + gender
    name, age, gender, birthdate, eye_color = name, str(birthdate), eye_color, str(age), gender 
    param = "{} is a {} years old {} born in {} with {} eyes".format(name, str(age), gender, str(birthdate), eye_color)
    return param


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))