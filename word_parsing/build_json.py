from .extract_workout_info import extract_workout_info
import json

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

    return workout_log

if __name__ == "__main__":
    json_data = build_json()
    with open("../data/workout_data.json", "w") as f:
        json.dump(json_data, f, indent=2)