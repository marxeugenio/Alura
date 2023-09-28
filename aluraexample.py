import openpyxl

# Cria uma nova planilha
wb = openpyxl.Workbook()

# Seleciona a planilha ativa
sheet = wb.active

# Adiciona dados a algumas células
sheet['A1'] = 'Nome'
sheet['B1'] = 'Idade'

sheet['A2'] = 'Alice'
sheet['B2'] = 30

sheet['A3'] = 'Bob'
sheet['B3'] = 25

sheet['A4'] = 'Charlie'
sheet['B4'] = 35

# Salva o arquivo Excel
wb.save('exemplo.xlsx')
