# User Data Authentication and Security

## Description
This project focuses on back-end security concepts, specifically handling user data safely, authenticating with databases, and logging information securely. It covers the identification and obfuscation of Personally Identifiable Information (PII), secure password hashing using `bcrypt`, and securely passing database credentials using environment variables.

## Requirements

* **Environment:** Ubuntu 20.04 LTS using Python 3 (version 3.9)
* **Style:** Code must conform to `pycodestyle` (version 2.5)
* **Execution:** All files must be executable and start with `#!/usr/bin/env python3`
* **Type Annotations:** All functions and coroutines must be type-annotated
* **Documentation:** All modules, classes, and functions must be fully documented with meaningful sentences explaining their purpose.

---

## Tasks

### 0. PII and Non-PII
**Objective:** Understand and categorize Personally Identifiable Information.
* **Description:** You must be able to define what PII is and distinguish it from non-PII. PII includes direct identifiers (like a passport number or email) and indirect identifiers (like a zip code or date of birth) that, when combined, can identify a specific individual. Non-PII is anonymized data that cannot trace back to a user.

### 1. Log Filter for PII Obfuscation
**Objective:** Implement a mechanism to prevent sensitive data from being written to log files.
* **Description:** Create a custom log formatter using Python's `logging` and `re` (regular expressions) modules. The formatter must intercept log messages and search for specific PII fields (such as `password`, `email`, or `ssn`). It should replace the actual values with a generic masking string (e.g., `***`) before the log is outputted to the console or a file.

### 2. Password Encryption and Validation
**Objective:** Securely store and verify user passwords.
* **Description:** Implement functions to securely hash a plaintext password using the `bcrypt` package. You will generate a salt and hash the password before it would theoretically be saved to a database. Additionally, implement a validation function that takes a plaintext input and compares it against the stored hash using `bcrypt.checkpw()` to verify the user's identity without ever storing the actual password.

### 3. Database Authentication via Environment Variables
**Objective:** Keep sensitive database credentials out of your source code.
* **Description:** Implement a secure way to connect to a database by retrieving credentials (like the database username, password, host, and database name) directly from the environment using Python's `os.getenv()`. This ensures that hardcoded secrets are not pushed to version control, minimizing security risks.

---
