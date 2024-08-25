from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_gameplay_and_text(part_path, gameplay_path, part_num):
    # Laden der Videoclips
    part_clip = VideoFileClip(part_path)
    gameplay_clip = VideoFileClip(gameplay_path).subclip(0, part_clip.duration)
    
    # Finale Größe des Videos
    final_width = 1440
    final_height = 2560

    # Finale Größe der Clips
    part_clip = part_clip.resize(width=final_width+100)
    gameplay_clip = gameplay_clip.resize(height=final_height-part_clip.h)
    
    # Positionierung der Clips
    part_clip = part_clip.set_position(('center', 'top'))
    gameplay_clip = gameplay_clip.set_position(('center', 'bottom'))
    
    # Erstellen des Textclips mit schwarzem Text und weißem Hintergrund
    txt_clip = TextClip(f'Part {part_num}', fontsize=48, color='black', font='Arial-Bold', bg_color='white')
    
    # Die Größe des Textclips wird basierend auf der Textgröße angepasst
    txt_clip = txt_clip.set_position(('center', 'center')).set_duration(part_clip.duration)
    
    # Bestimmen der Position für den Text: Auf der Grenze zwischen den beiden Clips
    txt_y_pos = part_clip.h + 200  # Position auf der Höhe des YouTube-Videos
    txt_clip = txt_clip.set_position(('center', txt_y_pos))

    # Erstellen des finalen Clips
    final_clip = CompositeVideoClip([part_clip, gameplay_clip, txt_clip], size=(final_width, final_height))
    
    # Setzen des Audios vom part_clip und sicherstellen, dass das Audio im finalen Video ist
    final_clip = final_clip.set_audio(part_clip.audio)
    
    # Sicherstellen, dass der Audio-Codec und Video-Codec korrekt eingestellt sind
    final_clip.write_videofile(
        f'./shorts/final_part_{part_num}.mp4',
        codec='libx264',  # H.265 Video-Codec für bessere Qualität
        audio_codec='aac',  # AAC Audio-Codec
        fps=24
    )