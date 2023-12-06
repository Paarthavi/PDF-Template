from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics_pdf.csv")

for index, row in df.iterrows():
	pdf.add_page()

	pdf.set_font(family="Times", style="B", size=24)
	# Defines the colour used for text. It can be expressed in RGB components or grayscale.
	pdf.set_text_color(100, 100, 100)
	pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
	pdf.line(10, 21, 200, 21)

pdf.output("output.pdf")