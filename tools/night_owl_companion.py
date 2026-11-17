#!/usr/bin/env python3
"""
Night Owl Companion - 专为被窝夜猫子准备的放松小助手
功能：
1. 定时提醒喝水与眨眼，缓解眼部疲劳
2. 随机抽取放松小建议（听轻音乐、伸展、揉眼睛）
3. 深夜被窝安全提示（防抓包雷达提醒）
"""

import time
import random
from datetime import datetime

TIPS = [
    "闭上眼睛深呼吸 20 秒，把视线从屏幕移开。",
    "去喝一口温水，润润嗓子。",
    "转动一下脖子和手腕，被窝里别缩成一团太久。",
    "听听窗外的声音，或者放一首白噪音。",
    "注意听门外动静，雷达扫描中……安全撤退准备好了没？"
]

def check_time_status():
    current_hour = datetime.now().hour
    if 23 <= current_hour or current_hour < 5:
        return "🌙 深夜护航模式已开启：被窝光线调暗一点，别伤眼睛。"
    return "✨ 摸鱼/放松时间：劳逸结合，状态更好。"

def main():
    print("=" * 45)
    print("  🦉 小颖的夜猫子放松伴侣启动成功")
    print("=" * 45)
    print(check_time_status())
    print("\n[当前放松建议]")
    print(f"👉 {random.choice(TIPS)}")
    print("=" * 45)

if __name__ == "__main__":
    main()
