# Power Consumption Hourly Summary

This Python script reads a CSV file provided by your electric company, containing timestamped power consumption data in 15-minute intervals, and generates a new CSV file that summarizes the total power consumed per hour.
---
## 📋 Input Format

The input CSV should be formatted as follows (no header needed):

"DD/MM/YYYY","HH:MM",<consumption_in_kWh>

Example:

"07/02/2024","09:00",2.994 
"07/02/2024","09:15",2.245 
"07/02/2024","09:30",0.531 

---

## 🧮 What the Script Does

1. Prompts the user to enter the full path to the input CSV file.
2. Reads each row of the file, combining the date and time into a single timestamp.
3. Rounds each timestamp **down to the nearest full hour** (e.g., `09:15` → `09:00`).
4. Sums the power consumption values for each hour.
5. Saves the result as a new CSV file in the **same directory as the script**.

---

## 📤 Output CSV Format

The resulting CSV contains the following columns:

| Column | Description |
|--------|-------------|
| `Date` | Date in DD/MM/YYYY format |
| `Day`  | Day of the week (e.g., Monday) |
| `Hour` | Time in HH:00 format |
| `Total` | Total kWh consumption for that hour |

### Example Output

Date,Day,Hour,Total 
07/02/2024,Wednesday,09:00,6.594 
07/02/2024,Wednesday,10:00,2.631


---

## 🚀 How to Use

### 📦 Prerequisites

Make sure Python 3 is installed:

```bash
python --version
