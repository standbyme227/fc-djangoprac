import re

source = open('crawler/melon.html', 'rt', encoding='utf-8').read()

# re.DOTALL을 포함시키지 않으면 공백문자에서 끊긴다
PATTERN_TD = re.compile(r'<td.*?>.*?</td>', re.DOTALL)
td_list = re.findall(PATTERN_TD, source)
# iterator는 index 접근이 불가능
# 그래서 finditer가 아닌 findall을 사



for index, td in enumerate(td_list):
    # td_strip = re.sub(r'[\n\t]+|\s\s+', '', td)
    td_strip = re.sub(r'[\n\t]+|\s{2,}', '', td) # {}는 몇 회, {2}이건 2회 반복 {2,}이 2회 이상 ','로 끝을 지정 안하면됨.
    print(f'{index:04}: {td_strip}')

    # 이 위쪽은 print했을때 쉽게 보기위함.

td_cover_img = td_list[3]
PATTERN_IMG = re.compile(r'<img.*?src="(.*?)".*?>', re.DOTALL)
url_img_cover = re.search(PATTERN_IMG, td_cover_img).group(1)
print(url_img_cover)

td_title_author = td_list[5]
PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')
div_rank01 = re.search(PATTERN_DIV_RANK01, td_title_author).group()
title = re.search(PATTERN_A_CONTENT, div_rank01).group(1)
print(title)