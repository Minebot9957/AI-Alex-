#truy cập, xử lí file hệ thống
import os
#Chuyển văn bản thành âm thanh
from gtts import gTTS
#Mở âm thanh
import playsound
#Chuyển âm thanh thành văn bản
import speech_recognition
#Xử lí thởi gian
from time import strftime
import time
import datetime
#Chọn ngẫu nhiên
import random
#Truy cập web, trình duyệt
import re
import webbrowser
#Lấy thông tin từ web
import requests
import json
#Truy cập web, trình duyệt, hỗ trợ tìm kiếm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
#Thư viện Tkinter hỗ trợ giao diện
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mbox
#các chức năng khác
import wikipedia
from googletrans import Translator
import pyautogui
import speedtest
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import urllib
import urllib.request as urllib2
import ctypes
import playsound
import openai
#các biến sử dụng
openai.api_key = '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'
completion = openai.Completion()
path=ChromeDriverManager().install()
root = Tk()
text_area = Text(root, height=26, width=45)
scroll = Scrollbar(root, command=text_area.yview)
wikipedia.set_lang('vi')
language = 'vi'
now = datetime.datetime.now()
#các hàm 
def speak(text):
    print("Alex:  {}".format(text))
    text_area.insert(INSERT,"Alex: "+text+"\n")
    tts = gTTS(text=text, lang='vi', slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")
    pass
def speak(text):
    print("Alex: {}".format(text))
    url = "https://viettelgroup.ai/voice/api/tts/v1/rest/syn"
    data = {"text": text, "voice": "hn-phuongtrang", "id": "2", "without_filter": False, "speed": 1.0, "tts_return_option": 3}
    headers = {'Content-type': 'application/json', 'token': 'B-MmYoYfSEavNfwNEGh8QoqI9GuMY8zWQUJn1-siPEdtxuu-oekQYbZQ8H5Iwqrr'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    data = response.content
    f = open("sound.mp3", "wb")
    f.write(data)
    f.close()
    playsound.playsound("sound.mp3")
    os.remove("sound.mp3")        
def get_audio():
    playsound.playsound("Ping.mp3", False)
    time.sleep(2)
    print("\nAlex: Mình đang nghe bạn đây ..")
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("You: ")
        audio = r.listen(source, phrase_time_limit=6)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text.lower()
        except:
            print("\n")
            return ""

def hello():
    image1 = Image.open("image\\hacker1.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    day_time = int(strftime('%H'))
    if day_time < 11:
        speak("Chào buổi sáng tốt lành.Mình là Alex,mình có thể giúp gì được cho bạn?")
    elif 11 <= day_time < 13:
        speak("Buổi trưa vui vẻ.Mình là Alex,mình có thể giúp gì được cho bạn?")
    elif 13 <= day_time < 18:
        speak("Chào buổi chiều tốt lành.Mình là Alex,mình có thể giúp gì được cho bạn?")
    else:
        speak("Hê sờ lô hơ sờ ly ly .Mình là Alex,mình có thể giúp gì được cho bạn?")
    root.update()
    time.sleep(5)

def get_time(text):
    image1 = Image.open("image\\thoigian.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    now = datetime.datetime.now()
    now1 = datetime.datetime.now().strftime("%w")
    now2 = int(now1)
    now3 = "Chủ Nhật"
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút %d giây' % (now.hour, now.minute, now.second))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year))
    elif "thứ" in text and now2!=0:
        speak('Hôm nay là thứ %s' % (now2+1))
    elif "thứ" in text and now2==0:
        speak('Hôm nay là %s' % (now3))
    else:
        speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
        time.sleep(6)
    root.update()
    time.sleep(5)

def open_application(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    if "cốc cốc" in text:
        os.startfile('C:\\Program Files\\CocCoc\\Browser\\Application')
        speak("Cốc Cốc được mở")
    elif "word" in text:
        os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
        speak("Microsoft Word được mở")
    elif "excel" in text:
        os.startfile('"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"')
        speak("Microsoft Excel được mở")
    elif "chrome" in text:
        os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\Chrome.exe')
        speak("Google Chrome được mở")
    elif "team" in text:
        os.startfile('C:\\Users\\ACER\\Desktop\\Microsoft Teams')
        speak("Microsoft Teams được mở")
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
    root.update()
    time.sleep(6)

def open_website(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
    else:
        webbrowser.open("https://tuvannguyen.000webhostapp.com")
        speak("Trang web của bạn được mở.")
    root.update()
    time.sleep(5)
def check_internet():
    test = speedtest.Speedtest()

    speak('Đang tải danh sách servers hiện có...')
    test.get_servers()
    time.sleep(2)
    speak('Đang chọn servers tốt nhất....')
    best = test.get_best_server()
    time.sleep(2)
    print(f"Đã tìm thấy:{best['host']} ở {best['country']}")
    time.sleep(3)
    speak("Đang kiểm tra tốc độ tải xuống...")
    download = test.download()
    speak("Đang kiểm tra tốc độ tải lên.....")
    upload = test.upload()
    ping = test.results.ping
    speak ("Tất cả đã xong !")
    text = ['Alex: ' + f"Tốc độ tải xuống của bạn là: {download / 1024 / 1024:.2f} Mbit/s",             
           'Alex: ' +  f"Tốc độ tải lên của bạn là: {upload / 1024 / 1024:.2f} Mbit/s",
           'Alex: ' +  f"Ping của bạn là: {ping / 1024 / 1024:.2f} ms"]
    text_area.insert(INSERT,text+"\n")
    time.sleep(3)

def open_google_and_search(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    search_for = text.split("kiếm", 1)[1]
    if search_for !="":
        speak('Đây là những thứ mà mình tìm được')
        url = "https://www.google.com/search?q=" + search_for
        webbrowser.open(url)
    else:
      speak('Bạn muốn tìm kiếm thứ gì vậy')
      topic = get_audio()
      url = "https://www.google.com/search?q=" + topic
      webbrowser.open(url)
      speak('Mình đã tìm thấy kết quả, mong là bạn thích nó !')

    root.update()
    time.sleep(5)
def tell_me():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    try:
        speak("Bạn muốn nghe về gì ạ!")
        root.update()
        time.sleep(2)
        text = get_audio()
        contents = wikipedia.summary(text).split('.')
        speak(contents[0])
        text_area.insert(INSERT,"You: "+text+"\n")
        time.sleep(25)
        for conten in contents[1:]:
            speak("Bạn muốn nghe tiếp hay không ?")
            ans = get_audio()
            if 'có' in ans :
             speak(contents)
             time.sleep(15)
            else:
              break  
        speak("Cảm ơn bạn đã lắng nghe!")

    except:
        speak("Mình không định nghĩa được ngôn ngữ của bạn!")
        
def weather(text):
    temp="Trời quang mây tạnh"
    if "moderate rain" in text:
        temp="Trời hôm nay có mưa vừa, bạn ra ngoài nhớ mang theo áo mưa" 
    elif "heavy intensity rain" in text or "thunderstorm with light rain" in text or "very heavy rain" in text:
        temp="Trời hôm nay có mưa rất lớn kèm theo giông sét, bạn nhớ đem ô dù khi ra ngoài" 
    elif "light rain" in text:
        temp="Trời hôm nay mưa nhẹ, rải rác một số nơi" 
    elif "heavy intensity shower rain" in text:
        temp="Trời hôm nay có mưa rào với cường độ lớn"
    elif "broken clouds" in text or "few clouds" in text:
        temp="Trời hôm nay có mây rải rác, không mưa"
    elif "overcast clouds" in text:
        temp="Trời hôm nay nhiều mây, u ám, dễ có mưa"
    elif "scattered clouds" in text:
        temp="Trời hôm nay có nắng, có mây rải rác"   
    
    if "rain" in text:
        image1 = Image.open("image\\thoitiet2.jpg")
        image_1 = ImageTk.PhotoImage(image1)    
        label1 = Label(image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)
    else :
        image1 = Image.open("image\\thoitiet1.jpg")
        image_1 = ImageTk.PhotoImage(image1)    
        label1 = Label(image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)

    return temp

def temperature(text):
    temp="mát mẻ"
    if text<15:
        temp="lạnh buốt giá"
    elif text<20:
        temp="khá lạnh"
    elif text<30:
        temp="mát mẻ"
    elif text<33:
        temp="khá nóng"
    else:
        temp="nóng bức"

    return temp

def current_weather(city):
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = city
    text_area.insert(INSERT,"You: "+city+"\n")
    if city=="":
        current_weather()
    else:
        api_key = "b0d4f9bfd2bbc40d10976e6fd3ea7514"
        call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(call_url)
        data = response.json()
        if data["cod"] != "404":
            city_res = data["main"]
            current_humidity = city_res["humidity"]
            current_temperature = city_res["temp"]
            temperature1=temperature(current_temperature)
            suntime = data["sys"]
            sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
            sunset = datetime.datetime.fromtimestamp(suntime["sunset"])

            weather_description = data["weather"][0]["description"]
            weather1=weather(weather_description)
            content = """
    -Mời bạn nghe bản tin thời tiết tại {city} ngày hôm nay:
     -Hôm nay là ngày {day} tháng {month} năm {year}
     -Thời tiết hôm nay {temperature} có nhiệt độ trung bình là {temp} độ C 
     -Độ ẩm là {humidity}%
     -{weather}
     -Mặt trời mọc vào {hourrise} giờ {minrise} phút
     -Mặt trời lặn vào {hourset} giờ {minset} phút.""".format(hourrise = sunrise.hour, minrise = sunrise.minute,
                                                            weather=weather1,temperature=temperature1,
                                                            hourset = sunset.hour, minset = sunset.minute, 
                                                            temp = current_temperature, humidity = current_humidity, city=city, month=now.month, year=now.year, day=now.day)
            speak(content)
            root.update()
            time.sleep(21)
        else:
            speak("Không tìm thấy địa chỉ của bạn")
            root.update()
            time.sleep(2)
            current_weather()

def week(x):
    switcher={
            0:'có môn Lập trình mạng do thầy Mai Văn Hà quản lí..Phòng B3-203. Tiết 2 3 4 .Giờ bắt đầu học 6 giờ.Và có môn Đô án chuyên ngành do cô Vũ Thị Trà quản lí. Tiết 6 7 .Giờ bắt đầu học 13 giờ',
            1:'có môn Hệ Quản Trị Cơ Sở dữ liệu do cô Phạm Dương Thu Hằng quản lí.Phòng A5-210 . Tiết 6 7 8 9 .Giờ bắt đầu học 13 giờ',
            2:'có môn Công nghệ phần mềm do cô Lê Thị Thanh Bình quản lí. Tiết 4 5 .Giờ bắt đầu học 10 giờ',
            3:'bạn được nghỉ. Hãy tranh thủ đi chơi với người yêu đi nha.',
            4:'có môn Đường lối Đảng Cộng sản Việt Nam do thầy Nguyễn Hải Như quản lí.Phòng B3-302. Tiết 6 7 .Giờ bắt đầu học 13 giờ',
            5:'có môn An toàn thông tin do thầy Phan Phú Cường quản lí.Phòng B3-403. Tiết 4 5 .Giờ bắt đầu học 10 giờ',
            6:'có môn Thiết kế website do thầy Nguyễn Thanh Tuấn quản lí.Phòng A5-206. Tiết 1 2 3 .Giờ bắt đầu học 7 giờ',
        }
    return switcher.get(x, "nothing")


def change_wallpaper():
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + api_key   
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']    
    urllib2.urlretrieve(photo, r"C:/Users/CuongNguyenPC/Pictures/anh.img")
    image = os.path.join(r"C:/Users/CuongNguyenPC/Pictures/anh.img")
    ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
    speak("Hình nền máy tính vừa được thay đổi")
def sleep_time(x):
    if x==1:
        time.sleep(13)
    elif x==2:
        time.sleep(10)
    elif x==3:
        time.sleep(7)
    elif x==4:
        time.sleep(13)
    elif x==5:
        time.sleep(11)
    elif x==6:
        time.sleep(11)
    else :
        time.sleep(21)

def subject(text):
    image1 = Image.open("image\\TKB.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    now1 = datetime.datetime.now().strftime("%w")
    if "hôm nay" in text:
        now2 = int(now1)
        speak("Hôm nay "+week(now2))
        root.update()
        sleep_time(now2)
    elif "ngày mai" in text:
        now2 = int(now1)+1
        if now2 >6:
            now2=0
        speak("Ngày mai "+week(now2))
        root.update()
        sleep_time(now2)

def subject_day(text):
    image1 = Image.open("image\\TKB.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    if "thứ hai" in text:
        speak("Thứ Hai có môn Hệ Quản Trị Cơ Sở dữ liệu do cô Phạm Dương Thu Hằng quản lí.Phòng A5-210 . Tiết 6 7 8 9 .Giờ bắt đầu học 13 giờ")
        root.update()
        sleep_time(1)
    elif "thứ ba" in text:
        speak("Thứ Ba có môn Công nghệ phần mềm do cô Lê Thị Thanh Bình quản lí. Tiết 4 5 .Giờ bắt đầu học 10 giờ")
        root.update()
        sleep_time(2)
    elif "thứ tư" in text:
        speak("Thứ Tư bạn được nghỉ. Hãy tranh thủ đi chơi với người yêu đi nha.")
        root.update()
        sleep_time(3)
    elif "thứ năm" in text:
        speak("Thứ Năm có môn Đường lối Đảng Cộng sản Việt Nam do thầy Nguyễn Hải Như quản lí.Phòng B3-302. Tiết 6 7 .Giờ bắt đầu học 13 giờ")
        root.update()
        sleep_time(4)
    elif "thứ sáu" in text:
        speak("Thứ Sáu có môn An toàn thông tin do thầy Phan Phú Cường quản lí.Phòng B3-403. Tiết 4 5 .Giờ bắt đầu học 10 giờ")
        root.update()
        sleep_time(5)
    elif "thứ bảy" in text:
        speak("Thứ Bảy có môn Thiết kế website do thầy Nguyễn Thanh Tuấn quản lí.Phòng A5-206. Tiết 1 2 3 .Giờ bắt đầu học 7 giờ")
        root.update()
        sleep_time(6)
    elif "chủ nhật" in text:
        speak("Chủ mật có môn Lập trình mạng do thầy Mai Văn Hà quản lí. Tiết 2 3 4 .Phòng B3-203.Giờ bắt đầu học 6 giờ.\n\tVà có môn Đô án chuyên ngành do cô Vũ Thị Trà quản lí. Tiết 6 7 .Giờ bắt đầu học 13 giờ")
        root.update()
        sleep_time(0)

def get_math():
    speak("Bạn nói phép tính đi, AI sẽ giúp bạn.")
    root.update()
    time.sleep(4)
    text1=get_audio()
    text_area.insert(INSERT,"You: "+text1+"\n")
    root.update()
    image_1 = ImageTk.PhotoImage(Image.open("image\\math.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    if "+" in text1:
        text2=text1.replace("+", "-")
        try:
            math_a = re.search('(.+) -', text2)
            a = math_a.group(1)
            math_b = re.search('- (.+)', text2)
            b = math_b.group(1)
            c = float(a)+float(b)
            speak("Kết quả phép tính "+a+" cộng "+b+" là: "+str(c))
            root.update()
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    elif "/" in text1 or "chia" in text1:
        text2=text1.replace("chia", "/")
        try:
            math_a = re.search('(.+) /', text2)
            a = math_a.group(1)
            math_b = re.search('/ (.+)', text2)
            b = math_b.group(1)
            c = float(a)/float(b)
            speak("Kết quả phép tính "+a+" chia "+b+" là: "+str(c))
            root.update()
            time.sleep(3)
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    elif "x" in text1 or "nhân" in text1:
        text2=text1.replace("nhân", "x")
        try:
            math_a = re.search('(.+) x', text2)
            a = math_a.group(1)
            math_b = re.search('x (.+)', text2)
            b = math_b.group(1)
            c = float(a)*float(b)
            speak("Kết quả phép tính "+a+" nhân "+b+" là: "+str(c))
            time.sleep(2)
            root.update()
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    elif "-" in text1:
        try:
            math_a = re.search('(.+) - ', text1)
            a = math_a.group(1)
            math_b = re.search(' - (.+)', text1)
            b = math_b.group(1)
            c = float(a)-float(b)
            speak("Kết quả phép tính "+a+" trừ "+b+" là: "+str(c))
            root.update()
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    else:
        speak("Phép tính không hợp lệ")
        root.update()
    
    time.sleep(6)

def youtube_search():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    speak('Xin mời bạn chọn tên để tìm kiếm ')
    root.update()
    time.sleep(3.5)
    text = get_audio()
    text_area.insert(INSERT,"You: "+text+"\n")
    root.update()
    if text == "":
        speak("Lỗi tìm kiếm. Do bạn chưa nói tên tìm kiếm.")
        root.update()
        time.sleep(4)
    else:
        search = SearchVideos(text, offset = 1, mode = "json", max_results = 20).result()
        data = json.loads(search)
        url = data["search_result"][0]["link"]
        print(url)
        webbrowser.open(url)
        if "bài hát" in text:
            speak("Bài hát bạn yêu cầu đã được mở.")
        elif "phim" in text:
            speak("Bộ phim bạn yêu cầu đã được mở.")
        else:
            speak("Yêu cầu của bạn đã hoàn thành.")
        time.sleep(7)   

def love_you():
    mylist = ["Thiếu 500 nghìn là em tròn một củ. Thiếu anh nữa là em đủ một đôi.",
    "Đố ai quyét sạch được lá rừng. Đố ai khuyên được em ngừng yêu anh!",
    "Trời không xanh, Mây cũng không trắng, Em không say nắng, Nhưng lại say anh.",
    "Cho em một cốc trà đào, Tiện cho em hỏi lối vào tim anh!",
    "Em đây rất thích đồng hồ, Thích luôn cả việc làm bồ của anh.",
    "Vertor chỉ có một chiều, Em dân chuyên toán chỉ yêu 1 người.",
    "Hoa vô tình bỏ rơi cành lá, Người vô tình bỏ lỡ tơ duyên",
    "Ngoài kia bão táp mưa sa, Bôn ba mệt quá về nhà với em",
    "Trăng kia ai vẽ mà tròn, Lòng anh ai trộm mà hoài nhớ thương",
    "Nhân gian vốn lắm bộn bề. Sao không bỏ hết mà về với em.",
    "Thức khuya em tỉnh bằng trà, yêu anh em trả bằng tình được không?",
    "Suốt bao năm lòng em luôn yên tĩnh. Gặp anh rồi, tĩnh lặng hóa phong ba.",
    "Nắng kia là của ông trời, còn anh đã của ai rồi hay chưa? ",
    "Mây kia là của hạt mưa, anh xem đã thích em chưa hay rồi?",
    "Cánh đồng xanh xanh, làn mây trăng trắng. Tưởng là say nắng ai ngờ say em."]
    love=random.choice(mylist)
    speak(love)
    root.update()
    time.sleep(7)
def volumedown():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume)) 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(curentsVolumeDb - 6.0, None)   
    root.update()
def volumeup():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume)) 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(curentsVolumeDb + 5.0, None)
    root.update()
def func():
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    content="""
    Tôi có những chức năng sau đây:
    1.Chào hỏi
    2.Thông báo thời gian 
    3.Dự báo thời tiết 
    4.Thời khóa biểu
    5.Thực hiện phép tính đơn giản 
    6.Thả thính crush
    7.Mở ứng dụng,mở website 
    8.Tìm kiếm thông tin trên google 
    9.Mở nhạc,phim trên youtube 
    10.Tạm biệt"""
    speak(content)
    root.update()
    time.sleep(23)

def color():
    mylist = ["#009999","black","green","grey","blue","orange","#cc0099","#00ff00","brown"]
    aa=random.choice(mylist)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here", background = aa)
    root.update()

def color1():
    mylist1 = ["yellow","#0000ff","white","#00ff00","black"]
    bb=random.choice(mylist1)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here",foreground = bb)
    root.update()

def info():
    mbox.showinfo("Giới thiệu", "-Nhấn Micro để bắt đầu thực hiện nói với AI.\n-Nhấn Làm mới để xóa toàn bộ cuộc trò chuyện.\n-Bạn có thể thay đổi màu nền hoặc màu chữ ngẫu nhiên.\n-Tiếng Pip xuất hiện là lúc AI đang nghe bạn nói.\n-Nói 'dừng lại' để tạm hoãn cuộc trò chuyện. \n-Nhấn Thoát để tắt chương trình.")

def r_set():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    text_area.delete("1.0", "1000000000.0")
def tran(text, vung):    
        image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
        label1 = Label(image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)
        nghia = text
        time.sleep(3)
        translator = Translator()
        translation = translator.translate( nghia , dest = vung)
        text_area.insert((INSERT,"Alex: "+translation+"\n"))
        noi(translation.text, vung)
        time.sleep(3)
        root.update()
def noi(text, dest):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    print("Alex: {}".format(text))
    tts = gTTS(text=text, lang=dest, slow = False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3") 
    root.update()
def alarm(timing):       
        alttime = str(datetime.datetime.now().strptime(timing,"%H:%M"))    
        alttime = alttime[11:-3]  
        Hour = alttime[:2]  
        Hour = int(Hour)
        Minute = alttime[3:5]
        Minute = int(Minute)
        speak(f'Mình đã đặt báo thức lúc {timing} cho bạn, nhớ đừng để trễ giờ nhé !')     
        while True:
            if Hour==datetime.datetime.now().hour and Minute==datetime.datetime.now().minute:
                playsound.playsound('sound1.mp3')   
                time.sleep(25)
                speak('Bạn có dậy hay không ?')
                ans = get_text()
                if "có" or "dậy" in ans:
                    break
                else:
                    speak(f"Đã quá {timing} rồi, dậy đi bạn ơi ")
                    time.sleep(4)
                    playsound.playsound('sound1.mp3')
                break 
def Reply(text) :
  prompt = text
  response = completion.create(prompt = prompt,engine = "text-davinci-003",temperature=0.7,max_tokens=256)
  answer = response.choices[0].text.strip()
  speak(answer)
  time.sleep(15)
def ham_main():
    r = speech_recognition.Recognizer()
    you=""
    ai_brain=""
    hello()
    time.sleep(1)
    while True:
        with speech_recognition.Microphone() as source:
            playsound.playsound("Ping.mp3", False)
            time.sleep(2)
            print("Alex:  Mình đang nghe bạn đây ...")
            audio = r.listen(source, phrase_time_limit=6)
            print("Alex:  ...")
        try:
            you = r.recognize_google(audio, language="vi-VN")
            print("\nYou: "+ you)	
            you = you.lower()
        except:
            ai_brain = "Tôi nghe không rõ. Bạn nói lại được không"
            print("\nAlex: " + ai_brain)

        text_area.insert(INSERT,"You: "+you+"\n")
        root.update()
        if "thời tiết" in you:
            if 'ở' in you :
                city = you.split("ở ", 1)[1]
                current_weather(city)
            elif 'xem thời tiết' in you:
                speak('Bạn muốn xem thời tiết ở đâu ạ ?')
                city = get_audio()
                current_weather(city)    
        elif "ngày mấy" in you or "mấy giờ" in you or "thứ mấy" in you:
            get_time(you)
        elif "phép tính"in you or "tính toán" in you:
            get_math()
        elif "mở ứng dụng" in you or "mở phần mềm" in you:
            open_application(you)
        elif "mở website" in you:
            open_website(you)
        elif "mở google và tìm kiếm" in you:
            open_google_and_search(you)
        elif ("hôm nay" in you and "môn" in you) or ("ngày mai" in you and "môn" in you):
            subject(you)
        elif ("thứ" in you and "môn" in you) or ("chủ nhật" in you and "môn" in you):
            subject_day(you)
        elif "nghe nhạc" in you or "xem phim" in you or "mở youtube" in you or "bài hát" in you:
            youtube_search()
        elif "to âm thanh" in you or "lớn âm thanh" in you :
            volumeup()
        elif "nhỏ âm thanh" in you or "bé âm thanh" in you :
            volumedown()
        elif "wikipedia" in you or "từ điển" in you:
            tell_me()
        elif "thả thính" in you or "bạn thích tôi à" in you:
            love_you()
        elif "bạn có" in you and "chức năng" in you:
            func()
        elif "kiểm tra tốc độ internet" in you:
            check_internet()
        elif "thay đổi hình nền máy tính" in you:
            change_wallpaper()
        elif "đổi màu nền" in you:
            color()
        elif "đổi màu chữ" in you:
            color1()
        elif "dịch từ" in you:
                try :    
                    text = you.split("từ ", 1)[1]
                    dest = you.split('sang tiếng ', 1)[1]
                    text1 = text.replace(f"sang tiếng {dest}", "")
                    dest = dest.replace("nga", "ru")
                    dest = dest.replace("anh", "en")
                    dest = dest.replace("đức", "de")
                    dest = dest.replace("ý", "it")
                    dest = dest.replace("trung", "zh-cn")
                    dest = dest.replace("nhật", "ja")
                    dest = dest.replace("hàn", "ko")
                    tran(text1, dest)
                except:
                    speak('Mình có thể dịch được các thứ tiếng sau : Anh,Nga,Đức,Ý,Trung,Nhật,Hàn')
                    time.sleep(5)
        elif "báo thức lúc" in you:
                  text = you.split('lúc ', 1)[1]
                  text1 = text.replace('lúc ', '')
                  text2 = text1.replace(".", "")
                  alarm(text2) 
        elif "dừng lại" in you:
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            break
        elif "hẹn gặp lại" in you or "tạm biệt" in you or "cảm ơn" in you:
            ai_brain="Rất vui khi được giúp đỡ bạn. Hẹn gặp lại bạn sau."
            speak(ai_brain)
            root.update()
            time.sleep(4)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(1)
            exit()
        else:
            Reply(you)

            root.update()
            time.sleep(4)

        you=""

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent) 
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Trợ lí ảo Macus Alex")
        self.style = Style()
        self.style.theme_use("default")
        
        scroll.pack(side=RIGHT, fill=Y)
        text_area.configure(yscrollcommand=scroll.set)
        text_area.pack(side=RIGHT)

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        image3 = Image.open("image\\micro.png")
        image_3 = ImageTk.PhotoImage(image3)  
        label = Label(image=image_3)
        label.image = image_3
        label.place(x=430, y=477)

        closeButton = Button(self, text="Tự Huỷ",command = exit,width=10,fg="white", bg="#000000",bd=3)
        closeButton.pack(side=RIGHT, padx=11, pady=10)
        okButton = Button(self, text="Micro",command = ham_main,width=10,fg="white", bg="#000000",bd=3)
        okButton.pack(side=RIGHT, padx=11, pady=10)
        doimau = Button(self,text="Đổi màu nền",command = color,width=10,fg="white", bg="#000000",bd=3)
        doimau.pack(side=RIGHT,padx=11, pady=10)
        doimau = Button(self,text="Đổi màu chữ",command = color1,width=10,fg="white", bg="#000000",bd=3)
        doimau.pack(side=RIGHT,padx=11, pady=10)
        thongtin = Button(self,text="Giới thiệu",command = info,width=10,fg="white", bg="#000000",bd=3)
        thongtin.pack(side=RIGHT,padx=11, pady=10)
        lammoi = Button(self,text="Làm mới",command = r_set,width=10,fg="white", bg="#000000",bd=3)
        lammoi.pack(side=RIGHT,padx=11, pady=10)

        # self.pack(fill=BOTH, expand=1)   
        # Style().configure("TFrame", background="#333")
        root.iconbitmap('C:\\Users\\CuongNguyenPC\\Documents\\Code\\python\\python\\image\\icon.ico')

        image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
        label1 = Label(self, image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)
        def clock():
            string=strftime('%H:%M:%S:%p')
            label.config(text=string)
            label.after(1000,clock)
        
        label= Label(root,font = ("Digital-7",20) , bg='white' , fg= 'green' )
        label.place(x = 10, y = 10, width=120, height=25)
        clock()
        
        l = Label(root, text='Lịch sử trò chuyện', fg='White', bg='black')
        l.place(x = 680, y = 10, width=250, height=25)
        l.config(font=("Arial", 15, 'bold'))
        l1 = Label(root, text='Hình ảnh đây nè ', fg='White', bg='black')
        l1.config(font=("Arial", 15, 'bold'))
        l1.place(x = 150, y = 11, width=300, height=25)

root.geometry("1000x510+250+50")
root.resizable(True, True)
app = Example(root)
root.mainloop()

#http://api.openweathermap.org/data/2.5/weather?appid=b0d4f9bfd2bbc40d10976e6fd3ea7514&q=da%20nang&units=metric