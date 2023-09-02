import time


def call_with_delay():
    # 检查上次调用的时间
    if 'last_called_time' not in call_with_delay.__dict__:
        call_with_delay.last_called_time = 0

    current_time = time.time()
    elapsed_time = current_time - call_with_delay.last_called_time

    # 判断是否已经过了30秒
    if elapsed_time < 300:
        print("调用时间间隔太短，稍等片刻再试！")
        return False

    # 进行你的函数逻辑
    print("调用成功！")

    # 更新上次调用的时间
    call_with_delay.last_called_time = current_time
    return True


# if call_with_delay():
#     print("调用成功")