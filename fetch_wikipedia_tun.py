"""
获取维基百科关于 TUN/TAP 的详细介绍
"""
import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

url = "https://en.wikipedia.org/wiki/TUN/TAP"
print(f"[+] 通过 Clash 代理获取 {url}...")
response = requests.get(url, proxies=proxies, headers=headers, timeout=30)
print(f"[+] 状态码: {response.status_code}")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content_div = soup.find(id="mw-content-text")
    if content_div:
        # 提取引言段落
        intro_paragraphs = []
        p_tags = content_div.find_all('p')
        for p in p_tags[:5]:
            if p.get_text(strip=True):
                intro_paragraphs.append(p.get_text(strip=True))

        # 提取目录
        toc = soup.find(id="toc")
        toc_items = []
        if toc:
            for li in toc.find_all('li')[:10]:
                toc_text = li.get_text(strip=True)
                toc_items.append(toc_text)

        # 保存结果
        output = "===== TUN/TAP - Wikipedia (通过 Clash 代理获取) =====\n\n"
        output += "### 简介\n\n"
        for p in intro_paragraphs:
            output += p + "\n\n"

        if toc_items:
            output += "### 目录\n\n"
            for item in toc_items:
                output += f"- {item}\n"
            output += "\n"

        output += f"\n完整页面: {url}\n"

        with open("tun_wikipedia_summary.txt", "w", encoding="utf-8") as f:
            f.write(output)

        print("\n" + output)
        print("\n[OK] 摘要已保存到 tun_wikipedia_summary.txt")
    else:
        print("[!] 未找到内容")
else:
    print(f"[!] 请求失败: {response.status_code}")
