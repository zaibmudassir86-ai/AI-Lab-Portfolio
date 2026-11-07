"""
Lab 2: Stateful smart classroom energy agent.
The modes are simulated target labels only. No physical hardware is controlled.
"""
class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        # Occupancy has priority over temperature.
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        send_command = target_mode != self.previous_mode
        previous_mode = self.previous_mode
        if send_command:
            self.previous_mode = target_mode

        return previous_mode, target_mode, send_command


def run_trace(percepts):
    agent = ClassroomAgent()
    print("Step | Previous mode | Percept (temp, occupied) | Target | Result")
    print("-" * 78)
    for step, (temp, occupied) in enumerate(percepts, 1):
        previous, target, send = agent.act(temp, occupied)
        result = "SEND COMMAND" if send else "NO COMMAND"
        print(f"{step:>4} | {str(previous):<13} | ({temp:>2}, {occupied!s:<5})              | {target:<6} | {result}")


if __name__ == "__main__":
    test_percepts = [
        (29, True),   # first COOL command
        (29, True),   # repeated COOL, no command
        (20, True),   # exact lower boundary, IDLE
        (26, True),   # exact upper boundary, remains IDLE
        (19, True),   # transition to WARM
        (29, False),  # empty room priority, ECO
        (29, False),  # repeated ECO, no command
        (29, True),   # transition back to COOL
    ]
    run_trace(test_percepts)
