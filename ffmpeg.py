from pathlib import Path
import os
import subprocess
video_input_path = 'statics/medias/videos/video1.mp4'
BASE_DIR = Path(video_input_path).parent
print(BASE_DIR)
image_name = 'baba.jpg'
img_output_path = os.path.join(BASE_DIR, image_name)
subprocess.call(['ffmpeg', '-i', video_input_path, '-ss',
                '0:00:59.000', '-vframes', '1', img_output_path])
