
def greeting(name):
    print("Hello COMP 170")
    print(f"Hello {name}")

# Pattern:
# "Hello" first_name", welcome to "course_code"

def personalized_greeting(name, course_code):

#parameters are "name" and "course_code"

    print(f"Hello {name}, welcome to {course_code}.")

personalized_greeting("lula", "COMP 170")

#now we can create a list of the students.

students = ["Omar", "Lula", "Enrique", "Arhub"]
your_course = "COMP 170"
#this is a loop.

for name in students:
    personalized_greeting(name, your_course)

#for name in students:
# personalized_greeting(name, your_course)

for index in range(len(students)):
    personalized_greeting(students[index], your_course)
    print(index)
