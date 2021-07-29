# Formatted strings > Python3.6

# Usage:
my_next_goal = 10000
print(f"Let's reach {my_next_goal} subscribers!")

# Arbitrary
import datetime

def calculate_age(born_year):
    return datetime.datetime.now().year - born_year

print(f"You are {calculate_age(1996)} years old!")

# Multiline
name = "Jim"
subject1 = "Python"
subject2 = "DevOps"
print(f"""
Hello, my name is {name}.
And this is my Youtube channel.
I create {subject1} videos.
And also create {subject2} videos.
""")

# Debug your values
complex_operation = 75 * 75 * 20
print(f"Complex Operation is: {complex_operation}")
# Do this:
# Don't worry from syntax error :)
print(f'{complex_operation = }')

# Float formatting
my_float = 34.944361
print(f"One decimal: {my_float:.1f}")
print(f"Two decimal: {my_float:.2f}")
print(f"Three decimal: {my_float:.3f}")

# Datetime formatting
import datetime
just_now = datetime.datetime.now()
print(f"Year: {just_now:%Y}")
print(f"Month: {just_now:%m}")
print(f"Day: {just_now:%d}")