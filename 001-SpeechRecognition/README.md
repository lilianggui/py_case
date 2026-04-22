### SpeechRecognition 简介
在 Python 生态中，SpeechRecognition 是目前最主流、易用且功能全面的语音识别库，适合从入门到工业级应用的多种场景。

### ‌优势特点‌：
- ‌多引擎支持‌：封装了 Google Web Speech API、CMU Sphinx、Microsoft Bing、Wit.ai 等主流引擎。
- ‌跨平台兼容‌：支持 Windows、macOS、Linux。
- ‌低门槛集成‌：仅需几行代码即可实现基础语音转文本。
‌支持多种音频源‌：可从麦克风实时采集，也可处理 WAV、AIFF、FLAC 等音频文件。

### ‌安装命令‌：
```
pip install SpeechRecognition pyaudio
```

若需离线识别（如中文），还需额外安装：
```
pip install pocketsphinx
```

### ‌主流识别引擎对比
| 引擎                        | 离线支持   | 准确率      | 适用场景       | 注意事项              |
|---------------------------|--------|----------|------------|-------------------|
| Google Web Speech         | ❌ 需联网  | ⭐⭐⭐⭐⭐（高） | 快速原型、通用应用  | 	免费但有调用限制（约50次/天） |
| CMU Sphinx (PocketSphinx) | ✅ 完全离线 | ⭐⭐⭐（中）   | 隐私敏感、嵌入式设备 | 支持中文，需下载语言包       |
| Microsoft Bing            | ❌ 需联网  | ⭐⭐⭐⭐⭐    | 企业级应用      | 需 API 密钥，免费层有限    |
| Wit.ai                    | ❌ 需联网  | ⭐⭐⭐⭐     | 对话系统开发     | 支持自定义意图识别         |

### 注意事项
1. 如果你的电脑是苹果MacOS，需要先安装portaudio
    ```
    brew uninstall portaudio
    ```
2. 并且如果你的电脑是Apple Silicon (M1/M2/M3)，务必保证你的python版本和你的Homebrew都是ARM版本的
    ```
    # 查看python 版本
    python3 -c "import platform; print(platform.machine())"
   ```
3. 并且如果你刚好使用的是conda，那么恭喜你，你默认的python版本是x86_64，这时候我保证无论你怎么安装pyaudio，在使用的时候都不会成功的，这时候你需要使用原机上的python，最好是创建虚拟环境来安装SpeechRecognition和pyaudio