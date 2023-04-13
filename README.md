## Whisper-OpenAI：一款语音转文字的Python脚本

Whisper-OpenAI是一款利用ChatGPT和OpenAI的Whisper技术制作的语音转文字的Python脚本。该脚本有如下特点：

### 特点：
1. 自动将大于25MB的音频文件压缩（因为OpenAI只支持25MB以下的文件），使得用户可以使用更大的音频文件进行语音转文字。
2. 输出的字幕格式支持txt、vtt、srt、tsv、json，满足用户不同的需求。
3. 生成时间短（一小时音频文件尽用时三分钟），让用户可以快速得到想要的结果。

### 使用须知：
使用该脚本前，需要确保电脑已安装以下环境和库：
- Python
    - OpenAI
    - tqdm
- 处理音频的ffmpeg
- openai的[api-key](https://platform.openai.com/account/api-keys)

如果你不知道如何安装上述环境和库，如果你不知道怎么操作，请放心咨询ChatGPT，因为脚本作者我就是这么做的。

总之，Whisper-OpenAI是一款方便快捷的语音转文字的Python脚本，支持大文件压缩和多种字幕格式输出。使用该脚本前，用户需要安装相应的环境和库，或者咨询ChatGPT获取帮助和支持。

## 版本更新
1.0.1v 2023/04/13
修改了对文件处理的逻辑，现在文件处理逻辑遵守以下流程

```mermaid
graph LR
    A[输入文件] --> B{文件体积是否大于25mb?}
    B -->|否| C(音频转文字)
    B -->|是| D[压缩原文件]
    D --> C
    C --> E{是否有压缩文件?}
    E -->|是| F[删去压缩文件]-->G
    E -->|否| G[完成]