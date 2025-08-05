# Student Marks and Grades Summary System

def calculate_grade(average):
    """Calculate grade based on average marks"""
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

def main():
    print("=== Student Marks and Grades Summary System ===\n")
    
    # Get number of students
    num_students = int(input("Enter number of students: "))
    
    students_data = []
    all_totals = []
    
    # Input data for each student
    for i in range(num_students):
        print(f"\n--- Student {i+1} ---")
        name = input("Enter student name: ")
        
        print("Enter marks for 3 subjects:")
        subject1 = float(input("Subject 1: "))
        subject2 = float(input("Subject 2: "))
        subject3 = float(input("Subject 3: "))
        
        # Calculate total and average
        total = subject1 + subject2 + subject3
        average = total / 3
        grade = calculate_grade(average)
        
        # Store student data
        student_info = {
            'name': name,
            'marks': [subject1, subject2, subject3],
            'total': total,
            'average': average,
            'grade': grade
        }
        
        students_data.append(student_info)
        all_totals.append(total)
    
    # Calculate class statistics
    class_total = sum(all_totals)
    class_average = class_total / (num_students * 3)
    
    # Find topper
    topper = max(students_data, key=lambda x: x['total'])
    
    # Display results
    print("\n" + "="*60)
    print("STUDENT MARKS AND GRADES SUMMARY")
    print("="*60)
    
    print(f"{'Name':<15} {'Sub1':<6} {'Sub2':<6} {'Sub3':<6} {'Total':<7} {'Avg':<6} {'Grade':<5}")
    print("-" * 60)
    
    for student in students_data:
        print(f"{student['name']:<15} "
              f"{student['marks'][0]:<6.1f} "
              f"{student['marks'][1]:<6.1f} "
              f"{student['marks'][2]:<6.1f} "
              f"{student['total']:<7.1f} "
              f"{student['average']:<6.1f} "
              f"{student['grade']:<5}")
    
    print("-" * 60)
    print(f"\nCLASS STATISTICS:")
    print(f"Class Average: {class_average:.2f}")
    print(f"Class Topper: {topper['name']} (Total: {topper['total']:.1f}, Average: {topper['average']:.1f})")
    
    # Grade distribution
    grade_count = {}
    for student in students_data:
        grade = student['grade']
        grade_count[grade] = grade_count.get(grade, 0) + 1
    
    
    print(f"\nGRADE DISTRIBUTION:")
    for grade, count in sorted(grade_count.items()):
        print(f"Grade {grade}: {count} student(s)")

if __name__ == "__main__":
    main()