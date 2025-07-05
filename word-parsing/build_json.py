from extract_workout_info import extract_workout_info
import json

# Output format:
#  workout_log = [
#     {
#         "exercise": "exercise_name",
#         "sets": [
#             {
#                 "reps": 10,
#                 "weight": 100
#             },
#             ...
#         ]
#     },
#     ...
# ]

def build_json():
    exercise_list, sets_list, reps_list, weight_list = extract_workout_info()
    
    workout_log = []
    
    current_set_idx = 0
    for exercise in exercise_list:
        exercise_data = {
            "exercise": exercise,
            "sets": []
        }
        
        # If we have sets info for this exercise
        if current_set_idx < len(sets_list):
            num_sets = sets_list[current_set_idx]
            
            # Create the sets array
            for _ in range(num_sets):
                if current_set_idx < len(reps_list) and current_set_idx < len(weight_list):
                    set_data = {
                        "reps": reps_list[current_set_idx],
                        "weight": weight_list[current_set_idx]
                    }
                    exercise_data["sets"].append(set_data)
                current_set_idx += 1
                
        workout_log.append(exercise_data)
    
    return workout_log

if __name__ == "__main__":
    json_data = build_json()
    with open("../data/workout_data.json", "w") as f:
        json.dump(json_data, f, indent=2)