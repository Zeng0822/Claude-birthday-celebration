"""把 Artifact 源文件 clawd-feast.html 包装成可直接部署到 GitHub Pages 的 index.html。

用法：python3 build.py
"""
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
SITE = "https://zeng0822.github.io/Claude-birthday-celebration/"
TITLE = "Clawd 满月宴"
DESC = "Clawd 满月啦！来月亮上喝杯赛博满月酒：放烟花、干杯、摸摸头，走时领个红鸡蛋。"

# 网站图标：像素 Clawd（和页面里的造型一致）
ICON_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 2 18 14" shape-rendering="crispEdges">'
    '<g fill="#d97757">'
    '<rect x="3" y="4" width="12" height="2"/><rect x="3" y="6" width="2" height="2"/>'
    '<rect x="6" y="6" width="6" height="2"/><rect x="13" y="6" width="2" height="2"/>'
    '<rect x="1" y="8" width="16" height="2"/><rect x="3" y="10" width="12" height="2"/>'
    '<rect x="4" y="12" width="1" height="2"/><rect x="6" y="12" width="1" height="2"/>'
    '<rect x="11" y="12" width="1" height="2"/><rect x="13" y="12" width="1" height="2"/>'
    '</g></svg>'
)
ICON = "data:image/svg+xml," + quote(ICON_SVG)

HEAD = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{DESC}">
<meta name="theme-color" content="#0d1022">
<meta property="og:type" content="website">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{SITE}">
<meta property="og:image" content="{SITE}thumb.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="{SITE}thumb.png">
<link rel="icon" href="{ICON}">
</head>
<body>
"""

src = (ROOT / "clawd-feast.html").read_text(encoding="utf-8")
body = "\n".join(line for line in src.splitlines() if 'rel="artifact-thumbnail"' not in line)
(ROOT / "index.html").write_text(HEAD + body + "\n</body>\n</html>\n", encoding="utf-8")
print("index.html 已生成")
