import os
import pandas as pd

def excel_file():
    """
    Reads Excel files from the 'Games' folder and parses their contents into a structured dictionary.
    
    Each Excel file is expected to have columns:
    - 'Question' (the question text)
    - 'Answer' (the correct answer)
    - 'False1', 'False2', 'False3' (incorrect answers)

    Returns:
        dict: A dictionary where keys are game names (based on file names) and values contain questions and answers.
    """
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
            
        except Exception as e:
            print(f"Error loading {game}: {e}")
    return game_data

GAMES = excel_file()
    # print("Game data:", game_data.keys())