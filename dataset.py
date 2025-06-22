import csv

# Define dictionaries to store information
disease_info = {}
antibiotic_info = {}

# Extract disease/symptom names and their uses
disease_info["Otitis externa (acute)"] = "Ear canal infection; Topical treatment with caution."
disease_info["Otitis media"] = "Middle ear infection; Antibiotics considered in specific cases."
disease_info["Pharyngitis"] = "Throat inflammation; Antibiotics for Streptococcus pyogenes in certain cases."
disease_info["Sinusitis - acute"] = "Acute sinus infection; Antibiotics for severe cases."

# Extract antibiotic/medicine information
antibiotic_info["Clioquinol + flumethasone (Locorten Vioform)*"] = {
    "Adult and Child > 2 years Dose": "2 to 3 drops, twice daily, for 7 days",
    "Uses": "Treatment for Otitis externa (acute)"
}

antibiotic_info["Dexamethasone + framycetin + gramicidin (Sofradex)*"] = {
    "Adult and Child Dose": "2 to 3 drops, three to four times daily, for 7 days",
    "Uses": "Treatment for Otitis externa (acute)"
}

antibiotic_info["Amoxicillin"] = {
    "Child Dose": "15 mg/kg/dose, three times daily, for five days (seven to ten days in specific cases)",
    "Uses": "First choice for Otitis media (child)"
}

antibiotic_info["Co-trimoxazole"] = {
    "Child Dose": "0.5 mL/kg/dose oral liquid, twice daily, for five to seven days (if child can swallow tablets)",
    "Uses": "Alternative for Otitis media (child)"
}

antibiotic_info["Phenoxymethylpenicillin (Penicillin V)"] = {
    "Child Dose (< 20 kg)": "250 mg, two or three times daily, for ten days",
    "Child Dose (2 ≥ 20 kg) and Adults": "500 mg, two or three times daily, for ten days",
    "Uses": "First choice for Pharyngitis"
}

antibiotic_info["Amoxicillin (Pharyngitis)"] = {
    "Child Dose (< 30 kg)": "750 mg, once daily, OR 25 mg/kg, twice daily (maximum 1000 mg/day), for ten days",
    "Child Dose (2 ≥ 30 kg) and Adults": "1000 mg, once daily, for ten days",
    "Uses": "Alternative for Pharyngitis"
}

antibiotic_info["Doxycycline"] = {
    "Adult and Child > 12 years Dose": "200 mg on day one, followed by 100 mg, once daily, on days two to seven",
    "Uses": "Alternative for Sinusitis (acute)"
}

antibiotic_info["Amoxicillin clavulanate"] = {
    "Child Dose": "10 mg/kg/dose (amoxicillin component), three times daily, for seven days",
    "Adult Dose": "500+125 mg three times daily for seven days",
    "Uses": "Alternative for Sinusitis (acute) if symptoms persist despite amoxicillin treatment"
}

# Create and write the dataset to a CSV file named "ENT_dataset.csv"
with open('ENT_dataset.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Disease', 'Description', 'Antibiotic', 'Child and Child > 2 years Dose', 'Uses']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write disease information rows
    for disease, description in disease_info.items():
        writer.writerow({
            'Disease': disease,
            'Description': description,
            'Antibiotic': '',
            'Child and Child > 2 years Dose': '',
            'Uses': ''
        })
    
    # Write antibiotic information rows
    for antibiotic, info in antibiotic_info.items():
        writer.writerow({
            'Disease': '',
            'Description': '',
            'Antibiotic': antibiotic,
            'Child and Child > 2 years Dose': info.get('Child and Child > 2 years Dose', ''),
            'Uses': info.get('Uses', '')
        })

print("ENT dataset has been created and saved as 'ENT_dataset.csv'.")
