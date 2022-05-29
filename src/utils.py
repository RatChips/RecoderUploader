import json
import os
import subprocess
from pathlib import Path
from subprocess import SubprocessError

from const import APP_DIR, BILIUP_EXE, COOKIES_JSON, QRCODE_PNG, RECODER_PATH_JSON


def clear():
    """清空屏幕"""
    os.system("cls")


def is_logon() -> bool:
    """判断是否已经登录"""
    return COOKIES_JSON.exists()


def login() -> bool:
    """调用biliup.exe登录"""
    try:
        os.chdir(APP_DIR)
        subprocess.run([str(BILIUP_EXE), "login"], check=True)
        QRCODE_PNG.unlink(missing_ok=True)  # 删除由于扫码登陆产生的二维码
    except SubprocessError:
        print("biliup.exe 发生错误")
        return False
    except FileNotFoundError:
        print("biliup.exe 不存在")
        return False
    except KeyboardInterrupt:
        print("biliup.exe 被中断")
        return False

    return is_logon()


def get_recoder_working_dir() -> Path:
    """获取录播姬工作目录"""
    return Path(json.loads(RECODER_PATH_JSON.read_text()).get("Path"))
