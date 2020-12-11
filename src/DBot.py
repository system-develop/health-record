import json, random, datetime, re, config
import mysql.connector as db
from urllib.parse import urlparse
import discord
from discord.ext import commands
from discord.utils import find
intents = discord.Intents.all()
intents.members = True

 # コネクションの作成
conn = db.connect(
    host=config.HST,
    port=config.PRT,
    user=config.USN,
    password=config.PSW,
    database=config.DBS
)

#接続再試行
conn.ping(reconnect=True)
#接続確認
print(conn.is_connected())
#省略
cur = conn.cursor()

link_regex = re.compile(
    r'^https?://(?:(ptb|canary)\.)?discordapp\.com/channels/'
    r'(?:([0-9]{15,21})|(@me))'
    r'/(?P<channel_id>[0-9]{15,21})/(?P<message_id>[0-9]{15,21})/?$'
)

client = discord.Client()

random_contents = [
    "元気そうで何よりです。その調子で健康を維持しましょう",
    "今の時期、健康第一が何よりモットーです。その心がけをこれからも",
    "(｀･ω･´)",
]


@client.event
async def on_ready():
    print('私は {0.user} です。'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == "!health 😄":
        content = random.choice(random_contents)
        await message.channel.send(content)
        print(message.author.id)

        try:
            customer = [
                (message.author.id, message.author.display_name, 'テスト')
            ]
            health = [
                (message.author.id, 1, 'テスト')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name, remark) VALUES (%s, %s, %s)', customer)
            cur.executemany('insert into health (customer_id, normal, remark) VALUES (%s, %s, %s)', health)
            conn.commit()

        except:
            conn.rollback()
            raise

    elif message.content == "!health 😷":
        await message.channel.send('咳メッセージ')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name, 'テスト')
            ]
            health = [
                (message.author.id, 1, 'テスト')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name, remark) VALUES (%s, %s, %s)', customer)
            cur.executemany('insert into health (customer_id, cough, remark) VALUES (%s, %s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 🤐":
        await message.channel.send('息苦しさメッセージ')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name, 'テスト')
            ]
            health = [
                (message.author.id, 1, 'テスト')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name, remark) VALUES (%s, %s, %s)', customer)
            cur.executemany('insert into health (customer_id, choking, remark) VALUES (%s, %s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 🤧":
        await message.channel.send('鼻水メッセージ')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name, 'テスト')
            ]
            health = [
                (message.author.id, 1, 'テスト')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name, remark) VALUES (%s, %s, %s)', customer)
            cur.executemany('insert into health (customer_id, nose, remark) VALUES (%s, %s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 😵":
        await message.channel.send('喉の痛みメッセージ')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name, 'テスト')
            ]
            health = [
                (message.author.id, 1, 'テスト')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name, remark) VALUES (%s, %s, %s)', customer)
            cur.executemany('insert into health (customer_id, throat, remark) VALUES (%s, %s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 👿":
        await message.channel.send('体のだるさメッセージ')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name, 'テスト')
            ]
            health = [
                (message.author.id, 1, 'テスト')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name, remark) VALUES (%s, %s, %s)', customer)
            cur.executemany('insert into health (customer_id, tired, remark) VALUES (%s, %s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 🥶":
        await message.channel.send('腹痛メッセージ')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name, 'テスト')
            ]
            health = [
                (message.author.id, 1, 'テスト')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name, remark) VALUES (%s, %s, %s)', customer)
            cur.executemany('insert into health (customer_id, stomachache, remark) VALUES (%s, %s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 🤢":
        await message.channel.send('下痢メッセージ')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name, 'テスト')
            ]
            health = [
                (message.author.id, 1, 'テスト')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name, remark) VALUES (%s, %s, %s)', customer)
            cur.executemany('insert into health (customer_id, diarrhea, remark) VALUES (%s, %s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 🤕":
        await message.channel.send('頭痛メッセージ')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name, 'テスト')
            ]
            health = [
                (message.author.id, 1, 'テスト')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name, remark) VALUES (%s, %s, %s)', customer)
            cur.executemany('insert into health (customer_id, headache, remark) VALUES (%s, %s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 👅":
        await message.channel.send('味覚異常メッセージ')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name, 'テスト')
            ]
            health = [
                (message.author.id, 1, 'テスト')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name, remark) VALUES (%s, %s, %s)', customer)
            cur.executemany('insert into health (customer_id, dysgeusia, remark) VALUES (%s, %s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    elif message.content == "!health 👃":
        await message.channel.send('嗅覚異常メッセージ')
        print(message.author.id)
        try:
            customer = [
                (message.author.id, message.author.display_name, 'テスト')
            ]
            health = [
                (message.author.id, 1, 'テスト')
            ]
            cur.executemany('insert ignore into customer (customer_id, customer_name, remark) VALUES (%s, %s, %s)', customer)
            cur.executemany('insert into health (customer_id, dysosmia, remark) VALUES (%s, %s, %s)', health)
            conn.commit()
        except:
            conn.rollback()
            raise

    if message.content == '!cmdlist':
        await message.channel.send\
        ('``` !health_対応する絵文字 → 現在の体調を絵文字で表す。\
        \n !temp_〇〇.〇 → 現在の体温を記録する。\
        \n !elist → !healthの対応する絵文字を表示する。\
        \n !mylist → 自分が投稿した過去の情報を返す。```')

    if message.content == '!elist':
        await message.channel.send\
        ('```異常なし 😄\
        \n 咳 😷\
        \n 鼻水 🤧\
        \n 喉の痛み 😫\
        \n 体のだるさ 😔\
        \n 腹痛 😰\
        \n 下痢 😖\
        \n 頭痛 🤕\
        \n 味覚異常 👅\
        \n 嗅覚異常 👃```')

# temp
@bot.command()
async def temp(ctx, arg):
    
    if float(arg) < 35 or float(arg) > 41:
        # print("aacc")
        embed = discord.Embed(title="体温入力", color=0xdc2502)
        embed.add_field(name='エラー ', value=f'{arg}は無効の体温数値です。内容を再確認してください。')
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title="体温入力", color=0x3cd070)
        embed.add_field(name='送信できました。', value='一日に2回以上送った場合は最後のメッセージのみが有効です。')
        await ctx.send(embed = embed)


client.run(config.TKN)
cur.close()
conn.close()
