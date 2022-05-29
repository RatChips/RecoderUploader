from utils import clear, is_logon, login

if is_logon():
    print("已经登录")

elif ret := login():
    print("登录成功")
    clear()
else:
    print("登录失败")

