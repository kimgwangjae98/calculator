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
import cmath # 복소수 편각, 극좌표 변환 매서드 작성용
import utils
from engineering import EngineeringCalculator


class ComplexCalculator(EngineeringCalculator):
    """
    complex_add, complex_subtract, complex_multiply, complex_divide 매서드는 차례대로 덧셈, 뺄셈, 곱셈, 나눗셈을 처리하는 함수이다.
    위 매서드들은 *args을 써서 여러 숫자들을 입력으로 받는다.
    basic과 engineering과 달리 **kwargs을 써서 조건을 지정하지 않는다.
    complex_divide는 0나누기 오류도 처리할 수 있다.
    사칙연산들은 이러한 순서로 동작한다.
    1. 다수의 복소수들을 입력받는다. 
    2. 계산을 실시한다.
    3. 복소수 결과를 반환한다.
    
    complex_magnitude, complex_argument, cartesian_to_polar 매서드는 차례대로 절대값, 편각, 좌표계 전환을 처리하는 함수이다.
    complex_magnitude, complex_argument는 복소수 입력 x와 키워드 **kwargs을 입력받는다.
    cartesian_to_polar는 입력 *args 와 키워드 **kwargs을 입력받는다.

    """

    def init(self, *args: complex):
        pass

    def complex_add(self, *args: complex) -> complex:
        '''
        복소수의 덧셈합을 계산하는 매서드. 
        complex_add(1 + 1j, 2 + 2j, 3 + 3j) = (1+1j+2+2j+3+3j) = (6+6j) 을 반환함
        다수의 복소수들을 입력받기 위해 *args를 사용함
        '''

        result = sum(args)

        return result

    def complex_subtract(self, *args: complex) -> complex:
        '''
        복소수의 뺄셈을 계산하는 매서드
        args[0]은 처음 값, sum(args[1:])는 빼야할 값들의 합으로 퉁쳐서 뺌.
        complex_subtract(10 + 10j, 2 + 5j, 3 - 5j) = (10+10j-(2+5j+3-5j)) = (5+10j) 을 반환함.
        다수의 복소수들을 입력받기 위해 *args를 사용함
        '''

        result = args[0] - sum(args[1:])

        return result

    def complex_multiply(self, *args: complex) -> complex:
        '''
        math.prod를 사용해서 복소수의 곱셈합을 계산함. 
        complex_multiply(2 + 1j, 3, 4j) = (2+1j)*3*4j = (-12+24j)을 반환함
        다수의 복소수들을 입력받기 위해 *args를 사용함
        
        '''

        result = math.prod(args)

        return result

    def complex_divide(self, *args: complex) -> complex:
        '''
        복소수 나눗셈을 계산하는 매서드.
        math.prod(args[1:]) 로 나눌 값들의 곱셈을 계산해서 합치고 처음값 args[0]에 나눠버림.
        complex_divide(100 - 10j, 2) = (100-10j)/2 = (50-5j) 을 반환함.
        다수의 복소수들을 입력받기 위해 *args를 사용함.
        0나누기 오류를 발견하는 기능 탑재.
        '''

        # 0나누기 오류 발생시 에러났다고 표시
        try:
            result = args[0] / math.prod(args[1:])
            return result
        except ZeroDivisionError as e:
            print(" 에러났습니다 : ", e)  # 출력: "Division by zero is not allowed"

    def complex_magnitude(self, x:complex,**kwargs: dict[str, any]) -> float:
        '''
        복소수의 절대값을 계산하는 매서드.
        복소수 x를 입력받아 복소수의 절대값을 실수형으로 반환한다.
        입력받을 수 있는 키워드는 precision=int.
        키워드로 precision를 입력받아 소수점 자릿수를 설정할수있다.
        complex_magnitude(1 + 1j, precision = 4) = 1.4142
        이러한 순서로 동작한다.
        1. 복소수와 키워드들을 입력받는다. 
        2. 계산을 실시한다.
        3. prec을 통해 소수점 자릿수를 결정짓는다.
        4. 변환된 결과를 출력한다.
        '''
        r, f = utils.get_kwarg(**kwargs)

        result = abs(x)
        result = utils.round_result(value=result, precision=r)
        
        return result

    def complex_argument(self, x:complex,**kwargs: dict[str, any]) -> float:
        '''
        복소수의 절대값을 계산하는 매서드.
        복소수 x를 입력받아 복소수의 절대값을 실수형으로 반환한다.
        입력받을 수 있는 키워드는 precision=int, angle_unit = 'degree'
        키워드로 precision를 입력받아 소수점 자릿수를 설정할수있다.
        키워드로 angle_unit를 degree로 입력받아 라디안을 각도로 변환할 수 있다.
        complex_argument(1+1j, angle_unit = 'degree') = 45.0
        complex_argument(1+1j, precision = 3) = 0.785
        이러한 순서로 동작한다.
        1.get_kwarg을 통해 초기조건들을 불러온다.
        2. 계산을 실시한다.
        3. prec을 통해 소수점 자릿수를 결정짓는다.
        4. 키워드가 있다면 키워드에 따라 각도로 변환한다.
        5. 변환된 결과를 출력한다.
        '''
        r, f = utils.get_kwarg(**kwargs)

        result = cmath.phase(x)
        result = utils.round_result(value=result, precision=r)
        if f == 'degree': 
            result = math.degrees(result)
        return result

    def cartesian_to_polar(self, *args:any, **kwargs: dict[str, any])->any:
        '''
        복소수의 절대값을 계산하는 매서드.
        복소수 x를 입력받아 복소수의 절대값을 실수형으로 반환한다.
        입력받을 수 있는 키워드는 precision=int, angle_unit = 'degree', coordinate = 'cartesian' or 'polar'
        키워드로 precision를 입력받아 소수점 자릿수를 설정할수있다.
        키워드로 angle_unit를 degree로 입력받아 라디안을 각도로 변환할 수 있다.
        키워드로 coordinate로 입력받아 현재 입력x값이 직교 or 극좌표계인지 알려준다.
        
        cartesian를 입력받는다면 입력 x 는 직교 좌표계로, 출력을 극 좌표계 값을 반환한다.
        polar를 입력받는다면 입력 x 는 극 좌표계로, 출력을 직교 좌표계 값을 반환한다.
        coordinate값을 반드시 표기해야 버그가 나지 않는다. 극 좌표계 입력은 1, 0 처럼 두개여야 한다.
        cartesian_to_polar(1+1j, coordinate ='cartesian', precision = 3) = [1.414, 0.785]
        cartesian_to_polar(1,0, coordinate ='polar') = (1+0j)
        이러한 순서로 동작한다.
        1.get_kwarg을 통해 초기조건들을 불러온다.
        2. coordinate값을 저장한다.
        3. coordinate값에 따라 계산을 실시한다.
        3-1. 지평 좌표계'cartesian' 라면  precision을 통해 소수점 자릿수를 결정짓는다.
        3-2. 극 좌표계 'polar' 라면 키워드가 필요하지 않는다. 복소수 결과가 나오기 때문이다.
        4. angle_unit 키워드가 있다면 키워드에 따라 각도로 변환한다.
        5. 변환된 결과를 출력한다.
        '''
        r, f = utils.get_kwarg(**kwargs)
        c = []
        for key, value in kwargs.items(): # 좌표계 키워드 추출
            if key == 'coordinate':
                c = value

        
        result = 0
        new_result = [0,0]
        if c == 'cartesian': #
            result = cmath.polar(args[0]) # 튜플로 반환
            # print('result = ', result)
            new_result[0] , new_result[1] = utils.round_result(value=result[0], precision=r) ,\
                                    utils.round_result(value=result[1], precision=r) # 소수점 맞추기 및 리스트로 전환
            
            if f == 'degree': 
                new_result[1] = math.degrees(new_result[1])
        elif c == 'polar':
            result = cmath.rect(args[0], args[1])
            # print('result = ', result)
            new_result = result
            
        return new_result


__all__ = ['ComplexCalculator']

if __name__ == '__main__':
    # 클래스 테스트용 코드
    print("Complex Calculator Demo:")
    calc = ComplexCalculator()
    print(calc.complex_add(1 + 1j, 2 + 2j, 3 + 3j))  # 출력: (6+6j)
    print(calc.complex_subtract(10 + 10j, 2 + 5j, 3 - 5j))  # 출력: (5+10j)
    print(calc.complex_multiply(2 + 1j, 3, 4j))  # 출력: (-12+24j)
    print(calc.complex_divide(100 - 10j, 2))  # 출력: (50-5j)
    print(calc.complex_magnitude(1 + 1j, precision = 4))  # 출력: 1.4142
    print(calc.complex_argument(1 + 1j, angle_unit = 'degree'))  # 출력:45.0 
    print(calc.complex_argument(1 + 1j, precision = 3))  # 출력:0.785 
    print(calc.cartesian_to_polar(1+1j, coordinate ='cartesian', precision = 3))  # 출력: [1.414, 0.785]
    print(calc.cartesian_to_polar(1,0, coordinate ='polar'))  # 출력:0.785 

    calc.divide(5, 0) # 에러처리 확인용 코드
