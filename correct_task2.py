# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
def count_valid_emails(emails):
    """
    Counts the number of strings in the input list that resemble valid email addresses.
    
    A valid email is defined as a string containing exactly one '@' symbol,
    with at least one character before it (local part) and at least one dot ('.')
    in the part after it (domain part), which must also be non-empty.
    
    Non-string entries are ignored.
    
    Args:
        emails (list): List of potential email strings.
        
    Returns:
        int: Count of valid-looking email addresses.
    """
    if not isinstance(emails, list):
        return 0
        
    count = 0
    for email in emails:
        if not isinstance(email, str):
            continue
            
        # Reject strings with any whitespace (space, tab, newline, etc.)
        if any(char.isspace() for char in email):
            continue
        
        if email.count('@') != 1:
            continue
            
        local, domain = email.split('@')
        
        if not local or not domain:
            continue
            
        # Require at least one dot in domain for basic validity (e.g., "user@example.com")
        # This excludes valid but uncommon cases like "user@localhost", but improves real-world accuracy
        if '.' not in domain:
            continue
            
        count += 1
        
    return count