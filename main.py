import pyautogui
import time, random

time.sleep(3)
cmt = [
	'cmt 1',
	'cmt 2',
	'cmt 3'
]
ran_cmt = random.choice(cmt)
print(ran_cmt)
i = 0
while True:
	i +=1
	pyautogui.moveTo(293, 107, duration=2)
	time.sleep(2.4)
	pyautogui.click()
	time.sleep(2.4)
	pyautogui.write(ran_cmt, interval=0.5)
	pyautogui.press('enter')
	if i == 2:
		break