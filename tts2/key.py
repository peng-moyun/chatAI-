import random
import pyautogui
import time


def generate_random_number(random_num):
    pyautogui.keyDown(str(random_num))
    pyautogui.keyUp(str(random_num))
    time.sleep(5)  # 暂停2秒
    print(random_num)

# while 1:
#     # 生成随机数字
#     print("程序开始执行")
#     time.sleep(2)  # 暂停2秒
#     print("暂停2秒后继续执行")
#     random_num = random.randint(1, 5)
#     pyautogui.keyDown(str(random_num))
#     pyautogui.keyUp(str(random_num))
    # random_number = generate_random_number()
    #
    # # 打印随机数字
    # print("随机数字为：", random_number)
