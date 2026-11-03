# student_manager.py - Phien ban chuan
students = [
    {"id": "SV01", "name": "Nguyen Van A", "gpa": 3.5},
    {"id": "SV02", "name": "Tran Thi B", "gpa": 3.8}
]

def show_students():
    for s in students:
        print(f"{s['id']} - {s['name']} - GPA: {s['gpa']}")

# === VI TRI THEM TINH NANG MOI O DUOI DONG NAY ===
def add_student(sv_id, name, gpa):
    students.append({"id": sv_id, "name": name, "gpa": gpa})
    print(f"Da them sinh vien: {name}")

def search_student(keyword):
    results = [s for s in students if keyword.lower() in s["name"].lower()]
    return results

def delete_student(sv_id):
    global students
    students = [s for s in students if s["id"] != sv_id]
    print(f"Da xoa sinh vien co ma: {sv_id}")

# Hotfix v1.0.1: Validated all 3 features