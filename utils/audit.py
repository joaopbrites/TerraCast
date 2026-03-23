from pathlib import Path
import json
from datetime import datetime


#configura arquivo separado para gravação dos arquivos que serão processados
def audit(product_list, SINGLE_PRODUCT_NAME = None):
    # Preparação diretório
    caminho_arquivo = Path(__file__).resolve().parent.parent / "logs" / "files" 
    caminho_arquivo.mkdir(parents=True, exist_ok=True)

    # single_product para debug 
    # product_result para retornar apenas os que produtos que serão processados ou seja os que estão ativos
    number_of_prods = 0
    product_result = []


    #with open(caminho_arquivo / "audit_products.json", 'w', encoding='utf-8') as f:
    for product in product_list:
        if SINGLE_PRODUCT_NAME != None:
            if product['name'] == SINGLE_PRODUCT_NAME:
                product['enabled'] = True
            else:
                product['enabled'] = False
        if product['enabled']:
            product_result.append(product)
            number_of_prods += 1
            # Cria dict com as 3 variáveis + timestamp
            audit_entry = {
                "timestamp": datetime.now().strftime('%d %b %Y, %H:%M'),
                "name": product['name'],
                "script": product['script'],
                "pattern": product['input'] + product['filename pattern']
            }
                # Grava uma linha JSON por produto (JSONL)
                #json.dump(audit_entry, f, ensure_ascii=False, indent=4)
                #f.write('\n')

    return product_result, number_of_prods


if __name__ == "__main__":
    audit(product_list, SINGLE_PRODUCT_NAME)
