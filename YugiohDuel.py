import datetime
import tkinter as tk
import Calc as calc
import MsgMod as msg


largeFont = ("Veranda", 18)
normFont = ('Veranda', 12)
smallFount = ('veranda', 10)
names = ['Player 1', 'Player 2', 'Player 3', 'Player 4']

now = datetime.date.today()


class Yugioh_backEnd(tk.Tk):

    # set default initialization
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "YuGiOh Duel Calculator")

        # containers
        container = tk.Frame(self)

        # set pack method for container
        container.pack(side="top", fill="both", expand=True)

        # set grid method for container
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Set up Menu Bar
        menubar = tk.Menu(container)
        fileMenu = tk.Menu(menubar, tearoff=0)
        fileMenu.add_command(label='Quit', command=lambda: self.client_exit())
        option = tk.Menu(menubar, tearoff=0)
        option.add_command(label='Change Quantity', command=lambda: self.show_frame(NumPlayers))
        number_players = tk.Menu(option, tearoff=0)
        number_players.add_command(label='2 player', command=lambda: self.show_frame(TwoPlayer))
        number_players.add_command(label='3 player', command=lambda: self.show_frame(ThreePlayer))
        number_players.add_command(label='4 player', command=lambda: self.show_frame(FourPlayer))
        option.add_cascade(label='# of players', menu=number_players)
        logview = tk.Menu(menubar, tearoff=0)
        logview.add_command(label='ViewLog', command=lambda: msg.viewlog())
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label='Options', menu=option)
        menubar.add_cascade(label='View', menu=logview)

        tk.Tk.config(self, menu=menubar)

        # selects which frame to show
        self.frames = {}

        for F in (StartPage, NumPlayers, TwoPlayer, ThreePlayer, FourPlayer):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # show Frame
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def hide_frame(self, cont):
        frame = self.frames[cont]
        frame.destroy()

    def client_exit(self):
        exit()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # greet the user
        greeting = tk.Label(self, text="Welcome to\n YuGiOh Duel Calculator!", font=largeFont)
        greeting.pack(pady=(10, 20), padx=30)

        # Enter the next window
        lets_duel = tk.Button(self, text="Lets Duel!!!", command=lambda: controller.show_frame(NumPlayers))
        lets_duel.pack(pady=(0, 20), padx=30)


class NumPlayers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=30, height=20)

        # Add frames
        self.top_frame = tk.Frame(self)
        self.mid_frame = tk.Frame(self)
        self.bot_frame = tk.Frame(self)

        # prompt for players quantity
        self.prompt1 = tk.Label(self.top_frame, text="How many duelist?", font=largeFont)

        # Number of players
        self.twoPlayers = tk.Button(self.mid_frame, text="2 Duelists", command=lambda: controller.show_frame(TwoPlayer))
        self.threePlayers = tk.Button(self.mid_frame, text="3 Duelists",
                                      command=lambda: controller.show_frame(ThreePlayer))
        self.fourPlayers = tk.Button(self.mid_frame, text="4 Duelists",
                                     command=lambda: controller.show_frame(FourPlayer))
        self.return1 = tk.Button(self.bot_frame, text="Return Home", command=lambda: controller.show_frame(StartPage))

        # Pack frames
        self.top_frame.pack(pady=(30, 10))
        self.mid_frame.pack(pady=10)
        self.bot_frame.pack(pady=(10, 30))

        # Pack Prompt
        self.prompt1.pack()

        # Add buttons to frame
        self.twoPlayers.pack(pady=(5, 5))
        self.threePlayers.pack(pady=(5, 5))
        self.fourPlayers.pack(pady=(5, 5))
        self.return1.pack(side='left')


# Two player mode
class TwoPlayer(tk.Frame):

    # sets up main window for setup of game
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.top_frame = tk.Frame(self)
        self.mid_frame = tk.Frame(self)
        self.bot_frame = tk.Frame(self)

        # duelist1
        self.duelist1Label = tk.Label(self.top_frame, text="Duelist 1")
        self.duelist2Label = tk.Label(self.mid_frame, text="Duelist 2")
        self.duelist1Entry = tk.Entry(self.top_frame, width=10)
        self.duelist2Entry = tk.Entry(self.mid_frame, width=10)
        self.messageDuel = tk.Label(self.top_frame, text="Duelist have been entered.\n Please press \"Duel\" to start!",
                                    font=('Verdana', 12, 'bold'))

        # Command Buttons
        self.listAppend = tk.Button(self.bot_frame, text="Add Duelists", command=self.createDuelButton)
        self.duel = tk.Button(self.bot_frame, text="Duel", command=self.duelTwo, font=('Verdana', 20))
        self.back = tk.Button(self.bot_frame, text="Back", command=lambda: controller.show_frame(NumPlayers))
        self.changePlayers = tk.Button(self.bot_frame, text="Change Duelists", command=self.errorBack)

        # pack frames
        self.top_frame.pack(pady=(30, 0))
        self.mid_frame.pack(pady=(5, 5))
        self.bot_frame.pack(pady=(5, 10), padx=30)

        # Add widgets to frame
        self.duelist1Label.pack(side='left', padx=(0, 10))
        self.duelist1Entry.pack(side='right')
        self.duelist2Label.pack(side='left', padx=(0, 10))
        self.duelist2Entry.pack(side='right')

        # Pack buttons
        self.back.pack(side='left', padx=(0, 50))
        self.listAppend.pack()

    # Will allow you to go back a step and change players names.
    def errorBack(self):
        # hide error widgets
        self.messageDuel.pack_forget()
        self.duel.pack_forget()
        self.changePlayers.pack_forget()
        self.top_frame.pack_forget()
        self.mid_frame.pack_forget()
        self.bot_frame.pack_forget()

        # Add Frames Again
        self.top_frame.pack(pady=(30, 0))
        self.mid_frame.pack(pady=(5, 5))
        self.bot_frame.pack(pady=(5, 10), padx=30)

        # Add widgets to frame
        self.duelist1Label.pack(side='left')
        self.duelist1Entry.pack(side='right')
        self.duelist2Label.pack(side='left')
        self.duelist2Entry.pack(side='right')

        # Pack buttons
        self.back.pack(side='left', padx=(0, 50))
        self.listAppend.pack()

    # creates window and duel button the send you to main game window.
    def createDuelButton(self):
        names.clear()
        self.nameAppend()
        name = names

        if len(name) == 2 and self.listAppend and '' not in names:
            self.listAppend.pack_forget()
            self.duelist1Label.pack_forget()
            self.duelist2Label.pack_forget()
            self.duelist1Entry.pack_forget()
            self.duelist2Entry.pack_forget()
            self.back.pack_forget()
            self.mid_frame.pack_forget()
            self.messageDuel.pack(pady=(0, 30))
            self.changePlayers.pack(side='left', padx=(0, 50))
            self.duel.pack()
        else:
            msg.errormsg('Not enough players. Please enter all names.')

    # Adds names to list
    def nameAppend(self):
        duelist1 = self.duelist1Entry.get()
        names.append(duelist1)
        duelist2 = self.duelist2Entry.get()
        self.duelist2Entry.get()
        names.append(duelist2)
        return names

    # Runs creates and brings up main window for two player mode.
    @staticmethod
    def duelTwo():
        calc.twoPduel(names)


class ThreePlayer(tk.Frame):

    # sets up my window for Three player mode
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.top_frame = tk.Frame(self)
        self.mid_frame = tk.Frame(self)
        self.d3_frame = tk.Frame(self)
        self.bot_frame = tk.Frame(self)

        # duelist1
        self.duelist1Label = tk.Label(self.top_frame, text="Duelist 1")
        self.duelist2Label = tk.Label(self.mid_frame, text="Duelist 2")
        self.duelist3Label = tk.Label(self.d3_frame, text="Duelist 3")
        self.duelist1Entry = tk.Entry(self.top_frame, width=10)
        self.duelist2Entry = tk.Entry(self.mid_frame, width=10)
        self.duelist3Entry = tk.Entry(self.d3_frame, width=10)
        self.messageDuel = tk.Label(self.top_frame, text="Duelist have been entered.\n Please press \"Duel\" to start!",
                                    font=('Verdana', 12, 'bold'))

        # Command Buttons
        self.listAppend = tk.Button(self.bot_frame, text="Add Duelists", command=self.createDuelButton)
        self.duel = tk.Button(self.bot_frame, text="Duel", command=self.duelThree, font=('Verdana', 20))
        self.back = tk.Button(self.bot_frame, text="Back", command=lambda: controller.show_frame(NumPlayers))
        self.changePlayers = tk.Button(self.bot_frame, text="Change Duelists", command=self.errorBack)

        # pack frames
        self.top_frame.pack(pady=(30, 0))
        self.mid_frame.pack(pady=(5, 5))
        self.d3_frame.pack(pady=(5, 5))
        self.bot_frame.pack(pady=(5, 10), padx=30)

        # Add widgets to frame
        self.duelist1Label.pack(side='left')
        self.duelist1Entry.pack(side='right')
        self.duelist2Label.pack(side='left')
        self.duelist2Entry.pack(side='right')
        self.duelist3Label.pack(side='left')
        self.duelist3Entry.pack(side='right')

        # Pack buttons
        self.back.pack(side='left', padx=(0, 50))
        self.listAppend.pack()

    # Will allow you to go back a step and change players names.
    def errorBack(self):
        # hide error widgets
        self.messageDuel.pack_forget()
        self.duel.pack_forget()
        self.changePlayers.pack_forget()
        self.top_frame.pack_forget()
        self.mid_frame.pack_forget()
        self.bot_frame.pack_forget()

        # Add Frames Again
        self.top_frame.pack(pady=(30, 0))
        self.mid_frame.pack(pady=(5, 5))
        self.d3_frame.pack(pady=(5, 5))
        self.bot_frame.pack(pady=(5, 10), padx=30)

        # Add widgets to frame
        self.duelist1Label.pack(side='left')
        self.duelist1Entry.pack(side='right')
        self.duelist2Label.pack(side='left')
        self.duelist2Entry.pack(side='right')
        self.duelist3Label.pack(side='left')
        self.duelist3Entry.pack(side='right')

        # Pack buttons
        self.back.pack(side='left', padx=(0, 50))
        self.listAppend.pack()

    # creates window and duel button the send you to main game window.
    def createDuelButton(self):
        names.clear()
        self.nameAppend()
        name = names

        if len(name) == 3 and self.listAppend and '' not in names:
            self.listAppend.pack_forget()
            self.duelist1Label.pack_forget()
            self.duelist2Label.pack_forget()
            self.duelist3Label.pack_forget()
            self.duelist1Entry.pack_forget()
            self.duelist2Entry.pack_forget()
            self.duelist3Entry.pack_forget()
            self.back.pack_forget()
            self.mid_frame.pack_forget()
            self.d3_frame.pack_forget()
            self.messageDuel.pack(pady=(0, 30))
            self.changePlayers.pack(side='left', padx=(0, 50))
            self.duel.pack()
        else:
            msg.errormsg('Not enough players. Please enter all names.')

    def nameAppend(self):
        duelist1 = self.duelist1Entry.get()
        names.append(duelist1)
        duelist2 = self.duelist2Entry.get()
        names.append(duelist2)
        duelist3 = self.duelist3Entry.get()
        names.append(duelist3)
        return names

    @staticmethod
    def duelThree():
        calc.threePduel(names)


class FourPlayer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.top_frame = tk.Frame(self)
        self.mid_frame = tk.Frame(self)
        self.d3_frame = tk.Frame(self)
        self.d4_frame = tk.Frame(self)
        self.bot_frame = tk.Frame(self)

        # duelist1
        self.duelist1Label = tk.Label(self.top_frame, text="Duelist 1")
        self.duelist2Label = tk.Label(self.mid_frame, text="Duelist 2")
        self.duelist3Label = tk.Label(self.d3_frame, text="Duelist 3")
        self.duelist4Label = tk.Label(self.d4_frame, text='Duelist 4')
        self.duelist1Entry = tk.Entry(self.top_frame, width=10)
        self.duelist2Entry = tk.Entry(self.mid_frame, width=10)
        self.duelist3Entry = tk.Entry(self.d3_frame, width=10)
        self.duelist4Entry = tk.Entry(self.d4_frame, width=10)
        self.messageDuel = tk.Label(self.top_frame, text="Duelist have been entered.\n Please press \"Duel\" to start!",
                                    font=('Verdana', 12, 'bold'))

        # Command Buttons
        self.listAppend = tk.Button(self.bot_frame, text="Add Duelists", command=self.createDuelButton)
        self.duel = tk.Button(self.bot_frame, text="Duel", command=self.duelFour, font=('Verdana', 20))
        self.back = tk.Button(self.bot_frame, text="Back", command=lambda: controller.show_frame(NumPlayers))
        self.changePlayers = tk.Button(self.bot_frame, text="Change Duelists", command=self.errorBack)

        # pack frames
        self.top_frame.pack(pady=(30, 0))
        self.mid_frame.pack(pady=(5, 5))
        self.d3_frame.pack(pady=(5, 5))
        self.d4_frame.pack(pady=(5, 5))
        self.bot_frame.pack(pady=(5, 10), padx=30)

        # Add widgets to frame
        self.duelist1Label.pack(side='left')
        self.duelist1Entry.pack(side='right')
        self.duelist2Label.pack(side='left')
        self.duelist2Entry.pack(side='right')
        self.duelist3Label.pack(side='left')
        self.duelist3Entry.pack(side='right')
        self.duelist4Label.pack(side='left')
        self.duelist4Entry.pack(side='right')

        # Pack buttons
        self.back.pack(side='left', padx=(0, 50))
        self.listAppend.pack()

    def errorBack(self):
        # hide error widgets
        self.messageDuel.pack_forget()
        self.duel.pack_forget()
        self.changePlayers.pack_forget()
        self.top_frame.pack_forget()
        self.mid_frame.pack_forget()
        self.bot_frame.pack_forget()

        # Add Frames Again
        self.top_frame.pack(pady=(30, 0))
        self.mid_frame.pack(pady=(5, 5))
        self.d3_frame.pack(pady=(5, 5))
        self.d4_frame.pack(pady=(5, 5))
        self.bot_frame.pack(pady=(5, 10), padx=30)

        # Add widgets to frame
        self.duelist1Label.pack(side='left')
        self.duelist1Entry.pack(side='right')
        self.duelist2Label.pack(side='left')
        self.duelist2Entry.pack(side='right')
        self.duelist3Label.pack(side='left')
        self.duelist3Entry.pack(side='right')
        self.duelist4Label.pack(side='left')
        self.duelist4Entry.pack(side='right')

        # Pack buttons
        self.back.pack(side='left', padx=(0, 50))
        self.listAppend.pack()

    def createDuelButton(self):
        names.clear()
        self.nameAppend()
        name = names

        if len(name) == 4 and self.listAppend and '' not in names:
            self.listAppend.pack_forget()
            self.duelist1Label.pack_forget()
            self.duelist2Label.pack_forget()
            self.duelist3Label.pack_forget()
            self.duelist1Entry.pack_forget()
            self.duelist2Entry.pack_forget()
            self.duelist3Entry.pack_forget()
            self.back.pack_forget()
            self.mid_frame.pack_forget()
            self.d3_frame.pack_forget()
            self.d4_frame.pack_forget()
            self.messageDuel.pack(pady=(0, 30))
            self.changePlayers.pack(side='left', padx=(0, 50))
            self.duel.pack()
        else:
            msg.errormsg('Not enough players. Please enter all names.')

    def nameAppend(self):
        duelist1 = self.duelist1Entry.get()
        names.append(duelist1)
        duelist2 = self.duelist2Entry.get()
        names.append(duelist2)
        duelist3 = self.duelist3Entry.get()
        names.append(duelist3)
        duelist4 = self.duelist4Entry.get()
        names.append(duelist4)
        return names

    @staticmethod
    def duelFour():
        calc.fourPduel(names)


app = Yugioh_backEnd()
app.mainloop()
