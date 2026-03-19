"""
使用 requests 通过 Clash 代理搜索 "tun"
代理: 127.0.0.1:7890
"""
import requests

# 配置代理
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}

# 请求头模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5,zh-CN;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

print("[+] 正在通过 Clash 代理 (127.0.0.1:7890) 搜索 'tun'...")

# 直接搜索
url = 'https://www.google.com/search?q=tun&hl=en'
response = requests.get(url, proxies=proxies, headers=headers, timeout=30)

print(f"[+] 状态码: {response.status_code}")

# 保存结果
with open('google_search_tun_response.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

print("[OK] 响应已保存到 google_search_tun_response.html")

if response.status_code == 200:
    print("\n[+] 搜索成功，正在分析结果...")
    # 粗略提取标题来看看内容
    import re
    titles = re.findall(r'<h3[^>]*>(.*?)</h3>', response.text)
    cleaned_titles = []
    for title in titles:
        # 去除 HTML 标签
        clean = re.sub(r'<[^>]+>', '', title)
        if len(clean.strip()) > 5:
            cleaned_titles.append(clean.strip())

    with open('google_search_tun_extracted.txt', 'w', encoding='utf-8') as f:
        f.write("Google 搜索 'tun' 提取的结果\n")
        f.write("=" * 50 + "\n\n")
        for i, title in enumerate(cleaned_titles[:15], 1):
            f.write(f"{i}. {title}\n")
            print(f"{i}. {title}")

    print(f"\n[OK] 已提取 {len(cleaned_titles)} 个标题到 google_search_tun_extracted.txt")
else:
    print(f"[!] 请求返回状态码 {response.status_code}，可能需要人机验证")
