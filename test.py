def calculate_total(items):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    discounts = {'A': (3, 130), 'B': (2, 45)}
    
    item_counts = {}
    for item in items:
        item_counts[item] = item_counts.get(item, 0) + 1
    
    total = 0
    for item, count in item_counts.items():
        if item in discounts:
            special_qty, special_price = discounts[item]
            total += (count // special_qty) * special_price + (count % special_qty) * prices[item]
        else:
            total += count * prices[item]
    
    return total
    
# Given inputs to check the result
inputs = ["", "A", "AB", "CDBA", "AA", "AAA", "AAAA", "AAAAA", "AAAAAA", "AAAB", "AAABB", "AAABBD", "DABABA"]

for test_input in inputs:
    print(f'Input: "{test_input}" -> Output: {calculate_total(test_input)}')