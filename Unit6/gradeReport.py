"""
grade_report.py
A class grade report generator, extending the Unit 5 grade classifier.

For each student we calculate an average mark across three subjects,
then assign a grade and a pass/fail status using the same logic used
in Unit 5:

    Average >= 75  -> Grade A
    Average >= 60  -> Grade B
    Average >= 50  -> Grade C
    Average >= 40  -> Grade D
    Average <  40  -> Grade F

    Grade F -> status 'Fail'
    Any other grade -> status 'Pass'
"""

# ---------------------------------------------------------
# 1. Student data: list of dictionaries
# ---------------------------------------------------------
students = [
    {"name": "Amara Ndlovu",   "maths": 82, "english": 74, "science": 91},
    {"name": "Sipho Khumalo",  "maths": 55, "english": 60, "science": 48},
    {"name": "Priya Naidoo",   "maths": 39, "english": 45, "science": 42},
    {"name": "Liam Botha",     "maths": 91, "english": 88, "science": 95},
    {"name": "Thandiwe Zulu",  "maths": 67, "english": 71, "science": 58},
]

# ---------------------------------------------------------
# 2. Grade/status logic (from Unit 5)
# ---------------------------------------------------------
def get_grade(average):
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def get_status(grade):
    if grade == "F":
        return "Fail"
    else:
        return "Pass"


# ---------------------------------------------------------
# 3. Main loop: process each student
# ---------------------------------------------------------
results = []

for student in students:
    average = (student["maths"] + student["english"] + student["science"]) / 3
    grade = get_grade(average)
    status = get_status(grade)

    results.append({
        "name": student["name"],
        "average": round(average, 2),
        "grade": grade,
        "status": status,
    })

# ---------------------------------------------------------
# 4. Class statistics
# ---------------------------------------------------------
all_averages = [r["average"] for r in results]

class_average = round(sum(all_averages) / len(all_averages), 2)
highest_mark = max(all_averages)
lowest_mark = min(all_averages)

# Find the student(s) attached to the highest/lowest average
top_student = next(r["name"] for r in results if r["average"] == highest_mark)
bottom_student = next(r["name"] for r in results if r["average"] == lowest_mark)

# ---------------------------------------------------------
# 5. Display the formatted class report
# ---------------------------------------------------------
def print_report():
    print("=" * 55)
    print("               CLASS GRADE REPORT")
    print("=" * 55)
    print(f"{'Name':<20}{'Average':<10}{'Grade':<8}{'Status':<8}")
    print("-" * 55)

    for r in results:
        print(f"{r['name']:<20}{r['average']:<10}{r['grade']:<8}{r['status']:<8}")

    print("-" * 55)
    print(f"Class Average : {class_average}")
    print(f"Highest Mark  : {highest_mark} ({top_student})")
    print(f"Lowest Mark   : {lowest_mark} ({bottom_student})")
    print("=" * 55)


print_report()

# ---------------------------------------------------------
# 6. Search for a student by name (while loop)
# ---------------------------------------------------------
print("\nStudent search (type 'exit' to quit)")

searching = True
while searching:
    query = input("Enter a student name to search: ").strip()

    if query.lower() == "exit":
        searching = False
        print("Goodbye!")
        continue

    found = None
    for r in results:
        if r["name"].lower() == query.lower():
            found = r
            break

    if found:
        print(f"\nName    : {found['name']}")
        print(f"Average : {found['average']}")
        print(f"Grade   : {found['grade']}")
        print(f"Status  : {found['status']}\n")
    else:
        print("No student found with that name. Please try again.\n")