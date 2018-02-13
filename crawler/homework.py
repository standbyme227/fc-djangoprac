import re

from utils import *

source = open('melon.html', 'rt', encoding='utf8').read()

PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# 자주써야할 코드를 패턴으로 변환, div 중 class가 ellipsis rank01인 것 안을 찾아라
PATTERN_DIV_RANK02 = re.compile(r'<div class="ellipsis rank02">.*?</div>', re.DOTALL)
# 자주써야할 코드를 패턴으로 변환, div 중 class가 ellipsis rank02인 것 안을 찾아라

PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')
# 자주써야할 코드를 패턴으로 변환, a 태그 안쪽을 찾아라
PATTERN_TR = re.compile(r'<tr*.?class="lst50".*?>.*?</tr>',re.DOTALL)
# 자주써야할 코드를 패턴으로 변환,tr 태그중 class가 lst50인것을 찾아라
PATTERN_TD = re.compile(r'<td.*?>.*?</td>', re.DOTALL)
# td태그 안쪽을 찾아라
PATTERN_IMG = re.compile(r'<img.*?src="(.*?)".*?>',re.DOTALL)
# img태그 안쪽의 url을 찾아라
PATTERN_RANK = re.compile(r'<span.*?class=".*?rank.*?".*?>(.*?)</span>', re.DOTALL)
# span중 class를 rank로 같는 태그 안쪽을 찾아라.

result = []

for tr in re.finditer(PATTERN_TR, source):
    # source안의 PATTERN_TR을 찾아서 finditer로 iterator 객체반환, 순회를 위해서???
    td_list = re.findall(PATTERN_TD, tr.group())
    #

    td_rank = td_list[1]
    td_img_cover = td_list[3]
    td_title_artist = td_list[5]
    div_title = re.search(PATTERN_DIV_RANK01, td_title_artist).group()
    div_artist = re.search(PATTERN_DIV_RANK02, td_title_artist).group()
    td_album = td_list[6]
    # 값들이 들어있는 태그들(인데 좀 범위가 넓다)

    rank_span_tag = find_tag('span', td_rank)
    img_cover_a_tag = find_tag('img', td_img_cover)
    title_a_tag = find_tag('a', div_title)
    artist_a_tag = find_tag('a', div_artist)
    # 값들이 직접적으로 들어있는 태그들로 축약


    rank = get_tag_content(rank_span_tag)
    # rank = re.search(PATTERN_RANK, td_rank).group(1)
    url_img_cover = get_tag_attribute('src', img_cover_a_tag)
    # url_img_cover = re.search(PATTERN_IMG, td_img_cover).group(1)
    title = get_tag_content(title_a_tag)
    artist = get_tag_content(artist_a_tag)
    album = get_tag_content(td_album)
    # 각 태그들에서 값을 찾음

    result.append({
        'rank': rank,
        'title' : title,
        'url_img_cover': url_img_cover,
        'artist': artist,
        'album' : album
    })

for item in result:
    print(item)


melon_list_text = str(result)
open('melon_list.html', 'wt', encoding='utf8').write(melon_list_text)









