import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_csv(data, filename):
    """Generate a CSV report from the provided data."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    return f"CSV report generated: {filename}"

def generate_pdf(data, filename):
    """Generate a PDF report from the provided data."""
    pdf = canvas.Canvas(filename, pagesize=letter)
    pdf.setFont("Helvetica", 12)

    y_position = 750  # Starting position for text
    for key, value in data.items():
        pdf.drawString(100, y_position, f"{key}: {value}")
        y_position -= 20  # Move down for the next line

    pdf.save()
    return f"PDF report generated: {filename}"

# Example usage
if __name__ == "__main__":
    sample_data = {
        "IP Address": "192.168.1.1",
        "Hostname": "example-host",
        "Status": "Active"
    }
    print(generate_csv([sample_data], "report.csv"))
    print(generate_pdf(sample_data, "report.pdf"))
