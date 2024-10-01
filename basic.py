"""

editor : Kim Gwang=Jae
date : 2024-10-1

이 파이썬 파일은 사칙연산을 하는 계산기 클래스 Calculator로 이루어져있다.
Calculator 클래스의 add, subtract, multiply, divide 매서드는 사칙연산을 위한 매서드이다.
get_kwarg, prec, fl 는 사칙연산 매서드들의 코드에서 공통적으로 계속 쓰인 코드들은 매서드로 만들어 코드의 길이를 줄이고 보기 쉽게 정리하기 위해 만들었다.
divide 매서드는 0나누기 오류를 방지하는 코드가 들어가있다.
precision은 소수점 자릿수를 결정하는 입력이고 return_float는 결과를 실수(True) 혹은 정수형(False)으로 변환하는데 쓰이는 입력이다.
precision의 초기값은 0, return_float의 초기값은 False이다.

EngineeringCalculator는 Calculator의 확장 버전으로 공학계산 기능이 추가되어있다.
EngineeringCalculator의 매서드들은 대부분 math 라이브러리의 기능을 이용해 만들었고, 소수점 결정 기능과 실수형 변환 기능이 들어가있다.
"""

import math  # 곱셈, 나눗셈 함수 작성용
import utils

class Calculator:
    """
    add, subtract, multiply, divide 매서드는 차례대로 덧셈, 뺄셈, 곱셈, 나눗셈을 처리하는 함수이다.
    위 매서드들은 *args을 써서 여러 숫자들을 입력으로 받는다.
    또한 **kwargs을 써서 조건을 지정해 줄 수 있다.
    kwargs에는 precision = int값, return_float = True or False 값을 사용하며 각각 소수점 자릿수, 출력의 실수형, 정수형을 결정하는 키워드입니다. 
    사칙연산들은 이러한 순서로 동작한다.
    1.get_kwarg을 통해 초기조건들을 불러온다.
    2. 계산을 실시한다.
    3. prec을 통해 소수점 자릿수를 결정짓는다.
    4. fl을 통해 출력의 실수형, 정수형을 결정짓는다.
    5. 변환된 결과를 출력한다.
    
    """
    def init(self, *args:int, **kwargs: dict[str : any]):
        pass

    def add(self, *args:int, **kwargs: dict[str, any])->any:
        '''
        덧셈합을 계산하는 매서드. add(1,2,3) = 1+2+3 = 6 을 반환함
        '''
        r, f = utils.get_kwarg(**kwargs)

        result = sum(args)
        result = utils.round_result(value=result, precision=r)
        result = utils.fl(result=result, f=f)

        return result

    def subtract(self, *args:int, **kwargs: dict[str, any])->any:
        '''
        args[0]은 처음 값, sum(args[1:])는 빼야할 값들의 합으로 퉁쳐서 뺌.
        subtract(10,2,3) = 10-2-3 = 5 을 반환함.
        명확히 할려면 args[0] 대신 새로운 변수를 만들 수 있으나 매서드 입력의 통일성을 위해 *args, **kwargs로 통일함
        '''
        r, f = utils.get_kwarg(**kwargs)

        result = args[0] - sum(args[1:])
        result = utils.round_result(value=result, precision=r)
        result = utils.fl(result=result, f=f)

        return result

    def multiply(self, *args:int, **kwargs: dict[str, any])->any:
        '''
        math.prod를 사용해서 곱셈합을 계산함. multiply(3,4,5) = 3*4*5 = 60을 반환함
        '''
        r, f = utils.get_kwarg(**kwargs)

        result = math.prod(args)
        result = utils.round_result(value=result, precision=r)
        result = utils.fl(result=result, f=f)

        return result

    def divide(self, *args:int, **kwargs: dict[str, any])->any:
        '''
        math.prod(args[1:]) 로 나눌 값들의 곱셈을 계산해서 합치고 처음값 args[0]에 나눠버림
        divide(100,2,5,2) = 100/2/5/2 = 5 을 반환함
        명확히 할려면 args[0] 대신 새로운 변수를 만들 수 있으나 매서드 입력의 통일성을 위해 *args, **kwargs로 통일함        
        '''
        r, f = utils.get_kwarg(**kwargs)

        # 0나누기 오류 발생시 에러났다고 표시
        try:
            result = args[0] / math.prod(args[1:])
            result = utils.round_result(value=result, precision=r)
            result = utils.fl(result=result, f=f)
            return result
        except ZeroDivisionError as e:
            print(" 에러났습니다 : ",e)  # 출력: "Division by zero is not allowed"


__all__ = ['Calculator'] # 외부에서 import * 를 사용할 때 노출될 이름들을 명시

if __name__ == '__main__':
    # 클래스 테스트용 코드
    print("Basic Calculator Demo:")
    calc = Calculator()
    print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00
    print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0
    print(calc.multiply(2, 3, 4))  # 출력: 24
    print(calc.divide(100, 2, precision=3))  # 출력: 50.000
    
