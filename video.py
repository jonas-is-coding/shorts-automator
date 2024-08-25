import yt_dlp
from moviepy.editor import VideoFileClip

def download_video(url, path):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{path}/video.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', 'No Title')
    return f'{path}/{video_title}.mp4'

def split_video(video_path, part_length=70):
    clip = VideoFileClip(video_path)
    duration = int(clip.duration)
    start = 0
    part_num = 1
    
    while start < duration:
        end = min(start + part_length, duration)
        part = clip.subclip(start, end)
        part_filename = f'./splitted/part_{part_num}.mp4'
        part.write_videofile(part_filename)
        start = end
        part_num += 1