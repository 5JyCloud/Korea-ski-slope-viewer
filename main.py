import tkinter as tk
from tkinter import ttk
import webview


# 무주 웹캡 실행 함수
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
def muju_sundown():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=04"
    webview.create_window('서역기행, 썬다운', url)
    webview.start()
def muju_hideyhouse():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=03"
    webview.create_window('하이디하우스', url)
    webview.start()
def muju_mansuntop():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=02"
    webview.create_window('만선봉 정상', url)
    webview.start()
def muju_silkroad():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=10"
    webview.create_window('실크로드, 미뉴에트하단', url)
    webview.start()
def muju_polka():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=09"
    webview.create_window('폴카', url)
    webview.start()
def muju_mozart():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=08"
    webview.create_window('모차르트, 미뉴에트', url)
    webview.start()
def muju_surlcheon_t_s():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=06"
    webview.create_window('설천상단슬로프', url)
    webview.start()
def muju_surlcheontop():
    url = "http://www.mdysresort.com/guide/webcam_popup.asp?cam_num=07"
    webview.create_window('설천봉 정상', url)
    webview.start()

# 하이원 웹캠 실행 함수
def high1_1():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=1"
    webview.create_window('도도', url)
    webview.start()
def high1_2():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=2"
    webview.create_window('도도', url)
    webview.start()
def high1_3():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=3"
    webview.create_window('도도', url)
    webview.start()
def high1_4():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=4"
    webview.create_window('도도', url)
    webview.start()
def high1_5():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=5"
    webview.create_window('도도', url)
    webview.start()
def high1_6():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=6"
    webview.create_window('도도', url)
    webview.start()
def high1_7():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=7"
    webview.create_window('도도', url)
    webview.start()
def high1_8():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=8"
    webview.create_window('도도', url)
    webview.start()
def high1_9():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=9"
    webview.create_window('도도', url)
    webview.start()
def high1_10():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=10"
    webview.create_window('도도', url)
    webview.start()
def high1_11():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=11"
    webview.create_window('도도', url)
    webview.start()
def high1_12():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=12"
    webview.create_window('도도', url)
    webview.start()
def high1_13():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=13"
    webview.create_window('도도', url)
    webview.start()
def high1_14():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=14"
    webview.create_window('도도', url)
    webview.start()
def high1_15():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=15"
    webview.create_window('도도', url)
    webview.start()
def high1_16():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=16"
    webview.create_window('도도', url)
    webview.start()
def high1_17():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=17"
    webview.create_window('도도', url)
    webview.start()
def high1_18():
    url = "http://www.high1.com/webcam/pop_webcam.do?ch=18"
    webview.create_window('도도', url)
    webview.start()

# 무주 GUI
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
    button_webcam = tk.Button(new_window, text="서역기행, 썬다운", command=muju_sundown)
    button_webcam.place(relx=0.77, rely=0.68)
    button_webcam = tk.Button(new_window, text="하이디하우스", command=muju_hideyhouse)
    button_webcam.place(relx=0.68, rely=0.52)
    button_webcam = tk.Button(new_window, text="만선봉 정상", command=muju_mansuntop)
    button_webcam.place(relx=0.6, rely=0.41)
    button_webcam = tk.Button(new_window, text="실크로드, 미뉴에트하단", command=muju_silkroad)
    button_webcam.place(relx=0.07, rely=0.45)
    button_webcam = tk.Button(new_window, text="폴카", command=muju_polka)
    button_webcam.place(relx=0.105, rely=0.38)
    button_webcam = tk.Button(new_window, text="모차르트, 미뉴에트", command=muju_mozart)
    button_webcam.place(relx=0.2, rely=0.29)
    button_webcam = tk.Button(new_window, text="설천상단슬로프", command=muju_surlcheon_t_s)
    button_webcam.place(relx=0.186, rely=0.18)
    button_webcam = tk.Button(new_window, text="설천봉 정상", command=muju_surlcheontop)
    button_webcam.place(relx=0.325, rely=0.115)

# 하이원 GUI
def open_high1():
    new_window = tk.Toplevel(window)
    new_window.geometry("1300x800")
    new_window.title("하이원 리조트")

    # 이미지 로드 및 표시
    high1_photo = tk.PhotoImage(file="high1.png")
    image_label = tk.Label(new_window, image=high1_photo)
    image_label.pack(fill="both", expand=True)

    # 이미지 객체를 참조하여 가비지 컬렉션 방지
    new_window.high1_photo = high1_photo

    button_webcam = tk.Button(new_window, text="18", command=high1_18)
    button_webcam.place(relx=0.465, rely=0.899)
    button_webcam = tk.Button(new_window, text="17", command=high1_17)
    button_webcam.place(relx=0.511, rely=0.863)
    button_webcam = tk.Button(new_window, text="16", command=high1_16)
    button_webcam.place(relx=0.505, rely=0.745)
    button_webcam = tk.Button(new_window, text="15", command=high1_15)
    button_webcam.place(relx=0.565, rely=0.62)
    button_webcam = tk.Button(new_window, text="14", command=high1_14)
    button_webcam.place(relx=0.48, rely=0.588)
    button_webcam = tk.Button(new_window, text="13", command=high1_13)
    button_webcam.place(relx=0.465, rely=0.535)
    button_webcam = tk.Button(new_window, text="12", command=high1_12)
    button_webcam.place(relx=0.515, rely=0.48)
    button_webcam = tk.Button(new_window, text="11", command=high1_11)
    button_webcam.place(relx=0.494, rely=0.45)
    button_webcam = tk.Button(new_window, text="10", command=high1_10)
    button_webcam.place(relx=0.458, rely=0.377)
    button_webcam = tk.Button(new_window, text="9", command=high1_9)
    button_webcam.place(relx=0.3135, rely=0.23)
    button_webcam = tk.Button(new_window, text="1", command=high1_1)
    button_webcam.place(relx=0.5145, rely=0.1)
    button_webcam = tk.Button(new_window, text="2", command=high1_2)
    button_webcam.place(relx=0.533, rely=0.148)
    button_webcam = tk.Button(new_window, text="3", command=high1_3)
    button_webcam.place(relx=0.56, rely=0.138)
    button_webcam = tk.Button(new_window, text="4", command=high1_4)
    button_webcam.place(relx=0.635, rely=0.305)
    button_webcam = tk.Button(new_window, text="5", command=high1_5)
    button_webcam.place(relx=0.613, rely=0.36)
    button_webcam = tk.Button(new_window, text="6", command=high1_6)
    button_webcam.place(relx=0.65, rely=0.415)
    button_webcam = tk.Button(new_window, text="7", command=high1_7)
    button_webcam.place(relx=0.725, rely=0.718)
    button_webcam = tk.Button(new_window, text="8", command=high1_8)
    button_webcam.place(relx=0.701, rely=0.74)
    
# main GUI 생성
window = tk.Tk()
window.geometry("300x300+100+100")
window.resizable(False, False)
window.title("Slope Viewer")

# 버튼 추가
button = ttk.Button(window, text="무주 덕유산 리조트", command=open_muju)
button.pack(pady=20)
button = ttk.Button(window, text="하이원 리조트", command=open_high1)
button.pack(pady=20)

# Tkinter 이벤트 루프 시작
window.mainloop()
