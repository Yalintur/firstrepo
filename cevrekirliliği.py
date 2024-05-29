import discord
import os
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('help'):
        await message.channel.send('Sorular: \n Çevre kirliliği nedir? \n Çevre kirliliğini önlemek için yapılması gerekenler nelerdir? \n Çevre kirliliğine örnek fotoğraflar gösterebilir misin? \n Çevreye önem veren ve çevre dostu uygulamalar ve atıkları azaltmanın yolları hakkında daha fazla bilgi edinmek isteyen kişiler için öneriniz nedir? \n Çevre kirliliğini önemlemeye çalışan türk kuruluşlar hangileridir? \n TEMA Vakfı Nedir? \n ÇEVKO Nedir? \n Doğa Koruma Merkezi Nedir? \n Buğday Ekolojik Yaşamı Destekleme Derneğii Nedir?')

    if message.content.startswith('Çevre kirliliği nedir?'):
        await message.channel.send('Çevre kirliliği, insan faaliyetleri sonucu hava, su ve toprağın zararlı maddelerle kirlenmesidir. Bu kirlilik, ekosistemlere ve insan sağlığına ciddi zararlar verebilir. Sanayi atıkları, plastik kullanımı ve fosil yakıtların yanması çevre kirliliğinin başlıca sebepleridir.')


    if message.content.startswith('Çevre kirliliğini önlemek için yapılması gerekenler nelerdir?'):
        await message.channel.send("Çevre kirliliğini önlemek için geri dönüşüm ve atık yönetimine önem verilmelidir. Yenilenebilir enerji kaynakları kullanılmalı ve fosil yakıt tüketimi azaltılmalıdır. Ayrıca, çevre dostu ürünler tercih edilerek plastik kullanımından kaçınılmalıdır.")


    if message.content.startswith('Çevre kirliliğine örnek fotoğraflar gösterebilir misin?'):
        liste = os.listdir("cevreimage")
        resim = random.choice(liste)
        with open(f'cevreimage/{resim}', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file = picture)


    if message.content.startswith('Çevreye önem veren ve çevre dostu uygulamalar ve atıkları azaltmanın yolları hakkında daha fazla bilgi edinmek isteyen kişiler için öneriniz nedir?'):
        await message.channel.send("Çevre bilinci kazanmak için çevre dostu uygulamalar hakkında kitaplar ve makaleler okuyun, online kurslara ve belgesellere göz atın. Yerel veya uluslararası çevre gruplarına katılarak etkinliklere ve toplantılara katılın. Kendi bahçenizi yetiştirin ve sürdürülebilir alışveriş alışkanlıkları edinin. Mobil uygulamalar ve enerji tasarrufu sağlayan teknolojileri kullanarak doğal kaynak tüketiminizi azaltın")


    if message.content.startswith("Çevre kirliliğini önemlemeye çalışan türk kuruluşlar hangileridir?"):
        await message.channel.send("TEMA Vakfı (Türkiye Erozyonla Mücadele, Ağaçlandırma ve Doğal Varlıkları Koruma Vakfı) \n ÇEVKO (Çevre Koruma ve Ambalaj Atıkları Değerlendirme Vakfı) \n Doğa Koruma Merkezi (DKM) \n Buğday Ekolojik Yaşamı Destekleme Derneği")


    if message.content.startswith("TEMA Vakfı Nedir?"):
        await message.channel.send("1992 yılında kurulan TEMA Vakfı, erozyonla mücadele, ağaçlandırma ve doğal varlıkları koruma alanlarında çalışmalar yürütmektedir. Ayrıca çevre bilincini artırmak ve sürdürülebilir yaşamı teşvik etmek amacıyla eğitim programları düzenlemektedir.") 


    if message.content.startswith("ÇEVKO Nedir?"):
        await message.channel.send("1991 yılında kurulan ÇEVKO, Türkiye'de ambalaj atıklarının geri dönüşümünü teşvik eden ve bu konuda projeler geliştiren bir vakıftır. ÇEVKO, geri dönüşüm bilincini artırmak ve atık yönetimini iyileştirmek için çeşitli eğitim ve bilinçlendirme faaliyetleri yürütmektedir.")


    if message.content.startswith("Doğa Koruma Merkezi Nedir?"):
        await message.channel.send("2004 yılında kurulan Doğa Koruma Merkezi, biyolojik çeşitliliği koruma, sürdürülebilir kalkınma ve doğa koruma politikalarının geliştirilmesi alanlarında faaliyet gösteren bir sivil toplum kuruluşudur. DKM, çeşitli ekosistemlerin korunması ve sürdürülebilir kullanımı için projeler ve araştırmalar yürütmektedir.")
    

    if message.content.startswith("Buğday Ekolojik Yaşamı Destekleme Derneğii Nedir?"):
         await message.channel.send("2002 yılında kurulan Buğday Derneği, ekolojik yaşamı desteklemek ve sürdürülebilir tarım uygulamalarını yaygınlaştırmak amacıyla çalışmalar yapmaktadır. Dernek, ekolojik pazarlar, ekolojik turizm ve permakültür gibi alanlarda projeler geliştirerek çevre bilincini artırmayı hedeflemektedir.")

client.run("GİZLİ TOKEN BURAYA KONULACAK")
