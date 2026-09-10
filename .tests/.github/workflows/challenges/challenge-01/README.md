import os
import hashlib
import pytest
import sys

# Add challenge directory to path
sys.path.append(os.path.abspath("challenges/challenge-01"))

try:
    from submission import decrypt_payload
except ImportError:
    decrypt_payload = None

def test_challenge_01_flag():
    assert decrypt_payload is not None, "submission.py must define 'decrypt_payload()'"
    
    # Run student function
    student_flag = decrypt_payload("challenges/challenge-01/cipher.txt")
    
    # Retrieve true flag from environment secret
    expected_flag = os.getenv("EXPECTED_FLAG_CHALLENGE_1", "")
    
    # Hash both to prevent accidental plain-text leak in test logs
    student_hash = hashlib.sha256(student_flag.strip().encode()).hexdigest()
    expected_hash = hashlib.sha256(expected_flag.strip().encode()).hexdigest()
    
    assert student_hash == expected_hash, "Decrypted flag does not match the secret key."
