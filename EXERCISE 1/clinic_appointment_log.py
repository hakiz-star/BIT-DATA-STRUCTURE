# Project 24: Clinic Appointment Log

import array

# === Integers: Appointment counts for each day (e.g., Monday to Sunday) ===
appointments = [12, 15, 10, 18, 20, 17, 14]

# Compute total, average, minimum, and maximum
total_appointments = sum(appointments)
average_appointments = total_appointments / len(appointments)
min_appointments = min(appointments)
max_appointments = max(appointments)

print("=== Appointment Statistics ===")
print("Total Appointments:", total_appointments)
print("Average Appointments per Day:", average_appointments)
print("Minimum Appointments in a Day:", min_appointments)
print("Maximum Appointments in a Day:", max_appointments)

# === Strings: Report using f-strings ===
report = (
    f"\n Weekly Clinic Appointment Summary\n"
    f"Total appointments: {total_appointments}\n"
    f"Average per day: {average_appointments:.2f}\n"
    f"Minimum: {min_appointments}, Maximum: {max_appointments}"
)

print(report)

# === Booleans: Threshold check ===
threshold = 15

# Compound boolean condition
if average_appointments > threshold and max_appointments > 18:
    print("\nStatus: Above Standard")
else:
    print("\nStatus: Below Standard")

# === Lists: Manage patient list ===
patients = ["Alice", "Bob", "Charlie", "David"]
print("\nPatients (original):", patients)

# Add new patient
patients.append("Eva")

# Remove patients whose names start with "C"
patients = [p for p in patients if not p.startswith("C")]

print("Patients after adding and removing:", patients)

# Sort the list
patients.sort()
print("Patients after sorting:", patients)

# === Arrays: Store subset of appointments ===
appointments_array = array.array('i', appointments[:5])  # First 5 days

# Sum of array values
array_sum = sum(appointments_array)

# Compare with list version
list_sum = sum(appointments[:5])

print("\n=== Array Data ===")
print("Appointments Array:", appointments_array.tolist())
print("Sum from array:", array_sum)
print("Sum from list (first 5 days):", list_sum)

# === Dictionaries: Appointment records by day ===
appointment_records = [
    {"id": 1, "name": "Mon", "value": 12},
    {"id": 2, "name": "Tue", "value": 15},
    {"id": 3, "name": "Wed", "value": 10},
    {"id": 4, "name": "Thu", "value": 18},
]

# Update Wednesday's value
for record in appointment_records:
    if record["name"] == "Wed":
        record["value"] = 11

# Delete Tuesday's record
appointment_records = [rec for rec in appointment_records if rec["name"] != "Tue"]

# Compute total value
total_value = sum(record["value"] for record in appointment_records)

print("\n=== Appointment Records ===")
for record in appointment_records:
    print(record)

print("Total Value from Records:", total_value)

# === End of Program ===
print("\n Clinic Appointment Log processed successfully.")
