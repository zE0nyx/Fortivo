# Fortivo
   Fortivo is a powerful tool that evaluates the strength of passwords based on length, complexity, and entropy. It helps ensure your passwords are strong enough to resist modern attack techniques, improving your security posture.

# Features
  **Minimum Length Requirement:** Passwords must be at least 12 characters long.
  
  **Character Diversity:** Requires a mix of uppercase letters, lowercase letters, numbers, and special characters for enhanced complexity.
  
  **No Common or Guessable Passwords:** Detects and rejects passwords that use common dictionary words (rockyou.txt), names, or easily guessable patterns. Ensures no repetitive or predictable patterns (e.g., "12345" or "password123").

# Setup
      git clone "https://github.com/zE0nyx/Fortivo.git"
      cd Fortivo
      python setup.py install
In case of issue in installation use python3 instead of python

# Usage
      python3 fortivo.py 'A12ch4r4ct3rP4s5wOrd'
   Run the python file using a password as the argument
