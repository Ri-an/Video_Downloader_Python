#first the project need the libraries as pytube and tkinter along with python3.8.2

from pytube import YouTube
import tkinter

def dwn():
	
	link=E1.get()
	yt=YouTube(link)


	strms = yt.streams.filter(audio_codec="mp4a.40.2")

	i=1
	
	dwn=int(E2.get())

	vid=strms[dwn-1]

	src=str(E3.get())
	vid.download(src)

def disp():
	link=E1.get()
	yt=YouTube(link)
	strms = yt.streams.filter(audio_codec="mp4a.40.2")
	Tx.delete('1.0',tkinter.END)
	i=1
	for vid in strms:
		Tx.insert(tkinter.END,str(vid)+"\n")
		i += 1

top = tkinter.Tk()

L1 = tkinter.Label(master=top, text="video link")
L1.grid(row=0,column=0)
E1 = tkinter.Entry(master=top, bd =10)
E1.grid(row=0,column=1)
B1= tkinter.Button (master=top, text="submit", command=disp)
B1.grid(row=0,column=2)

Tx=tkinter.Text(master=top,height=20,width=40)
Tx.grid(row=2,column=0,columnspan=3)

L2=tkinter.Label(master=top,text="which")
L2.grid(row=3,column=0)
E2=tkinter.Entry(master=top,bd=10)
E2.grid(row=3,column=1)

L3 = tkinter.Label(master=top,text="where")
L3.grid(row=4,column=0)
E3=tkinter.Entry(master=top,bd=10)
E3.grid(row=4,column=1)

B2= tkinter.Button (master=top ,text="download",command=dwn)
B2.grid(row=5,column=1)


top.mainloop()
