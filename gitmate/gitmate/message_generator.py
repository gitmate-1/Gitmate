import os
from datetime import datetime

def generate_smart_message():
    """Generate smart commit message based on changes"""
    changed_files = os.popen('git diff --name-only').read().strip().split('\n')
    changed_files = [f for f in changed_files if f]
    count = len(changed_files)

    if count == 0:
        return "No changes detected"
    
    date_str = datetime.now().strftime("%d %b %Y, %I:%M %p")
    msg = f"Updated {count} file{'s' if count > 1 else ''} on {date_str}"
    return msg
