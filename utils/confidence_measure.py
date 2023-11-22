def is_low_confidence(answer):
    # Checking for phrases that might indicate uncertainty
    uncertainty_phrases = ["I'm not sure", "I don't know", "no information provided"]
    return any(phrase in answer for phrase in uncertainty_phrases) or len(answer.split()) < 5  