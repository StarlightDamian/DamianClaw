"""
解析 Google 搜索结果 HTML
"""
from bs4 import BeautifulSoup

with open('google_search_tun_response.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 查找搜索结果
results = []

# 查找所有 h3 标题
for h3 in soup.find_all('h3'):
    title = h3.get_text(strip=True)
    if not title or len(title) < 3:
        continue

    # 查找父级 a 标签
    a = h3.find_parent('a')
    url = a.get('href') if a else None

    # 查找摘要
    summary = ""
    parent_div = h3.find_parent('div')
    if parent_div:
        # 查找包含摘要的 div
        possible_summary = parent_div.find_next_sibling('div')
        if possible_summary:
            summary = possible_summary.get_text(strip=True)

    results.append({
        'title': title,
        'url': url,
        'summary': summary
    })

print(f"===== Google 搜索 'tun' 结果 =====\n")
print(f"找到 {len(results)} 个结果:\n")

for i, result in enumerate(results[:10], 1):
    print(f"{i}. **{result['title']}**")
    if result['summary']:
        # 截断过长的摘要
        summary_short = result['summary'][:150] + ('...' if len(result['summary']) > 150 else '')
        print(f"   {summary_short}")
    print()

# 保存完整结果
with open('tun_search_results_parsed.txt', 'w', encoding='utf-8') as f:
    f.write(f"Google 搜索 'tun' 解析结果\n")
    f.write(f"代理: 127.0.0.1:7890 (Clash)\n")
    f.write("=" * 60 + "\n\n")
    for i, result in enumerate(results, 1):
        f.write(f"{i}. {result['title']}\n")
        if result['summary']:
            f.write(f"   {result['summary']}\n")
        if result['url']:
            f.write(f"   URL: {result['url']}\n")
        f.write("\n")

print(f"\n完整结果已保存到 tun_search_results_parsed.txt")
