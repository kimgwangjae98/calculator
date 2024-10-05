"""

editor : Kim Gwang=Jae
date : 2024-10-1

이 파이썬 파일은 공학용 계산기 클래스 EngineeringCalculator에 복소수 연산 기능을 추가한 ComplexCalculator로 이루어져있다.
complex_divide 매서드는 0나누기 오류를 방지하는 코드가 들어가있다.
ComplexCalculator로 EngineeringCalculator에 확장 버전으로 복소수 계산 기능(사칙연산, 절대값, 편각, 좌표계 전환)이 추가되어있다.
ComplexCalculator로 매서드들은 대부분 math 라이브러리의 기능을 이용해 만들었다.
ComplexCalculator는 Calculator, EngineeringCalculator 클래스들을 참조해서 제작하였다.
사칙연산은 Calculator, 그 외의 매서드는 EngineeringCalculator 를 기반으로 제작하였다.
과제 요구사항이 간결하기 때문에 복소수 사칙연산의 입력은 대체로 *args로 받는다.
complex_magnitude, complex_argument, cartesian_to_polar 는 구현상의 이유로 *args, x, **kwargs 를 입력으로 취급한다.

"""
import math  # 곱셈, 나눗셈 함수 작성용
import cmath  # 복소수 편각, 극좌표 변환 매서드 작성용
import utils
from engineering import EngineeringCalculator


class ComplexCalculator(EngineeringCalculator):
    """
    복소수 연산을 수행하는 계산기 클래스입니다.

    복소수의 사칙연산, 절대값, 편각, 좌표계 전환 기능을 제공합니다.
    공학용 계산기 클래스 EngineeringCalculator 를 상속받아 사용합니다.

    Attributes:
        None

    Methods:
        complex_add(*args: complex) -> complex:
            복소수 덧셈 연산을 수행합니다.
        complex_subtract(*args: complex) -> complex:
            복소수 뺄셈 연산을 수행합니다.
        complex_multiply(*args: complex) -> complex:
            복소수 곱셈 연산을 수행합니다.
        complex_divide(*args: complex) -> complex:
            복소수 나눗셈 연산을 수행합니다.
        complex_magnitude(x: complex, **kwargs: dict[str, any]) -> float:
            복소수의 절대값을 계산합니다.
        complex_argument(x: complex, **kwargs: dict[str, any]) -> float:
            복소수의 편각을 계산합니다.
        cartesian_to_polar(*args: any, **kwargs: dict[str, any]) -> any:
            복소수의 좌표계를 직교 좌표계에서 극 좌표계로 또는 극 좌표계에서 직교 좌표계로 변환합니다.

    Args:
        *args (complex): 연산에 사용할 복소수들을 가변 인자로 받습니다.
        x (complex): 복소수의 절대값 또는 편각을 계산할 때 사용할 복소수입니다.
        **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
            - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
            - angle_unit (str): 'degree' 이면 출력이 극좌표형태일 때 라디안에서 각도로 변환해주는 문자열 (예 : angle_unit = 'degree')
            - coordinate (str): 입력이 지평좌표계(cartesian), 극좌표계(polar)인지 표기해주는 문자열. 지평좌표계라면 극좌표계로, 극좌표계라면 지평좌표계로 변환하라는 시지를 내리는 문자열 (예 : coordinate = 'cartesian', coordinate = 'polar')

    Returns:
        complex: 복소수 연산 결과를 반환합니다.
        float: 복소수의 절대값 또는 편각을 반환합니다.
        list: 직교 좌표계에서 극 좌표계로 변환한 결과를 길이와 각도가 든 리스트로 반환합니다. ([길이, 각도])
        complex: 극 좌표계에서 직교 좌표계로 변환한 결과를 복소수로 반환합니다. (x+yj)

    Raises:
        ZeroDivisionError: complex_divide() 메서드에서 0으로 나누는 경우 발생합니다.
    """

    def init(self, *args: complex):
        """현재는 아무런 초기화도 하지 않습니다."""
        pass

    def complex_add(self, *args: complex) -> complex:
        """
        복소수 덧셈 연산을 수행합니다.

        이 매서드는 basic.py의 add 매서드를 기반으로 제작되었습니다.
        복소수 외의 값을 입력받으면 오류가 날 수 있습니다.

        Args:
            *args (complex): 덧셈 연산에 사용할 복소수들을 가변 인자로 받습니다.

        Returns:
            complex: 복소수 덧셈 연산 결과를 반환합니다.

        Examples:
            >>> calc = ComplexCalculator()
            >>> calc.complex_add(1+1j, 2+2j, 3+3j)  
            (6+6j)
        """

        result = sum(args)  # 덧셈 연산 수행

        return result

    def complex_subtract(self, *args: complex) -> complex:
        """
        복소수 뺄셈 연산을 수행합니다.

        가변 인자에 처음으로 들어가는 복소수에서 나머지 복소수들을 뺀 값을 반환합니다.
        이 매서드는 basic.py의 subtract 매서드를 기반으로 제작되었습니다.



        Args:
            *args (complex): 뺄셈 연산에 사용할 복소수들을 가변 인자로 받습니다.

        Returns:
            complex: 복소수 뺄셈 연산 결과를 반환합니다.

        Examples:
            >>> calc = ComplexCalculator()
            >>> calc.complex_subtract(10+10j, 2+5j, 3-5j) 
            (5+10j)

        """

        result = args[0] - sum(args[1:])  # 뺄셈 연산 수행

        return result

    def complex_multiply(self, *args: complex) -> complex:
        """
        복소수 곱셈 연산을 수행합니다.

        복소수의 곱셈 연산을 수행하는 매서드입니다.
        이 매서드는 basic.py의 multiply 매서드를 기반으로 제작되었습니다.

        Args:
            *args (complex): 곱셈 연산에 사용할 복소수들을 가변 인자로 받습니다.

        Returns:
            complex: 복소수 곱셈 연산 결과를 반환합니다.

        Examples:
            >>> calc = ComplexCalculator()
            >>> calc.complex_multiply(2+1j, 3, 4j)
            (-12+24j)

        """

        result = math.prod(args)  # 곱셈 연산 수행

        return result

    def complex_divide(self, *args: complex) -> complex:
        """
        복소수 나눗셈 연산을 수행합니다.

        복소수의 나눗셈 연산을 수행하는 매서드입니다.
        이 매서드는 basic.py의 divide( 매서드를 기반으로 제작되었습니다.
        가변 인자에 처음으로 들어가는 복소수에서 나머지 복소수들로 나눈 값을 반환합니다.
        0으로 나누는 경우 오류를 출력합니다.

        Args:
            *args (complex): 나눗셈 연산에 사용할 복소수들을 가변 인자로 받습니다.

        Returns:
            complex: 복소수 나눗셈 연산 결과를 반환합니다.

        Raises:
            ZeroDivisionError: 0으로 나누는 경우 발생합니다.

        Examples:
            >>> calc = ComplexCalculator()
            >>> calc.complex_divide(100 - 10j, 2)
            (50-5j)

        """

        # 0나누기 오류 발생시 에러났다고 표시
        try:
            result = args[0] / math.prod(args[1:])  # 나눗셈 연산 수행
            return result
        except ZeroDivisionError as e:
            print(" 에러났습니다 : ", e)  # 출력: "Division by zero is not allowed"

    def complex_magnitude(self, x: complex, **kwargs: dict[str, any]) -> float:
        """
        복소수의 절대값을 계산합니다.

        Args:
            x (complex): 절대값을 계산할 복소수입니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)

        Returns:
            float: 복소수의 절대값을 반환합니다.

        Examples:
            >>> calc = ComplexCalculator()
            >>> calc.complex_magnitude(1 + 1j, precision = 4)
            1.4142
        """

        # precision, return_float 키워드 인자를 받음. return_float는 사용안함
        precision, return_float = utils.get_kwarg(**kwargs)

        result = abs(x)  # 절대값 계산 수행
        result = utils.round_result(
            value=result, precision=precision)  # 소수점 자릿수 맞춤

        return result

    def complex_argument(self, x: complex, **kwargs: dict[str, any]) -> float:
        """
        복소수의 편각을 계산합니다.

        Args:
            x (complex): 편각을 계산할 복소수입니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - angle_unit (str): 'degree' 이면 출력이 극좌표 형태일 때 라디안에서 각도로 변환해주는 문자열 (예 : angle_unit = 'degree')

        Returns:
            float: 복소수의 편각을 반환합니다. 키워드 인자에 따라 각도, 라디안 형태를 띕니다.

        Examples:
            >>> calc = ComplexCalculator()
            >>> calc.complex_argument(1+1j, angle_unit = 'degree')
            45.0
            >>> calc.complex_argument(1+1j, precision = 3)
            0.785
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)
        angle_unit = []  # 각도 저장할 변수 생성
        for key, value in kwargs.items():  # angle_unit 키워드 인자 추출
            if key == 'angle_unit':
                angle_unit = value

        result = cmath.phase(x)  # 편각 계산 수행
        result = utils.round_result(
            value=result, precision=precision)  # 소수점 자릿수 맞춤
        if angle_unit == 'degree':
            result = math.degrees(result)
        return result

    def cartesian_to_polar(self, *args: any, **kwargs: dict[str, any]) -> any:
        """
        복소수의 좌표계를 직교 좌표계에서 극 좌표계로 또는 극 좌표계에서 직교 좌표계로 변환합니다.

        coordinate 키워드 인자는 반드시 적어줘야 함수가 정상적으로 동작합니다.
        가변 인자에 들어가는 값의 형식이 극좌표(r,pi)인지, 지평좌표(x+yj)인지 확인하셔야 합니다.
        가변 인자에 복소수가 들어가면 지평좌표계입니다.
        가변 인자에 두 개의 숫자가 들어가면 극좌표계입니다.

        Args:
            *args (any): 좌표계 변환에 사용할 복소수 또는 극좌표 정보를 가변 인자로 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - angle_unit (str): 'degree' 이면 출력이 극좌표형태일 때 라디안에서 각도로 변환합니다. (예 : angle_unit = 'degree')
                - coordinate (str): 입력이 지평좌표계(cartesian), 극좌표계(polar)인지 표기해주는 문자열. 지평좌표계라면 극좌표계로, \
                                    극좌표계라면 지평좌표계로 변환하라는 시지를 내리는 문자열 \
                                    (예 : coordinate = 'cartesian', coordinate = 'polar')

        Returns:
            list: 직교 좌표계에서 극 좌표계로 변환한 결과를 길이와 각도가 포함된 리스트로 반환합니다. ([길이, 각도])
            complex: 극 좌표계에서 직교 좌표계로 변환한 결과를 복소수로 반환합니다. (x+yj)

        Example:
            calc = ComplexCalculator()
            >>> calc.cartesian_to_polar(1+1j, coordinate ='cartesian', precision = 3)
            [1.414, 0.785]
            >>> calc.cartesian_to_polar(1,0, coordinate ='polar')
            (1+0j)
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)
        coordinate = []
        for key, value in kwargs.items():  # 좌표계 키워드 추출
            if key == 'coordinate':
                coordinate = value

        result = 0
        new_result = [0, 0]
        if coordinate == 'cartesian':
            result = cmath.polar(args[0])  # 튜플로 반환
            new_result[0], new_result[1] = utils.round_result(
                value=result[0],
                precision=precision), utils.round_result(
                value=result[1],
                precision=precision)
            # 소수점 맞추기 및 리스트로 전환

            if return_float == 'degree':
                new_result[1] = math.degrees(new_result[1])

        elif coordinate == 'polar':
            result = cmath.rect(args[0], args[1])
            new_result = result

        return new_result


__all__ = ['ComplexCalculator']  # 외부에서 import * 를 사용할 때 노출될 이름들을 명시

if __name__ == '__main__':
    # 클래스 테스트용 코드
    print("Complex Calculator Demo:")
    calc = ComplexCalculator()
    print(calc.complex_add(1+1j, 2+2j, 3+3j))  # 출력: (6+6j)
    print(calc.complex_subtract(10+10j, 2+5j, 3-5j))  # 출력: (5+10j)
    print(calc.complex_multiply(2+1j, 3, 4j))  # 출력: (-12+24j)
    print(calc.complex_divide(100-10j, 2))  # 출력: (50-5j)
    print(calc.complex_magnitude(1+1j, precision=4))  # 출력: 1.4142
    print(calc.complex_argument(1+1j, angle_unit='degree'))  # 출력:45.0
    print(calc.complex_argument(1+1j, precision=3))  # 출력:0.785
    # 출력: [1.414, 0.785]
    print(calc.cartesian_to_polar(1+1j, coordinate='cartesian', precision=3))
    print(calc.cartesian_to_polar(1, 0, coordinate='polar'))  # 출력:0.785

    calc.divide(5, 0)  # 에러처리 확인용 코드
