styles_css = """
:root{
    font-size: 16px;
}

*{
    font-family: Arial, Helvetica, sans-serif;
    margin: 0;
    padding: 0;
    border: 0;
    outline: 0;
    box-sizing: border-box;
}

body{
    padding-bottom: 1rem;
}

main{
    display: flex;
    justify-content: center;
    align-items: flex-start;
    min-height: 100vh;
    margin: 2rem auto 0;
}

main>div{
    max-width: 800px;
    display: block;
    width: 90%;
    margin: auto;
    box-shadow: 2px 2px 7px 1px rgba(194, 191, 191, 0.2);
    padding: 1rem;
}

h1, h2, h3, h4, h5, h6{
    font-family: Arial, Helvetica, sans-serif;
}

.w50{
    width: 50%;
    justify-content: initial !important;
}

.bold{
    font-weight: bold;
}

section.upper_fact{

}

section.upper_fact > div{
    position: relative;
}

section.upper_fact div.column_fix{
    justify-content: space-between;
    align-items: flex-start;
    display: flex;
}

section.upper_fact div.row_fix{
    border: 1px solid #000;
    width: 382px;
    height: 57px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
}

section.upper_fact div.row_fix > div{
    width: 50%;
    align-items: center;
    justify-content: center;
    text-align: center;
    display: flex;
    flex-direction: column;
}

section.upper_fact div ul li{
    text-decoration: none;
    list-style: none;
}

section.upper_fact div p{
    height: 28px;
    display: flex;
    align-items: center;
}

section table{
    width: 100%;
    border-collapse: collapse;
}

section table thead{
    text-align: center;
}

section table thead tr th{
    text-align: center;
    background-color: #2f75b5;
    color: white;
}

section table tbody tr{
    border-collapse: collapse;
}

section table tbody tr td{
    border: 1px solid #000;
    border-collapse: collapse;
}

section table tbody tr td:first-of-type{
    /* border-top: none; */
    border-left: none;
}

section table tbody tr:last-of-type td{
    /* border-top: none; */
    /* border-left: none; */
    border-bottom: none;
}

section table tbody tr td:last-of-type{
    border-right: none;
}

section table tbody tr td:nth-of-type(2){
    text-align: center;
    /* border-top: none; */
}

section table tbody tr:first-of-type td{
    border-top: none;
}

section table tbody tr td:nth-of-type(3), section table tbody tr td:nth-of-type(4){
    text-align: right;
    padding-right: 0.75rem;
    /* border-top: none; */
}

section table tfoot tr:first-of-type td{
    border-top: 2px solid #90b6d9;
}

section table tfoot tr:first-of-type td:nth-of-type(1){
    background-color: #ddebf7;
}

/* section table tfoot tr td:nth-of-type(1), section table tfoot tr td:nth-of-type(3){
    background-color: #ddebf7;
} */

/* section table tfoot tr td:nth-of-type(2){
    background-color: #bdd7ee;
    text-transform: uppercase;
    font-size: 0.8rem;
    padding: 0 10px;
    font-weight: 600;
} */

section table tfoot tr td:nth-of-type(2), section table tfoot tr td:nth-of-type(1):not(section table tfoot tr:first-of-type td:nth-of-type(1)), section table tfoot tr:first-of-type td:last-of-type{
    font-size: 0.8rem;
    padding: 0 10px;
}

section table tfoot tr:last-of-type td{
    font-size: 1rem !important;
}

section table tfoot tr:first-of-type td:nth-of-type(3), section table tfoot tr td:nth-of-type(2):not(section table tfoot tr:first-of-type td:nth-of-type(2)){
    text-align: right;
}

section table tfoot tr td:first-of-type{
    text-align: left;
}

section table tfoot tr:last-of-type td{
    font-size: 1rem;
}

section table tfoot tr:last-of-type td:nth-of-type(2){
    color: #0d3f6a;
}

footer{
    margin-top: 0.5rem;
    text-align: center;
    font-size: 0.75rem;
}

.header_decoration{
    border: 1px solid #000;
    background-color: #2f75b5;
    width: 100%;
    text-align: center;
    align-items: center;
    justify-content: center;
    color: white;
}

.info_head{
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.info_head p{
    color:#06376e;
    font-weight: 800;
    font-size: 1.2rem;
}

.info_head h2{
    color: #2770B2;
    font-size: 2.1rem;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.met_pay_box{

}

.met_pay_box h6{
    font-size: 1rem;
}

.met_pay_box{
    display: flex;
    justify-content: space-between;
    align-items: self-start;
}

.met_pay_box ul{
    gap: 0.5rem;
    display: flex;
    flex-direction: column;
    margin-top: 0.5rem;
}

.met_pay_box ul li{
    list-style: none;
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
}

.met_pay_box ul li svg{
    object-fit: contain;
    height: 15px;
    width: auto;
}

.met_pay_box ul li p{
    font-size: 0.7rem;
    font-style: italic;
}

.met_pay_box .qr{
    display: flex;
}

.met_pay_box .qr svg{
    object-fit: contain;
    height: 5.88rem;
    width: auto;
}
"""
