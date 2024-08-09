import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """供所有测试函数使用的实例"""
    question = "first language"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_single_response(language_survey):
    """测试单个答案会被妥善存储"""
    language_survey.store_response('english')
    assert 'english' in language_survey.responses


def test_three_response(language_survey):
    """三个答案会被妥善存储"""
    responses = ['english', 'chinese']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
