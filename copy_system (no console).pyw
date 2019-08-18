import win32clipboard
import pyautogui
from pynput import keyboard
import shutil
import os
from distutils.dir_util import copy_tree
from shutil import copy

copied_items=[]
def copy_path():
	pyautogui.keyDown('shift')
	pyautogui.rightClick()
	pyautogui.keyUp('shift')
	try:
		pyautogui.click(pyautogui.locateCenterOnScreen("Screenshot (1).png"))
	except:
		try:
			pyautogui.click(pyautogui.locateCenterOnScreen("Screenshot (2).png"))
		except:
			pass
def set_clipboard_data_none():
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText('')
	win32clipboard.CloseClipboard()
def set_clipboard_data(x):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(x)
	win32clipboard.CloseClipboard()
def get_copied_path():
	copy_path()
	try:
		get_clipboard_data()
	except:
		pass
	set_clipboard_data_none()
def get_copied_item():
	try:
		get_clipboard_data()
	except:
		pass
	set_clipboard_data_none()
def get_clipboard_data():
	os.system('CLS')
	global copied_items
	win32clipboard.OpenClipboard()
	try:
		data=win32clipboard.GetClipboardData()
		if "\r\n" in data and os.path.exists(data.split("\r\n")[0].replace('"','')):
			data=data.split("\r\n")
		if data in copied_items:
			x=copied_items.index(data)
			copied_items.insert(0, copied_items.pop(x))
			printing_copied_items()
		if data not in copied_items and data!='':
			copied_items.insert(0,data)
			printing_copied_items()		
		if len(copied_items)==10:
			copied_items.pop()
	except:
		pass
def printing_copied_items():
	global  copied_items
	for i in range(len(copied_items)):
		if type(copied_items[i])==list:
			print(i+1,'.', end='')
			for k in range (len(copied_items[i])):
				print('\t',k+1,'. ',copied_items[i][k])
		else:
			print(i+1,'. ',copied_items[i])
def copy_folder(source, destination):
	new_folder=os.path.basename(source)
	os.chdir(destination)
	os.mkdir(new_folder)
	new_destination=os.path.join(destination, new_folder)
	copy_tree(source, new_destination)
def copy_file(source, destination):
	copy(source, destination)
def file_handeler(folder):
	try:
		pyautogui.hotkey('ctrl','l')
		pyautogui.hotkey('ctrl','c')
		win32clipboard.OpenClipboard()
		dest=win32clipboard.GetClipboardData()
		win32clipboard.CloseClipboard()
		set_clipboard_data_none()
		folder=folder.replace('"','')
		if os.path.isdir(folder):
			copy_folder(folder,dest)
		if os.path.isfile(folder):
			copy_file(folder, dest)
	except:
		pass
def main3(on_index):
	global current, copied_items, curr, curr2
	if os.path.exists((on_index).replace('"','')):
		file_handeler(on_index)
	else:
		set_clipboard_data(on_index)
		print()
		pyautogui.hotkey('ctrl', 'v')
		set_clipboard_data_none()
curr2=''
curr=''
current=[]
def on_press(key):
	global current, curr, curr2, copied_items
	if key not in current:
		current.append(key)
		try:
			curr=int(eval(str(current).split(',')[-1].rstrip(']')))
		except:
			curr=False
		try:
			curr2=int(eval(str(current).split(',')[-2].rstrip(']')))
		except:
			curr2=False
		if len(current)==3 and curr!=False:
			on_index=copied_items[curr-1]
			try:
				main3(on_index)
			except:
				for i in on_index:
					main3(i)
		if len(current)==4 and curr!=False and curr2!=False:
			on_index=copied_items[curr2-1][curr-1]
			main3(on_index)
		if current==[keyboard.Key.shift, keyboard.KeyCode(char='x')]:
			get_copied_path()
		if current==[keyboard.Key.ctrl_l, keyboard.KeyCode(char='c')]:
			get_copied_item()
		if current==[keyboard.Key.ctrl_l, keyboard.KeyCode(char='v')]:
			pass
def on_release(key):
	global current, combinations1
	current=[]

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
