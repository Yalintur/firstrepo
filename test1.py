@bot.command()
async def nasilsin(ctx):
    await ctx.send("İyiyim sen?")

@bot.command()
async def çarp(ctx, left: int, right: int):
    await ctx.send(f'İstediğin sayı:{left*right}')

@bot.command()
async def topla(ctx, left: int, right: int):
    await ctx.send(f'İstediğin sayı:{left+right}')

@bot.command()
async def çıkar(ctx, left: int, right: int):
    await ctx.send(f'İstediğin sayı:{left-right}')

@bot.command()
async def böl(ctx, left: int, right: int):
    if left == 0 and right == 0 :
        await ctx.send("Yazdığın şey tanımsız 0 ile 0 bölünemez")
    else:       
        await ctx.send(f'İstediğin sayı:{left/right}')

@bot.command()
async def üs(ctx, left: int, right: int):
    await ctx.send(f'İstediğin sayı:{left**right}')

bot.run("Gizli Token Buraya")
