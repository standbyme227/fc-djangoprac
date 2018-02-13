import re
import requests

__all__ = (
    'get_tag_attribute',
    'get_tag_content',
    'find_tag',
)
# 이렇게 하면 이 utils.py를 다른 곳에서 import할때 // 위에 두개만 import되고 re는 import되지 않는다
# 같은 이름의 모듈을 겹치게 하지 않을 수 있다.

def save_melon():
    # save_melon함수라는 것을 명시함
    response = requests.get('https://www.melon.com/chart/index.htm')
    # requests를 이용 get함수로 url의 HTML 정보를 response함수에 할당
    source = response.text
    # source라는 변수엔 response의 text 할당
    with open('melon.html', 'wt') as f:
        # melon.html을 글쓰기상태로 열고 f라는 변수에 할당
        # f에 source을 씀.
        f.write(source)
        # 고로 melon.html엔 response받아온 url의 html정보가 text로 저장되어있다.
        # 선생님 주석....!! 멜론 사이트의 인기차트 1~50위에 해당하는 페이지를 melon.html로 저장.




# source = '''
# <div class="fdfdf">
#     <div class="abc">
#         <a id="222222">gygjjkji999j</a>
#     </div>
# </div>'''

def get_tag_attribute(attribute_name, tag_string):

    p_first_tag = re.compile(r'^.*?<.*?>', re.DOTALL)
    first_tag = re.search(p_first_tag, tag_string).group()

    p = re.compile(r'^.*?<.*?{attribute_name}="(?P<value>.*?)".*?>'.format(
        attribute_name=attribute_name
    ), re.DOTALL)
    # 찾을 패턴
    # 그룹에 이름짓기 (?P<name>...)
    # 한 번에 해보려 했으나 alphabet안에 '<'같은 것들도 포함되는걸로봐서 나누기가 힘들지 않을까싶다.

    m = re.search(p, first_tag)
    if m:
        return m.group('value')
    return ''

# result = get_tag_attribute('class', source)
# print(result)


def get_tag_content(tag_string):
    # 태그 안의 내용 다 나오게 하기!!!
    # source 예제가 source = '<div class="fdfdf"><span class="abc"><a id="222222">ASDFdddddd</a></span></div>' 라면
    # div 안쪽이 다 나와야 한다.
    # p_self = re.compile(r'<.*?>(?!.*<.*?>)', re.DOTALL)
    # m_self = re.search(p_self, tag_string)
    # if m_self:
    #     print(f'm_self: {m_self.group()}')


    p = re.compile(r'<.*?>(?P<value>.*)</.*?>', re.DOTALL) #re.DOTALL은 줄바꿈과도 매칭되게 하는 말이다.
    # content = re.search(r'<.....re.DOTALL을 지울거같다.>')
    m = re.search(p, tag_string)
    if m:
        return get_tag_content(m.group('value'))
    # 함수를 재귀적으로 돌리기 위한 코드
    elif re.search(r'[<>]', tag_string):
        return ''
        # 위에는 빈문자를 리턴
        # return m.group('value') 이건 전에 함수
    return tag_string

# result2 = get_tag_content(source)
# print(f'result2: {result2}')
# result3 = get_tag_content('<img src="abc">')
# print(f'result3: {result3}')


def find_tag(tag, tag_string):


    '''
    tag_string에서 tag요소를 찾아 리턴
    :param tag: 찾을 tag명
    :param tag_string: 검색할 tag문자열
    :return: 첫 번째로 찾은 tag문자열
    '''

    p = re.compile(r'.*?(<{tag}.*?>.*?</{tag}>|<{tag}.*?>)'.format(tag=tag), re.DOTALL)
    m = re.search(p, tag_string)
    if m:
        return m.group(1)
    return None
