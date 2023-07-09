import random

names = ["Alex", "Sam", "Robin", "Pierre", "Emily", "Gus", "Shane", "Penny", "Abigail", "Pam", "Leah", "Haley", "Caroline", "Kent"]
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

# Create a dictionary of passed students (students scored 60 or above)
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)



# Exercise 2 - find the number of letters in each word of a sentence

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split(" ")}
print(result)



# Exercise 3 - Convert temperature in Celcius into Farenheight

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)
