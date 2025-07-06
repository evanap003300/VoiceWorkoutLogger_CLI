from .extract_workout_info import extract_workout_info
import json
import os

def build_json():
    # Extract lists from NLP extraction
    exercise_list, sets_list, reps_list, weight_list = extract_workout_info()
    
    workout_log = []
    rep_weight_idx = 0  # Tracks index into reps/weights arrays

    for i, exercise in enumerate(exercise_list):
        exercise_data = {
            "exercise": exercise,
            "sets": []
        }

        # Get number of sets for this exercise, default to 1 if missing
        num_sets = sets_list[i] if i < len(sets_list) else 1

        for _ in range(num_sets):
            # Ensure we don't go out of bounds
            if rep_weight_idx < len(reps_list) and rep_weight_idx < len(weight_list):
                set_data = {
                    "reps": reps_list[rep_weight_idx],
                    "weight": weight_list[rep_weight_idx]
                }
                exercise_data["sets"].append(set_data)
                rep_weight_idx += 1
            else:
                break  # No more rep/weight pairs to use

        workout_log.append(exercise_data)

    # Save the JSON file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    json_path = os.path.join(project_root, 'data', 'workout_data.json')
    
    with open(json_path, 'w') as f:
        json.dump(workout_log, f, indent=2)

    return workout_log