import syncedlyrics

# Correct: Pass the provider as a list
# y = syncedlyrics.search("puke eminem", synced_only=True, providers=["Genius"])


# y = syncedlyrics.search("x YTD", plain_only=True, providers=["Genius"])


############################################################
# y = syncedlyrics.search("x YTD", synced_only=True)
# if y:
#     print(y)
# else:
#     print("kos")
#     print(y)


############################################################
# Måneskin – Beggin' Lyrics
############################################################
############################################################

# try:
#     # First try: synced lyrics (with timestamps)
#     providers = ["LrcLib", "NetEase", "Musixmatch", "Megalobiz"]
#     lrc = syncedlyrics.search("x YTD", synced_only=True, providers=providers)
#     if lrc:
#         print(lrc)
# except:
# Second try: plain text lyrics
lrc = syncedlyrics.search("x YTD", plain_only=True, providers=["Genius"])
if lrc:
    print(f"Lyrics fetched successfully for {"x YTD"}")
    print(lrc)
############################################################
