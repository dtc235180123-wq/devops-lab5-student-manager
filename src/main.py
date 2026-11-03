# Student Manager - DevOps Lab 5
# Module: Main Application
from student import Student

def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER - DevOps Lab 5")
    print("=" * 50)

    # Tạo danh sách sinh viên mẫu
    students = [
        Student("sv001", "Nguyen Van A", 20, "K20"),
        Student("sv002", "Tran Thi B", 21, "K20"),
        Student("sv003", "Le Van C", 19, "K21"),
    ]

    # Hiển thị danh sách
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")

if __name__ == "__main__":
    main()
