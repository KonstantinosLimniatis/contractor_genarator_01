from docxtpl import DocxTemplate
import os
import shutil
import subprocess


def convert_to_pdf(docx_file: str, pdf_file: str):
    if shutil.which("libreoffice") is None:
        raise RuntimeError("Δεν βρέθηκε το libreoffice στο PATH")

    output_dir = os.path.dirname(pdf_file) or "."
    os.makedirs(output_dir, exist_ok=True)

    subprocess.run(
        [
            "libreoffice",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            output_dir,
            docx_file,
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    expected_pdf = os.path.join(
        output_dir,
        os.path.splitext(os.path.basename(docx_file))[0] + ".pdf",
    )
    if expected_pdf != pdf_file and os.path.exists(expected_pdf):
        os.replace(expected_pdf, pdf_file)

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

output_dir = "contracts"
os.makedirs(output_dir, exist_ok=True)

doc.render(context)

docx_filename = os.path.join(output_dir, "contract_filled.docx")
pdf_filename = os.path.join(output_dir, "contract_filled.pdf")

doc.save(docx_filename)
convert_to_pdf(docx_filename, pdf_filename)

print("OK: δημιουργήθηκε πλήρως συμπληρωμένη σύμβαση")
print(f"OK: δημιουργήθηκε το {pdf_filename}")
