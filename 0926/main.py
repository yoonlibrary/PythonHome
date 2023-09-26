#0926 project
def myfunction(msg):
    """
    This function is a testing function.
    """
    msg_local = msg                  #왼쪽이 지역변수, 오른쪽이 파라미터 변수
    def myfunction_inner():
        return msg_local

    return myfunction_inner

MSG = "Hello, Wolrd"          #문자열은 imutable이고, 그런 문자열을 가진 변수는 상수이므로 대문자로 써야 함
aaa = myfunction(MSG)
print(aaa())
