import datetime
import tkinter as tk

# 새 창 만들기
root = tk.Tk()
root.title("2023 정보처리기사 실기 시험")

# 이미지 불러오기
image = tk.PhotoImage(file="쏘나타_2.png")

# 이미지 라벨 생성
image_label = tk.Label(root, image=image)
image_label.pack()

# 디데이 설정 (YYYY, MM, DD 순서대로 입력)
d_day = datetime.datetime(2023, 4, 23)

# 날짜 입력 위젯 생성
date_entry_label = tk.Label(root, text="디데이 날짜 (YYYY-MM-DD):",)
date_entry_label.pack()
date_entry = tk.Entry(root, width=20)
date_entry.pack()

# 날짜 입력 함수
def submit_date():
    # 입력된 날짜 가져오기
    input_date_str = date_entry.get()
    # 날짜 문자열을 datetime 객체로 변환
    try:
        input_date = datetime.datetime.strptime(input_date_str, "%Y-%m-%d")
    except ValueError:
        # 날짜 입력이 잘못되었을 경우 메시지 박스 출력
        tk.messagebox.showerror("Error", "올바른 날짜 형식을 입력하세요 (YYYY-MM-DD)")
        return
    # 입력된 날짜로 디데이 설정
    global d_day
    d_day = input_date
    # 메시지 박스 출력
    tk.messagebox.showinfo("Success", "날짜가 성공적으로 변경되었습니다.")
    
# "Submit" 버튼 생성
submit_button = tk.Button(root, text="Submit", command=submit_date)
submit_button.pack(side="bottom")
# 디데이까지 남은 일 수 계산
days_left = (d_day - datetime.datetime.now()).days

# 디데이 출력 함수
def print_d_day():
    # 현재 시각 계산
    now = datetime.datetime.now()
    # 디데이까지 남은 일 수 계산
    days_left = (d_day - now).days
    # 라벨에 출력
    d_day_label.config(text="D - {}".format(days_left),font=("Helvetica", 60, "bold"), fg="red")
    # 1초마다 반복 호출
    d_day_label.after(1000, print_d_day)

# 라벨 생성
d_day_label = tk.Label(root, font=("Helvetica", 30), pady=20)
d_day_label.pack()

# 디데이 출력 함수 호출
print_d_day()

# 종료 시각 설정 (시간과 분은 자유롭게 변경 가능)
end_time = d_day.replace(hour=23, minute=59, second=59)

# 남은 시간 계산
remaining_time = end_time - datetime.datetime.now()

# 남은 시간을 시간, 분, 초로 나누기
hours, remainder = divmod(remaining_time.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# 남은 시간과 일 수를 출력하는 함수
def print_remaining_time():
    # 현재 시각 계산
    now = datetime.datetime.now()
    # 남은 시간 계산
    remaining_time = end_time - now
    # 남은 시간을 시간, 분, 초로 나누기
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    # 디데이까지 남은 일 수 계산
    days_left = (d_day - now).days
    # 라벨에 출력
    remaining_time_label.config(text="남은 시간: {}시간 {}분 {}초 남았습니다.".format(hours, minutes, seconds, ),font =("Verdana",20, "bold"), fg="red")
    # 1초마다 반복 호출
    remaining_time_label.after(1000, print_remaining_time)

# 라벨 생성
remaining_time_label = tk.Label(root, font=("Helvetica", 20), pady=20)
remaining_time_label.pack()

# 남은 시간 출력 함수 호출
print_remaining_time()

# 창 실행
root.mainloop()