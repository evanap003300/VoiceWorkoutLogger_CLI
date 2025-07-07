import spacy
from spacy.matcher import Matcher, PhraseMatcher
from word2number import w2n
import os
import sys

sys.path.append('..')
from exercises.loading_exercises import get_exercises

nlp = spacy.load("en_core_web_sm")

# Load exercise names
exercise_terms = get_exercises("../data/exercises.json")
exercise_variations = []
for term in exercise_terms:
    term = term.lower()
    exercise_variations.append(term)
    if ' ' not in term and not term.endswith('s'):
        exercise_variations.append(term + 's')

# Create matchers
matcher = Matcher(nlp.vocab)
exercise_matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# Add patterns
pattern_sets = [{"LIKE_NUM": True}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": {"IN": ["set", "sets"]}}]
pattern_reps = [{"LIKE_NUM": True}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": {"IN": ["rep", "reps"]}}]
pattern_weight = [{"LIKE_NUM": True}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": {"IN": ["lbs", "kg", "kgs", "pounds", "kilograms"]}}]

matcher.add("SETS_PATTERN", [pattern_sets])
matcher.add("REPS_PATTERN", [pattern_reps])
matcher.add("WEIGHT_PATTERN", [pattern_weight])

exercise_patterns = [nlp(text) for text in exercise_variations]
exercise_matcher.add("EXERCISE", exercise_patterns)

def extract_workout_info():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    text_path = os.path.join(base_dir, '../data/text.txt')
    
    with open(text_path, 'r') as file:
        text = file.read()

    doc = nlp(text)

    timeline = []

    # Get all matches in order of appearance
    for match_id, start, end in matcher(doc):
        label = nlp.vocab.strings[match_id]
        span = doc[start:end]
        raw_val = span[0].text

        try:
            value = int(raw_val)
        except ValueError:
            try:
                value = w2n.word_to_num(raw_val)
            except:
                continue

        timeline.append((start, label, value))

    for match_id, start, end in exercise_matcher(doc):
        span = doc[start:end]
        timeline.append((start, "EXERCISE", span.text.lower()))

    # Sort everything by token position
    timeline.sort(key=lambda x: x[0])

    # Now rebuild lists in order
    exercise_list = []
    sets_list = []
    reps_list = []
    weight_list = []

    for _, label, value in timeline:
        if label == "EXERCISE":
            exercise_list.append(value)
        elif label == "SETS_PATTERN":
            sets_list.append(value)
        elif label == "REPS_PATTERN":
            reps_list.append(value)
        elif label == "WEIGHT_PATTERN":
            weight_list.append(value)

    return exercise_list, sets_list, reps_list, weight_list

if __name__ == "__main__":
    e, s, r, w = extract_workout_info()
    print("Exercises:", e)
    print("Sets:", s)
    print("Reps:", r)
    print("Weights:", w)