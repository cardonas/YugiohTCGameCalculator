import tkinter as tk
from tkinter import ttk
import datetime

# view logs
def viewlog():

    try:
        now = datetime.date.today()
        log = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'r')
        viewer = tk.Tk()
        scroll = tk.Scrollbar(viewer)
        scroll.pack(side='right', fill='y')
        viewer.wm_title('Game Log')
        logview = tk.Text(viewer, state='normal', height=30, width=60, yscrollcommand=scroll.set)
        logview.insert('end', log.read())
        log.close()
        scroll.config(command=logview.yview)
        b1 = ttk.Button(viewer, text='Close', command=viewer.destroy)
        logview.pack()
        b1.pack(pady=10)

        viewer.mainloop()

    except FileNotFoundError:
        errormsg("There is no log available")

    else:
        exit()

# msg when error occurs
def errormsg(msg):
        popup = tk.Tk()

        popup.wm_title('! Error')
        label = tk.Label(popup, text=msg)
        label.pack(side='top', fill='x', pady=10)
        b1 = ttk.Button(popup, text='OK', command=popup.destroy)
        b1.pack()
        popup.resizable(0, 0)
        popup.mainloop()

# message for winner
def winmsg(msg):
        win = tk.Tk()

        win.wm_title('Winner!!!')
        label = tk.Label(win, text=msg)
        label.pack(side='top', fill='x', pady=10)
        b1 = ttk.Button(win, text='OK', command=win.destroy)
        b1.pack()
        win.resizable(0, 0)
        win.mainloop()
