import spacy
from spacy.matcher import Matcher, PhraseMatcher
from word2number import w2n
import sys
sys.path.append('..')
from exercises.loading_exercises import get_exercises

# TODO: Handle these edge cases:
# I hit bench press today. Did 3 sets — first one was 135 for 10, then 145 for 8, and finished with 155 for 6.
# "Deadlift: 225x5, 245x3, 275x1. Then curls 3x12 @ 35s."
# "Started with squats — 4 sets of 12 at 185. Then overhead press, did two sets of 10 at 95 and one burnout set with just the bar."
import os

# Load model
nlp = spacy.load("en_core_web_sm")

base_dir = os.path.dirname(os.path.abspath(__file__))
text_path = os.path.join(base_dir, '../data/text.txt')
with open(text_path, 'r') as file:
    text = file.read()

doc = nlp(text)

# Matcher setup for sets/reps/weight
matcher = Matcher(nlp.vocab)

# Patterns
# TODO: Ignore punctuation and handle the edge case of one set and one rep i.e. don't end in sets or reps
pattern_sets = [{"LIKE_NUM": True}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": {"IN": ["sets", "set"]}}]
pattern_reps = [{"LIKE_NUM": True}, {"IS_PUNCT": True, "OP": "?"}, {"LOWER": {"IN": ["reps", "rep"]}}]
pattern_weight = [
    {"LIKE_NUM": True},
    {"IS_PUNCT": True, "OP": "?"},
    {"LOWER": {"IN": ["lbs", "kg", "kgs", "pounds", "kilograms"]}}
]

matcher.add("SETS_PATTERN", [pattern_sets])
matcher.add("REPS_PATTERN", [pattern_reps])
matcher.add("WEIGHT_PATTERN", [pattern_weight])

# Get exercise list and create variations (e.g., "squat" -> "squats")
exercises = get_exercises("../data/exercises.json")
exercise_variations = []
for exercise in exercises:
    exercise_variations.append(exercise)
    # Add plural form for single-word exercises
    if ' ' not in exercise and not exercise.endswith('s'):
        exercise_variations.append(exercise + 's')

# Exercise matching using PhraseMatcher (better for exact phrase matching)
exercise_matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
exercise_patterns = [nlp(text) for text in exercise_variations]
exercise_matcher.add("EXERCISE", exercise_patterns)

sets_list = []
reps_list = []
weight_list = []
exercise_list = []

def extract_workout_info():
    # Run matchers
    matches = matcher(doc)
    exercise_matches = exercise_matcher(doc)
    # Print detected sets/reps/weights
    for match_id, start, end in matches:
        span = doc[start:end]
        label = nlp.vocab.strings[match_id]

        raw_val = span[0].text
        try:
            value = int(raw_val)
        except ValueError:
            value = w2n.word_to_num(raw_val)

        if label == "SETS_PATTERN":
            sets_list.append(value)
        elif label == "REPS_PATTERN":
            reps_list.append(value)
        elif label == "WEIGHT_PATTERN":
            weight_list.append(value)

    found_exercises = set()
    for match_id, start, end in exercise_matches:
        span = doc[start:end]
        found_exercises.add(span.text.lower())
    # Also look for partial matches
    for token in doc:
        token_lower = token.text.lower()
        # Check if it's in our exercise list or its plural form
        if token_lower in [ex.lower() for ex in exercise_variations]:
            found_exercises.add(token_lower)

    for exercise in found_exercises:
        exercise_list.append(exercise)

    return exercise_list, sets_list, reps_list, weight_list

if __name__ == "__main__":
    exercise_list, sets_list, reps_list, weight_list = extract_workout_info()
    print(exercise_list)
    print(sets_list)
    print(reps_list)
    print(weight_list)