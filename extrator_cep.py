endereco = "Rua Flores 72, apartamento 1002, Laranjeiras, Rio, RJ, 222392-2390"
import re
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)