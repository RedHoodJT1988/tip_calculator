# 💸 Pythonic Tip Calculator 🤓🍽️

Ever been stuck at dinner, awkwardly trying to figure out who owes what?  
Fear no more — the **Pythonic Tip Calculator** is here to make your life easier, your splits fairer, and your math *way* cooler.

This sleek little script helps you:
- Calculate the total tip
- Find the grand total (bill + tip)
- Divide the damage evenly between everyone at the table

---
## 🎯 What Does It Do?
✨ Input:
- The total bill 🧾  
- The tip percentage (be generous, your server deserves it! 💁‍♂️)  
- The number of people (even the friend who "forgot their wallet")  

🎉 Output:
- Total tip 💰  
- Total amount (bill + tip) 💳  
- How much each person owes 🙋‍♀️🙋‍♂️

---
##  🧪 Example
- Enter the total bill amount: 80
- Enter the tip percentage (default is 15): 20
- Enter the number of people (default is 1): 4

## 📤 Output:
```bash
Tip calculation result
Total Tip: $16.0
Total Amount: $96.0
Amount per Person: $24.0
```
---
## 🛡️ Input Validation (a.k.a. "No Funny Business")

- ❌ No negative tips (unless you're *that* kind of person...)  
- ❌ No zero-dollar bills (unless dinner was imaginary)  
- ❌ No splitting the bill with 0 people (who are you sharing with, ghosts?)

---

## 🧠 How It Works

Under the hood, there’s some nice clean Python magic:

- `validate_tip_inputs()` – Makes sure everything makes sense
- `calculate_tip()` – Crunches the numbers and splits the bill
- `main()` – Gathers user input and prints the results

---

## 🚀 Getting Started
1. Clone this repo:
```bash
git clone https://github.com/your-username/tip-calculator.git
cd tip-calculator
```
2. Run the script:
```bash
python tip_calculator.py
```
3. Follow the prompts and let Python do the rest.

---
🧊 Cool Ideas for the Future
- Add default values if users press enter without input
- Convert to a GUI or web app
- Auto-calculate suggested tip ranges (15%, 18%, 20%)
- Handle different currencies

## 🙌 Contributing
Got a better way to split the bill? Found a bug?
Pull requests are welcome, just like friends who actually pay their share 🍕.

## 📄 License
MIT License — free to use, modify, and tip with 💸.

👨‍💻 Author
Made with ❤️ and some heavy math lifting by [RedHoodJT1988](https://github.com/RedHoodJT1988)

Bon appétit! 🥂