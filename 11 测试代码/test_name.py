from name import get_name

def test_first_last_name():
    """能否正确处理first和last name"""
    name = get_name('li', 'hua')
    assert name == 'Li Hua'


def test_first_middle_last_name():
    """能否处理中间名"""
    name = get_name('li', 'hua', 'ming')
    assert name == 'Li Ming Hua'
