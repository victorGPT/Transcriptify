import os
import time
import openai
from tqdm import tqdm
import subprocess

# Define API key file path
API_KEY_PATH = os.path.expanduser("~/.openai")

# Load API key from file if it exists
if os.path.isfile(API_KEY_PATH):
    with open(API_KEY_PATH, "r") as f:
        api_key = f.read().strip()
        openai.api_key = api_key

# Ask for API key if it's not loaded
while not openai.api_key:
    api_key = input("请输入 OpenAI API key：").strip()
    openai.api_key = api_key
    # Save API key to file
    with open(API_KEY_PATH, "w") as f:
        f.write(api_key)

# Get ffmpeg path
if os.name == 'nt':  # Windows系统
    try:
        ffmpeg_path = subprocess.check_output(['where', 'ffmpeg']).decode().strip()
    except:
        print('请确认ffmpeg已安装并配置到环境变量PATH中')
        exit()
else:  # Linux和Mac系统
    try:
        ffmpeg_path = subprocess.check_output(['which', 'ffmpeg']).decode().strip()
    except:
        print('请确认ffmpeg已安装并配置到环境变量PATH中')
        exit()

def compress_audio(input_file):
    # Get input file size
    file_size = os.path.getsize(input_file)
    if file_size <= 25000000:
        return input_file

    # Compress audio file using ffmpeg
    output_file = f"{os.path.splitext(input_file)[0]}_compressed.mp3"
    command = f"{ffmpeg_path} -i {input_file} -ac 1 -ar 16000 -ab 32k {output_file}"
    os.system(command)

    return output_file

def transcribe_audio(input_file, output_file, response_format, progress_bar):
    with open(input_file, "rb") as f:
        transcript = openai.Audio.transcribe("whisper-1", f, response_format=response_format)

    progress_bar.update(100)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcript)

    # Remove compressed file
    compressed_file = f"{os.path.splitext(input_file)[0]}_compressed.mp3"
    if os.path.exists(compressed_file):
        os.remove(compressed_file)

input_file = input("请输入音频文件名（包括扩展名）：").strip("'\"")
output_format = input("请输入输出格式（txt、vtt、srt、tsv、json、all）：").strip("'\"")

if output_format not in ["txt", "vtt", "srt", "tsv", "json", "all"]:
    print("无效的输出格式。")
    exit()

file_name, _ = os.path.splitext(input_file)
output_file = f"{file_name}_transcript.{output_format}"

# Compress audio file if larger than 25MB
input_file = compress_audio(input_file)

progress_bar = tqdm(total=100, desc="音频转录中", ncols=80)

start_time = time.time()

transcribe_audio(input_file, output_file, output_format, progress_bar)

progress_bar.close()

elapsed_time = time.time() - start_time
print(f"音频转录完成，用时 {elapsed_time:.2f} 秒")

print(f"音频转录已保存到 {output_file}")
