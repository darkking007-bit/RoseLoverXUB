from Wylie import ubot, tbot, stacy, xbot, TOKEN
import Wylie.events
import sys

try:
  stacy.start()
  xbot.start()
  ubot.start()
  tbot.start(bot_token=TOKEN)
except:
  print("Invalid STRING/Token__bot exiting...")
  sys.exit()
  
ubot.run_until_disconnected()
xbot.run_until_disconnected()
stacy.run_until_disconnected()
tbot.run_until_disconnected()
