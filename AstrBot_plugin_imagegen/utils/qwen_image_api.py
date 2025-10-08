import requests

def generate_image(prompt, api_key, api_url, size="1920x1080"):
    """
    调用 Qwen API 生成图像
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "qwen-vl-plus",
        "input": {
            "prompt": prompt,
            "size": size
        }
    }

    try:
        resp = requests.post(api_url, headers=headers, json=payload, timeout=60)
        data = resp.json()
        if resp.status_code == 200 and "output" in data:
            image_url = data["output"]["image_url"]
            return image_url
        else:
            return f"[错误] {data.get('message', '无法生成图片')}"
    except Exception as e:
        return f"[异常] {str(e)}"
