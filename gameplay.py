from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_gameplay_and_text(part_path, gameplay_path, part_num):
    part_clip = VideoFileClip(part_path)
    gameplay_clip = VideoFileClip(gameplay_path).subclip(0, part_clip.duration)
    
    final_width = 1440
    final_height = 2560

    part_clip = part_clip.resize(width=final_width+100)
    gameplay_clip = gameplay_clip.resize(height=final_height-part_clip.h)
    
    part_clip = part_clip.set_position(('center', 'top'))
    gameplay_clip = gameplay_clip.set_position(('center', 'bottom'))
    
    txt_clip = TextClip(f'Part {part_num}', fontsize=48, color='black', font='Arial-Bold', bg_color='white')

    txt_clip = txt_clip.set_position(('center', 'center')).set_duration(part_clip.duration)
    
    txt_y_pos = part_clip.h + 200 
    txt_clip = txt_clip.set_position(('center', txt_y_pos))

    final_clip = CompositeVideoClip([part_clip, gameplay_clip, txt_clip], size=(final_width, final_height))
    
    final_clip = final_clip.set_audio(part_clip.audio)
    
    final_clip.write_videofile(
        f'./shorts/final_part_{part_num}.mp4',
        codec='libx264',  
        audio_codec='aac', 
        fps=24
    )
