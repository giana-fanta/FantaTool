import pandas as pd
import json
import math

# Usa il nome corretto del file
FILE_EXCEL = 'Fanta_2627 (2).xlsx'

def clean_nan(val, default=""):
    if isinstance(val, float) and math.isnan(val):
        return default
    return val

def main():
    print("Lettura del file Excel in corso...")
    xls = pd.ExcelFile(FILE_EXCEL)
    
    dati = {
        "giocatori": [],
        "extra": [],
        "config": {
            "budget_iniziale": 500,
            "slot_ruoli": {"P": 3, "D": 8, "C": 8, "A": 6}
        }
    }
    
    # 1. Estrazione Giocatori (Fogli P, D, C, A)
    for ruolo in ['P', 'D', 'C', 'A']:
        df = pd.read_excel(xls, sheet_name=ruolo)
        for _, row in df.iterrows():
            if pd.isna(row.get('NOME')): 
                continue
            
            dati["giocatori"].append({
                "nome": clean_nan(row.get('NOME')),
                "ruolo": ruolo,
                "cat": clean_nan(row.get('CAT')),
                "max": float(clean_nan(row.get('MAX'), 0)),
                "stato": "L", # Tutti liberi di default
                "costo_reale": 0,
                "note": clean_nan(row.get('NOTE'))
            })
            
    # 2. Estrazione Extra
    if 'Extra' in xls.sheet_names:
        df_extra = pd.read_excel(xls, sheet_name='Extra')
        for _, row in df_extra.iterrows():
            dati["extra"].append({
                "ruolo": clean_nan(row.get('Ruolo')),
                "costo": float(clean_nan(row.get('Crediti', 0))),
                "descrizione": "Acquisto Extra"
            })
    
    # Salvataggio JSON
    with open('dati.json', 'w', encoding='utf-8') as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)
        
    print("Database 'dati.json' generato con successo! Pronto per GitHub.")

if __name__ == "__main__":
    main()
