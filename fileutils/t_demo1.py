import pytest
import webdriver_manager.chrome
from selenium import webdriver


# def test_firstprogram():
#     print("hello")
#
# driver=webdriver.Chrome()
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


    for i in range(x + 1):

        for j in range(y + 1):
            for k in range(z + 1):
              if i + j + k != n:
                print(list([i, j, k]))


