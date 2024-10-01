from setuptools import setup, find_packages

setup(
    name='calculator',
    version='0.0.1',
    description='PYPI tutorial package creation written by TeddyNote',
    author='kimgwangjae98',
    author_email='gimgwangjae@gmail.com',
    url='https://github.com/kimgwangjae98/calculator',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['kimgawngjae_test_calu'],
    python_requires='>=3.11',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.11'
    ],
)
# https://teddylee777.github.io/python/pypi/
# 위 페이지를 참고하여 setup.py 제작