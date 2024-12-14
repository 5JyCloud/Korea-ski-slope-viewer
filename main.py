import tkinter as tk
from tkinter import ttk
import webview

def muju_surlcheon():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=05"
    webview.create_window('설천하우스', url)
    webview.start()
def muju_connection():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=11"
    webview.create_window('커넥션', url)
    webview.start()
def muju_mansun():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=01"
    webview.create_window('만선하우스', url)
    webview.start()

def open_muju():
    new_window = tk.Toplevel(window)
    new_window.geometry("1200x800")
    new_window.title("무주 덕유산 리조트")
    
    # 이미지 로드 및 표시
    muju_photo = tk.PhotoImage(file="muju.png")
    image_label = tk.Label(new_window, image=muju_photo)
    image_label.pack(fill="both", expand=True)

    # 이미지 객체를 참조하여 가비지 컬렉션 방지
    new_window.muju_photo = muju_photo

    # 버튼을 이미지 위에 배치
    button_webcam = tk.Button(new_window, text="설천하우스", command=muju_surlcheon)
    button_webcam.place(relx=0.25, rely=0.8)
    button_webcam = tk.Button(new_window, text="커넥션", command=muju_connection)
    button_webcam.place(relx=0.35, rely=0.73)
    button_webcam = tk.Button(new_window, text="만선하우스", command=muju_mansun)
    button_webcam.place(relx=0.53, rely=0.81)

# main 창 생성
window = tk.Tk()
window.geometry("300x300+100+100")
window.resizable(False, False)
window.title("Slope Viewer")

# 버튼 추가
button = ttk.Button(window, text="무주 덕유산 리조트", command=open_muju)
button.pack(pady=20)

# Tkinter 이벤트 루프 시작
window.mainloop()
