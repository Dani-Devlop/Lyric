#from mutagen import  *
#from mutagen.mp3 import MP3

#audio = MP3("04. J. Cole - Old Dog.mp3")
#print(audio.info.length)
#print(audio.info.bitrate)


#from mutagen import File

#audio = File("J. Cole - Old Dog.mp3")


#if audio is not None:
#    from mutagen.easyid3 import EasyID3
#    audio = EasyID3(audio.filename)

#audio["title"] = "Old Dog"
#audio.save()

import music_tag
import os

lyric = """Alone at parties in a deadly silhouette
She loves the cocaine, but cocaine don't love her back
When she's upset, she talks to Maury and takes deep breaths
She's a 90's supermodel, uh-uh-uh
Way back in high school, when she was a good Christian
I used to know her, but she's got a new best friend
A drag queen named The Virgin Mary takes confessions
She's a 90's supermodel

Yeah, she's a monster, my compliments
If you wanna love her, just deal with that
She'll never love you more than money and cigarettes
Every night's a heartbreak

Hey, don't think about it, hey, just let it go
'Cause her boyfriend is the rock 'n' roll (hey)
Savor every moment 'til she has to go
'Cause her boyfriend is the rock 'n' roll

Alone at parties, she's working around the clock
When you're not looking, she's stealing your Basquiat
Low-waisted pants on OnlyFans, I'll pay for that
She's a 90's supermodel

Yeah, she's a monster, my compliments
If you wanna love her, just deal with that
She'll never love you, you just look a bit like her dad
Every night's a heartbreak

Hey, don't think about it, hey, just let it go
'Cause her boyfriend is the rock 'n' roll (hey)
Savor every moment 'til she has to go
'Cause her boyfriend is the rock 'n' roll, uh

Yeah, uh-huh
She's a 90's supermodel, uh-uh-uh
She's a 90's supermodel, uh-uh-uh
Okay"""

f = music_tag.load_file('04. J. Cole - Old Dog.mp3')

#f['lyrics'] = 
#
#art = f['lyrics']
#f.save()
#print(art)

from mutagen.id3 import ID3, USLT, ID3NoHeaderError

# بارگذاری فایل
file_path = "04. J. Cole - Old Dog.mp3"

# ایجاد یا بارگذاری تگ ID3
try:
    tags = ID3(file_path)
except ID3NoHeaderError:
    tags = ID3()

# حذف لیریک قبلی (اختیاری)
tags.delall('USLT')

# اضافه کردن لیریک جدید
tags.add(USLT(
    encoding=3,           # 3 = UTF-8
    lang='eng',           # کد زبان
    desc='',              # توضیحات (می‌تواند خالی باشد)
    text= lyric
))

audio = '04. J. Cole - Old Dog.mp3'

audio["title"] = "Old Dog"
audio.save()

tags.save(file_path)

print("✅ لیریک با موفقیت اضافه شد!")