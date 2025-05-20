
def greeting(name):
    print("Hello COMP 170")
    print(f"Hello {name}")

# Pattern:
# "Hello" first_name", welcome to "course_code"

def personalized_greeting(name, course_code):
    print(f"Hello {name}, welcome to {course_code}.")

personalized_greeting("lula", "COMP 170")

students = ["Omar", "Lula", "Enrique", "Arhub"]
your_course = "COMP 170"

for name in students:
    personalized_greeting(name, your_course)