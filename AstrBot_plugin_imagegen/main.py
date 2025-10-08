from astrbot.api.event import Event
from astrbot.api.message_components import Text, Image
from utils.qwen_image_api import generate_image
import os

def on_message(event: Event):
    text = event.text.strip()

    # 检测触发指令
    if text.startswith("生成图片") or text.startswith("画图") or text.startswith("draw") or text.startswith("image"):
        prompt = text.replace("生成图片", "").replace("画图", "").replace("draw", "").replace("image", "").strip()
        if not prompt:
            event.reply(Text("请输入提示词，例如：生成图片 未来都市夜景"))
            return

        api_key = event.get_config("QWEN_API_KEY") or os.getenv("QWEN_API_KEY")
        api_url = event.get_config("QWEN_API_URL")
        size = event.get_config("DEFAULT_SIZE", "1920x1080")

        event.reply(Text(f"🎨 正在生成图片，请稍候...\n提示词：{prompt}"))
        image_url = generate_image(prompt, api_key, api_url, size)

        if image_url.startswith("http"):
            event.reply(Image(url=image_url))
        else:
            event.reply(Text(image_url))
