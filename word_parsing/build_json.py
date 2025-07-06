from .extract_workout_info import extract_workout_info
import json
import os 
# Output format:
# workout_log = [
#     {
#         "exercise": "exercise_name",
#         "sets": [
#             {"reps": 10, "weight": 100},
#             ...
#         ]
#     },
#     ...
# ]

def build_json():
    exercise_list, sets_list, reps_list, weight_list = extract_workout_info()
    
    workout_log = []
    
    rep_weight_idx = 0  # Index into flat reps/weights list

    for i, exercise in enumerate(exercise_list):
        exercise_data = {
            "exercise": exercise,
            "sets": []
        }

        if i < len(sets_list):
            num_sets = sets_list[i]

            for _ in range(num_sets):
                if rep_weight_idx < len(reps_list) and rep_weight_idx < len(weight_list):
                    set_data = {
                        "reps": reps_list[rep_weight_idx],
                        "weight": weight_list[rep_weight_idx]
                    }
                    exercise_data["sets"].append(set_data)
                    rep_weight_idx += 1

        workout_log.append(exercise_data)

    # Save the JSON file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    json_path = os.path.join(project_root, 'data', 'workout_data.json')
    
    with open(json_path, 'w') as f:
        json.dump(workout_log, f, indent=2)
    
    return workout_log