## README: Password Strength Checker

This repository contains a **Python-based GUI application** that evaluates the strength of a password based on common security criteria. The application uses the `tkinter` library for the interface and regular expressions to validate password complexity.



### Features

* **Real-time Analysis:** Evaluates passwords based on five key security metrics.
* **Visual Feedback:** Provides color-coded results (**Green** for Strong, **Orange** for Medium, and **Red** for Weak).
* **Privacy-Focused:** Uses a masked input field (password characters are hidden with `*`).
* **User-Friendly Interface:** A clean, lightweight window built with Python's standard GUI toolkit.



### Security Criteria

The application calculates a score from **0 to 5** by checking for the following:

1. **Length:** At least 8 characters.
2. **Uppercase:** At least one capital letter (A-Z).
3. **Lowercase:** At least one lowercase letter (a-z).
4. **Digits:** At least one numerical digit (0-9).
5. **Special Characters:** Includes symbols such as `!@#$%^&*`.


### Installation & Usage

To make the **Running the App** section clear and professional, you should provide step-by-step instructions that account for different operating systems.

Here is a refined version you can copy directly into your README:

---

### Running the App

Follow these steps to launch the Password Strength Checker on your local machine:

#### 1. Save the Script

Copy the provided Python code and save it as a file named `password_strength_checker.py`.

#### 2. Open Your Terminal

Navigate to the folder where you saved the file using your command line interface (Terminal on macOS/Linux or Command Prompt/PowerShell on Windows).

#### 3. Execute the Program

Run the script by typing the following command and pressing **Enter**:

```bash
python password_strength_checker.py

```

> **Note:** Depending on your installation, you may need to use `python3` instead of `python`.

#### 4. Interaction

* A window titled **"Password Strength Checker"** will appear.
* Type a password into the entry field.
* Click the enter to see your results and improvement tips.

---

### Troubleshooting

* **ModuleNotFoundError:** If you receive an error regarding `tkinter`, it may not be installed by default on some Linux distributions. You can install it via:
* *Ubuntu/Debian:* `sudo apt-get install python3-tk`
* *Fedora:* `sudo dnf install python3-tkinter`


* **Python Not Found:** Ensure Python is added to your system's PATH during installation.

---

### Example Results

|Score| Result | Description                  |
| --- | ---    | ---                          |
| 5/5 | Strong | Meets all security criteria. |
| 3-4 | Medium | Lacks one or two elements    |
| 0-2 | Weak   | Fails multiple criteria      |

