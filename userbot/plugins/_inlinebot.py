#    Copyright (C) @SupRemE_AnanD 2021-2022
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
#    This Inline Helper Code is solely owned by @SupRemE_AnanD
#    You Should Not Copy This Code Without Proper Permission.

from math import ceil
from re import compile
import asyncio

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import *
from userbot.cmdhelp import *
from savage.utils import *
from userbot.Config import Config

mafia_row = Config.BUTTONS_IN_HELP
mafia_emoji = Config.EMOJI_IN_HELP
# thats how a lazy guy imports
# SAVAGE

def button(page, modules):
    Row = 6
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::3], modules[1::3])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"๐ " + pair, data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"โ๏ธ๏ธ๏ธ ๐ฑ๐ฐ๐ฒ๐บเผ", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"เผ๏ธ ๐ฒ๐ป๐พ๐๐ด เผ๏ธ", data="close"
            ),
            custom.Button.inline(
               f"เผ๐ฝ๐ด๐๐ โ๏ธ๏ธ๏ธ", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]
    # Changing this line may give error in bot as i added some special cmds in savage channel to get this module work...

    modules = CMD_HELP
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@savage_userbot":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            result = await builder.article(
                f"Hey! Only use .help please",
                text=f"**Rแดษดษดษชษดษข ๐๐๐๐๐๐ 2.0**\n\n__Nแดแดสแดส Oา Pสแดษขษขษชษดs Iษดsแดแดสสแดแด__ :`{len(CMD_HELP)}`\n**Pแดษขแด:** 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[โโโ โ]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        elif event.text=='':
            result = builder.article(
                "@MafiaBot_Support",
                text="""**Hแดส TสษชS Is [๐๐๐๐๐๐ 2.0](https://t.me/SAVAGE_USERBOT) \nYแดแด Cแดษด Kษดแดแดก Mแดสแด AสOแดแด Mแด Fสแดแด LษชษดแดS Gษชแด?แดษด Bแดสแดแดก ๐**""",
                buttons=[
                    [
                        custom.Button.url("๐ฅ CสแดNษดแดส ๐ฅ", "https://t.me/SAVAGE_TECHY"),
                        custom.Button.url(
                            "โก GสแดแดP โก", "https://t.me/sแดแด?แดษขแด_แดsแดสสแดแด"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "โจ Rแดแดแด โจ", "https://github.com/sameerpanthi/SAVAGE-2.0-BOT"),
                        custom.Button.url
                    (
                            "๐ฐ Cสแดแดแดแดส ๐ฐ", "https://t.me/SAMEER_795"
                    )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Hแดส Bษชแดแดส Dแดษดแด Usแด Mส สแดแด .. แดแดแดแด Uส Oแดกษด Usแดสสแดแด Aษดแด Usแด @SAVAGE_USERBOT",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"**Lแดษขแดษดแดสส Aา** [๐๐๐๐๐๐ 2.0](https://t.me/SAVAGE_USERBOT) __Wแดสแดษชษดษข...__\n\n**Nแดแดษดแดส Oา Mแดแดแดสแดs Iษดsแดแดสสแดแด :** `{len(CMD_HELP)}`\n**Pแดษขแด:** {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=False,
        )
        
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await delete_mafia(event,
              "โ๏ธ๐๐๐๐๐๐ 2.0 Bแดแด Mแดษดแด Pสแดแด?ษชแดแดส ษชs CLแดsแดแด Nแดแดกโ๏ธ\n\n         **[ยฉ ๐บ๐จ๐ฝ๐จ๐ฎ๐ฌ โข](t.me/SAVAGE_USERBOT)**", 5, link_preview=False
            )
        else:
            mafia_alert = "Hแดส Bษชแดแดส Dแดษดแด Usแด Mส สแดแด .. แดแดแดแด Uส Oแดกษด Usแดสสแดแด Aษดแด Usแด @SAVAGE_USERBOT"
            await event.answer(mafia_alert, cache_time=0, alert=True)
          
    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Hแดส Bษชแดแดส Dแดษดแด Usแด Mส สแดแด .. แดแดแดแด Uส Oแดกษด Usแดสสแดแด Aษดแด Usแด @SAVAGE_USERBOT",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "๐ " + cmd[0], data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("โ๏ธ๏ธ๏ธ ๐ฟ๐๐ด๐๐ธ๐พ๐๐เผ", data=f"page({page})")])
        await event.edit(
            f"**๐ File:** `{commands}`\n**๐ข Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Hแดส Bษชแดแดส Dแดษดแด Usแด Mส สแดแด .. แดแดแดแด Uส Oแดกษด Usแดสสแดแด Aษดแด Usแด @SAVAGE_USERBOT",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**๐ File:** `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**โฌ๏ธ Official:** {'โ' if CMD_HELP_BOT[cmd]['info']['official'] else 'โ'}\n"
                result += f"**โ?๏ธ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**โฌ๏ธ Official:** {'โ' if CMD_HELP_BOT[cmd]['info']['official'] else 'โ'}\n\n"
        else:
            result += f"**โฌ๏ธ Official:** {'โ' if CMD_HELP_BOT[cmd]['info']['official'] else 'โ'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**โ?๏ธ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**โน๏ธ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**๐? Commands:** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**๐? Commands:** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"**๐ฌ Explanation:** `{command['usage']}`\n\n"
        else:
            result += f"**๐ฌ Explanation:** `{command['usage']}`\n"
            result += f"**โจ๏ธ For Example:** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("โ๏ธ๏ธ๏ธ ๐ฟ๐๐ด๐๐ธ๐พ๐๐เผ", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )


# Ask owner before using it in your codes
# Kangers like LB stay away...
