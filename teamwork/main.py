# 최태윤, 이한재, 양재준

import employee_input
import employee_output
import employee_calc

print('Prigram is Starting...')
employee = {}
employee_input.myInput(employee) # Call by Reference
employee_calc.calc(employee)
employee_output.output(employee)

print('Program is Shutting down...')
