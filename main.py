import tkinter as tk
from tkinter import ttk
import webview

def open_webcam():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=05"
    webview.create_window('Webcam Feed', url)
    webview.start()

# Tkinter 창 생성
root = tk.Tk()
root.title("Slope Viewr")

# 버튼 추가
button = ttk.Button(root, text="Open Webcam", command=open_webcam)
button.pack(pady=20)

# Tkinter 이벤트 루프 시작
root.mainloop()