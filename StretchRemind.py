import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import sleep
from ttkthemes import themed_tk as tk

timer = 0
snooze = 0
stretch_time = 0
############################
# Looping the App Function #
############################
def stretchy_truthy(win, more, ee1,ee2):
    global timer
    global root
    global snooze
    global stretch_time
    print('Answer', more)
    if more:
        win.destroy()
        if ee1 and ee2:
            snooze = int(ee1)
            stretch_time = int(ee2)
            print(ee1)
            print(ee2)
        sleep(snooze)
        timer = timer + 1
        StretchRemindMain(more, stretch_time)
    else:
        win.destroy()
        root.destroy()


#################################
# Progress Bar loading Function #
#################################
def bar(progress, stretchTime):
    import time
    stretchTime = stretchTime / 5
    progress['value'] = 20
    root.update()
    time.sleep(stretchTime)

    progress['value'] = 40
    root.update()
    time.sleep(stretchTime)

    progress['value'] = 50
    root.update()
    time.sleep(stretchTime)

    progress['value'] = 60
    root.update()
    time.sleep(stretchTime)

    progress['value'] = 80
    root.update()
    time.sleep(stretchTime)
    progress['value'] = 100


#####################
# Main App Function #
#####################
def StretchRemindMain(more, stretchTime):
    global root
    print('Execution', timer)
    win = Toplevel()
    win.withdraw()
    win.update_idletasks()
    x = (win.winfo_screenwidth() + win.winfo_reqwidth()) / 2
    y = (win.winfo_screenheight() + win.winfo_reqheight()) / 2
    win.geometry("+%d+%d" % (x, y))
    win.deiconify()
    # win = root
    win.title('Stretchy Time!!')
    message1 = 'Time for Stretch Bud!'
    message2 = 'Current Snooze time={0} seconds'.format(snooze)
    message3 = 'Do you wanna continue?'
    if not more:
        message1 = 'Stretch reminder cos your a busy wolf!'
        message3 = 'Do you wanna Start?'
    ttk.Label(win, text=' ').grid(column=0, row=0)
    ttk.Label(win, text=message1, font=("Times Bold", 14)).grid(column=0, row=1, padx=(100, 100))
    ttk.Label(win, text=message2, font=("Times Bold", 10)).grid(column=0, row=2, padx=(100, 100))
    ttk.Label(win, text=message3, font=("Times Bold", 10)).grid(column=0, row=3, padx=(100, 100))
    if not more:
        e1 = ttk.Entry(win)
        e1.grid(column=0, row=4, sticky='w', padx=(100, 0), pady=(15, 15),ipadx=(5))
        e2 = ttk.Entry(win)
        e2.grid(column=0, row=4,sticky='e', padx=(0, 100), pady=(15, 15),ipadx=(5))
        def ee1():
            val1 = e1.get()
            val2 = e2.get()
            try:
                val1 = int(val1)
                val2 = int(val2)
            except OSError as err:
                print("OS error: {0}".format(err))
                tkinter.messagebox.showwarning('Uh-Oh', 'Somthing went wrong, try to reopen the App')
            except ValueError:
                print("Could not convert data to an integer.")
                tkinter.messagebox.showwarning('I want Numbers', 'Sorry My Dude, those fields are for numbers only')
            except:
                print("Unexpected error:", sys.exc_info()[0])
                tkinter.messagebox.showerror('Unexpected error', 'Please Restart the Application')
            else:
                print(val1)
                print(val2)
                stretchy_truthy(win, True, val1, val2)
        continue_btn = ttk.Button(win, text='Yes', command=lambda: ee1())
        continue_btn.grid(column=0, row=5, padx=(100, 100), pady=(15, 15))
    if more:
        yes_btn = ttk.Button(win, text='Yes', command=lambda: stretchy_truthy(win, True, False, False))
        yes_btn.grid(column=0, row=4, sticky='w', padx=(100, 0), pady=(15, 15))
        no_btn = ttk.Button(win, text='No', command=lambda: stretchy_truthy(win, False, False, False)).grid(column=0, row=4,sticky='e', padx=(0, 100),pady=(15, 15))
        yes_btn.focus()
        ttk.Label(win, text=' ').grid(column=0, row=5)
        progress = ttk.Progressbar(win, orient=HORIZONTAL, length=200, mode='determinate')
        progress.grid(column=0, row=6, pady=(0, 15))
        bar(progress, stretchTime)
    win.lift()
    win.attributes('-topmost', True)

    def on_closing():
        tkinter.messagebox.showinfo('Really Dude?', 'You really done working for today?')
        root.destroy()
    win.protocol("WM_DELETE_WINDOW", on_closing)


print('\n\n\n')
print('Welcome to Stretchy Time!')
print('-------------------------------------------------')
print('The app will keep running until you select no')
print('-------------')
# snooze = int(input('Enter Snooze interval:'))  # * 60
# stretch_time = int(input('Enter Stretch Time interval (Seconds):'))
print('\n\nThanks! You will get your first reminder in {0} seconds'.format(snooze))
print('\n')
print('Starting....')

root = Tk()
root.withdraw()

timer = 1
StretchRemindMain(False, stretch_time)



#
# root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
print('Exiting, bye')
