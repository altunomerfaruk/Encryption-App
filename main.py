import tkinter

#Screen
screen = tkinter.Tk()
screen.title("Encryption App")
screen.minsize(400, 700)

#First text
title = tkinter.Label(screen, text="Encryption App", font=("Arial", 20))
title.pack(side="top")

#Gif
img = tkinter.PhotoImage(file="topSecret.gif").subsample(3, 3)
panel = tkinter.Label(screen, image=img)
panel.image = img
panel.pack(side="top")

#Text(Title)
textTitle = tkinter.Label(screen, text="Enter your title", font=("Arial", 14),pady=10)
textTitle.pack(side="top")

#Entry(Title)
EntryTitle = tkinter.Entry(screen)
EntryTitle.pack(side="top")

#Text(Secret)
textSecret = tkinter.Label(screen, text="Enter your secret", font=("Arial", 14),pady=10)
textSecret.pack(side="top")

#Text(Secret)
EntrySecret = tkinter.Text(screen,height = 15, width = 29)
EntrySecret.pack(side="top")

#Text(Key)
textKey = tkinter.Label(screen, text="Enter master key", font=("Arial", 14),pady=10)
textKey.pack(side="top")

#Entry(Key)
EntryKey = tkinter.Entry(screen)
EntryKey.pack(side="top")

#Button(Save)
ButtonSave = tkinter.Button(screen, width=14 , text= "Save and Encrypt",pady=10, height=1)
ButtonSave.pack(side="top")

#Button(Decrypt)
ButtonSave = tkinter.Button(screen, width=10 , text= "Decrypt",pady=10 , height=1)
ButtonSave.pack(side="top")

screen.mainloop()