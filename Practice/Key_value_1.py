Student_info = {
    "name" : "Sayan Koley",
    "age" : 22,
    "college" : "ABC College",
    "course" : "BSc in CSE",
     "year" : 3,
    "Marks" : [85, 90, 78, 92, 88],
}
print("Student Name:", Student_info["name"])
print("Student Age:", Student_info["age"])
print("Student College:", Student_info["college"])
print("Student Course:", Student_info["course"])
print("Student Year:", Student_info["year"])
print("Student Marks:", Student_info["Marks"])
print("Highest Mark:", max(Student_info["Marks"]))
print("Lowest Mark:", min(Student_info["Marks"]))
print("Average Mark:", sum(Student_info["Marks"]) / len(Student_info["Marks"]))
Student_info["year"] = 4
print("Updated Student Year:", Student_info["year"])
Student_info["Marks"].append(95)
print("Updated Student Marks:", Student_info["Marks"])
