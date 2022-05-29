from dataclasses import dataclass
from pathlib import Path
from datetime import datetime
from enum import Enum, auto

APP_DIR = Path(__file__).parent
BILIUP_EXE = APP_DIR / "biliup.exe"
COOKIES_JSON = APP_DIR / "cookies.json"
QRCODE_PNG = APP_DIR / "qrcode.png"

RECODER_DIR = Path.home() / "AppData" / "Local" / "BililiveRecorder"
RECODER_PATH_JSON = RECODER_DIR / "path.json"


class EventType(Enum):
    """webhook事件类型"""

    @staticmethod
    def _generate_next_value_(name, *_):
        return name

    SESSION_STARTED = auto()
    SESSION_ENDED = auto()
    FILE_OPENING = auto()
    FILE_CLOSED = auto()


@dataclass
class EventData:
    """
    事件数据
    """

    relative_path: Path  # 相对于录播姬工作目录的路径
    file_open_time: datetime  # 文件打开时间
    session_id: str  # 录播姬会话ID
    room_id: int  # 直播间ID
    short_id: int  # 直播间短ID
    name: str  # 主播名字
    title: str  # 直播标题
    area_name_parent: str  # 主分区
    area_name_child: str  # 子分区


@dataclass
class WebhookData:
    """
    Webhook数据
    """

    event_type: EventType # 事件类型
