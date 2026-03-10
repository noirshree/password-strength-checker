## README: Password Strength Checker

This repository contains a **Python-based GUI application** that evaluates the strength of a password based on common security criteria. The application uses the `tkinter` library for the interface and regular expressions to validate password complexity.



### Features

* **Real-time Analysis:** Evaluates passwords based on five key security metrics.
* **Visual Feedback:** Provides color-coded results (**Green** for Strong, **Orange** for Medium, and **Red** for Weak).
* **Privacy-Focused:** Uses a masked input field (password characters are hidden with `*`).
* **User-Friendly Interface:** A clean, lightweight window built with Python's standard GUI toolkit.



### Security Criteria

The application calculates a score from **0 to 5** by checking for the following:

1.Length: At least 8 characters.
2.Uppercase: At least one capital letter (A-Z).
3.Lowercase: At least one lowercase letter (a-z).
4.Digits: At least one numerical digit (0-9).
5.Special Characters: Includes symbols such as `!@#$%^&*`.


### Installation & Usage

#### Prerequisites

* Python 3.x must be installed on your system.
* The `tkinter` library (usually included with standard Python installations).

#### Running the App

1. Save the code as `password_strength_checker.py`.
2. Open your terminal or command prompt.
3. Run the following command:
```bash

python password_strength_checker.py

### Code Overview

The script is structured into two main sections:

* `check_strength()`: The logic engine. It uses the `re` (regular expression) module to scan the input string for required patterns and calculates a score by subtracting errors from the maximum possible points.
* GUI Setup: Defines the main window (`root`), entry field, and the "Check Strength" button that triggers the validation function.

---

### Example Results

| Score|Result Label|     Description              |
| ---  | ---            | ---                          |
| 5/5  | Strong         | Meets all security criteria. |
| 3-4  | Medium         | Lacks one or two elements    |
| 0-2  | Weak           | Fails multiple criteria      |

