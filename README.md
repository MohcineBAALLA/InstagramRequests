# InstagramRequests
## Instagram Brute Force Attack

This Python script is designed to perform a brute force attack on Instagram accounts. It attempts to find the correct password for a given Instagram username by trying multiple passwords from a word list.

### How the Script Works
1. The script utilizes various libraries and modules to handle HTTP requests, encryption, user agents, and Tor proxy configuration.
2. It prompts the user to enter the target Instagram username and the path to the password word list file.
3. The script reads the word list file and extracts passwords from it.
4. For each password in the word list, the script creates a separate thread to perform the brute force attack.
5. Within each thread, the script performs the following steps:
   - Configures a Tor proxy for anonymity.
   - Retrieves necessary encryption parameters and tokens from the Instagram website.
   - Encrypts the password using a combination of AES and public-key cryptography.
   - Sends a login request to Instagram using the encrypted password and other required parameters.
   - Checks the response to determine if the login attempt was successful or if there are any error messages.
   - Prints the result of each login attempt, including the username, password, and country code (if available).
6. The script continues the brute force attack until it has tried all the passwords from the word list.
7. The results of each login attempt are displayed on the console.

### Important Notes and Disclaimers
- This script is intended for educational purposes only and should not be used for any illegal or unauthorized activities.
- Performing a brute force attack on someone's Instagram account without their permission is illegal and unethical.
- The script relies on a password word list, so the success of the attack depends on the quality and coverage of the word list.
- The use of Tor proxy is recommended for maintaining anonymity during the attack, but it does not guarantee complete anonymity.
- The author and OpenAI do not promote or endorse any illegal activities or unauthorized access to accounts. Use this script responsibly and at your own risk.

### Requirements
To run this script, you need to have the following dependencies installed:
- requests
- fake_useragent
- stem
- Cryptodome
- PyNaCl

You can install these dependencies using the `pip` package manager.

### Usage
1. Clone or download the repository containing this script from GitHub.
2. Make sure you have Python installed on your system.
3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
4. Open the script in a text editor of your choice and modify the following variables:
   - `Combo`: Provide the path to the password word list file.
5. Open a terminal or command prompt and navigate to the directory where the script is located.
6. Run the script using the following command:
   ```
   python script_name.py
   ```
7. Follow the prompts to enter the Instagram username and start the brute force attack.

### Legal and Ethical Considerations
- This script should only be used on your own accounts or with explicit permission from the account owner.
- Do not use this script for any illegal or unethical activities, including unauthorized access to someone's Instagram account.
- Be aware of the legal implications and consequences before using this script.

### Disclaimer
I do not promote or endorse any illegal activities or unauthorized access to accounts. This script is intended for educational purposes only. Use it responsibly and at your own risk.
