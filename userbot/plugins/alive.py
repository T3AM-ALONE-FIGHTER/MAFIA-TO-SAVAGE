
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in Mafia Userbot by @H1M4N5HU0P

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, mafiaversion
from savage.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SAVAGE BOT"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...


ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/f3a82860656f0263bc8aa.jpg"
file2 = "https://telegra.ph/file/a12fa182ccac24b2bb9a5.jpg"
file3 = "https://telegra.ph/file/581e32d5dae4c05d82fa1.jpg"
file4 = "https://telegra.ph/file/b39d4a5cb3f4ae080924b.jpg"
""" =======================CONSTANTS====================== """

pm_caption = "_π₯ ππ°ππ°πΆπ΄ π±πΎπ πΈπ πΎπ½ π΅πΈππ΄ π₯_\n\n"


pm_caption += f"               __βΌπΌπ°πππ΄π β__\n**      γ{DEFAULTUSER}γ**\n\n"


pm_caption += "π£ π°π±πΎππ πΌπ πππππ΄πΌ π£\n\n"


pm_caption += "βΎ ππ·π΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½ : 1.19.5\n"
pm_caption += "βΎ ππ΄π°πΌ πΆππΎππΏ  β£ [πΉπΎπΈπ½](https://t.me/joinchat/RPrJW2IU-Uo4MGRl)\n"
pm_caption += "βΎ πππΏπΏπΎππ π²π·π½π½π΄π» β£ [πΉπΎπΈπ½](https://t.me/joinchat/0KCyT0MHyAhmMmRl)\n"
pm_caption += "βΎ πππΏπΏπΎππ πΆππΎππΏ β£ [πΉπΎπΈπ½](https://t.me/joinchat/qCIk-af6VW1kNDll)\n"
pm_caption += "βΎ π²ππ΄π°ππΎπ    β£ [β‘ππ°πΌπ΄π΄πβ‘](@SAMEER_795)\n" 
                  
pm_caption += " \n"
pm_caption += "[β¨ π³π΄πΏπ»πΎπ ππΎππ πΎππ½ ππ°ππ°πΆπ΄ β¨](https://github.com/sameerpanthi/SAVAGE-2.0-BOT)"


# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(alive.chat_id, ok7, file=file2) 

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(alive.chat_id, ok8, file=file3)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(alive.chat_id, ok9, file=file1)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(alive.chat_id, ok10, file=file3)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(alive.chat_id, ok11, file=file2)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(alive.chat_id, ok12, file=file4)
    
    await asyncio.sleep(edit_time)
    ok14 = await borg.edit_message(alive.chat_id, on, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "savage", None, "To check am i alive with your favorite alive pic"
).add()
