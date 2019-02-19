from xpinyin import Pinyin
import pytest
p=Pinyin()
data_get_py=[
    ('','','','',''),
    (u'深圳',u'-','marks','lower','shēn-zhèn'),
    (u'惠州',u'','numbers','upper','HUI4ZHOU1'),
    (u'说服',u'','numbers','upper','SHUI4FU2'),
    ('!@#+','','marks','upper','!@#+'),
    ('1','','numbers','lower','1'),
    ('āáǎ','','numbers','upper','āáǎ'),
    (u'壹贰叁',u'-','numbers','upper','YI1-ER4-SAN1'),
    (u'台灣',u'-','numbers','lower','tai2-wan1'),
    (u'重庆', u'-', 'numbers', 'lower', 'chong2-qin4')]
data_get_init=[
    (u'深','S'),
    ('!','!'),
    ('1','1'),
    ('āáǎ','āáǎ'),
    (u'壹','Y')]
data_get_inits=[
    (u'深圳','S-Z'),
    ({u'深圳',u''}, 'SZ'),
    ({u'深圳',u' '}, 'S Z'),
    ({u'深圳', u','}, 'S,Z'),
    ('!@#+','!-@-#-+'),
    ('āáǎ','ā-á-ǎ')]
@pytest.mark.parametrize('chars,splitter,tone_marks,convert,excpet',data_get_py)
def test_pinyin(chars,splitter,tone_marks,convert,excpet):
    assert p.get_pinyin(chars=chars,splitter=splitter,tone_marks=tone_marks,convert=convert) ==excpet
def test_pinyin_default():
    assert p.get_pinyin()=='ni-hao'
@pytest.mark.parametrize('char,excpet',data_get_init)
def test_init(char,excpet):
    assert p.get_initial(char)==excpet
@pytest.mark.parametrize('chars,excpet',data_get_inits)
def test_inits(chars,excpet):
    assert p.get_initials(chars)==excpet
