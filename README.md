English |[中文](https://github.com/victorGPT/Transcriptify/blob/main/README_ZH.md)
## Transcriptify: A Python Script for Speech-to-Text

Transcriptify is a Python script for converting speech to text, created using ChatGPT and OpenAI's Whisper technology. The script has the following features:

### Features:
1. Automatically compresses audio files larger than 25MB (because OpenAI only supports files under 25MB), allowing users to use larger audio files for speech-to-text.
2. Supports output of subtitle formats such as txt, vtt, srt, tsv, and json to meet different user needs.
3. Generates results quickly (using only three minutes to transcribe an hour-long audio file), allowing users to quickly obtain the desired results.

### Instructions for use:
Before using the script, make sure that the following environments and libraries are installed on your computer:
- Python
    - OpenAI
    - tqdm
- ffmpeg for processing audio
- OpenAI's [API key](https://platform.openai.com/account/api-keys)

If you don't know how to install the above environments and libraries, don't worry, you can consult ChatGPT for help and support, as the script author did.

In summary, Transcriptify is a convenient and efficient Python script for speech-to-text, supporting compression of large files and output in multiple subtitle formats. Users need to install the corresponding environment and libraries before using the script, or consult ChatGPT for help and support.

## Version Update
### 1.0.1v 

2023/04/13

Changed the file processing logic, now following the process flow:

```mermaid
graph LR
    A[Input File] --> B{Is the file size larger than 25mb?}
    B -->|No| C(Convert speech to text)
    B -->|Yes| D[Compress the original file]
    D --> C
    C --> E{Is there a compressed file?}
    E -->|Yes| F[Delete the compressed file]-->G
    E -->|No| G[Finished]
