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

    # Collect all Excel files
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
            
            for _, row in data.iterrows():
                question = row.get("Question", "")
                answer = row.get("Answer", "")
                false1 = row.get("False1", "")
                false2 = row.get("False2", "")
                false3 = row.get("False3", "")

                # Ensure values are strings and handle NaN gracefully
                question = str(question).strip() if pd.notna(question) else ""
                answer = str(answer).strip() if pd.notna(answer) else ""
                false1 = str(false1).strip() if pd.notna(false1) else ""
                false2 = str(false2).strip() if pd.notna(false2) else ""
                false3 = str(false3).strip() if pd.notna(false3) else ""

                game_data[game]["questions"].append({
                    "question": question,
                    "answers": [answer, false1, false2, false3]
                })
            
        except Exception as e:
            print(f"Error loading {game}: {e}")
    return game_data

GAMES = excel_file()
