import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to code?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is store properly."""
    language_survey.store_response("Python")
    assert "Python" in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are store properly."""
    responses = ["Python", "R", "javascript"]
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses
