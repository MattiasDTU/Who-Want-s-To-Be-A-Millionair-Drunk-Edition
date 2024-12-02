# Who Wants to Be a Millionaire - Quiz Game

A Python-based interactive quiz game inspired by "Who Wants to Be a Millionaire.". In this game you're able to include your own questions by modefying one of the Excel sheets. MAX and MIN 20 questions. You must go into settings (when running the program) and choose which quiz to use, before pressing start. Currently you have to restart the program after running it once :^)

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
4. [File Structure](#file-structure)
---
![image](https://github.com/user-attachments/assets/4480e2f1-b055-4473-9c8e-1d44a81501fe)

## Prerequisites

Ensure you have the following installed:
- **Python 3.7+**
- **Libraries**:
  - `pygame`: For GUI (`pip install pygame`)
  - `pandas`: For handling Excel files (`pip install pandas`)
---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MattiasDTU/millionaire-quiz-game.git
   cd millionaire-quiz-game

## File Structure
📁 millionaire-quiz-game/
├── 📁 Games/                # Folder for Excel game data

├── 📁 images/               # Folder for required images

├── 📄 main.py               # Entry point for the game

├── 📄 classes.py            # Core classes (e.g., Box for GUI elements)

├── 📄 colors.py             # Color constants and utility functions

├── 📄 controls.py           # Mouse and event handling

├── 📄 layout.py             # UI rendering functions

├── 📄 image.py              # Image rendering functions

├── 📄 excel_loader.py       # Excel data loader

├── 📄 global_variables.py   # Global variables

└── 📄 requirements.txt      # Python dependencies
