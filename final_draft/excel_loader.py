import os
import pandas as pd

def excel_file():
    folder_path = "Games"
    game_files = {}

    for file_name in os.listdir(folder_path):

        if file_name.endswith((".xls", ".xlsx")):
            file_path = os.path.join(folder_path, file_name)
            game_files[file_name.strip(".xlsx")] = file_path

    game_data = {}
    for game in game_files:
        try:
            file_path = game_files[game]
            data = pd.read_excel(file_path)

            if game not in game_data:
                game_data[game] = {"questions": []}
            
            for idx, row in data.iterrows():
                question = row.get("Question", "").strip()
                answers = [
                    row.get("Answer", "").strip(),
                    row.get("False1", "").strip(),
                    row.get("False2", "").strip(),
                    row.get("False3", "").strip(),
                ]
                
                game_data[game]["questions"].append({
                    "question": question,
                    "answers": answers
                })
            
            print(f"Loaded data from {game}")
        except Exception as e:
            print(f"Error loading {game}: {e}")
    return game_data

    # print("Game data:", game_data.keys())