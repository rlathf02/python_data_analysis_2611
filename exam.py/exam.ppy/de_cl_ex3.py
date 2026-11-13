
"""

print("===== 1단계: 함수 안에 함수 만들기 =====")

# 파이썬에서는 함수 안에 또 다른 함수를 정의할 수 있습니다.
def outer():
    print("outer 함수가 실행되었습니다.")

    def inner():
        print("inner 함수가 실행되었습니다.")

    # inner 함수를 실행하는 것이 아니라,
    # 함수 자체를 반환합니다.
    return inner

# outer()를 실행하면 inner 함수가 반환됩니다.
func = outer()
func()

"""
#설명:
#-outer()를 실행하면 inner 함수가 반환됩니다.
#func는 inner 함수를 가리키게 됩니다.
#즉, 파이썬에서는 함수를 값처럼 다룰 수 있습니다.
"""

print("\n===== 2단계: 클로저(Closure) =====")

# 클로저는 '외부 함수의 변수를 기억하는 내부 함수'입니다.
def make_multiplier(x):
    # x는 make_multiplier 함수의 지역 변수입니다.

    def multiplier(n):
        # 내부 함수 multiplier는
        # 바깥 함수의 변수 x를 사용하고 있습니다.
        return x * n

    return multiplier

times3 = make_multiplier(3)

print(times3(10))  # 30
print(times3(5))   # 15

"""
#설명:
#- make_multiplier(3)을 실행하면 multiplier 함수가 생성됩니다.
#- 이 multiplier 함수는 x=3이라는 값을 기억합니다.
#- 이렇게 내부 함수가 외부 변수 값을 기억하는 구조를 '클로저'라고 합니다.
"""

print("\n===== 3단계: 데코레이터 기본 구조 =====")

# 데코레이터는 '함수를 꾸며주는 함수'입니다.
# 내부 구조는 클로저와 매우 유사합니다.

def decorator(func):
    # func는 꾸며줄 함수입니다.

    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")

    return wrapper

def say_hello():
    print("안녕하세요.")

decorated = decorator(say_hello)
decorated()

"""
#설명:
#- decorator는 함수를 하나 받아서,
#- wrapper라는 새로운 함수를 만들어 반환합니다.
#- wrapper 안에서 원래 함수(func)를 실행합니다.
#- 이렇게 기존 함수에 기능을 추가하는 구조를 데코레이터라고 합니다.
"""

print("\n===== 4단계: @데코레이터 문법 =====")

# 위에서 했던 과정을 더 간단하게 표현하는 문법이 @입니다.

def my_decorator(func):
    def wrapper():
        print("실행 전")
        func()
        print("실행 후")
    return wrapper

@my_decorator
def greet():
    print("반갑습니다.")

greet()

"""
#설명:
#- @my_decorator는 아래 코드와 같은 의미입니다.

#    greet = my_decorator(greet)

#- 즉, greet 함수를 자동으로 감싸서(wrapper) 실행합니다.

''''
print("\n===== 5단계: 클로저와 데코레이터 비교 =====")


[클로저]
- 함수 안에 함수가 있습니다.
- 내부 함수가 외부 변수 값을 기억합니다.
- 주로 '상태를 유지하는 함수'를 만들 때 사용됩니다.

[데코레이터]
- 함수를 인자로 받아 새로운 함수로 감쌉니다.
- 기존 함수에 기능을 추가합니다.
- 로그 출력, 실행 시간 측정 등에 사용됩니다.

[관계]
- 데코레이터의 내부 구조는 클로저입니다.
- wrapper 함수가 func를 기억하고 있기 때문에 동작합니다.


print("\n===== 6단계: 매개변수가 있는 데코레이터 =====")

def decorator_with_args(func):
    def wrapper(name):
        print("실행 전")
        func(name)
        print("실행 후")
    return wrapper

@decorator_with_args
def say_name(name):
    print("이름:", name)

say_name("길동")


설명:
- 원래 함수에 매개변수가 있다면,
wrapper에서도 동일하게 받아야 합니다.
- 그렇지 않으면 실행 시 오류가 발생합니다.


print("\n===== 최종 정리 =====")

1. 클로저는 외부 변수 값을 기억하는 함수입니다.
2. 데코레이터는 함수를 감싸서 기능을 추가하는 구조입니다.
3. 데코레이터는 내부적으로 클로저 구조를 사용합니다.
4. 두 개념은 함수가 '함수를 반환한다'는 점에서 공통
'''