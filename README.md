# Password Strength Checker 🔐

A Python-based tool to evaluate the strength of passwords. This project was developed as part of the Prodigy Infotech Internship by **Ayush Thakur (Hunter001x)**.

## Features
- **Interactive Mode**: Enter passwords directly in the terminal for analysis.
- **CLI Mode**: Pass a password as a command-line argument for quick evaluation.
- Provides detailed feedback on how to improve weak passwords.
- Categorizes passwords as **Strong**, **Moderate**, or **Weak** based on:
  - Length (minimum 8 characters)
  - Presence of lowercase letters
  - Presence of uppercase letters
  - Presence of numbers
  - Presence of special characters (`!@#$%^&*(),.?":{}|<>`)

## Usage

### Prerequisites
- Python 3.x installed on your system.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Hunter001x/password-strength-checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-strength-checker
   ```
3. Install any required dependencies (if applicable).


### Running the Tool
1. Clone or download this repository.
2. Navigate to the directory containing `pass-checker.py`.

#### Interactive Mode
Run the script without any arguments:
```bash
python pass-checker.py
```
You will be prompted to enter a password for analysis.

#### CLI Mode
Pass a password as an argument:
```bash
python pass-checker.py --password "YourPassword123!"
```

### Example Output
#### Strong Password
```
🔎 Result: ✅ Strong Password
```

#### Weak Password
```
🔎 Result: 🚫 Weak Password
❌ Password must be at least 8 characters
❌ Add uppercase letters
❌ Add special characters (!@#$ etc.)
```

## Banner
The tool displays the following banner upon execution:
```
 ____                                _               ____ _               _             
|  _ \ __ _ ___ _____      _____  __| | ___  _ __   / ___| |__   ___  ___| | _____ _ __ 
| |_) / _` / __/ __\ \ /\ / / _ \/ _` |/ _ \| '__| | |   | '_ \ / _ \/ __| |/ / _ \ '__|
|  __/ (_| \__ \__ \\ V  V /  __/ (_| | (_) | |    | |___| | | |  __/ (__|   <  __/ |   
|_|   \__,_|___/___/ \_/\_/ \___|\__,_|\___/|_|     \____|_| |_|\___|\___|_|\_\___|_|   
                                                                                       
==========================================================================================
            Password Strength Checker - Prodigy Infotech Internship
                Developed by: Ayush Thakur (Hunter001x) 🔐
==========================================================================================
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git commit -m "Add feature-name"
   git push origin feature-name
   ```
4. Open a pull request.

## Acknowledgments
- **Prodigy Infotech** for providing the opportunity to work on this project.
- **Ayush Thakur (Hunter001x)** for developing this tool.

## 📧 Contact
For any questions or feedback, feel free to reach out:
- **GitHub**: [Hunter001x](https://github.com/aayushthakur001)


## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

## Author
Developed by **Ayush Thakur (Hunter001x)** as part of the Prodigy Infotech Internship.