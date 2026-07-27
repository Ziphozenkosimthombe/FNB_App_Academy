"""
Student Grade Classifier
-------------------------
Collects a learner's name and marks for three subjects, calculates the
average, assigns a letter grade and pass/fail status, flags subjects
that need intervention, and displays a formatted report card.
"""

# 1. Collect learner name and marks for three subjects
name = input("Enter learner's name: ")
subject1_name = input("Enter name of Subject 1: ")
subject1_mark = float(input(f"Enter mark for {subject1_name}: "))
subject2_name = input("Enter name of Subject 2: ")
subject2_mark = float(input(f"Enter mark for {subject2_name}: "))
subject3_name = input("Enter name of Subject 3: ")
subject3_mark = float(input(f"Enter mark for {subject3_name}: "))

# 2. Calculate the average mark across the three subjects
average = (subject1_mark + subject2_mark + subject3_mark) / 3

# 3. Assign a letter grade using if/elif/else
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# 4. Assign Pass/Fail status based on the average
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# 5. Flag any individual subject mark below 40 as 'needs intervention'
subjects = [
    (subject1_name, subject1_mark),
    (subject2_name, subject2_mark),
    (subject3_name, subject3_mark),
]

intervention_flags = []
for subject_name, mark in subjects:
    if mark < 40:
        intervention_flags.append(subject_name)

# 6. Display the formatted report card
print("\n" + "=" * 40)
print("           STUDENT REPORT CARD")
print("=" * 40)
print(f"Learner Name: {name}")
print("-" * 40)
for subject_name, mark in subjects:
    print(f"{subject_name:<20}: {mark:.2f}")
print("-" * 40)
print(f"Average Mark : {round(average, 2)}")
print(f"Grade        : {grade}")
print(f"Status       : {status}")

if intervention_flags:
    flagged_subjects = ", ".join(intervention_flags)
    print(f"Intervention Needed For: {flagged_subjects}")
else:
    print("Intervention Needed For: None")
print("=" * 40)