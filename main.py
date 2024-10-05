from video import download_video, split_video
from gameplay import add_gameplay_and_text
import os
import glob

def main(youtube_url, gameplay_path):
    download_video(youtube_url, './videos')
    split_video("./videos/video.mp4")
    
    num_parts = 3 
    
    for i in range(1, num_parts + 1):
        part_filename = f'./splitted/part_{i}.mp4'
        add_gameplay_and_text(part_filename, gameplay_path, i)
    
    delete_splitted_videos('./splitted')

def delete_splitted_videos(folder_path):
    files = glob.glob(os.path.join(folder_path, '*.mp4'))
    for file in files:
        try:
            os.remove(file)
            print(f"{file} wurde erfolgreich gelöscht.")
        except OSError as e:
            print(f"Fehler beim Löschen von {file}: {e}")

main('https://www.youtube.com/watch?v=8NYvQEQqbzQ', './assets/gta_gameplay.mp4')
