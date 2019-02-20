import random as ran
import MsgMod as msg
import datetime

# subtract lifepoints
def subLifePoint(lifepoints, damage):
    total = lifepoints - damage
    return total

# add lifepoints
def addLifePoint(lifepoints, damage):
    total = lifepoints + damage
    return total

def flipCoin():
    now = datetime.date.today()
    toss = ran.randint(0, 1) # Toss variable's value randomly generated between the number 0 and 1
    if toss == 0:
        logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
        logfile.write("Coin Flip result: Heads" + '\n')
        logfile.close()
        msg.errormsg("Heads")
    else:
        logfile = open('logs/log_' + now.strftime('%Y_%m_%d') + '.txt', 'a')
        logfile.write("Coin Flip result: Tails" + '\n')
        logfile.close()
        msg.errormsg("Tails")