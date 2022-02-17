import PyPDF2

arquivo = open('teste.pdf', 'rb')
print(arquivo)

lerPDF = PyPDF2.PdfFileReader(arquivo)
print(lerPDF)

numero_de_pagina = lerPDF.getNumPages()
print(numero_de_pagina)

pagina = lerPDF.getPage(0)
print(pagina)

conteudo = pagina.extractText()
print(conteudo)