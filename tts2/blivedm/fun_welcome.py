import time

# 文件路径，用于保存用户信息
file_path = "user_info.txt"

# 读取本地已保存的用户信息
try:
    with open(file_path, "r") as file:
        users = eval(file.read())  # 使用eval函数将字符串转换为字典
except FileNotFoundError:
    users = {}


def save_user_info():
    # 保存用户信息到本地txt文件
    with open(file_path, "w") as file:
        file.write(str(users))  # 将字典转换为字符串并写入文件


def welcome_user(user_type, username):
    global users
    if user_type == "粉丝":
        print(f"欢迎粉丝 {username} 进入直播间！")
    else:
        if username in users:
            last_visit_time = users[username]
            current_time = time.time()
            if current_time - last_visit_time < 120:
                print(f"{username} 非粉丝，需等待 {int(120 - (current_time - last_visit_time))} 秒后再次进入直播间。")
                return
        print(f"欢迎非粉丝 {username} 进入直播间！")
        users[username] = time.time()
        save_user_info()


# 测试
welcome_user("粉丝", "张三")
welcome_user("非粉丝", "李四")
welcome_user("非粉丝", "王五")
time.sleep(3)
welcome_user("非粉丝", "李四")
welcome_user("粉丝", "张三")
