# COMP 163 - Assignment 4: College Life Adventure Game
# Author: Ajani Davis
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
# -------------------------------
# Step 3: Study Strategy Decision
# -------------------------------

subjects = ["Programming", "Math", "English", "History"]

print("\nChoose a subject to focus on:", subjects)
study_choice = input("Your subject: ")

if study_choice in subjects:
    if study_choice == "Programming" and current_gpa < 3.0:
        current_gpa += 0.4
        print("Focusing on Programming improved your GPA.")
    elif study_choice == "Math" or study_choice == "English":
        social_points -= 5
        print("Extra work on Math/English decreased your social life a bit.")
    elif not study_choice == "History":
        stress_level += 5
        print("This subject added some stress.")
    else:
        print("Balanced effort in English kept you steady.")
elif study_choice not in subjects:  # membership operator with not in
    print("Invalid study choice. No changes made.")

# -------------------------------
# Step 4: Final Semester Assessment
# -------------------------------

print("\n--- Final Semester Assessment ---")

# Identity operator example: type checking
if type(current_gpa) is not float:
    print("Warning: GPA is not a float. Converting...")
    current_gpa = float(current_gpa)

# Nested if statements
if current_gpa >= 3.5:
    if stress_level < 50:
        ending = "Graduated with Honors"
    else:
        ending = "Graduated, but burned out from stress."
elif current_gpa >= 2.0:
    if social_points > 40:
        ending = "Graduated with a healthy balance of academics and social life."
    else:
        ending = "Barely passed due to stress and low social support."
else:
    ending = "On academic probation. Better luck next time."

# Final results
print(f"Final Stats → GPA: {current_gpa:.2f}, Study Hours: {study_hours}, "
      f"Social Points: {social_points}, Stress Level: {stress_level}")
print("Ending:", ending)

