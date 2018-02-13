import re

source = '''
<div class="fdfdf">
    <div class="abc">
        <a id="222222">gygjjkji999j</a>
    </div>
</div>'''

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

result = get_tag_attribute('class', source)
print(result)


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

result2 = get_tag_content(source)
print(f'result2: {result2}')
result3 = get_tag_content('<img src="abc">')
print(f'result3: {result3}')