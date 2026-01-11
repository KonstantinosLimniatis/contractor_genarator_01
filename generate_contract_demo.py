from docxtpl import DocxTemplate

doc = DocxTemplate("template.docx")

context = {
    # Γενικά
    "imerominia": "10/01/2026",

    # Διευθυντής ΠΜΣ
    "onoma_diefthynti_pms": "Ιωάννης Παπαδόπουλος",
    "titlos_pms": "Πληροφορική και Τηλεπικοινωνίες",
    "kodikos_pms": "ΠΜΣ-ICT-01",
    "katoikia_diefthynti": "Αθήνα",
    "odos_diefthynti": "Πατησίων",
    "arithmos_diefthynti": "76",
    "tk_diefthynti": "10434",
    "adt_diefthynti": "ΑΒ123456",
    "afm_diefthynti": "012345678",
    "doy_diefthynti": "Αθηνών",

    # Διδάσκων
    "onoma_didaskontos": "Γεώργιος Κωνσταντίνου",
    "idiotita_didaskontos": "Επίκουρος Καθηγητής",
    "katoikia_didaskontos": "Πειραιάς",
    "odos_didaskontos": "Ηρώων Πολυτεχνείου",
    "arithmos_didaskontos": "15",
    "tk_didaskontos": "18532",
    "adt_didaskontos": "ΧΥ654321",
    "afm_didaskontos": "987654321",
    "doy_didaskontos": "Πειραιά",

    # Απόφαση Επιτροπής
    "arithmos_synedriasis": "12",
    "imerominia_synedriasis": "05/01/2026",
    "ada_apofasis": "ΨΞΩ123ΑΒΓ",

    # Έργο / Αντικείμενο
    "mathimata": "Βάσεις Δεδομένων",
    "ores_didaskalias": "40",
    "poso_amoivis": "τέσσερις χιλιάδες",
    "poso_amoivis_arithmos": "4000",

    # Χρονικό διάστημα
    "examino": "χειμερινού",
    "akadimaiko_etos": "2025–2026",
    "imerominia_enarxis": "01/10/2025",
    "imerominia_lixis": "31/01/2026",
}

doc.render(context)
doc.save("contract_filled.docx")

print("OK: δημιουργήθηκε πλήρως συμπληρωμένη σύμβαση")
