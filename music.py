import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

import yt_dlp
import vlc
import time
import random
import keyboard

def play_from_search(query):
    search_query = f"ytsearch1:{query}"
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        'cookiefile': 'cookies.txt',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"🔍 Searching for: {query}...")
            info = ydl.extract_info(search_query, download=False)['entries'][0]
            audio_url = info['url']
            title = info.get('title', 'Unknown Track')
            duration = info.get('duration', 0)

            print(f"🎵 Playing: {title}")
            print(f"⏱️ Duration: {duration // 60}:{duration % 60:02d}")

            # VLC Streaming
            instance = vlc.Instance()
            player = instance.media_player_new()
            media = instance.media_new(audio_url)
            player.set_media(media)
            player.play()

            time.sleep(2) 
            while player.is_playing() or player.get_state() not in [vlc.State.Ended, vlc.State.Error]:
                time.sleep(0.1)
            if keyboard.is_pressed('space'):
                player.pause()
                time.sleep(0.3)
            if keyboard.is_pressed('l'):
                player.set_time(player.get_time() + 10000)
                time.sleep(0.3)
            if keyboard.is_pressed('j'):
                player.set_time(player.get_time() - 10000)
                time.sleep(0.3)
                
        except Exception as e:
            print(f"Could not play song: {e}")

playlist = {
    #Here the playlist dictionary will come
    #Format playlist_name: list of song names
}

if __name__ == "__main__":
        play = input('Enter your playlist name or exit to exit: ')
        shuffle = input('Do you want it to shuffle: ') #Ans should be yes or no
        
        try:
            for key, value in playlist.items():
                if play.lower() == key:
                    if shuffle.lower() == 'yes':
                        random.shuffle(value)
                    for i in value:
                        play_from_search(i)
                        time.sleep(4)
        except KeyboardInterrupt:
            print("Interrupted by user!")
        except Exception as e:
            print(f'ERROR {e}')   
