from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you learn to code in first?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("Python")
    assert "Python" in language_survey.responses

def test_store_three_responses():
    """Test that three individual responses are stored properly"""
    question = "What language dud you learn to code in first?"
    language_survey = AnonymousSurvey(question)
    responses = ["R", "Python", "javascript"]
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses