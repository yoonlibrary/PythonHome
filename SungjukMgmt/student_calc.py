#student_calc.py

def calc(student) :
    total = student["kor"] + student["eng"] + student["math"]
    avg = total / 3
    grade = None       #keyword 중에 앞에가 대문자인 것 - False, True, None
    if 90 <= avg <= 100 : grade = "A"
    elif 80 <= avg < 90 : grade = "B"
    elif 70 <= avg < 80 : grade = "C"
    elif 60 <= avg < 70 : grade = "D"
    else : grade = "F"
    
    student["total"] = total
    student["avg"] = avg
    student["grade"] = grade