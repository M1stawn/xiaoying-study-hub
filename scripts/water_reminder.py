import time
import sys

def drink_water_reminder(interval_minutes=45):
    """
    贴心喝水/伸懒腰提醒小脚本
    写代码或刷题时放后台跑着，到点提醒休息一下，保护颈椎与眼睛。
    """
    print(f"[已启动] 喝水与久坐提醒器，每 {interval_minutes} 分钟提醒一次。按 Ctrl+C 退出。")
    try:
        while True:
            time.sleep(interval_minutes * 60)
            now = time.strftime("%H:%M:%S", time.localtime())
            print(f"\n[{now}] 叮！已经坐了 {interval_minutes} 分钟啦。喝口水，转转脖子，闭眼休息 30 秒～")
    except KeyboardInterrupt:
        print("\n提醒已结束。记得多喝水！")

if __name__ == '__main__':
    # 默认 45 分钟提醒一次
    drink_water_reminder(45)
