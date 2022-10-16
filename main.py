import json

import requests
import chompjs
import requests
from io import StringIO
from lxml import etree
import re
import asyncio
from telethon import TelegramClient
# import feedparser
import requests


def olx_query():
    url = "https://www.olx.ua/d/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/zaporozhe"

    querystring = {"currency":"UAH","search[filter_float_price:to]":"12000","search[filter_enum_number_of_rooms_string][0]":"dvuhkomnatnye","search[filter_enum_number_of_rooms_string][1]":"trehkomnatnye"}

    payload = ""
    headers = {
        "cookie": "mobile_default=desktop; lang=uk; fingerprint=MTI1NzY4MzI5MTsxMjswOzA7MDsxOzA7MDswOzA7MDsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MDsxOzA7MDswOzA7MDswOzA7MDswOzA7MTsxOzA7MTswOzA7MDswOzA7MTswOzA7MDswOzA7MDswOzA7MDsxOzA7MDswOzA7MDswOzA7MTsxOzA7MDsxOzE7MDsxOzA7MDszMzE4ODUyNDk3OzI7MjsyOzI7MjsyOzU7Mjg0ODAwNjQxODsxMzU3MDQxNzM4OzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTswOzE7MDs0MTAwMjE5OTszNDY5MzA2NTUxOzQxMzMxNDk3NjM7Nzg1MjQ3MDI5OzMwMjEwNTkzMzY7MTkyMDsxMDgwOzI0OzI0OzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzE4MDsxMjA7MTgwOzEyMDsxODA7MTIwOzE4MDsxMjA7MDswOzA=; dfp_user_id=e49ff3a6-4c5d-43d6-a7bb-4551da1a2ad5-ver2; from_detail=0; __utmc=250720985; __utmz=250720985.1663062275.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); observed_aui=762712fe54da49e88838a12353a56467; _hjIncludedInSessionSample=0; user_adblock_status=true; ldTd=true; _gid=GA1.2.99454931.1663062279; __gfp_64b=7iC7DEn8YD_7wODC8rgBg52thIaL2cd.Y5.ue1caIhX.67|1663062284; lister_lifecycle=1663062313; _hjSessionUser_1617300=eyJpZCI6IjY2OGEwZGZlLWUzYTItNWYwOC1hNjdiLTk1NDU2NjgwOWEzZSIsImNyZWF0ZWQiOjE2NjMwNjIzMTYzMzMsImV4aXN0aW5nIjpmYWxzZX0=; __gsas=ID=50b32288b2c68156:T=1663062318:S=ALNI_MaiHVq9Q6EfqbdlbPpUS47w8oeGXA; laquesis=buy-2895@b#decision-377@b#decision-536@a#deluareb-1677@a#er-1708@a#er-1725@a#er-1778@b#f8nrp-1183@b#jobs-3482@a#jobs-3717@d#jobs-3722@a#jobs-3728@b#jobs-3837@c#jobs-3845@a#jobs-4023@a#oesx-1547@a#oeu2u-2441@b; laquesisff=aut-716#buy-2811#decision-657#euonb-114#euonb-48#grw-124#kuna-307#oesx-1437#oesx-1643#oesx-645#oesx-867#olxeu-29763#srt-1289#srt-1346#srt-1434#srt-1593#srt-1758#srt-477#srt-479#srt-682; laquesissu=; last_locations=194-0-0-%D0%97%D0%B0%D0%BF%D0%BE%D1%80%D1%96%D0%B6%D0%B6%D1%8F-%D0%97%D0%B0%D0%BF%D0%BE%D1%80%D1%96%D0%B7%D1%8C%D0%BA%D0%B0+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C-zaporozhe; my_city_2=194_0_0_%D0%97%D0%B0%D0%BF%D0%BE%D1%80%D1%96%D0%B6%D0%B6%D1%8F_0_%D0%97%D0%B0%D0%BF%D0%BE%D1%80%D1%96%D0%B7%D1%8C%D0%BA%D0%B0+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C_zaporozhe; _hjSessionUser_2218922=eyJpZCI6ImI0ZWI2YTcxLWM0OWQtNTA2Mi04ZDlmLWRkZDljMDgwNzI4NiIsImNyZWF0ZWQiOjE2NjMwNjIyNzU5MTksImV4aXN0aW5nIjp0cnVlfQ==; deviceGUID=324ab60f-eb2a-431d-b490-2f70a9484d73; a_access_token=25a96a68cef2c080dae80988924b197c43d2e732; a_refresh_token=7ee6fc106973f80149bc7cc4be6a3bcfb6443cd7; a_grant_type=device; user_id=919628355; user_business_status=private; delivery_l1=nedvizhimost; newrelic_cdn_name=CF; PHPSESSID=o3ove99301og7jodsijk020b8d; dfp_segment=%5B%5D; __utma=250720985.972830656.1663062275.1663062275.1663068331.2; __utmt=1; __utmb=250720985.1.10.1663068331; _hjSession_2218922=eyJpZCI6Ijc0ZjVhYmY1LTc5NTctNDUyMC1hYTY2LTY2MWMxYzk2YjZhNSIsImNyZWF0ZWQiOjE2NjMwNjgzMzE1MjAsImluU2FtcGxlIjpmYWxzZX0=; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2022-09-13%2014%3A25%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.olx.ua%2Fd%2Fuk%2Fnedvizhimost%2Fkvartiry%2Fzaporozhe%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.olx.ua%2Fuk%2F; sbjs_first_add=fd%3D2022-09-13%2014%3A25%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.olx.ua%2Fd%2Fuk%2Fnedvizhimost%2Fkvartiry%2Fzaporozhe%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.olx.ua%2Fuk%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F105.0.0.0%20Safari%2F537.36; _ga=GA1.1.972830656.1663062275; cto_bundle=qcBfVV9ZWEtpYng4R1dhVVFQZmtDUzliNmZ1TTglMkI4Y25xVEhzVUdXeFduSk1QRWhYMXhVM2pHUkM4NUZuU0ZVSVlsUDg3YVd4T2N4UUdkRmo2eTJiYzlxeHBWZlJPVVhFNU1MbURrZjFpQldUcUlGd1NidiUyRmZqeWRveVFMdmQlMkJzV1hDZCUyQm1mZ3ZLSmxMOHBROHBlVG5kcW5ldyUzRCUzRA; lqstatus=1663069852|1833698dcd7x396e716c|jobs-3717#buy-2895||; _gat_clientNinja=1; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.olx.ua%2Fd%2Fuk%2Fnedvizhimost%2Fkvartiry%2Fdolgosrochnaya-arenda-kvartir%2Fzaporozhe%2F%3Fcurrency%3DUAH%26search%255Bfilter_float_price%3Ato%255D%3D12000%26search%255Bfilter_enum_number_of_rooms_string%255D%255B0%255D%3Ddvuhkomnatnye%26search%255Bfilter_enum_number_of_rooms_string%255D%255B1%255D%3Dtrehkomnatnye; _ga_QFCVKCHXET=GS1.1.1663068331.2.1.1663068740.49.0.0; session_start_date=1663070556397; onap=183363c7f18x757710-2-1833698dcd7x396e716c-34-1663070556",
        "authority": "www.olx.ua",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9,uk;q=0.8",
        "cache-control": "max-age=0",
        "dnt": "1",
        "referer": "https://www.olx.ua/uk/",
        # "sec-ch-ua": ""Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"",
        "sec-ch-ua-mobile": "?0",
        # "sec-ch-ua-platform": ""Linux"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    return response.text


def parse(html):
    htmlparser=etree.HTMLParser()
    tree=etree.parse(StringIO(html),htmlparser)
    data = tree.xpath('//script[contains(text(),"window.__PRERENDERED_STATE__=")]/text()')
    if data:
        data = re.search(r'PRERENDERED_STATE__= \"(.*?)}}\";\n', data[0]).group(1) + '}}'
        data = data.replace('\\"', '"').replace('\\"', '"')
        data = json.loads(data)
        data = data['listing']['listing']['ads']




if __name__ == '__main__':
    data=olx_query()
    parse(data)
# async def main():
#     data=set()
#     data2=set()
#     while True:
#         page = olx_query()
#         await asyncio.sleep(60)
#         data_new = parse(page)
#         print(data_new-data)
#         if data_new-data:
#             for i in data_new-data:
#                 await bot.send_message(my_id, f'{i[0]}\n{i[1]}')
#             print(data_new-data)
#             data=data_new
#         page2 = get_xml(link_marina)
#         await asyncio.sleep(60)
#         data_new2=parse(page2)
#         if data_new2 - data2:
#             for i in data_new2 - data2:
#                 await bot.send_message(marina_id, f'{i[0]}\n{i[1]}')
#             print(data_new2 - data2)
#             data2 = data_new2
#
#
#
# with bot:
#     bot.loop.run_until_complete(main())