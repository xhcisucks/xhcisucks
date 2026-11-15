#!/usr/bin/env python3
"""Rewrite the age between <!--AGE--> and <!--/AGE--> in README.md."""
import re
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

BIRTHDATE = date(2007, 9, 6)

README = Path(sys.argv[1] if len(sys.argv) > 1 else "README.md")
PATTERN = re.compile(r"(<!--AGE-->).*?(<!--/AGE-->)")

today = datetime.now(ZoneInfo("Europe/London")).date()
age = today.year - BIRTHDATE.year - ((today.month, today.day) < (BIRTHDATE.month, BIRTHDATE.day))

text = README.read_text(encoding="utf-8")
if not PATTERN.search(text):
    sys.exit("Age markers <!--AGE--><!--/AGE--> not found in README.")

new_text = PATTERN.sub(rf"\g<1>{age}\g<2>", text, count=1)
if new_text != text:
    README.write_text(new_text, encoding="utf-8")
    print(f"Updated age to {age}")
else:
    print(f"Age already {age}, nothing to do")
