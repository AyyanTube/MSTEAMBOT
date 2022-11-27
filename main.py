#bot made by @srfxdz 
#contact me on telegram @srfxdz 
#edit it at your own risk
#if translator not working try runnig "pip install googletrans==3.1.0a0" in terminal


from gtts import gTTS
from glitch_this import ImageGlitcher
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterPhotos
from requests import get
from io import BytesIO
import glob
from googletrans import Translator
import io
from ip import LOGO_LINKS
from bs4 import BeautifulSoup
from serpapi import GoogleSearch
from ff import gh
from aiogram.types import InputFile
from aiogram import Bot, Dispatcher, executor, types
import logging
import os
import argparse
from multiprocessing import Pool
import tqdm
from pexels_api import API
import string
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import Throttled
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import time
import re
from values import *
import requests
import string
import random
import argparse
import sys
import os
session = requests.Session()


OWNER = ["5234223466"]

TOKEN = "enter-your-bot-token-here"
PREFIX = "!/."



logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start', 'help'], commands_prefix=PREFIX)
async def helpstr(message: types.Message):

    kk = await message.reply("<b> Welcome Sir </b>")

    seconds = time.time()
    local_time = time.ctime(seconds)

    await kk.edit_text(
        f"""<b>Hey ! @{message.from_user.username} \nYou Started A Shining Star on  : {local_time} \nIf you are interested in knowing my commands send /cmds \n By the way your UserID is <code> {message.from_user.id} </code>\n Bot by: </b> <a href='https://t.me/srfxdz'>srfxdz</a>""",
        disable_web_page_preview=True)


@dp.message_handler(commands=['tr'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
  try:
    inp = message.text[len('/tr '):]
    rd3_lang = inp[0:2]

    if message.reply_to_message:
      language = message.reply_to_message.text

    else:
      language = inp[3:]

    translator = Translator()
    to_lang = rd3_lang
    text_to_translate = translator.translate(language, dest=to_lang)
    text = text_to_translate.text
    await message.reply(text)

  except :
    await message.reply(
      'Invalid Format example: /voice (language code) text to translate \n to see language code type /code'
    )


@dp.message_handler(commands=['voice'], commands_prefix=PREFIX)
async def cdgfgh(message: types.Message):
  try:
    inp = message.text[len('/voice '):]
    rd3_lang = inp[0:2]

    if message.reply_to_message:
      language = message.reply_to_message.text

    else:
      language = inp[3:]

    translator = Translator()
    to_lang = rd3_lang
    text_to_translate = translator.translate(language, dest=to_lang)
    text = text_to_translate.text
    speak = gTTS(text=text, lang=to_lang, slow=False)
    name = random.randint(1, 2000)
    title = f"voice{name}.mp3"
    speak.save(title)
    await message.reply_voice(InputFile(title))
    os.remove(title)
  except:
    await message.reply(
      'Invalid Format example: /voice (language code) text to translate \n to see language code type /code'
    )


@dp.message_handler(commands=['code'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):

  text = """
    
Language Name	Language Code
Afrikaans	af
Irish	ga
Albanian	sq
Italian	it
Arabic	ar
Japanese	ja
Azerbaijani	az
Kannada	kn
Basque	eu
Korean	ko
Bengali	bn
Latin	la
Belarusian	be
Latvian	lv
Bulgarian	bg
Lithuanian	lt
Catalan	ca
Macedonian	mk
Chinese Simplified	zh-CN
Malay	ms
Chinese Traditional	zh-TW
Maltese	mt
Croatian	hr
Norwegian	no
Czech	cs
Persian	fa
Danish	da
Polish	pl
Dutch	nl
Portuguese	pt
English	en
Romanian	ro
Esperanto	eo
Russian	ru
Estonian	et
Serbian	sr
Filipino	tl
Slovak	sk
Finnish	fi
Slovenian	sl
French	fr
Spanish	es
Galician	gl
Swahili	sw
Georgian	ka
Swedish	sv
German	de
Tamil	ta
Greek	el
Telugu	te
Gujarati	gu
Thai	th
Haitian Creole	ht
Turkish	tr
Hebrew	iw
Ukrainian	uk
Hindi	hi
Urdu	ur
Hungarian	hu
Vietnamese	vi
Icelandic	is
Welsh	cy
Indonesian	id
Yiddish	yi"""

  await message.reply(text)


PAYMENTS_TOKEN = "284685063:TEST:NTRiNjUwNWNlZjg1"
item_url = "https://images.indianexpress.com/2022/06/Telegram-premium-subscription.jpg"
# prices
PRICE = types.LabeledPrice(label="Bot Premium",
                           amount=10 * 100)  # amount need be in cents!



@dp.message_handler(commands=['pass', 'password'], commands_prefix=PREFIX)
async def kk(message: types.Message):

    cc = 12

    import random
    import array
    MAX_LEN = cc

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    UPCASE_CHARACTERS = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    SYMBOLS = [
        '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~',  '*', '(', ')',

    ]

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(int(MAX_LEN) - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        passwrd = password + x
        password = f"<code>{passwrd}</code>"

    return await message.reply(f"Your Password Is {password}")


def spotify():

    import array
    MAX_LEN = 12

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(int(MAX_LEN) - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    passx = password

    email_length = 9
    characters = string.ascii_letters + string.ascii_uppercase
    email = ""
    for index in range(email_length):
        email = email + random.choice(characters)
    first = email
    last = first

    def getRandomString(length):  # Letters and numbers
        pool = string.ascii_lowercase+string.digits
        return "".join(random.choice(pool) for i in range(length))

    yopmail = "yopmail.com"

    mail = (yopmail)

    nickname = last

    def generate():
        nick = nickname+getRandomString(3)
        passw = passx
        email = nickname+"@"+mail

        headers = {"Accept-Encoding": "gzip",
                   "Accept-Language": "en-US",
                   "App-Platform": "Android",
                   "Connection": "Keep-Alive",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Host": "spclient.wg.spotify.com",
                   "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
                   "Spotify-App-Version": "8.6.72",
                   "X-Client-Id": getRandomString(32)}

        payload = {"creation_point": "client_mobile",
                   "gender": "male" if random.randint(0, 1) else "female",
                   "birth_year": random.randint(1990, 2000),
                   "displayname": nick,
                   "iagree": "true",
                   "birth_month": random.randint(1, 11),
                   "password_repeat": passw,
                   "password": passw,
                   "key": "142b583129b2df829de3656f9eb484e6",
                   "platform": "Android-ARM",
                   "email": email,
                   "birth_day": random.randint(1, 20)}

        r = requests.post(
            'https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload)

        if r.status_code == 200:
            if r.json()['status'] == 1:
                return (True, f"""<b>Spotify Account Generated ✅ </b>
    
<b>Email</b> : {email}
<b>password </b>: <code>{passw}</code>""")
            else:
                # Details available in r.json()["errors"]
                return (False, "Could not create the account, some errors occurred")
        else:
            return (False, "Could not load the page. Response code: " + str(r.status_code))

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", "--number", help="how many accounts to generate, default is 1",
                            type=lambda x: (int(x) > 0) and int(x) or sys.exit("Invalid number: minimum amount is 1"))
        parser.add_argument(
            "-o", "--output", help="output file, default mm = s to the console")
        args = parser.parse_args()

        N = args.number if args.number else 1
        file = open(args.output, "a") if args.output else sys.stdout

        for i in range(N):
            result = generate()
            if result[0]:
                kk = result[1]

                if file is not sys.stdout:
                    kk = result[1]

            else:
                kk = str(i+1) + "/" + str(N)+": "+result[1]

        return kk


@dp.message_handler(commands=['spotify'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):

    return await message.reply(spotify())


# --------------------------------------------------------promote---------------------------------------------------------------------------------


@dp.message_handler(commands=['bio'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):

    ff = random.choice(gh)
    return await message.reply(ff)


@dp.message_handler(commands=['fake'], commands_prefix=PREFIX)
async def igfgnfokc(message: types.Message):
    import requests
    import random
    import string

    URL = "https://random-data-api.com/api/users/random_user"

    response = requests.get(url=URL)

    data = response.json()

    N = 8
    ph = ''.join(random.choices(string.digits, k=N))
    phone = "98" + ph
    name1 = data["first_name"]
    name2 = data["last_name"]
    email = data["email"]
    dob = data["date_of_birth"]
    zip = data["address"]["zip_code"]
    add1 = data["address"]["street_address"]
    city = data["address"]["city"]
    state = data["address"]["state"]
    co = data["address"]["country"]

    inf = f"""
data generated :)
<b>
Name  = <code> {name1} {name2} </code>
Email = <code>{email}</code>
phone = <code>+91{phone}</code>
street = <code>{add1}  </code> 
city = <code>{city}</code>
state = <code>{state}</code>
country = <code>{co}</code>
zip code = <code>{zip}</code>
DOB = <code>{dob}</code>

<b>generated by</b> -» <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
</b>
  """

    return await message.reply(inf)


@dp.message_handler(commands=['us'], commands_prefix=PREFIX)
async def igfgnfokc(message: types.Message):

    import requests as r
    #s = r.Session()

    h = {
        'authority': 'randommer.io',
        'method': 'POST',
        'path': '/random-address',
        'scheme': 'https',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '51',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'ezoadgid_232529=-1; ezoref_232529=bing.com; ezosuibasgeneris-1=480921f6-bf96-4e03-660f-f25e86951321; ezoab_232529=mod40-c; active_template::232529=pub_site_mobile.1667732569; ezopvc_232529=1; ezepvv=155; ezovid_232529=400410709; lp_232529=https://randommer.io/random-address; ezovuuidtime_232529=1667732569; ezovuuid_232529=bc7360d7-797b-4ef9-7419-8d96d36c1777; ezds=ffid%3D2%2Cw%3D494%2Ch%3D1021; ezohw=w%3D494%2Ch%3D924; ezux_lpl_232529=1667732574390|2c105d66-37d9-4161-6289-09273b7ae93a|false; __cf_bm=4w0A8fO_1jpPr7bc6_An4MVQZo82Br3fDjnhPfor1oY-1667732573-0-AUWXoOhssxEtagzMUmByZyOqjkl+gqCo7v7SsxHejQQM2YJBhdcMgmMCqzs+1egKMQ==; ezux_ifep_232529=true; ezux_et_232529=73; ezux_tos_232529=171',
        'origin': 'https://randommer.io',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; POCO F1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    url = "https://randommer.io/random-address"
    d = "number=1&culture=en&X-Requested-With=XMLHttpRequest"

    re = r.post(url, data=d, headers=h)
    ret = re.text

    street = ret.split(",")[0]
    street = street[2:]
    apt = ret.split(",")[1]
    apt = apt[1:]
    zip = ret.split(",")[2]
    zip = zip[1:]
    state = ret.split(",")[3]
    state = state[1:]
    city = ret.split(",")[4]
    city = city[1:]
    country = ret.split(",")[5]
    country = country[1:-2]

    inf = f"""
data generated :)
<b>
street = <code>{street}  </code> 
city = <code>{city}</code>
state = <code>{state}</code>
country = <code>{country}</code>
zip code = <code>{zip}</code>

<b>generated by</b> -» <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
</b>
  """

    return await message.reply(inf)


@dp.message_handler(commands=['image'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
    try:

        query = message.text[len('/image '):]
        params = {
            "q": query,
            "tbm": "isch",
            "ijn": "0",
            "api_key": "80f54721cc44c87baaaabcce5f2bd5082095f9e363263e9d53215771726c3674"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        images_result = results["images_results"]
        images_results = images_result[0:random.randint(0, 14)]
        for x in images_results:
            xm = x["thumbnail"]
        r = requests.Session()
        img_url = f"{xm}"
        response = r.get(img_url)
        if response.status_code:

            name = random.randint(1, 2000)
            fname = f"x-{name}.jpg"
            fp = open(fname, 'wb')
            fp.write(response.content)
            fp.close()
        photo = open(fname, "rb")
        await message.reply_photo(photo)
        os.remove(fname)

    except Exception as e:
        await message.reply(f'Error, Report @srfxdz, {e}')


@dp.message_handler(commands=['face'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):

    ck = random.randint(0, 500)
    img_url = f"https://thispersondoesnotexist.com/image"
    response = requests.get(img_url)
    if response.status_code:
        name = random.randint(1, 2000)
        fname = f"green-{name}.jpg"
        fp = open(fname, 'wb')
        fp.write(response.content)
        fp.close()
    photo = open(fname, "rb")

    URL = "https://random-data-api.com/api/users/random_user"

    response = requests.get(url=URL)

    data = response.json()

    N = 8
    ph = ''.join(random.choices(string.digits, k=N))
    phone = "98" + ph
    name1 = data["first_name"]
    name2 = data["last_name"]
    email = data["email"]
    dob = data["date_of_birth"]
    zip = data["address"]["zip_code"]
    add1 = data["address"]["street_address"]
    city = data["address"]["city"]
    state = data["address"]["state"]
    co = data["address"]["country"]

    caption = f"""
data generated :)
<b>
Name  = <code> {name1} {name2} </code>
Email = <code>{email}</code>
phone = <code>+1{phone}</code>
street = <code>{add1}  </code> 
city = <code>{city}</code>
state = <code>{state}</code>
country = <code>{co}</code>
zip code = <code>{zip}</code>
DOB = <code>{dob}</code>

<b>generated by</b> -» <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
</b>
  """

    await message.reply_photo(photo, caption=caption)
    os.remove(fname)


@dp.message_handler(commands=['web'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
    try:

        web = message.text[len('/web '):]
        img_url = f"https://screenshot.abstractapi.com/v1/?api_key=9b83ac747dee4f8fb881fbca5ca84d1c&url=https://{web}"
        response = requests.get(img_url)
        if response.status_code:
            name = random.randint(1, 2000)
            fname = f"green-{name}.jpg"
            fp = open(fname, 'wb')
            fp.write(response.content)
            fp.close()
        photo = open(fname, "rb")

        await message.reply_photo(photo)
        os.remove(fname)

    except Exception as e:
        await message.reply(f'Error, Report @srfxdz, {e}')


@dp.message_handler(commands=['random'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):

    ck = random.randint(0, 500)
    img_url = f"https://random.imagecdn.app/500/{ck}"
    response = requests.get(img_url)
    if response.status_code:
        name = random.randint(1, 2000)
        fname = f"green-{name}.jpg"
        fp = open(fname, 'wb')
        fp.write(response.content)
        fp.close()
    photo = open(fname, "rb")
    await message.reply_photo(photo)
    os.remove(fname)



@dp.message_handler(commands=['phone'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
    phone = message.text[len('/phone '):]
    if not phone or not phone.startswith('+') or len(phone) < 10:
        await message.reply("invalid Phone Number")
        return
    key = "fe65b94e78fc2e3234c1c6ed1b771abd"
    api = (
        "http://apilayer.net/api/validate?access_key="
        + key
        + "&number="
        + phone
        + "&country_code=&format=1"
    )
    output = requests.get(api)
    data = output.json()
    text = "Phone Number Information\n"
    for x in data:
        text += str(x.replace('_', ' ').title()) + " : " + str(data[x]) + "\n"
    return await message.reply(text)


def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None

@dp.message_handler(commands=['ip'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
    button1 = InlineKeyboardButton(
        text="GET-IP-SCORE", url="https://check.srfxdz.repl.co/")
    keyboard_inline = InlineKeyboardMarkup().add(button1)
    try:
        return await message.answer(f"""
<b>GET YOUR IP DETAILS HERE</b>
""", disable_web_page_preview=True, reply_markup=keyboard_inline)
    except:
        return await message.answer(f"""
        <b>🚫 DEAD KEY 🚫</b>
""")


@dp.message_handler(commands=['ig'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
    try:

        username = message.text[len('/ig '):]
        URL = f"https://www.instagram.com/{username}/"
        r = requests.get(URL)
        sn = BeautifulSoup(r.text, "html.parser")
        meta = sn.find("meta", property="og:description")
        s = meta.attrs['content']
        data = {}
        s = s.split("-")[0]
        s = s.split(" ")
        data1 = s[0]
        data2 = s[2]
        data3 = s[4]

        name = find_between(r.text, '{"title":"', '(')
        return await message.reply(f"""
NAME = <b> {name} </b>
FOLLOWERS =  <b> {data1} </b>
FOLLOWING =  <b> {data2} </b>
POST =  <b> {data3} </b>
    """)
    except Exception as e:
        await message.reply(f'Error, Report @srfxdz, {e}')



@dp.message_handler(commands=['fix'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
    try:
        all_cards = message.text.split('\n')
        for x in all_cards:
            cc = x.split(': ')[0]
            cc1 = x.split(': ')[1]
            ccq = "'"+cc+"'"
            ccw = ":'"+cc1+"',"
            with open("v.txt", "a") as f:
                f.write(f"{ccq}{ccw}\n")

        f = open("v.txt", "r")
        ccj = f.read()
        await message.reply(f"<code>'{ccj[7:]}</code> ", disable_web_page_preview=True)
        f.close()
        os.remove("v.txt")

    except Exception as e:
        await message.reply(f'Error, Report @srfxdz, {e}')


@dp.message_handler(commands=['search'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
    phone = message.text[len('/search '):]

    try:

        PAGE_LIMIT = 1
        RESULTS_PER_PAGE = 1

        PEXELS_API_KEY = "563492ad6f91700001000001d5db2780d6bd44599052f2a24d515c43"
        api = API(PEXELS_API_KEY)
        query = phone
        photos_dict = {}
        page = 1
        counter = 0

        api.search(query, page=page, results_per_page=RESULTS_PER_PAGE)
        photos = api.get_entries()
        for photo in tqdm.tqdm(photos):
            photos_dict[photo.id] = vars(photo)['_Photo__photo']

        # Step 2: Downloading
        PATH = './pics'
        RESOLUTION = 'original'

        if photos_dict:
            os.makedirs(PATH, exist_ok=True)

            for val in tqdm.tqdm(photos_dict.values()):
                url = val['src'][RESOLUTION]
                fname = os.path.basename(val['src']['original'])
                image_path = os.path.join(PATH, fname)
                if not os.path.isfile(image_path):
                    response = requests.get(url, stream=True)
                    with open(image_path, 'wb') as outfile:
                        outfile.write(response.content)

                    gg = random.choice(os.listdir("pics"))

                    photo = open(f"pics/{gg}", 'rb')
                    await message.reply_photo(photo)
                    os.remove(gg)
                else:
                    # ignore if already downloaded
                    mm = (f"File {gg} exists")

    except Exception as e:
        await message.reply(f'Error, Report @srfxdz, {e}')


anime_query = """
           query ($id: Int,$search: String) {
              Media (id: $id, type: ANIME,search: $search) {
                id
                title {
                  romaji
                  english
                  native
                }
                description (asHtml: false)
                startDate{
                    year
                  }
                  episodes
                  season
                  type
                  format
                  status
                  duration
                  siteUrl
                  studios{
                      nodes{
                           name
                      }
                  }
                  trailer{
                       id
                       site
                       thumbnail
                  }
                  averageScore
                  genres
                  bannerImage
              }
            }
        """
anime_url = "https://graphql.anilist.co"


@dp.message_handler(commands=['anime'], commands_prefix=PREFIX)
async def anime_info(message: types.Message):
    """
    Responds to the /anime <title> command
    :param message:
    :return:
    """
    anime = message.text
    find = ' '.join(anime.split(' ')[1:])

    variables = {"search": find}
    status_code = requests.post(anime_url, json={'query': anime_query,
                                                 'variables': variables}).status_code
    if status_code == 200:
        anime_data = requests.post(anime_url, json={'query': anime_query,
                                                    'variables': variables}).json()['data'].get('Media', None)
        anime_site = anime_data.get('siteUrl')
        image = anime_site.replace('anilist.co/anime/', 'img.anili.st/media/')
        anime_keyboard = InlineKeyboardMarkup()
        more_button = InlineKeyboardButton(text="🟡 More ", url=anime_site)
        anime_keyboard.insert(more_button)
        if anime_data['title']['english']:
            title = anime_data['title']['english']
        else:
            title = anime_data['title']['romaji']
        if anime_data['title']['native']:
            native_title = anime_data['title']['native']
        else:
            native_title = 'not found ;)'

        await message.answer(f"{title} <code>({native_title})</code>\n"
                             f"Type: <b>{anime_data['type']}</b>\n"
                             f"Score: <b>{anime_data['averageScore']}</b>\n"
                             f"Duration: <b>{anime_data['duration']}</b>\n"
                             f"Format: <b>{anime_data['format']}</b>\n"
                             f"Genres: <code>{' '.join(anime_data['genres'])}</code>\n"
                             f"Status <b>{anime_data['status']}</b>"
                             f"<a href='{image}'>&#xad</a>", disable_web_page_preview=True)
    else:

        await message.answer("<code>Not found 😭 </code>")


@dp.message_handler(commands=['cmd', 'cmds', 'command', 'commands'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):

    mm = """
/anime <b>(anime name) to search an anime </b>

/search <b>(query) to search an image </b>

/fix <b>(headers) edit headers for python </b>


/ig <b>(username) to search  on instagram </b>

/pass <b>to generate strong password</b>

/spotify <b>spotify acc generator </b>

/fake <b>fake data </b>

/gay <b>check percent of your gayness</b>

/bio <b>generate random bio</b>

/us <b>fake  US address </b>

/image <b>(query) to get image of query</b>

/random <b>to get a random pciture from internet</b>

/phone <b>(phone number with area code) 
to get detail of phone number</b>


/ip <b>(ip address) check risk score of ip </b>
  """
    return await message.reply(mm)

@dp.message_handler(commands=['logo'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
    quew = message.text[len('/logo '):]

    if not quew:
        await message.reply('Provide Some Text To Draw!')
        return
    else:
        pass
    pesan = await message.reply('Preparing logo')
    try:
        text = message.text[len('/logo '):]
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        pointsize = 500
        fillcolor = "black"
        shadowcolor = "blue"
        fnt = glob.glob("./resources/font/*")
        randf = random.choice(fnt)
        font = ImageFont.truetype(randf, 120)
        w, h = draw.textsize(text, font=font)
        h += int(h*0.21)
        image_width, image_height = img.size
        draw.text(((image_widthz-w)/2, (image_heightz-h)/2),
                  text, font=font, fill=(255, 255, 255))
        x = (image_widthz-w)/2
        y = ((image_heightz-h)/2+6)
        draw.text((x, y), text, font=font, fill="white",
                  stroke_width=5, stroke_fill="black")

        name = random.randint(1, 2000)
        fname = f"Pikachu-{name}.jpg"
        img.save(fname, "png")
        await pesan.edit_text('Done')
        photo = open(fname, "rb")
        await message.reply_photo(photo)
        await pesan.delete()
        if os.path.exists(fname):
            os.remove(fname)
    except Exception as e:
        await message.reply(f'Error, Report @srfxdz, {e}')


@dp.message_handler(commands=['gif'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):
    try:

        kk = await message.reply("<b> please wait making video from your image .... </b>")
        name = random.randint(1, 2000)
        photo_abspath = f'gpeg{name}.jpg'
        # Download photo
        file_id = message.reply_to_message.photo[-1].file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        await bot.download_file(file_path, photo_abspath)
        glitcher = ImageGlitcher()
        img = Image.open(photo_abspath)

        glitched = os.path.join("./resources", f"glitch-{name}.webp")
        glitch_img = glitcher.glitch_image(
            img, glitch_amount=int(2), color_offset=True)
        glitch_img.save(glitched)

        glitched = os.path.join("./resources", f"glitched{name}.gif")
        glitch_img = glitcher.glitch_image(
            img, glitch_amount=int(2), color_offset=True, gif=True
        )
        DURATION = 200
        LOOP = 0
        glitch_img[0].save(
            glitched,
            format="GIF",
            append_images=glitch_img[1:],
            save_all=True,
            duration=DURATION,
            loop=LOOP,
        )
        await kk.edit_text("<b> done</b>")
        fname = f"resources/glitched{name}.gif"
        photo = open(fname, "rb")
        await message.reply_video(photo)
        os.remove(f"resources/glitch-{name}.webp")
        os.remove(f"resources/glitched{name}.gif")
        os.remove(photo_abspath)

    except Exception as e:
        await message.reply(f'Error, Report @srfxdz, {e}')



@dp.message_handler(commands=['gay', 'gey'], commands_prefix=PREFIX)
async def cdgh(message: types.Message):

  rs = random.randint(0, 100)
  query = message.text[len('/gay '):]
  if len(query) != 0:
    if "@srfxdz" in str(query):
      return await message.reply(
        f" {query} <b> This person is alpha male  and  </b>"
      )

    return await message.reply(
      f"𝗛𝗲𝘆 {query}!𝗬𝗼𝘂 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗛𝗮𝗽𝗽𝘆 𝘁𝗼 𝗞𝗻𝗼𝘄 𝘁𝗵𝗮𝘁 𝗬𝗼𝘂 𝗮𝗿𝗲 {rs}% 𝗚𝗮𝘆 😝😝")

  try:

    namef = message.reply_to_message.from_user.first_name
    userf = message.reply_to_message.from_user.id

    if "5234223466" in str(userf):
      return await message.reply(
        f" {query} <b> This person is alpha male  </b>"
      )

    return await message.reply(
      f"𝗛𝗲𝘆 <a href='tg://user?id={userf}'>{namef}</a> !𝗬𝗼𝘂 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗛𝗮𝗽𝗽𝘆 𝘁𝗼 𝗞𝗻𝗼𝘄 𝘁𝗵𝗮𝘁 𝗬𝗼𝘂 𝗮𝗿𝗲 {rs}% 𝗚𝗮𝘆 😝😝"
    )
  except:
    return await message.reply("<b>I don't know who you're talking about, you're going to need to specify a user...! </b>")
 
#------------------------------------------------------demote-------------------------------------
  

      
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
