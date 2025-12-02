# 📈 NumPy Mean-Variance-Standard Deviation Calculator

## Hello there! 

Thanks for checking out my solution for the Mean-Variance-Standard Deviation Calculator project. This is one of the five required projects for the **[freeCodeCamp Data Analysis with Python Certification](**. My goal here was to use the NumPy library to efficiently handle matrix algebra and statistics.

---

## 🚀 Project Overview

The core of this project is a single function, `calculate()`, which accepts a flat list of nine digits. The function first converts that list into a 3x3 NumPy array and then performs statistical calculations across three dimensions:

* **1. Axis 0 (Columns):** Calculation applied down each column.
* **2. Axis 1 (Rows):** Calculation applied across each row.
* **3. Flattened Array:** Calculation applied to all nine elements together.

### ✨ Calculations Performed:

* Mean
* Variance
* Standard Deviation
* Max
* Min
* Sum

---

## ⚙️ Local Setup and Run Instructions

To test this function locally:
1.  Clone this repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run the main file (which executes the unit tests): `python main.py`

---

## 💻 Example Output

The function returns a dictionary structured as follows. Using the input list `[0, 1, 2, 3, 4, 5, 6, 7, 8]` results in:

```python
# Note: Axis 0 (Columns) results come first, followed by Axis 1 (Rows).
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  # ... (Other metrics follow the same structure)
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
...
## 💻 Example Output

[Your code output block goes here]

---

## ⚖️ Licensing ⬅️ ADD THIS SECTION HERE

This project is licensed under the **MIT License**. For the full terms and conditions, see the [LICENSE](LICENSE) file in this repository.

---

*If you have any questions or feedback, please feel free to reach out!*
