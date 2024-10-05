"""

editor : Kim Gwang=Jae
date : 2024-10-1

이 파이썬 파일은 사칙연산을 하는 계산기 클래스 Calculator 와 EngineeringCalculator 를 보조하는 함수들로 이루어져있다.
Calculator 클래스의 add, subtract, multiply, divide 매서드는 사칙연산을 위한 매서드이다.
get_kwarg, round_result, fl, convert_to_radians 는 사칙연산 매서드들의 코드에서 공통적으로 계속 쓰인 코드들은 매서드로 만들어 코드의 길이를 줄이고 보기 쉽게 정리하기 위해 만들었다.
**kwargs 에 들어가는 키워드로는 'precision', 'return_float', 'angle_unit' 이다.
precision은 소수점 자릿수를 결정하는 입력이고 return_float는 결과를 실수(True) 혹은 정수형(False)으로 변환하는데 쓰이는 입력이다.
precision의 초기값은 0, return_float의 초기값은 False이다.
precision=3, return_float=True or False, angle_unit = 'degree' 로 쓰인다.

get_kwarg 는 키워드 파라미터에서 precision, return_float 의 value 값을 추출한다.
round_result 는 입력한 값을 precision값에 맞춰 소수점 자릿수에 맞춰서 변환해주는 함수이다.
fl 는 return_float = True 이면 부동소수점으로 변환해주는 함수이다.
convert_to_radians 는 angle_unit = 'degree' 이면 degree 각도를 radians 값으로 변환해주는 함수이다.
"""

import math  # 곱셈, 나눗셈, 공학용 함수 작성용


# precision, return_float 값들 추출하는 매서드.
def get_kwarg(**kwargs: dict[str: any]) -> any:
    """
    키워드 파라미터를 입력받아 precision의 값(정수), return_float의 값(부울)을 변수로 반환합니다.
    precision의 기본값(소수점은 없다!)을 0으로 설정했습니다.
    return_float의 기본값(float가 아님!)을 False로 설정했습니다.
    add, subtract, multiply, divide 매서드 내부에서 동작하는 매서드입니다.

    Args:
        **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
            - precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)
            - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)

    Returns:
        any: 추출한 연산 조건들을 반환합니다.

    """
    precision = 0
    return_float = False
    for key, value in kwargs.items():
        if key == 'precision':
            precision += value
        elif key == 'return_float':
            return_float = value
    return precision, return_float

# precision 에 맞춰 소수점을 맞춰주는 함수. 값을 문자열로 변환해서 0값을 소수점에 추가함


def round_result(value: float, precision: int) -> any:
    """
    get_kwarg에서 출력된 precision값과 사칙연산을 거친 출력값result을 입력받아 precision 에 맞춰 소수점을 맞춰 반환합니다.
    result의 소수점 자릿수 갯수가 precision=precision의 값보다 작으면 작은 만큼 0을 채워 넣어서 반환합니다.
    반환값은 int, float, str로 다양합니다. 
    add, subtract, multiply, divide 매서드 내부에서 동작하는 매서드입니다.

    먼저 precision값이 존재한다면 round함수로 소수점을 맞춰줍니다. precision값보다 result값의 소수점 자릿수가 많으면 잘라주는 역할을 합니다.
    그다음 소수점 자릿수를 맞추기 위해 result 형식을 문자열 형태로 변환합니다.

    이후 result값이 정수형이라면 '.'까지 붙여서 소수점 자릿수를 0으로 채워줍니다.
    정수형이 아닌 부동소수점 형식이라면 자릿수도 계산한 후 빈 소수점 자릿수를 0으로 채워줍니다.

    Args:
        value (float): 소수점 자릿수를 바꿀 값을 받습니다.
        precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)

    Returns:
        any: 소수점 자릿수를 바꾼 값을 반환합니다.
    """
    # precision 값이 주어진다면 소수점 자릿수 맞추기 실행
    if precision:
        value = round(value, precision)  # 소수점을 먼저 맞춤
        value = str(value)  # 소수점 자릿수를 맞추기 위해 문자열 형태로 변환

        # 정수형이면 소수점 갯수만큼.0 을 붙임. 아니면 자릿수 맞춰서 0 붙임
        if value.find(".") == -1:
            value = value + '.' + precision*'0'
        else:
            dot = value.find(".")  # 점의 위치를 찾음
            zeros = len(value[dot+1:])  # 점의 위치로 뒤의 숫자가 몇개있는지 확인함
            value = value + (precision-zeros)*"0"  # 뒤의 숫자도 고려해 0붙이기
    else:
        pass
    return value


def fl(result: float, return_float: bool) -> float:
    """
    get_kwarg에서 출력된 f값과 사칙연산을 거친 출력값result을 입력받아 return_float 에 맞춰 소수점을 맞춰 반환합니다.
    f는 True or False 값을 가지며 True 값이면 입력 result를 부동소수점으로 변환하여 반환합니다. 아니면 그대로 반환합니다. 

    Args:
        value (float): 소수점 자릿수를 바꿀 값을 받습니다.
        precision (int): 소수점 자릿수를 지정합니다. (기본값: 0)

    Returns:
        any: 소수점 자릿수를 바꾼 값을 반환합니다.
    """
    if return_float:
        result = float(result)
    else:
        pass
    return result


def convert_to_radians(x: float, **kwargs: dict[str, any]) -> any:
    """
    디그리로 설정된 각도(입력x)를 라디안으로 변환해 출력하는 매서드. 키워드 파라미터kwargs 를 이용한다.
    angle_unit = 'degree' 키워드가 있으면 입력 x를 degree에서 라디안으로 변환한 값을 반환합니다.
    angle_raidans(180, angle_unit = 'degree') = 3.141592

    Args:
        x (float): 각도를 받습니다.
        **kwargs (dict[str, any]): 연산 조건을 지정하는 키워드 인자를 받습니다.
            - angle_unit (str): 'degree' 이면 출력이 극좌표형태일 때 라디안에서 각도로 변환합니다. (예 : angle_unit = 'degree')
            - return_float (bool): 결과를 실수형으로 반환할지 여부를 지정합니다. (기본값: False)


    Returns:
        any: 변환한 값을 반환합니다.
    """
    for key, value in kwargs.items():
        if key == 'angle_unit' and value == 'degree':
            x = math.radians(x)
        else:
            pass

    return x
