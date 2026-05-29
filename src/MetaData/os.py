import os , re , time
# Music folder path
music_folder = "./music/"
music_files = os.listdir(music_folder)

print("📁 File list:", music_files)
print("-" * 40)
time.sleep(1)

for music in music_files:
    # Process only mp3 files (optional)
    delAsk = input('Do you want To Clear Your Song name? anwser Y/N \nLike: 10- Drake - iceman.mp3 -> Drake - iceman.mp3').lower()
    if delAsk == 'y':
   	 if not music.endswith(".mp3") or music[1].isalpha():
 	       continue
 	       #### TODO set condition 
 	  else:
 	 
 	    print(f"Before: {music}")
  
   # Remove everything before a capital letter
	    pattern = r'^.*?(?=[A-Z])'
 	   new_name = re.sub(pattern, '', music)
    
    # Use full paths
	    old_path = os.path.join(music_folder, music)
	    new_path = os.path.join(music_folder, new_name)
    
    # Rename the file
	    os.rename(old_path, new_path)
    
	    print(f"After: {new_name}")
	    print("-" * 30)
   else:
 	   pass
    