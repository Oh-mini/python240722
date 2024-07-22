# Demofunc.py

#함수정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수:", x)

#호출
retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

#호출
print(swap(3,4))

#기본값 명시
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드 인자: 매개변수명 기술
def connectURI(server, port):
    strURL = "https://" + server + ":" + port
    return strURL

#호출
print(connectURI("multi.com", "80"))
print(connectURI(port="8080", server="multi.com"))

#이름해석 : LGB이름 해석 규칙
x = 5       #전역변수
def func(a):
    return a+x

#호출
print(func(1))

def func2(a):
    x = 1   #지역변수
    return a+x

#호출
print(func2(1))


#가변인자 : *를 함수 인자 앞에 붙이면 정해지지 않은 수의 인자를 받겠다는 의미
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))