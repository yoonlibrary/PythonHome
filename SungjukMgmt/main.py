#main.py

import student_input
import student_calc
import student_output

print("Program is start...")
student = {}                           #학생 dictionary를 만듦
student_input.myinput(student)         #학생의 타입이 dictionary이므로 Call by Reference로 호출
student_calc.calc(student)
student_output.output(student)

print("Program is Over...")