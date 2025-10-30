import tkinter as tk
import random
import time

tips = [
    "多喝热水","保持微笑","每天都是好心情",
    "好好吃饭","好好睡觉","坏情绪都会被治愈",
    "你今天也要元气满满哦！",
    "不要焦虑","所有的努力都算数",
    "世界那么大","一定要好好看看",
    "再难也要坚持","明天会更好",
    "开心一点","你的笑容是最好的风景",
    "天天开心","加油，你是最棒的",
]

bg_colors = [
    'lightpink', 'skyblue', 'lightgreen', 'lavender',
    'lightyellow', 'plum', 'coral', 'bisque',
    'aquamarine', 'mistyrose', 'honeydew',
    'lavenderblush', 'oldlace'
]

def create_tip_window():
    win = tk.Toplevel(root)
    win.attributes('-topmost', True)

    width = 250
    height = 60

    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = random.randrange(0, sw - width)
    y = random.randrange(0, sh - height)
    win.geometry(f"{width}x{height}+{x}+{y}")

    tk.Label(
        win,
        text=random.choice(tips),
        bg=random.choice(bg_colors),
        font=("微软雅黑", 16),
        width=30,
        height=3
    ).pack()

def spam_windows():
    for _ in range(300):
        create_tip_window()
        root.update()
        time.sleep(0.01)

root = tk.Tk()
root.withdraw() 
root.after(100, spam_windows)
root.mainloop()
