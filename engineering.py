"""

editor : Kim Gwang=Jae
date : 2024-10-1

이 파이썬 파일은 사칙연산을 하는 계산기 클래스 Calculator에 공학용 계산 기능을 추가한 EngineeringCalculator로 이루어져있다.
precision은 소수점 자릿수를 결정하는 입력이고 return_float는 결과를 실수(True) 혹은 정수형(False)으로 변환하는데 쓰이는 입력이다.
EngineeringCalculator는 Calculator의 확장 버전으로 공학계산 기능(제곱근, 제곱, 로그, 삼각함수 계산)이 추가되어있다.
EngineeringCalculator의 매서드들은 대부분 math 라이브러리의 기능을 이용해 만들었고, 소수점 결정 기능과 실수형 변환 기능이 들어가있다.
"""

import math
import utils
from basic import Calculator


class EngineeringCalculator(Calculator):
    """
    EngineeringCalculator는 square_root, power, log, ln, sin, cos, tan 가 Calculator에 추가된 클래스이다.
    square_root, power, log, ln, sin, cos, tan 매서드는 차례대로 제곱근, 거듭제곱, 로그, 자연로그, 사인, 코사인, 탄젠트을 처리하는 함수이다.
    위 매서드들은 x을 써서 숫자를 입력으로 받는다.
    power의 입력 y는 거듭제곱을 의미한다.
    또한 **kwargs을 써서 조건을 지정해 줄 수 있다. 
    kwargs에는 precision = int값, return_float = True or False 값을 사용하며 각각 소수점 자릿수, 출력의 실수형, 정수형을 결정하는 키워드입니다. 
    sin, cos, tan 매서드는 angle_unit으로 입력값이 degree인지, raidans인지 표시해주는 키워드가 있으며 기본값은 degree이다.
    angle_raidans 매서드는 degree로 받은 입력x를 raidans으로 변환해주는 함수이다.


    매서드들은 이러한 순서로 동작한다.
    1.get_kwarg을 통해 초기조건들을 불러온다.
    1-2. sin, cos, tan은 angle_raidans 매서드를 거쳐 키워드를 통해 입력이 각도인지, 라디안인지 확인하고 각도이면 라디안으로 변환한다.
    2. 계산을 실시한다.
    3. prec을 통해 소수점 자릿수를 결정짓는다.
    4. fl을 통해 출력의 실수형, 정수형을 결정짓는다.
    5. 변환된 결과를 출력한다.

    Attributes:
        None

    Methods:
        square_root(self, x: float, **kwargs: dict[str, any]) -> any:
            제곱근 연산을 수행합니다.
        power(self, x: float, y: float, **kwargs: dict[str, any]) -> any:
            거듭제곱 연산을 수행합니다.
        log(self, x: float, **kwargs: dict[str, any]) -> any:
            밑이 10인 로그 연산을 수행합니다.
        ln(self, x: float, **kwargs: dict[str, any]) -> any:
            자연로그 연산을 수행합니다.
        sin(self, x: float, **kwargs: dict[str, any]) -> any:
            사인 연산을 수행합니다.
        cos(self, x: float, **kwargs: dict[str, any]) -> any:
            코사인 연산을 수행합니다.
        tan(self, x: float, **kwargs: dict[str, any]) -> any:
            탄젠트 연산을 수행합니다.

    Args:
        *args (complex): 연산에 사용할 복소수들을 가변 인자로 받습니다.
        x (complex): 복소수의 절대값 또는 편각을 계산할 때 사용할 복소수입니다.
        **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
            - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
            - angle_unit (str): 'degree' 이면 출력이 극좌표형태일 때 라디안에서 각도로 변환합니다. (예 : angle_unit = 'degree')

    Returns:
        any: 연산 결과를 반환합니다.

    """

    def init(self, **kwargs):
        pass

    def square_root(self, x: float, **kwargs: dict[str, any]) -> any:
        """
        제곱근. x=16 이면 결과로 4를 반환합니다.

        Args:
            x (int): 제곱근을 구할 숫자를 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)

        Returns:
            any: 제곱근 결과을 반환합니다.

        Examples:
            >>> eng_calc = EngineeringCalculator()
            >>> eng_calc.square_root(16, precision=3)
            4.000
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)

        result = math.sqrt(x)  # 제곱근 연산을 수행
        result = utils.round_result(
            value=result, precision=precision)  # 소수점 자릿수 맞춤
        # 결과를 실수형으로 반환할지 지정
        result = utils.fl(result=result, return_float=return_float)

        return result

    def power(self, x: float, y: float, **kwargs: dict[str, any]) -> any:
        """
        거듭제곱. x^y 이며 x=2, y=3 이면 2^3=8을 반환합니다.

        Args:
            x (int): 거듭제곱을 구할 숫자를 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)

        Returns:
            any: 거듭제곱 결과를 반환합니다.

        Examples:
            >>> eng_calc = EngineeringCalculator()
            >>> eng_calc.power(2,3)
            8
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)

        result = math.pow(x, y)  # 거듭제곱 연산을 수행
        result = utils.round_result(
            value=result, precision=precision)  # 소수점 자릿수 맞춤
        # 결과를 실수형으로 반환할지 지정
        result = utils.fl(result=result, return_float=return_float)

        return result

    def log(self, x: float, **kwargs: dict[str, any]) -> any:
        """
        로그. 밑이 10인 로그 매서드입니다. x=100 이면 log100=2를 반환합니다.

        Args:
            x (int): 밑이 10인 로그를 구할 숫자를 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)

        Returns:
            any: 밑이 10인 로그 결과 반환합니다.

        Examples:
            >>> eng_calc = EngineeringCalculator()
            >>> eng_calc.log(100)
            2
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)

        result = math.log10(x)  # 밑이 10인 로그 연산을 수행
        result = utils.round_result(
            value=result, precision=precision)  # 소수점 자릿수 맞춤
        # 결과를 실수형으로 반환할지 지정
        result = utils.fl(result=result, return_float=return_float)

        return result

    def ln(self, x: float, **kwargs: dict[str, any]) -> any:
        """
        자연로그. 밑이 e인 자연로그 매서드입니다. x=e(자연상수) 이면 lne=1을 반환합니다.

        Args:
            x (int): 자연로그를 구할 숫자를 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)

        Returns:
            any: 자연로그 결과를 반환합니다.

        Examples:
            >>> eng_calc = EngineeringCalculator()
            >>> eng_calc.ln(1)
            0
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)

        result = math.log(x)  # 자연로그 연산을 수행
        result = utils.round_result(
            value=result, precision=precision)  # 소수점 자릿수 맞춤
        # 결과를 실수형으로 반환할지 지정
        result = utils.fl(result=result, return_float=return_float)

        return result

    def sin(self, x: float, **kwargs: dict[str, any]) -> any:
        """
        사인. 각도 혹은 라디안 x를 입력하고 키워드로 angle_unit = 'degree' 가 입력되면 라디안 값으로 변환하여 sin값을 계산해 결과값을 반환합니다.

        Args:
            x (int): 사인값을 구할 숫자를 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)
                - angle_unit (str): 'degree' 이면 출력이 극좌표형태일 때 라디안에서 각도로 변환합니다. (예 : angle_unit = 'degree')

        Returns:
            any: 사인 결과를 반환합니다.

        Examples:
            >>> eng_calc = EngineeringCalculator()
            >>> eng_calc.sin(30, angle_unit='degree', precision=4)
            0.5000
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)

        x = utils.convert_to_radians(x=x, **kwargs)  # 각도를 라디안으로 변환

        result = math.sin(x)  # 사인 연산을 수행
        result = utils.round_result(
            value=result, precision=precision)  # 소수점 자릿수 맞춤
        # 결과를 실수형으로 반환할지 지정
        result = utils.fl(result=result, return_float=return_float)

        return result

    def cos(self, x: float, **kwargs: dict[str, any]) -> any:
        """
        코사인. 각도 혹은 라디안 x를 입력하고 키워드로 angle_unit = 'degree' 가 입력되면 라디안 값으로 변환하여 cos값을 계산해 결과값을 반환합니다.

        Args:
            x (int): 코사인 값을 구할 숫자를 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)
                - angle_unit (str): 'degree' 이면 출력이 극좌표형태일 때 라디안에서 각도로 변환합니다. (예 : angle_unit = 'degree')

        Returns:
            any: 코사인 결과를 반환합니다.

        Examples:
            >>> eng_calc = EngineeringCalculator()
            >>> eng_calc.cos(60, angle_unit='degree')
            0.5
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)
        x = utils.convert_to_radians(x=x, **kwargs)  # 각도를 라디안으로 변환

        result = math.cos(x)  # 코사인 연산을 수행
        result = utils.round_result(
            value=result, precision=precision)  # 소수점 자릿수 맞춤
        # 결과를 실수형으로 반환할지 지정
        result = utils.fl(result=result, return_float=return_float)

        return result

    def tan(self, x: float, **kwargs: dict[str, any]) -> any:
        """
        탄젠트. 각도 혹은 라디안 x를 입력하고 키워드로 angle_unit = 'degree' 가 입력되면 라디안 값으로 변환하여 tan값을 계산해 결과값을 반환합니다.

        Args:
            x (int): 탄젠트 값을 구할 숫자를 받습니다.
            **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
                - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
                - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)
                - angle_unit (str): 'degree' 이면 출력이 극좌표형태일 때 라디안에서 각도로 변환합니다. (예 : angle_unit = 'degree')

        Returns:
            any: 탄젠트 결과를 반환합니다.

        Examples:
            >>> eng_calc = EngineeringCalculator()
            >>> eng_calc.tan(0, angle_unit = 'degree')
            0
        """

        # precision, return_float 키워드 인자를 받음
        precision, return_float = utils.get_kwarg(**kwargs)
        x = utils.convert_to_radians(x=x, **kwargs)  # 각도를 라디안으로 변환

        result = math.tan(x)  # 탄젠트 연산을 수행
        result = utils.round_result(
            value=result, precision=precision)  # 소수점 자릿수 맞춤
        # 결과를 실수형으로 반환할지 지정
        result = utils.fl(result=result, return_float=return_float)

        return result


__all__ = ['EngineeringCalculator']  # 외부에서 import * 를 사용할 때 노출될 이름들을 명시

if __name__ == '__main__':
    # 클래스 테스트용 코드
    print("Engineering Calculator Demo:")
    eng_calc = EngineeringCalculator()
    print(eng_calc.add(1, 2, 3, precision=2))  # 출력: 6.00
    print(eng_calc.square_root(16, precision=3))  # 출력: 4.000
    print(eng_calc.log(100, precision=4))  # 출력: 2.0000
    print(eng_calc.sin(30, angle_unit='degree', precision=4))  # 출력: 0.5000

    eng_calc.divide(5, 0)  # 에러처리 확인용 코드
