#concatenar string
sumar_string = ('thirty ', 'day ', 'of ','python')
result = ''.join(sumar_string)
print(result)
concatenar_string = ('coding ', 'for ', 'all')
result = ''.join(concatenar_string)
print(result)
#declarando una variable inicial y con valor "Coding for all"
company = 'Coding for all'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize(), company.title(), company.swapcase())
print(company[6:14]) #borro la primer palabra
print(company.find('Coding'))
print(company.index('Coding'))
print(company.rindex('Coding'))
print(company.replace('Coding','Python'))
titulo = 'Python for everyone'
print(titulo)
titulo_02 = 'Python for all'
print(titulo.replace(titulo, titulo_02))
print(titulo.split())
marcas = 'facebook, Google , Microsoft, Apple, IBM, Oracle, Amazon'
print(marcas.split())
print(company[0])
print(company[-1])
print(company[10])
print(company[0:14:7])
print(titulo[0:3])
print(company.count('C'))
print(company.count('f'))
print(company.rfind('f'))
sentencia = 'You cannot end a sentence with because because because is a conjunction'
print(sentencia.find('because'))
print(len(sentencia))
print(sentencia.find('because'))#31
print(sentencia.rfind('se'))#52
print(sentencia[31:55])
