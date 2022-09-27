from tkinter import *
import subprocess

root = Tk()

root.geometry("300x250+300+300")
root.minsize(width=400, height=500)
root.title("Процессүүд дуудаж ажилуулах")

scrollbar = Scrollbar(root)

scrollbar.pack(side=RIGHT,
               fill=Y)

text_input = Text(root,
                  yscrollcommand=scrollbar.set)
text_input.pack(fill=BOTH)

text_output = Text(root, height=5,
                   bg="light cyan")
text_output.pack()
scrollbar.config(command=text_input.yview)


def call_batch_button():
    command = text_input.get("1.0", "end-1c")
    try:
        # p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
        result = subprocess.check_output(command, shell=True, cwd='.')
        text_input.insert(1.0, "\n$ " + command + result.decode("utf-8"))
    except Exception as e:
        text_output.insert(1.0, e)


batch_button = Button(root, text="Batch файл унших", command=call_batch_button)
batch_button.pack(ipadx=5, ipady=5, expand=True)
root.mainloop()
