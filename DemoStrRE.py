#DemoStrRE.py

#문자열 변수
data = "<<<  spam and ham  >>>"
result = data.strip("<> ")
print(data)
print(result)

result = result.replace("spam", "spam egg")
print(result)

lst = result.split()
print(lst)
print(":)".join(lst))

strA = "python is very powerful"
print(len(strA))
print(strA.capitalize())
print(strA.upper())
print(strA.lower())


#정규표현식
import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.search("apple", "this is apple")
print(result)
print(result.group())

result = re.search("\d{4}", "올해는 2024년입니다.")
print(result)
print(result.group())