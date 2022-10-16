import asyncio
from telethon import TelegramClient
import feedparser
import requests


link_my = 'https://www.upwork.com/ab/feed/jobs/rss?sort=recency&subcategory2_uid=531770282584862726%2C531770282589057025%2C531770282589057026%2C531770282589057032%2C531770282589057031%2C531770282589057028%2C531770282584862733&category2_uid=531770282580668420&job_type=hourly%2Cfixed&proposals=0-4%2C5-9%2C10-14%2C15-19&budget=10-&verified_payment_only=1&hourly_rate=10-&location=Argentina%2CAustralia%2CAustria%2CBelgium%2CBrazil%2CBulgaria%2CCanada%2CChina%2CColombia%2CCyprus%2CCzech+Republic%2CDenmark%2CEgypt%2CEstonia%2CFrance%2CGeorgia%2CGermany%2CGreece%2CHong+Kong%2CIndonesia%2CIreland%2CIsrael%2CItaly%2CJapan%2CLatvia%2CLithuania%2CLuxembourg%2CMacedonia%2CMalaysia%2CMexico%2CNetherlands%2CNew+Zealand%2CNorway%2CPhilippines%2CPoland%2CPortugal%2CRomania%2CSingapore%2CSlovakia%2CSlovenia%2CSouth+Korea%2CSpain%2CSri+Lanka%2CSweden%2CSwitzerland%2CThailand%2CTurkey%2CUkraine%2CUnited+Arab+Emirates%2CUnited+Kingdom%2CUnited+States%2CUnited+States+Minor+Outlying+Islands%2CUnited+States+Virgin+Islands&paging=0%3B10&api_params=1&q=&securityToken=b1b184fddf1eaef152ce86d69fc03b1015a560b6a56596dca6634c381a9404aa360cc91bf7424915017fd5ef60ded133c58ed3c752ea28d34ff72c531dadc4ae&userUid=1374842260917178368&orgUid=1374842260917178369'
link_marina='https://www.upwork.com/ab/feed/jobs/rss?paging=0%3B20&q=%28translate+OR+localization+OR+translation%29+AND+English+to+Russian+OR+English+to+Ukrainian&sort=recency&api_params=1&securityToken=ec8baa0070a5b3cb253d6fc79b6e2e678b2c9b7b006efcd140dd9d2cb64b0e45b35ff3b0466bfb7a80e2d2582f52a7331469778df3a2b1865e008a53a02d2af2&userUid=1114122571854450688&orgUid=1114122571862839297'
api_id = 7897720
bot_token='1740933906:AAG4EkAVJbyVC_igbUY3ydIdvPK0CdVAROM'
api_hash = 'b89e71a29a55f18b3bb2aeba7a40013d'
my_id=423010172
marina_id=308675844
# client = TelegramClient('anon', api_id, api_hash)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
def get_xml(link):
    return requests.get(link).text


def parse(page):
    parsed_page = feedparser.parse(page)
    print(parsed_page)
    return {(i['title'], i.get('link')) for i in parsed_page['entries'] if 'Convert images to PDF' not in i['title']}


# page = get_xml(link_my)
# data_new = parse(page)
# print(data_new)
async def main():
    data=set()
    data2=set()
    while True:
        page = get_xml(link_my)
        await asyncio.sleep(60)
        data_new = parse(page)
        print(data_new-data)
        if data_new-data:
            for i in data_new-data:
                await bot.send_message(my_id, f'{i[0]}\n{i[1]}')
            print(data_new-data)
            data=data_new
        page2 = get_xml(link_marina)
        await asyncio.sleep(60)
        data_new2=parse(page2)
        if data_new2 - data2:
            for i in data_new2 - data2:
                await bot.send_message(marina_id, f'{i[0]}\n{i[1]}')
            print(data_new2 - data2)
            data2 = data_new2



with bot:
    bot.loop.run_until_complete(main())