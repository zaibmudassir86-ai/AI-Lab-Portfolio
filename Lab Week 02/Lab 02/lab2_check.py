"""
Lab 2: Small checks for stateful classroom agent.
Run with: python lab2_check.py
"""
from lab2_model import ClassroomAgent

def check(label, condition):
    print(f"{label}: {'PASS' if condition else 'FAIL'}")

agent = ClassroomAgent()
first = agent.act(29, True)
second = agent.act(29, True)
boundary_low = agent.act(20, True)
boundary_high = agent.act(26, True)
empty = agent.act(29, False)

check("First target sends COOL", first == (None, "COOL", True))
check("Repeated COOL is suppressed", second == ("COOL", "COOL", False))
check("20 C boundary is IDLE", boundary_low[1] == "IDLE")
check("26 C boundary is IDLE", boundary_high[1] == "IDLE" and boundary_high[2] is False)
check("Empty room selects ECO", empty[1] == "ECO" and empty[2] is True)
