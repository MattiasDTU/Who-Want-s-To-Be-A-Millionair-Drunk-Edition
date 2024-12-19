# Who Wants to Be a Millionaire - Quiz Game

A Python-based interactive quiz game inspired by "Who Wants to Be a Millionaire.". In this game you're able to include your own questions by modefying one of the Excel sheets. MAX and MIN 20 questions. You must go into settings (when running the program) and choose which quiz to use, before pressing start.

---

## Features

- **Customizable Gameplay**: Add your own questions using Excel files.
- **Interactive Graphics**: Dynamic menus and in-game visual elements.
- **Lifelines**: Includes 50/50, Ask the Audience, Phone a Friend, and a unique "Take a Shot" feature.
- **Progressive Challenges**: Earn guaranteed prizes after answering 5, 10, and 15 questions.
- **Drink Game Mechanics**: Opt to drink to continue after wrong answers (for adult audiences).
---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Instructions](#instructions)
3. [Installation](#installation)
4. [File Structure](#file-structure)
5. [Excel File Format](#excel-file-format)
---
## Prerequisites

Ensure you have the following installed:
- **Python 3.7+**
- **Libraries**:
  - `pygame`: For GUI (`pip install pygame`)
  - `pandas`: For handling Excel files (`pip install pandas`)
  - `random`: For randomizing the possible answers (`pip install random`)
---

## Instructions
The whole program is based around the main.py file, so to run the program, you'll have to run that file.
---
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MattiasDTU/Who-Want-s-To-Be-A-Millionair-Drunk-Edition.git
   cd Who-Want-s-To-Be-A-Millionair-Drunk-Edition
---
## File Structure

📂 src

├── 📦 components.py    # 🧩 UI components like buttons and text rendering utilities.

├── 🖱️ events.py        # 🖱️ Handles mouse interactions and event management.

├── 📊 excel.py         # 📊 Loads and processes questions and answers from Excel files.

├── 🎮 game.py          # 🎮 Main game logic, including lifelines and score tracking.

├── 🚀 main.py          # 🚀 Entry point, responsible for initializing and running the game loop.

├── 🏠 menu.py          # 🏠 Main menu logic and navigation.

├── 📜 rules.py         # 📜 Displays game rules and handles the rules screen.

├── 🎨 screen.py        # 🎨 Screen initialization, scaling, and rendering the background.

├── ⚙️ settings.py      # ⚙️ Configuration options like frame rate and test mode.

├── 🔧 advanced.py      # 🔧 Advanced settings menu for lifelines configuration.

├── 🎨 colors.py        # 🎨 Defines color constants for consistent UI design.

📂 Excel/

├── example_game.xlsx    # 📝 Example Excel file with questions and answers.

---
### 📝 Excel File Format

Each Excel file must follow the format below to work correctly:

| **Column** | **Description**               |
|------------|--------------------------------|
| `Question` | The text of the question.     |
| `Answer`   | The correct answer.           |
| `False1`   | First incorrect answer.       |
| `False2`   | Second incorrect answer.      |
| `False3`   | Third incorrect answer.       |

### 📄 Example File: `example_game.xlsx`

| Question                        | Answer | False1  | False2 | False3 |
|---------------------------------|--------|---------|--------|--------|
| What is the capital of France?  | Paris  | Berlin  | Madrid | Rome   |
| 2 + 2 equals what?              | 4      | 3       | 5      | 6      |
| Who discovered gravity?         | Newton | Einstein| Tesla  | Hawking|

### 🚀 Adding New Games

1. Create a new Excel file in the `Excel/` folder.
2. Follow the column structure described above.
3. Save your file with a meaningful name (e.g., `science_trivia.xlsx`).
4. When you run the game, it will automatically include your file in the available game options.

> **Note:** Ensure all files are properly formatted to avoid errors during game execution.
