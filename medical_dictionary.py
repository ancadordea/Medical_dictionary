import pandas as pd
df = pd.read_csv("medical_terms.csv")

while True:
    term = input("Enter a medical term: ").lower()
    result = df[df['Term'] == term]
    if result.empty:
        print("Sorry, this term is not available")
    
    for element in result["Definition"]:
        print(element)
    
   