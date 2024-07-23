import re

def is_valid_email(email):
    # 이메일 주소를 체크하는 정규 표현식
    # ^ : 문자열의 시작
    # [a-zA-Z0-9._%+-]+ : 영문 대소문자, 숫자, 점(.), 밑줄(_), 퍼센트(%), 더하기(+), 빼기(-) 중 하나 이상
    # @ : @ 기호
    # [a-zA-Z0-9]+ : 영문 대소문자, 숫자 중 하나 이상
    # \. : 점(.) 문자
    # [a-zA-Z]{2,} : 영문 대소문자 중 2자 이상
    # $ : 문자열의 끝
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# 유효한 이메일 주소 샘플
valid_emails = [
    "test.email@gmail.com",
    "user.name@example.com",
    "email@subdomain.example.com",
    "firstname.lastname@example.com",
    "email@123.123.123.123",
    "email@example.co.jp",
    "firstname+lastname@example.com",
    "email@example.name",
    "email@example.museum",
    "email@example.travel"
]

# 유효하지 않은 이메일 주소 샘플
invalid_emails = [
    "plainaddress",
    "@missingusername.com",
    "username@.com",
    "username@.com.",
    "username@domain..com",
    "username@domain.com.",
    "username@-domain.com",
    "username@domain-.com",
    "username@domain.com,",
    "username@domain,com"
]

# 테스트 함수
def test_email_validation():
    print("Testing valid emails:")
    for email in valid_emails:
        result = is_valid_email(email)
        print(f"{email}: {result}")
    
    print("\nTesting invalid emails:")
    for email in invalid_emails:
        result = is_valid_email(email)
        print(f"{email}: {result}")

# 테스트 실행
test_email_validation()
