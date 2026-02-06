import os
import shutil
import subprocess

output_dir = "contracts"
input_docx = os.path.join(output_dir, "contract_filled.docx")
output_pdf = os.path.join(output_dir, "contract_filled.pdf")

if shutil.which("libreoffice") is None:
    raise RuntimeError("Δεν βρέθηκε το libreoffice στο PATH")

os.makedirs(output_dir, exist_ok=True)

subprocess.run(
    [
        "libreoffice",
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        output_dir,
        input_docx,
    ],
    check=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

expected_pdf = os.path.join(
    output_dir,
    os.path.splitext(os.path.basename(input_docx))[0] + ".pdf",
)
if expected_pdf != output_pdf and os.path.exists(expected_pdf):
    os.replace(expected_pdf, output_pdf)

print("OK: δημιουργήθηκε το contract_filled.pdf")
