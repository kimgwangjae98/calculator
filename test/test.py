
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# 상위 디렉토리 
'''
os.path.dirname(__file__) : 이는 현재 수행중인 코드를 담고 있는 파일의 위치한 Path를 알려준다.
os.path.abspath() : 절대경로를 구해준다.
sys.path.append() : 해당 경로에 있는 파이썬 파일을 import 할 수 있게 해준다.
'''

from basic import Calculator
from engineering import EngineeringCalculator

if __name__ == '__main__':
    # 클래스 테스트용 코드
    print("Basic Calculator Demo:")
    calc = Calculator()
    print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00
    print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0
    print(calc.multiply(2, 3, 4))  # 출력: 24
    print(calc.divide(100, 2, precision=3))  # 출력: 50.000

    print("\nEngineering Calculator Demo:")
    eng_calc = EngineeringCalculator()
    print(eng_calc.add(1, 2, 3, precision=2))  # 출력: 6.00
    print(eng_calc.square_root(16, precision=3))  # 출력: 4.000
    print(eng_calc.log(100, precision=4))  # 출력: 2.0000
    print(eng_calc.sin(30, angle_unit='degree', precision=4))  # 출력: 0.5000

    eng_calc.divide(5, 0) # 에러처리 확인용 코드