# COMP 163 - Assignment 4: College Life Adventure Game
# Author: Your Name
# This program simulates college decisions using branching logic.

# -------------------------------
# Step 1: Foundation Setup
# -------------------------------

student_name = "Ajani"
current_gpa = 4.0
study_hours = 25
social_points = 45
stress_level = 40

print(f"Welcome to college life {student_name}!")
print(f"GPA: {current_gpa}, Study Hours: {study_hours}, Social Points: {social_points}, Stress Level: {stress_level}")

# -------------------------------
# Step 2: Course Planning Decision
# -------------------------------

print("\nChoose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    # Light load: less stress, fewer study hours
    study_hours += 5
    stress_level -= 5
    print("You chose a light load. More free time, less stress.")

elif choice == "B":
    # Standard load: balanced
    study_hours += 10
    stress_level += 5
    print("You chose a standard load. Balanced path.")

elif choice == "C":
    # Heavy load depends on GPA
    if current_gpa >= 3.5:   # comparison operator
        study_hours += 15
        stress_level += 10
        print("You took a heavy load, but your GPA helps you manage.")
    else:
        study_hours += 25
        stress_level += 30
        social_points -= 10
        print("You chose a heavy load without a strong GPA. Stress gets really high.")
else:
    print("Invalid choice.")

