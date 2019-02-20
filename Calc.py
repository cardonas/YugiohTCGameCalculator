import datetime
import tkinter as tk
import MathMod as math
import MsgMod as msg

# lifepoints for each duelists
duelistLp1 = 8000
duelistLp2 = 8000
duelistLp3 = 8000
duelistLp4 = 8000


# Two Player Game Mode
def twoPduel(names):
    nameList = names

    # logger
    now = datetime.date.today()
    log = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
    log.write('New Two Player Game Started\n' + nameList[0] + ' has ' + str(duelistLp1) + ' lifepoints\n')
    log.write(nameList[1] + ' has ' + str(duelistLp2) + ' lifepoints\n')
    log.close()

    # function resets lifepoint label
    def reset_lp():
        global duelistLp1, duelistLp2
        duelistLp1 = 8000
        duelistLp2 = 8000

        duelist1LP.config(text=duelistLp1)
        duelist2LP.config(text=duelistLp2)

        logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
        logfile.write("New Game Started\n")
        logfile.close()

    # function to determine winner
    def Win_Lose():
        global duelistLp1, duelistLp2
        if duelistLp1 <= 0 and duelistLp2 <= 0:
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write('This Duel is a Tie!!!')
            logfile.close()
            msg.winmsg('This Duel is a Tie!!!')
        elif duelistLp1 <= 0:
            duelist1LP.config(text=0)
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write(nameList[1] + ' Wins the Duel!!!')
            logfile.close()
            msg.winmsg(nameList[1] + ' Wins the Duel!!!')
        elif duelistLp2 <= 0:
            duelist2LP.config(text=0)
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write(nameList[0] + ' Wins the Duel!!!')
            logfile.close()
            msg.winmsg(nameList[0] + ' Wins the Duel!!!')

    # function to calculate damage and log events
    def takeDamage():
        global duelistLp1, duelistLp2
        try:
            damage1 = int(duelist1Entry.get())
            damage2 = int(duelist2Entry.get())

            if damage1 >= 0 and damage2 >= 0:

                # Duelist1
                if damage1 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage1) + ' damage to ' + nameList[0] + '\n')
                    logfile.close()
                duelistLp1 = math.subLifePoint(duelistLp1, damage1)
                duelist1LP.config(text=duelistLp1)
                duelist1Entry.delete(0, 'end')
                duelist1Entry.insert(0, '0')

                # Duelist2
                if damage2 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage2) + ' damage to ' + nameList[1] + '\n')
                    logfile.close()
                duelistLp2 = math.subLifePoint(duelistLp2, damage2)
                duelist2LP.config(text=duelistLp2)
                duelist2Entry.delete(0, 'end')
                duelist2Entry.insert(0, '0')
                Win_Lose()
            else:
                msg.errormsg('Please Enter a Positive Number')

        except:
            duelist1Entry.delete(0, 'end')
            duelist1Entry.insert(0, '0')
            duelist2Entry.delete(0, 'end')
            duelist2Entry.insert(0, '0')
            msg.errormsg("Please Enter a Positive Whole Number")

    # function to restore life points and log events
    def restoreLp():
        global duelistLp1, duelistLp2
        try:
            damage1 = int(duelist1Entry.get())
            damage2 = int(duelist2Entry.get())
            if damage1 >= 0 and damage2 >= 0:

                # Duelist1
                if damage1 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage1) + ' restored to ' + nameList[0] + '\n')
                    logfile.close()
                duelistLp1 = math.addLifePoint(duelistLp1, damage1)
                duelist1LP.config(text=duelistLp1)
                duelist1Entry.delete(0, 'end')
                duelist1Entry.insert(0, '0')

                # Duelist2
                if damage2 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage2) + ' restored to ' + nameList[1] + '\n')
                    logfile.close()
                duelistLp2 = math.addLifePoint(duelistLp2, damage2)
                duelist2LP.config(text=duelistLp2)
                duelist2Entry.delete(0, 'end')
                duelist2Entry.insert(0, '0')
                Win_Lose()
            else:
                msg.errormsg('Please Enter a Positive Number')

        except:
            duelist1Entry.delete(0, 'end')
            duelist1Entry.insert(0, '0')
            duelist2Entry.delete(0, 'end')
            duelist2Entry.insert(0, '0')
            msg.errormsg("Please Enter a Positive Whole Number")

    # tkinter frame containers
    twoPcontainer = tk.Tk()
    duelist1_frame = tk.Frame(twoPcontainer)
    duelist2_frame = tk.Frame(twoPcontainer)
    button_frame = tk.Frame(twoPcontainer)
    duelist1_frame.pack(pady=(10, 5), padx=10, fill='x')
    duelist2_frame.pack(padx=10, fill='x')
    button_frame.pack(pady=10, fill='x')

    # Window title
    twoPcontainer.wm_title('YuGiOh Duel Calculator')

    # Create Labels
    duelist1Label = tk.Label(duelist1_frame, text=nameList[0] + ':', width=10)
    duelist2Label = tk.Label(duelist2_frame, text=nameList[1] + ':', width=10)
    duelist1LP = tk.Label(duelist1_frame, text=duelistLp1, width=5)
    duelist2LP = tk.Label(duelist2_frame, text=duelistLp2, width=5)

    # Create entry boxes
    duelist1Entry = tk.Entry(duelist1_frame, width=10)
    duelist1Entry.insert(0, '0')
    duelist2Entry = tk.Entry(duelist2_frame, width=10)
    duelist2Entry.insert(0, '0')

    # Create reset button
    reset = tk.Button(button_frame, text='Reset', command=reset_lp, width=5)
    reset.pack(side='left', padx=(10, 0))

    # Create button to close window
    duel_quit = tk.Button(button_frame, text='close', command=twoPcontainer.destroy)
    duel_quit.pack(side='right', padx=(0, 10))

    # Create Buttons
    takeDamage1 = tk.Button(button_frame, text='-', command=takeDamage, width=5, )
    restoreLP1 = tk.Button(button_frame, text='+', command=restoreLp, width=5)
    coinFlip = tk.Button(button_frame, text='Flip Coin', command=math.flipCoin, width=10)

    # Pack all into Frame
    duelist1Label.pack(side='left')
    duelist1LP.pack(side='left')
    duelist1Entry.pack(side='right')
    takeDamage1.pack(side='left', padx=(20, 0))
    restoreLP1.pack(side='left')
    coinFlip.pack(side='right', padx=(0, 20))
    duelist2Label.pack(side='left')
    duelist2LP.pack(side='left')
    duelist2Entry.pack(side='right')

    twoPcontainer.geometry('300x125')
    twoPcontainer.resizable(0, 0)


def threePduel(names):
    nameList = names

    # Creates log
    now = datetime.date.today()
    log = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
    log.write('New Three Player Game Started\n' + nameList[0] + ' has ' + str(duelistLp1) + ' lifepoints\n')
    log.write(nameList[1] + ' has ' + str(duelistLp2) + ' lifepoints\n')
    log.write(nameList[2] + ' has ' + str(duelistLp3) + ' lifepoints\n')
    log.close()

    # Resets life points Label to start new game
    def reset_lp():
        global duelistLp1, duelistLp2, duelistLp3
        duelistLp1 = 8000
        duelistLp2 = 8000
        duelistLp3 = 8000

        duelist1LP.config(text=duelistLp1)
        duelist2LP.config(text=duelistLp2)
        duelist3LP.config(text=duelistLp3)

        logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
        logfile.write("New Game Started\n")
        logfile.close()

    # determines who wins the game
    def Win_Lose():
        global duelistLp1, duelistLp2, duelistLp3
        if duelistLp1 <= 0 and duelistLp2 <= 0 and duelistLp3 <= 0:
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write('This Duel is a Tie!!!')
            logfile.close()
            msg.winmsg('This Duel is a Tie!!!')
        elif duelistLp1 <= 0 and duelistLp2 <= 0:
            duelist1LP.config(text=0)
            duelist2LP.config(text=0)
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write(nameList[2] + ' Wins the Duel!!!')
            logfile.close()
            msg.winmsg(nameList[2] + ' Wins the Duel!!!')
        elif duelistLp2 <= 0 and duelistLp3 <= 0:
            duelist2LP.config(text=0)
            duelist3LP.config(text=0)
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write(nameList[0] + ' Wins the Duel!!!')
            logfile.close()
            msg.winmsg(nameList[0] + ' Wins the Duel!!!')
        elif duelistLp1 <= 0 and duelistLp3 <= 0:
            duelist1LP.config(text=0)
            duelist3LP.config(text=0)
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write(nameList[1] + ' Wins the Duel!!!')
            logfile.close()
            msg.winmsg(nameList[1] + ' Wins the Duel!!!')

    # function to calculate damage and log the events
    def takeDamage():
        global duelistLp1, duelistLp2, duelistLp3
        try:
            damage1 = int(duelist1Entry.get())
            damage2 = int(duelist2Entry.get())
            damage3 = int(duelist3Entry.get())

            if damage1 >= 0 and damage2 >= 0 and damage3 >= 0:

                # Duelist1
                if damage1 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage1) + ' damage to ' + nameList[0] + '\n')
                    logfile.close()
                duelistLp1 = math.subLifePoint(duelistLp1, damage1)
                duelist1LP.config(text=duelistLp1)
                duelist1Entry.delete(0, 'end')
                duelist1Entry.insert(0, '0')

                # Duelist2
                if damage2 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage2) + ' damage to ' + nameList[1] + '\n')
                    logfile.close()
                duelistLp2 = math.subLifePoint(duelistLp2, damage2)
                duelist2LP.config(text=duelistLp2)
                duelist2Entry.delete(0, 'end')
                duelist2Entry.insert(0, '0')

                # Duelist3
                if damage3 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage3) + ' damage to ' + nameList[2] + '\n')
                    logfile.close()
                duelistLp3 = math.subLifePoint(duelistLp3, damage3)
                duelist3LP.config(text=duelistLp3)
                duelist3Entry.delete(0, 'end')
                duelist3Entry.insert(0, '0')

                Win_Lose()

            else:
                msg.errormsg('Please Enter a Positive Number')

        except:
            duelist1Entry.delete(0, 'end')
            duelist1Entry.insert(0, '0')
            duelist2Entry.delete(0, 'end')
            duelist2Entry.insert(0, '0')
            duelist3Entry.delete(0, 'end')
            duelist3Entry.insert(0, '0')
            msg.errormsg("Please Enter a Positive Whole Number")

    # functions to restore lifepoints and log the events
    def restoreLp():
        global duelistLp1, duelistLp2, duelistLp3
        try:
            damage1 = int(duelist1Entry.get())
            damage2 = int(duelist2Entry.get())
            damage3 = int(duelist3Entry.get())
            if damage1 >= 0 and damage2 >= 0 and damage3 >= 0:

                # Duelist1
                if damage1 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage1) + ' restored to ' + nameList[0] + '\n')
                    logfile.close()
                duelistLp1 = math.addLifePoint(duelistLp1, damage1)
                duelist1LP.config(text=duelistLp1)
                duelist1Entry.delete(0, 'end')
                duelist1Entry.insert(0, '0')

                # Duelist2
                if damage2 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage2) + ' restored to ' + nameList[1] + '\n')
                    logfile.close()
                duelistLp2 = math.addLifePoint(duelistLp2, damage2)
                duelist2LP.config(text=duelistLp2)
                duelist2Entry.delete(0, 'end')
                duelist2Entry.insert(0, '0')

                # Duelist3
                if damage3 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage3) + ' restored to ' + nameList[2] + '\n')
                    logfile.close()
                duelistLp3 = math.addLifePoint(duelistLp3, damage3)
                duelist3LP.config(text=duelistLp3)
                duelist3Entry.delete(0, 'end')
                duelist3Entry.insert(0, '0')

                Win_Lose()

            else:
                msg.errormsg('Please Enter a Positive Number')

        except:
            duelist1Entry.delete(0, 'end')
            duelist1Entry.insert(0, '0')
            duelist2Entry.delete(0, 'end')
            duelist2Entry.insert(0, '0')
            duelist3Entry.delete(0, 'end')
            duelist3Entry.insert(0, '0')
            msg.errormsg("Please Enter a Positive Whole Number")

    # tkinter frame containers
    threePcontainer = tk.Tk()
    duelist1_frame = tk.Frame(threePcontainer)
    duelist2_frame = tk.Frame(threePcontainer)
    duelist3_frame = tk.Frame(threePcontainer)
    button_frame = tk.Frame(threePcontainer)
    duelist1_frame.pack(pady=(10, 5), padx=10, fill='x')
    duelist2_frame.pack(padx=10, pady=(0, 5), fill='x')
    duelist3_frame.pack(padx=10, fill='x')
    button_frame.pack(pady=10, fill='x')

    # Window title
    threePcontainer.wm_title('YuGiOh Duel Calcuator')

    # Create Labels
    duelist1Label = tk.Label(duelist1_frame, text=nameList[0] + ':', width=5)
    duelist2Label = tk.Label(duelist2_frame, text=nameList[1] + ':', width=5)
    duelist3Label = tk.Label(duelist3_frame, text=nameList[2] + ':', width=5)
    duelist1LP = tk.Label(duelist1_frame, text=duelistLp1, width=5)
    duelist2LP = tk.Label(duelist2_frame, text=duelistLp2, width=5)
    duelist3LP = tk.Label(duelist3_frame, text=duelistLp3, width=5)

    # Create entry boxes
    duelist1Entry = tk.Entry(duelist1_frame, width=10)
    duelist1Entry.insert(0, '0')
    duelist2Entry = tk.Entry(duelist2_frame, width=10)
    duelist2Entry.insert(0, '0')
    duelist3Entry = tk.Entry(duelist3_frame, width=10)
    duelist3Entry.insert(0, '0')

    # Create reset button
    reset = tk.Button(button_frame, text='Reset', command=reset_lp, width=5)
    reset.pack(side='left', padx=(10, 0))

    duel_quit = tk.Button(button_frame, text='Close', command=threePcontainer.destroy)
    duel_quit.pack(side='right', padx=(0, 10))

    # Create Buttons
    takeDamage1 = tk.Button(button_frame, text='-', command=takeDamage, width=5, )
    restoreLP1 = tk.Button(button_frame, text='+', command=restoreLp, width=5)
    coinFlip = tk.Button(button_frame, text='Flip Coin', command=math.flipCoin, width=10)

    # Pack all into Frame
    duelist1Label.pack(side='left')
    duelist1LP.pack(side='left')
    duelist1Entry.pack(side='right')
    takeDamage1.pack(side='left', padx=(20, 0))
    restoreLP1.pack(side='left')
    coinFlip.pack(side='right', padx=(0, 20))
    duelist2Label.pack(side='left', )
    duelist2LP.pack(side='left', )
    duelist2Entry.pack(side='right')

    duelist3Label.pack(side='left')
    duelist3LP.pack(side='left')
    duelist3Entry.pack(side='right')

    threePcontainer.geometry('300x150')
    threePcontainer.resizable(0, 0)


def fourPduel(names):
    nameList = names

    # Creates Log
    now = datetime.date.today()
    log = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
    log.write('New Four Player Game Started\n' + nameList[0] + ' has ' + str(duelistLp1) + ' lifepoints\n')
    log.write(nameList[1] + ' has ' + str(duelistLp2) + ' lifepoints\n')
    log.write(nameList[2] + ' has ' + str(duelistLp3) + ' lifepoints\n')
    log.write(nameList[3] + ' has ' + str(duelistLp4) + ' lifepoints\n')
    log.close()

    # function to reset lifepoint count
    def reset_lp():
        global duelistLp1, duelistLp2, duelistLp3, duelistLp4
        duelistLp1 = 8000
        duelistLp2 = 8000
        duelistLp3 = 8000
        duelistLp4 = 8000

        duelist1LP.config(text=duelistLp1)
        duelist2LP.config(text=duelistLp2)
        duelist3LP.config(text=duelistLp3)
        duelist4LP.config(text=duelistLp4)

        logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
        logfile.write("New Game Started\n")
        logfile.close()

    # function to determine the winnner
    def Win_Lose():
        global duelistLp1, duelistLp2, duelistLp3, duelistLp4

        # Tie
        if duelistLp1 <= 0 and duelistLp2 <= 0 and duelistLp3 <= 0 and duelistLp4 <= 0:
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write('This Duel is a Tie!!!')
            logfile.close()
            msg.winmsg('This Duel is a Tie!!!')

        # duelist4 wins
        elif duelistLp1 <= 0 and duelistLp2 <= 0 and duelistLp3 <= 0:
            duelist1LP.config(text=0)
            duelist2LP.config(text=0)
            duelist3LP.config(text=0)
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write(nameList[3] + ' Wins the Duel!!!')
            logfile.close()
            msg.winmsg(nameList[3] + ' Wins the Duel!!!')

        # duelist1 wins
        elif duelistLp2 <= 0 and duelistLp3 <= 0 and duelistLp4 <= 0:
            duelist2LP.config(text=0)
            duelist3LP.config(text=0)
            duelist4LP.config(text=0)
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write(nameList[0] + ' Wins the Duel!!!')
            logfile.close()
            msg.winmsg(nameList[0] + ' Wins the Duel!!!')

        # duelist2 wins
        elif duelistLp1 <= 0 and duelistLp3 <= 0 and duelistLp4 <= 0:
            duelist1LP.config(text=0)
            duelist3LP.config(text=0)
            duelist4LP.config(text=0)
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write(nameList[1] + ' Wins the Duel!!!')
            logfile.close()
            msg.winmsg(nameList[1] + ' Wins the Duel!!!')

        # duelist3 wins
        elif duelistLp1 <= 0 and duelistLp2 <= 0 and duelistLp4 <= 0:
            duelist1LP.config(text=0)
            duelist2LP.config(text=0)
            duelist4LP.config(text=0)
            logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
            logfile.write(nameList[2] + ' Wins the Duel!!!')
            logfile.close()
            msg.winmsg(nameList[2] + ' Wins the Duel!!!')

    # function to calculate damage and log the events
    def takeDamage():
        global duelistLp1, duelistLp2, duelistLp3, duelistLp4
        try:
            damage1 = int(duelist1Entry.get())
            damage2 = int(duelist2Entry.get())
            damage3 = int(duelist3Entry.get())
            damage4 = int(duelist4Entry.get())

            if damage1 >= 0 and damage2 >= 0 and damage3 >= 0 and damage4 >= 0:

                # Duelist1
                if damage1 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage1) + ' damage to ' + nameList[0] + '\n')
                    logfile.close()
                duelistLp1 = math.subLifePoint(duelistLp1, damage1)
                duelist1LP.config(text=duelistLp1)
                duelist1Entry.delete(0, 'end')
                duelist1Entry.insert(0, '0')

                # Duelist2
                if damage2 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage2) + ' damage to ' + nameList[1] + '\n')
                    logfile.close()
                duelistLp2 = math.subLifePoint(duelistLp2, damage2)
                duelist2LP.config(text=duelistLp2)
                duelist2Entry.delete(0, 'end')
                duelist2Entry.insert(0, '0')

                # Duelist3
                if damage3 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage3) + ' damage to ' + nameList[2] + '\n')
                    logfile.close()
                duelistLp3 = math.subLifePoint(duelistLp3, damage3)
                duelist3LP.config(text=duelistLp3)
                duelist3Entry.delete(0, 'end')
                duelist3Entry.insert(0, '0')

                # Duelist4
                if damage4 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage4) + ' damage to ' + nameList[3] + '\n')
                    logfile.close()
                duelistLp4 = math.subLifePoint(duelistLp4, damage4)
                duelist4LP.config(text=duelistLp4)
                duelist4Entry.delete(0, 'end')
                duelist4Entry.insert(0, '0')

                Win_Lose()

            else:
                msg.errormsg('Please Enter a Positive Number')

        except:
            duelist1Entry.delete(0, 'end')
            duelist1Entry.insert(0, '0')
            duelist2Entry.delete(0, 'end')
            duelist2Entry.insert(0, '0')
            duelist3Entry.delete(0, 'end')
            duelist3Entry.insert(0, '0')
            duelist4Entry.delete(0, 'end')
            duelist4Entry.insert(0, '0')
            msg.errormsg("Please Enter a Positive Whole Number")

    # function to restore lifepoints and log the events
    def restoreLp():
        global duelistLp1, duelistLp2, duelistLp3, duelistLp4
        try:
            damage1 = int(duelist1Entry.get())
            damage2 = int(duelist2Entry.get())
            damage3 = int(duelist3Entry.get())
            damage4 = int(duelist4Entry.get())
            if damage1 >= 0 and damage2 >= 0 and damage3 >= 0 and damage4 >= 0:

                # Duelist1
                if damage1 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage1) + ' restored to ' + nameList[0] + '\n')
                    logfile.close()
                duelistLp1 = math.addLifePoint(duelistLp1, damage1)
                duelist1LP.config(text=duelistLp1)
                duelist1Entry.delete(0, 'end')
                duelist1Entry.insert(0, '0')

                # Duelist2
                if damage2 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage2) + ' restored to ' + nameList[1] + '\n')
                    logfile.close()
                duelistLp2 = math.addLifePoint(duelistLp2, damage2)
                duelist2LP.config(text=duelistLp2)
                duelist2Entry.delete(0, 'end')
                duelist2Entry.insert(0, '0')

                # Duelist3
                if damage3 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage3) + ' restored to ' + nameList[2] + '\n')
                    logfile.close()
                duelistLp3 = math.addLifePoint(duelistLp3, damage3)
                duelist3LP.config(text=duelistLp3)
                duelist3Entry.delete(0, 'end')
                duelist3Entry.insert(0, '0')

                # Duelist4
                if damage4 > 0:
                    logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
                    logfile.write('There was ' + str(damage4) + ' restored to ' + nameList[3] + '\n')
                    logfile.close()
                duelistLp4 = math.addLifePoint(duelistLp4, damage4)
                duelist4LP.config(text=duelistLp4)
                duelist4Entry.delete(0, 'end')
                duelist4Entry.insert(0, '0')

                Win_Lose()

            else:
                msg.errormsg('Please Enter a Positive Number')

        except:
            duelist1Entry.delete(0, 'end')
            duelist1Entry.insert(0, '0')
            duelist2Entry.delete(0, 'end')
            duelist2Entry.insert(0, '0')
            duelist3Entry.delete(0, 'end')
            duelist3Entry.insert(0, '0')
            duelist4Entry.delete(0, 'end')
            duelist4Entry.insert(0, '0')
            msg.errormsg("Please Enter a Positive Whole Number")

    # tkinter frame containers
    fourPcontainer = tk.Tk()
    duelist1_frame = tk.Frame(fourPcontainer)
    duelist2_frame = tk.Frame(fourPcontainer)
    duelist3_frame = tk.Frame(fourPcontainer)
    duelist4_frame = tk.Frame(fourPcontainer)
    button_frame = tk.Frame(fourPcontainer)
    duelist1_frame.pack(pady=(10, 5), padx=10, fill='x')
    duelist2_frame.pack(padx=10, pady=(0, 5), fill='x')
    duelist3_frame.pack(padx=10, pady=(0, 5), fill='x')
    duelist4_frame.pack(padx=10, fill='x')
    button_frame.pack(pady=10, fill='x')

    # Window title
    fourPcontainer.wm_title('YuGiOh Duel Calcuator')

    # Create Labels
    duelist1Label = tk.Label(duelist1_frame, text=nameList[0] + ':', width=5)
    duelist2Label = tk.Label(duelist2_frame, text=nameList[1] + ':', width=5)
    duelist3Label = tk.Label(duelist3_frame, text=nameList[2] + ':', width=5)
    duelist4Label = tk.Label(duelist4_frame, text=nameList[3] + ':', width=5)
    duelist1LP = tk.Label(duelist1_frame, text=duelistLp1, width=5)
    duelist2LP = tk.Label(duelist2_frame, text=duelistLp2, width=5)
    duelist3LP = tk.Label(duelist3_frame, text=duelistLp3, width=5)
    duelist4LP = tk.Label(duelist4_frame, text=duelistLp4, width=5)

    # Create entry boxes
    duelist1Entry = tk.Entry(duelist1_frame, width=10)
    duelist1Entry.insert(0, '0')
    duelist2Entry = tk.Entry(duelist2_frame, width=10)
    duelist2Entry.insert(0, '0')
    duelist3Entry = tk.Entry(duelist3_frame, width=10)
    duelist3Entry.insert(0, '0')
    duelist4Entry = tk.Entry(duelist4_frame, width=10)
    duelist4Entry.insert(0, '0')

    # Create reset button
    reset = tk.Button(button_frame, text='Reset', command=reset_lp, width=5)
    reset.pack(side='left', padx=(10, 0))

    duel_quit = tk.Button(button_frame, text='Close', command=fourPcontainer.destroy)
    duel_quit.pack(side='right', padx=(0, 10))

    # Create Buttons
    takeDamage1 = tk.Button(button_frame, text='-', command=takeDamage, width=5, )
    restoreLP1 = tk.Button(button_frame, text='+', command=restoreLp, width=5)
    coinFlip = tk.Button(button_frame, text='Flip Coin', command=math.flipCoin, width=10)

    # Pack all into Frame
    duelist1Label.pack(side='left')
    duelist1LP.pack(side='left')
    duelist1Entry.pack(side='right')
    takeDamage1.pack(side='left', padx=(20, 0))
    restoreLP1.pack(side='left')
    coinFlip.pack(side='right', padx=(0, 20))
    duelist2Label.pack(side='left', )
    duelist2LP.pack(side='left', )
    duelist2Entry.pack(side='right')

    duelist3Label.pack(side='left')
    duelist3LP.pack(side='left')
    duelist3Entry.pack(side='right')

    duelist4Label.pack(side='left')
    duelist4LP.pack(side='left')
    duelist4Entry.pack(side='right')

    fourPcontainer.geometry('300x190')
    fourPcontainer.resizable(0, 0)
