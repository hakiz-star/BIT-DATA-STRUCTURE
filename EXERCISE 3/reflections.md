# Challenge: Kigali Stadium Entry (FIFO vs LIFO)

## Scenario
When people arrive at Kigali Stadium, they line up in the order they came:

```
[P1, P2, P3, P4, ...]
```

- **If we use a stack (LIFO)** → the last person (P4) will enter before the first person (P1).  
  This creates unfairness, because someone who arrived earlier has to wait longer than someone who just came.  

---

## Reflection: Why FIFO is Fair in Events
A **queue (FIFO)** ensures fairness because:

- **First Come, First Served (FCFS):** The person who arrived first (P1) enters first.  
- **Fairness:** No one is skipped or overtaken by latecomers.  
- **Orderly Management:** It prevents fights, confusion, or complaints among people waiting.  

### Real-world Examples
- At a **concert**, the first fan who arrives at the gate should enter before those who come later.  
- At **banks or bus stops**, customers and passengers are served in the order they arrive.  

➡️ This principle shows why FIFO (queue) matches fairness: it respects people’s time and effort in arriving early.  

---

## Python Code Example

```python
from collections import deque

# People arriving at the stadium
people = ["P1", "P2", "P3", "P4"]

print("=== Using Queue (FIFO) ===")
queue = deque(people)   # queue
while queue:
    person = queue.popleft()  # remove from front
    print(f"{person} enters the stadium")

print("\n=== Using Stack (LIFO) ===")
stack = people[:]  # copy list
while stack:
    person = stack.pop()  # remove from end
    print(f"{person} enters the stadium")
```

---

## Output

```
=== Using Queue (FIFO) ===
P1 enters the stadium
P2 enters the stadium
P3 enters the stadium
P4 enters the stadium

=== Using Stack (LIFO) ===
P4 enters the stadium
P3 enters the stadium
P2 enters the stadium
P1 enters the stadium
```

---

## Explanation
- **Queue (FIFO):** The first person (P1) who arrived enters first → ✅ Fair.  
- **Stack (LIFO):** The last person (P4) who arrived enters first → ❌ Unfair, earlier arrivals wait longer.  

---

**END.**
