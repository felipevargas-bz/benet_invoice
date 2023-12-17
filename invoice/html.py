bill_rows = """
<tr>
    <td>
        <p>{description}</p>
    </td>
    <td>
        <p>{amount}</p>
    </td>
    <td>
        <p>{unit_price}</p>
    </td>
    <td>
        <p>{total}</p>
    </td>
</tr>
"""

empty_tr = """
<tr>
    <td>
    <p></p>
    </td>
    <td>
    <p></p>
    </td>
    <td>
    <p></p>
    </td>
    <td>
    <p>-</p>
    </td>
</tr>
"""
bill_to = """
<ul>
    <li>
        <p>Nombre: {name}</p>
</li>
    <li>
        <p>Barrio: {neighborhood}</p>
</li>
    <li>
        <p>Código Cliente: {code}</p>
</li>
    <li>
        <p>Teléfono: {phone}</p>
</li>
    <li>
        <p>Email: {email}</p>
</li>
</ul>
"""

html_body = """
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Factura</title>
</head>

<body>
  <main>
    <div>
      <section class="upper_fact">
        <div class="info_head">
          <p>RED BENED</p>
          <h2>Factura</h2>
        </div>
        <div>
          <div>
            <p class="bold">Barrio: Brisas</p>
          </div>
          <div class="column_fix">
            <p class="bold">Teléfono: 318 3778035</p>
            <div class="row_fix">
              <div class="w50">
                <p class="header_decoration">Número de Factura</p>
                <p class="bold">{invoice_number}</p>
              </div>
              <div class="w50">
                <p class="header_decoration">Fecha</p>
                <p class="bold">{invoice_date}</p>
              </div>
            </div>
          </div>
        </div>
        <div class="column_fix" style="margin-top: 2rem;">
          <div class="">
            <p class="header_decoration">Facturar A</p>
            {bill_to}
          </div>
          <div class="row_fix w50">
            <div class="w50">
              <p class="header_decoration">ID. del Cliente</p>
              <p class="bold">564</p>
            </div>
            <div class="w50">
              <p class="header_decoration">Términos</p>
              <p class="bold">Pago contra entrega</p>
            </div>
          </div>
        </div>
      </section>
      <section>
        <table>
          <thead>
            <tr>
              <th width="50%">Descripción</th>
              <th>Cant.</th>
              <th>Precio Unitario</th>
              <th width="25%">Importe</th>
            </tr>
          </thead>
          <tbody>
            {table}
          </tbody>
          <tfoot>
            <tr>
              <td rowspan="4">
                <div class="met_pay_box">
                  <div>
                    <h6>Métodos de Pago:</h6>
                    <ul>
                      <li>
                        {logo_bamcolombia}
                        <p>Cuenta de Ahorros: #<span id="banclmb">919876 04 88</span></p></li>
                      <li>
                          {logo_nequi}
                        <p>Nequi: <span id="nequi">312 438 76 55</span></p></li>
                    </ul>
                  </div>
                  <div class="qr">
                    {qr}
                  </div>
                </div>
              </td>
              <td colspan="2">
                  SubTotal
              </td>
              <td>
                525,00
              </td>
            </tr>
            <tr>
              <td colspan="2">
                  Tipo Impositivo
              </td>
              <td>
                4,250%
              </td>
            </tr>
            <tr>
              <td colspan="2">
                  Impuestos
              </td>
              <td>
                525,00
              </td>
            </tr>
            <tr>
              <td colspan="2">
                  <b>Total</b>
              </td>
              <td>
                <b>547,31€</b>
              </td>
            </tr>
          </tfoot>
        </table>
      </section>
    </div>
  </main>
</body>

</html>
"""
