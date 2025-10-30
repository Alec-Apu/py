import tkinter as tk
import random
import time

# 治愈语录列表
tips = [
    "多喝热水", "保持微笑", "每天都是好心情",
    "好好吃饭", "好好睡觉", "坏情绪都会被治愈",
    "你今天也要元气满满哦！",
    "不要焦虑", "所有的努力都算数",
    "世界那么大", "一定要好好看看",
    "再难也要坚持", "明天会更好",
    "开心一点", "你的笑容是最好的风景",
    "天天开心", "加油，你是最棒的",
]

# 柔和背景色列表
bg_colors = [
    'lightpink', 'skyblue', 'lightgreen', 'lavender',
    'lightyellow', 'plum', 'coral', 'bisque',
    'aquamarine', 'mistyrose', 'honeydew',
    'lavenderblush', 'oldlace'
]

def create_tip_window():
    """创建一个随机位置、随机颜色、随机语录的治愈弹窗"""
    win = tk.Toplevel(root)
    win.attributes('-topmost', True)  # 置顶显示
    win.overrideredirect(True)        # 去除窗口边框（可选：更轻量）

    width = 250
    height = 60
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = random.randrange(0, sw - width)
    y = random.randrange(0, sh - height)
    win.geometry(f"{width}x{height}+{x}+{y}")

    label = tk.Label(
        win,
        text=random.choice(tips),
        bg=random.choice(bg_colors),
        font=("微软雅黑", 16, "bold"),
        fg='#333333',
        relief='flat',
        pady=10
    )
    label.pack(expand=True)

    # 3秒后自动关闭（温柔不打扰）
    win.after(3000, win.destroy)

def spam_windows():
    """批量创建 300 个治愈弹窗"""
    for _ in range(300):
        create_tip_window()
        root.update()
        time.sleep(0.01)  # 控制节奏，避免卡死

# 主窗口（隐藏）
root = tk.Tk()
root.withdraw()  # 不显示主窗口

# 延迟启动，防止初始化冲突
root.after(100, spam_windows)

# 启动主循环
root.mainloop()
