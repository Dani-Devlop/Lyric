# if f["artist"]:
#     artist = f["artist"]
#     title = f["title"]


def append_lyric():
    # https://github.com/KristoforMaynard/music-tag
    import music_tag

    f = music_tag.load_file("Drake - New Bestie.mp3")

    with open("lyric.txt", "r") as txt:
        lyric = txt.read()

    # Get Name Artist and Song name
    noneHaveName = []
    if f["artist"]:
        artist = f["artist"]
        title = f["title"]
    # else:
    # 	noneHaveName.append(FileName)

    # Change The Lyric
    if f["lyrics"]:
        pass

    else:
        f["lyrics"] = lyric
        # Save into spefic path
        f.save()
