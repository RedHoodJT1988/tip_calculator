def validate_tip_inputs(total_bill, tip_percentage, num_people):
    if total_bill <= 0:
        raise ValueError('Total bill must be a positive number')
    if tip_percentage < 0:
        raise ValueError('Tip percentage cannot be negative')
    if num_people <= 0:
        raise ValueError('Number of people must be at least 1')

def calculate_tip(total_bill, tip_percentage=15, num_people=1):
    validate_tip_inputs(total_bill, tip_percentage, num_people)

    total_tip = total_bill * (tip_percentage / 100)
    total_amount = total_bill + total_tip

    amount_per_person = total_amount / num_people

    return {
        'total_tip': round(total_tip, 2),
        'total_amount': round(total_amount, 2),
        'amount_per_person': round(amount_per_person, 2)
    }

def main():
    try:
        total_bill = float(input("Enter the total bill amount: "))
        tip_percentage = float(input("Enter the tip percentage (default is 15%: "))
        num_people = int(input("Enter the number of people (default is 1): "))

        result = calculate_tip(total_bill, tip_percentage, num_people)

        print("Tip calculation result")
        print(f'Total Tip: ${result['total_tip']}')
        print(f'Total Amount: {result["total_amount"]}')
        print(f'Amount per Person: {result["amount_per_person"]}')
    except ValueError as e:
        print(f"Error: {e}")

main()
