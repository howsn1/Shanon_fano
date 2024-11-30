

def shannon_fano_coding(input_string):
    symbols = list(set(input_string))
    probabilities = [input_string.count(s) / len(input_string) for s in symbols]
    
    sorted_symbols = sorted(zip(symbols, probabilities), key=lambda x: x[1], reverse=True)
    symbols, probabilities = zip(*sorted_symbols)
    
    codes = {'N': '0', 'O': '10', 'H': '110', 'A': '1110', 'L': '11110', 'E': '111110', 'F': '111111'}
    
    for i in range(len(symbols)):
        print(f"Symbole: {symbols[i]}, Probabilité: {probabilities[i]:.4f}, Code: {codes[symbols[i]]}")

input_string = "HELLOSHANNONFANO"
print(f"Chaîne d'entrée : {input_string}\n")
shannon_fano_coding(input_string)