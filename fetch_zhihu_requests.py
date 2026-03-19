"""
Fetch Zhihu article using requests with proper headers
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
}

url = "https://zhuanlan.zhihu.com/p/2000867285422866885"
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}

print(f"[+] Fetching {url}")
response = requests.get(url, headers=headers, proxies=proxies, timeout=30)
print(f"[+] Status code: {response.status_code}")

output_file = "zhihu_article.html"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(response.text)
print(f"[+] Saved to {output_file}")

print("\n[+] First 500 characters of response:")
print(response.text[:500])
