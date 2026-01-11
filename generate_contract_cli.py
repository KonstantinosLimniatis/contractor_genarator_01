from docxtpl import DocxTemplate
from datetime import datetime
import pypandoc


# =========================
# VALIDATORS
# =========================

def not_empty(value: str) -> bool:
    return len(value.strip()) > 0


def is_positive_int(value: str) -> bool:
    return value.isdigit() and int(value) > 0


def is_date(value: str) -> bool:
    datetime.strptime(value, "%d/%m/%Y")
    return True


def is_afm(value: str) -> bool:
    return value.isdigit() and len(value) == 9


# =========================
# INPUT HANDLER
# =========================

def ask(prompt, validator=None, error_msg="Λάθος τιμή"):
    while True:
        value = input(f"{prompt}: ").strip()
        if validator is None:
            return value
        try:
            if validator(value):
                return value
        except Exception:
            pass
        print(f"❌ {error_msg}")


# =========================
# PDF GENERATION
# =========================

def convert_to_pdf(docx_file: str, pdf_file: str):
    pypandoc.convert_file(
        docx_file,
        "pdf",
        outputfile=pdf_file,
        extra_args=["--pdf-engine=xelatex"]
    )


# =========================
# MAIN PROGRAM
# =========================

def main():
    print("\n📄 Δημιουργία Σύμβασης Παροχής Διδακτικού Έργου\n")

    doc = DocxTemplate("template.docx")

    context = {
        # Γενικά
        "imerominia": ask(
            "Ημερομηνία σύμβασης (DD/MM/YYYY)",
            is_date,
            "Χρησιμοποίησε μορφή DD/MM/YYYY"
        ),

        # Διευθυντής ΠΜΣ
        "onoma_diefthynti_pms": ask("Όνομα Διευθυντή ΠΜΣ", not_empty),
        "titlos_pms": ask("Τίτλος ΠΜΣ", not_empty),
        "kodikos_pms": ask("Κωδικός ΠΜΣ", not_empty),
        "katoikia_diefthynti": ask("Κατοικία Διευθυντή ΠΜΣ", not_empty),
        "odos_diefthynti": ask("Οδός Διευθυντή ΠΜΣ", not_empty),
        "arithmos_diefthynti": ask("Αριθμός οδού", is_positive_int),
        "tk_diefthynti": ask("Τ.Κ.", is_positive_int),
        "adt_diefthynti": ask("Αριθμός ΑΔΤ", not_empty),
        "afm_diefthynti": ask(
            "ΑΦΜ Διευθυντή ΠΜΣ",
            is_afm,
            "Το ΑΦΜ πρέπει να αποτελείται από 9 ψηφία"
        ),
        "doy_diefthynti": ask("ΔΟΥ Διευθυντή ΠΜΣ", not_empty),

        # Διδάσκων
        "onoma_didaskontos": ask("Όνομα Διδάσκοντα", not_empty),
        "idiotita_didaskontos": ask("Ιδιότητα Διδάσκοντα", not_empty),
        "katoikia_didaskontos": ask("Κατοικία Διδάσκοντα", not_empty),
        "odos_didaskontos": ask("Οδός Διδάσκοντα", not_empty),
        "arithmos_didaskontos": ask("Αριθμός οδού", is_positive_int),
        "tk_didaskontos": ask("Τ.Κ.", is_positive_int),
        "adt_didaskontos": ask("Αριθμός ΑΔΤ", not_empty),
        "afm_didaskontos": ask(
            "ΑΦΜ Διδάσκοντα",
            is_afm,
            "Το ΑΦΜ πρέπει να αποτελείται από 9 ψηφία"
        ),
        "doy_didaskontos": ask("ΔΟΥ Διδάσκοντα", not_empty),

        # Απόφαση
        "arithmos_synedriasis": ask("Αριθμός συνεδρίασης", is_positive_int),
        "imerominia_synedriasis": ask(
            "Ημερομηνία συνεδρίασης (DD/MM/YYYY)",
            is_date
        ),
        "ada_apofasis": ask("ΑΔΑ Απόφασης", not_empty),

        # Έργο
        "mathimata": ask("Μάθημα/τα", not_empty),
        "ores_didaskalias": ask("Ώρες διδασκαλίας", is_positive_int),
        "poso_amoivis": ask("Ποσό αμοιβής (ολογράφως)", not_empty),
        "poso_amoivis_arithmos": ask("Ποσό αμοιβής (€)", is_positive_int),

        # Διάρκεια
        "examino": ask("Εξάμηνο (χειμερινού / εαρινού)", not_empty),
        "akadimaiko_etos": ask("Ακαδημαϊκό έτος", not_empty),
        "imerominia_enarxis": ask(
            "Ημερομηνία έναρξης (DD/MM/YYYY)",
            is_date
        ),
        "imerominia_lixis": ask(
            "Ημερομηνία λήξης (DD/MM/YYYY)",
            is_date
        ),
    }

    # =========================
    # UNIQUE FILENAMES
    # =========================

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = context["onoma_didaskontos"].replace(" ", "_")

    docx_filename = f"contract_{timestamp}_{safe_name}.docx"
    pdf_filename = f"contract_{timestamp}_{safe_name}.pdf"

    # =========================
    # GENERATION
    # =========================

    doc.render(context)
    doc.save(docx_filename)

    convert_to_pdf(docx_filename, pdf_filename)

    print("\n✅ Η σύμβαση δημιουργήθηκε επιτυχώς!")
    print(f"📄 DOCX: {docx_filename}")
    print(f"📄 PDF : {pdf_filename}\n")


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":
    main()
