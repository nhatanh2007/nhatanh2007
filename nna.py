import pyautogui, pyperclip, time, random
print("\nTool Spam Inbox v1.0")
msg = input("Nhap noi dung can spam: ").split(" , ")
n = int(input("Nhap so lan can spam: "))
m = float(input("Nhap time delay: "))


#Chuẩn bị
print("\nChuan bi")
for i in range(5,0,-1):
    print(i,end=" ",flush=True)
    time.sleep(1)
print("\nBat dau")
#Spam
for j in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(m) #Delay
