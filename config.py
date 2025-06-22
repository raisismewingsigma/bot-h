import discord
from discord.ext import commands


token = "dirahasiakan"

class detect_url:
    async def on_message(message):
        if message.author.bot:
            return
        if "https://" in message.content or "http://" in message.content:
        
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"[ALERT] {message.author} (ID: {message.author.id}) mengirim URL: {message.content}\n")

        # Coba ban user
            try:
                await message.author.ban(reason="Mengirim URL di chat")
                await message.channel.send(f"{message.author.mention} telah dibanned karena mengirim URL.")
            except discord.Forbidden:
                await message.channel.send("Bot tidak punya izin untuk ban member ini.")
            except discord.HTTPException as e:
                await message.channel.send("Terjadi error saat mencoba ban user.")
                print(e)
        else:
        
            await message.channel.send(message.content)
