from datetime import datetime
import pandas as pd
from weasyprint import HTML, CSS
from invoice.svg_images import logo_bamcolombia, logo_nequi, qr
from invoice.styles import styles_css
from invoice.html import bill_rows, empty_tr, bill_to, html_body
from datetime import datetime


def read_excel():
    excel_file = 'datos_facturas.xlsx'
    df = pd.read_excel(excel_file)

    return df


def create_pdf(html_content, output_file):
    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Factura</title>
    <link rel="stylesheet" href="./styles.css">
</head>
<body>
    <div class="container">
        <div class="bill_to">
            <div class="line"></div>
            <div>
                <h2>RED BENET</h2>
                <p>Parque Infantil</p>
                <p>Corregimiento San José de Mulatos</p>
                <p>323 866 88 68 WhatsApp</p>
            </div>
        </div>
        <div class="description">
            <h2>FACTURA</h2>
            <p>Fecha: 2020-10-10</p>
            
        </div>
        <div class="items">

        </div>
        <div class="payment">

        </div>
        <div class="warning">
        </div>
    </div>
</body>
</html>
    """
    styles = """
    body,
html {
    margin: 0;
    padding: 0;
}

.container {
    position: relative;
    border: 1px solid #000;
    width: 100%;
    height: 100%;
}

.bill_to,
.description {
    border: 1px solid #000;
    position: absolute;
    width: 100%;
    box-sizing: border-box;
}

.bill_to {
    height: 200px;
    top: 0px;
    left: 0px;
}

.description {
    background-color: red;
    height: 200px;
    top: 200px;
    left: 0px;
}

.items,
.payment,
.warning {
    border: 1px solid #000;
    position: absolute;
    width: 100%;
    box-sizing: border-box;
}

.items {
    background-color: green;
    top: 400px;
    left: 0px;
    height: 250px;
}

.payment {
    background-color: yellow;
    top: 650px;
    left: 0;
    height: 200px;
}

.warning {
    background-color: rgb(255, 80, 255);
    top: 850px;
    left: 0;
    height: 150px;
}
.line {
    background-color: rgb(27, 83, 156);
    position: absolute;
    width: 100%;
    height: 10px;
    box-sizing: border-box;
}
    """
    html = HTML(string=html_content)
    css = CSS(string=styles)
    pdf = html.write_pdf(stylesheets=[css])

    with open(output_file, 'wb') as pdf_file:
        pdf_file.write(pdf)


# Definir una función para generar facturas en PDF
def generar_factura(client_data):
    bill_to_data = client_data["bill_to_data"]
    bill_to_html = bill_to.format(
        name=bill_to_data["name"],
        neighborhood=bill_to_data["neighborhood"],
        code=bill_to_data["code"],
        phone=bill_to_data["phone"],
        email=bill_to_data["email"]
    )

    bill_rows_data = client_data["bill_rows_data"]
    bill_rows_html = ""

    for row in bill_rows_data:
        bill_rows_html += bill_rows.format(
            description=row["description"],
            amount=row["amount"],
            unit_price=row["unit_price"],
            total=row["total"]
        )
    bill_rows_html += empty_tr * (6 - len(bill_rows_data))

    invoice_html = html_body.format(
        invoice_number=client_data["invoice_number"],
        invoice_date=client_data["invoice_date"],
        bill_to=bill_to_html,
        table=bill_rows_html,
        logo_bamcolombia=logo_bamcolombia,
        logo_nequi=logo_nequi,
        qr=qr
    )
    output_file = f"./pdfs/{datetime.now().time()}.pdf"
    # Convertir el HTML de la factura a PDF usando WeasyPrint
    create_pdf(invoice_html, output_file)


if __name__ == "__main__":
    bill_to_data = {
        "name": "Juan Pérez",
        "neighborhood": "Centro",
        "code": "12345",
        "phone": "555-1234",
        "email": "juan@example.com"
    }
    bill_rows_data = [
        {
            "description": "Producto 1",
            "amount": 2,
            "unit_price": 10.00,
            "total": 20.00
        },
        {
            "description": "Producto 2",
            "amount": 1,
            "unit_price": 15.00,
            "total": 15.00
        },
        {
            "description": "Producto 3",
            "amount": 3,
            "unit_price": 5.00,
            "total": 15.00
        }
    ]
    client_data = {
        "bill_to_data": bill_to_data,
        "bill_rows_data": bill_rows_data,
        "invoice_number": "001",
        "invoice_date": datetime.now().date()
    }

    # generar_factura(client_data)
    create_pdf("", "./pdfs/test.pdf")
