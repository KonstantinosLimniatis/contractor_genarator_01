import pypandoc

input_docx = "contract_filled.docx"
output_pdf = "contract_filled.pdf"

pypandoc.convert_file(
    input_docx,
    "pdf",
    outputfile=output_pdf,
    extra_args=["--pdf-engine=xelatex"]
)

print("OK: δημιουργήθηκε το contract_filled.pdf")
