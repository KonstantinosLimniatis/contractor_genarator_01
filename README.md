# Contract Generator

Σκοπός: αρχικά από το command line να μπορούμε να αντικαθιστούμε tags μέσα σε Word templates και να τα κάνουμε PDF. Σε πρώτη φάση χρησιμοποιούμε ένα template, αλλά θα υπάρχουν και άλλα.

## Απαιτήσεις
- Python 3
- LibreOffice (για μετατροπή σε PDF)

## Εγκατάσταση
1) Δημιούργησε/ενεργοποίησε virtual env.
2) Εγκατέστησε τις βιβλιοθήκες:
```bash
pip install docxtpl python-docx
```

## Εκτέλεση από το τερματικό
Βεβαιώσου ότι βρίσκεσαι στον φάκελο:
```bash
cd /home/konstantinos/contract_generator
```

### Demo (έτοιμα δεδομένα)
```bash
python generate_contract_demo.py
```
Παράγει:
- `contracts/contract_filled.docx`
- `contracts/contract_filled.pdf` (μέσω LibreOffice)

Μετατροπή σε PDF:
```bash
python to_pdf.py
```
Παράγει `contracts/contract_filled.pdf`.

### Κανονική χρήση (CLI ερωτήσεις)
```bash
python generate_contract_cli.py
```
Παράγει:
- `contracts/contract_<timestamp>_<name>.docx`
- `contracts/contract_<timestamp>_<name>.pdf`

## Templates
Το ενεργό template είναι το `template.docx`. Στη συνέχεια μπορούν να προστεθούν επιπλέον templates με αντίστοιχα πεδία.
