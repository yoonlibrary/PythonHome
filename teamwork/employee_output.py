# 최태윤
# 출력 프로그램

def output(employee) :
    name="<<급여 관리 프로그램>>"
    detail="사번\t급수\t호\t수당\t지급액\t세금\t차인지급액"
    program=name.center(50)
    
    print(f"{program}")
    print("-----------------------------------------------------------")
    print(f"{detail}\t")
    print("-----------------------------------------------------------")
    print(f"{employee['employeeNumber']}\t{employee['gLevel']}\t{employee['hLevel']}\t{employee['bonus']}\t{employee['gMoney']}\t{employee['tax']}\t{employee['cMoney']}\t")
    print("-----------------------------------------------------------")