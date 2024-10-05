"""

editor : Kim Gwang-Jae
date : 2024-10-1

이 파이썬 파일은 사칙연산을 하는 계산기 클래스 Calculator로 이루어져있다.
Calculator 클래스의 add, subtract, multiply, divide 매서드는 사칙연산을 위한 매서드이다.
get_kwarg, prec, fl 는 사칙연산 매서드들의 코드에서 공통적으로 계속 쓰인 코드들은 매서드로 만들어 코드의 길이를 줄이고 보기 쉽게 정리하기 위해 만들었다.
divide 매서드는 0나누기 오류를 방지하는 코드가 들어가있다.
precision은 소수점 자릿수를 결정하는 입력이고 return_float는 결과를 실수(True) 혹은 정수형(False)으로 변환하는데 쓰이는 입력이다.
precision의 초기값은 0, return_float의 초기값은 False이다.

"""

import math  # 곱셈, 나눗셈 함수 작성용
import utils


class Calculator:
    """
    사칙연산을 수행하는 계산기 클래스입니다.

    사칙연산을 수행하는 계산기에 소수점 자릿수 설정 기능과 실수형 반환 여부 기능을 추가한 계산기입니다.
    반환값이 any로 str, int, float로 다양하니 print문으로 출력할 때만 사용하길 권장합니다.

    Attributes:
        None

    Methods:
        add(*args: int, **kwargs: dict[str, any]) -> any:
            덧셈 연산을 수행합니다.
        subtract(*args: int, **kwargs: dict[str, any]) -> any:
            뺄셈 연산을 수행합니다.
        multiply(*args: int, **kwargs: dict[str, any]) -> any:
            곱셈 연산을 수행합니다.
        divide(*args: int, **kwargs: dict[str, any]) -> any:
            나눗셈 연산을 수행합니다.

    Args:
        *args (int): 연산에 사용할 숫자들을 가변 인자로 받습니다.
        **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
            - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
            - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)

    Returns:
        any: 연산 결과를 반환합니다.

    Raises:
        ZeroDivisionError: divide() 메서드에서 0으로 나누는 경우 발생합니다.

    Process:
        1. 연산 조건을 지정하는 키워드를 저장합니다.
        2. 연산을 수행합니다.
        3. 소수점 자릿수를 맞춥니다.
        4. 결과를 실수형으로 반환할지 지정합니다.
        5. 변환된 결과를 반환합니다.

    """

    def init(self, *args: int, **kwargs: dict[str: any]):
        pass

    def add(self, *args: int, **kwargs: dict[str, any]) -> any:
        """
        덧셈 연산을 수행합니다.



        Args:
            *args (int): 덧셈에 사용할 숫자들을 가변 인자로 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)

        Returns:
            any: 덧셈 결과를 반환합니다.

        Examples:
            >>> calc = Calculator()
            >>> calc.add(1, 2, 3)
            6
            >>> calc.add(1, 2, 3, precision=2)
            6.00
            >>> calc.add(1, 2, 3, return_float=True)
            6.0
        """

        # precision, return_float 키워드 인자를 받음  # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)

        result = sum(args)  # 덧셈 연산 수행
        # 소수점 자릿수 맞춤 # 소수점 자릿수 맞춤
        result = utils.round_result(value=result, precision=precision)
        # 결과를 실수형으로 반환할지 지정 # 결과를 실수형으로 반환할지 지정
        result = utils.fl(result=result, return_float=return_float)

        return result

    def subtract(self, *args: int, **kwargs: dict[str, any]) -> any:
        """
        뺄셈 연산을 수행합니다.

        가변 인자에 처음으로 들어가는 숫자에서 나머지 숫자들을 뺀 값을 반환합니다.

        Args:
            *args (int): 뺄셈에 사용할 숫자들을 가변 인자로 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)

        Returns:
            any: 뺄셈 결과를 반환합니다.

        Examples:
            >>> calc = Calculator()
            >>> calc.subtract(10, 2, 3)
            5
            >>> calc.subtract(10, 2, 3, precision=2)
            5.00
            >>> calc.subtract(10, 2, 3, return_float=True)
            5.0
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)

        result = args[0] - sum(args[1:])  # 뺄셈 연산 수행
        result = utils.round_result(
            value=result, precision=precision)  # 소수점 자릿수 맞춤
        # 결과를 실수형으로 반환할지 지정
        result = utils.fl(result=result, return_float=return_float)

        return result

    def multiply(self, *args: int, **kwargs: dict[str, any]) -> any:
        """
        곱셈 연산을 수행합니다.

        Args:
            *args (int): 곱셈에 사용할 숫자들을 가변 인자로 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)

        Returns:
            any: 곱셈 결과를 반환합니다.

        Examples:
            >>> calc = Calculator()
            >>> calc.multiply(2, 3, 4)
            24
            >>> calc.multiply(2, 3, 4, precision=2)
            24.00
            >>> calc.multiply(2, 3, 4, return_float=True)
            24.0
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)

        result = math.prod(args)  # 곱셈 연산 수행
        result = utils.round_result(
            value=result, precision=precision)  # 소수점 자릿수 맞춤
        # 결과를 실수형으로 반환할지 지정
        result = utils.fl(result=result, return_float=return_float)

        return result

    def divide(self, *args: int, **kwargs: dict[str, any]) -> any:
        """
        나눗셈 연산을 수행합니다.

        가변 인자에 처음으로 들어가는 숫자에서 나머지 숫자들로 나눈 값을 반환합니다.
        0으로 나누는 경우 오류를 출력합니다.

        Args:
            *args (int): 나눗셈에 사용할 숫자들을 가변 인자로 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)

        Returns:
            any: 나눗셈 결과를 반환합니다.

        Raises:
            ZeroDivisionError: 0으로 나누는 경우 발생합니다.

        Examples:
            >>> calc = Calculator()
            >>> calc.divide(100, 2)
            50
            >>> calc.divide(100, 2, precision=3)
            50.000
            >>> calc.divide(100, 2, return_float=True)
            50.0
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)

        # 0나누기 오류 발생시 에러났다고 표시
        try:
            result = args[0] / math.prod(args[1:])  # 나눗셈 연산 수행
            result = utils.round_result(
                value=result, precision=precision)  # 소수점 자릿수 맞춤
            # 결과를 실수형으로 반환할지 지정
            result = utils.fl(result=result, return_float=return_float)
            return result
        except ZeroDivisionError as e:
            print(" 에러났습니다 : ", e)  # 출력: "Division by zero is not allowed"


__all__ = ['Calculator']  # 외부에서 import * 를 사용할 때 노출될 이름들을 명시

if __name__ == '__main__':
    # 클래스 테스트용 코드
    print("Basic Calculator Demo:")
    calc = Calculator()
    print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00
    print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0
    print(calc.multiply(2, 3, 4))  # 출력: 24
    print(calc.divide(100, 2, precision=3))  # 출력: 50.000
