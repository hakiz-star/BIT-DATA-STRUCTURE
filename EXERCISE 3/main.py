# main.py
# Practical Stack and Queue Exercises

# --- Stack Practical 1: Irembo ---
print('--- Stack Practical 1: Irembo ---')
stack = []
stack.extend(["Step1", "Step2", "Step3"])
print(f"Initial stack: {stack}")
stack.pop()
print(f"Stack after one pop: {stack}")

# --- Stack Practical 2: UR Exam ---
print('\n--- Stack Practical 2: UR Exam ---')
exam_stack = []
exam_stack.extend(["Q1", "Q2", "Q3"])
print(f"Initial stack: {exam_stack}")
exam_stack.pop()
exam_stack.pop()
print(f"Stack after undoing 2: {exam_stack}")

# --- Queue Practical 1: RSSB ---
print('\n--- Queue Practical 1: RSSB ---')
from collections import deque
queue = deque()
queue.extend(["Applicant1", "Applicant2", "Applicant3", "Applicant4", "Applicant5"])
print(f"Initial queue: {list(queue)}")
queue.popleft()
queue.popleft()
queue.popleft()
print(f"Queue after serving 3: {list(queue)}")
print(f"Person in front: {queue[0]}")

# --- Queue Practical 2: Airtel ---
print('\n--- Queue Practical 2: Airtel ---')
airtel_queue = deque()
airtel_queue.extend([f"Client{i+1}" for i in range(7)])
print(f"Initial queue: {list(airtel_queue)}")
served = [airtel_queue.popleft() for _ in range(3)]
print(f"Clients served: {served}")
print(f"Third client served: {served[2]}")
