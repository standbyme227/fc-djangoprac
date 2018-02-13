# import requests
#
# html = requests.get('https://www.melon.com/chart/index.htm')
#
# # f = open('melon.html', 'wt')
# # f.write(html)
# # f.close
#
# f = open('melon.html', 'wt', encoding='utf8').write(html.text)

import re

# Patterns
# <div class="ellipsis rank01> ~ </div> 부분의 텍스트
PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# <a href"..."> (내용) </a>
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

# 로컬 HTML문서 불러오기
source = open('crawler/melon.html', 'rt', encoding='utf8').read()


# # 전체 문서에 PATTERN_DIV_RANK01에 해당하는 match object 목록을 순회
# match_list = re.finditer(PATTERN_DIV_RANK01, source)
# for match_div_rank01 in match_list:
#     # 각 순회에서 매치 전체 문자(<div class... ~ </div>)부분을 가져
#     div_rank01_content = match_div_rank01.group()
#
#     # 부분 문자열에 a태그의 내용을 title변수에 할당
#     match_title = re.search(PATTERN_A_CONTENT, div_rank01_content)
#     title = match_title.group(1)
#     # print(title)


PATTERN_TR_LST50 = re.compile(r'<tr class="lst50".*?>(.*?)</tr>',re.DOTALL)
PATTERN_IMG = re.compile(r'<img.*?src="(.*?)".*?>',re.DOTALL)








match_list = re.finditer(PATTERN_TR_LST50, source)

for match_object in match_list:
    tr_content = match_object.group(1)

    div_rank01_content = re.search(PATTERN_DIV_RANK01, tr_content)
    div = div_rank01_content.group()
    match_title = re.search(PATTERN_A_CONTENT, div)
    title = match_title.group(1)

    match_img_url = re.search(PATTERN_IMG, tr_content)
    img_url = match_img_url.group(1)


    print(f'제목 : {title}   url : {img_url}')