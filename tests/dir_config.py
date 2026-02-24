#!/usr/bin/env python3
"""
Script de teste para validar refatoração do Config/

Testa se products-list.py e processing-products.py funcionam
sem modificar showcast_start.py ainda.
"""

"""Rode python test_refactoring.py para testar na pagina de testes"""

import sys
import yaml
from pathlib import Path

# Adiciona o diretório raiz do projeto ao PYTHONPATH
project_root = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(project_root))

from products import products_list
from products import processing_products as processing



def test_products_list():
    """Testa se consegue listar produtos."""
    print("=" * 70)
    print("TESTE 1: Importar e listar produtos")
    print("=" * 70)
    
    try:
        Products = products_list.Products
        
        # Load configproducts_list.Products
        showcast_file = project_root / 'showcast.yml'
        with open(showcast_file, 'r') as f:
            CONFIG = yaml.safe_load(f)
        CONFIG['srcDir'] = str(Path(__file__).parent.absolute()) + '/'
        # Get products
        produtos = Products(CONFIG)
        
        print(f"✅ Importação bem-sucedida!")
        print(f"✅ Total de produtos: {len(produtos)}")
        
        # Show first 3
        print(f"\nPrimeiros 3 produtos:")
        for p in produtos[:3]:
            enabled = "✅" if p.get('enabled') else "❌"
            print(f"  {enabled} {p['name']}")
        
        # Count enabled
        enabled_count = sum(1 for p in produtos if p.get('enabled'))
        print(f"\n✅ Produtos habilitados: {enabled_count}/{len(produtos)}")
        
        return True, produtos, CONFIG
        
    except Exception as e:
        print(f"❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
        return False, None, None


def test_processing():
    """Testa se consegue processar (sem executar de verdade)."""
    print("\n" + "=" * 70)
    print("TESTE 2: Importar módulo de processamento")
    print("=" * 70)
    
    try:
        ProcessProduct = processing.ProcessProduct
        
        print(f"✅ Módulo importado com sucesso!")
        print(f"✅ Função ProcessProduct disponível: {callable(ProcessProduct)}")
        
        # Don't actually process, just check if function exists
        return True
        
    except Exception as e:
        print(f"❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_config_wrapper():
    """Testa se config.py ainda funciona como wrapper."""
    print("\n" + "=" * 70)
    print("TESTE 3: Compatibilidade com config.py (se existir wrapper)")
    print("=" * 70)
    
    try:
        import config
        
        if hasattr(config, 'Products'):
            print("✅ config.Products existe")
        else:
            print("⚠️  config.Products não existe (esperado se não fez wrapper ainda)")
            
        if hasattr(config, 'ProcessProduct'):
            print("✅ config.ProcessProduct existe")
        else:
            print("⚠️  config.ProcessProduct não existe (esperado se não fez wrapper ainda)")
        
        return True
        
    except Exception as e:
        print(f"ℹ️  config.py não testado: {e}")
        return True  # Not an error


if __name__ == '__main__':
    print("\n🧪 TESTES DE VALIDAÇÃO - Refatoração Config/\n")
    
    # Test 1: Products list
    success1, produtos, CONFIG = test_products_list()
    
    # Test 2: Processing
    success2 = test_processing()
    
    # Test 3: Wrapper (optional)
    success3 = test_config_wrapper()
    
    # Summary
    print("\n" + "=" * 70)
    print("RESUMO")
    print("=" * 70)
    
    tests = [
        ("Listagem de produtos", success1),
        ("Módulo de processamento", success2),
        ("Wrapper config.py", success3),
    ]
    
    for name, success in tests:
        status = "✅ PASSOU" if success else "❌ FALHOU"
        print(f"{name}: {status}")
    
    all_passed = all(s for _, s in tests[:2])  # Only first 2 are critical
    
    if all_passed:
        print("\n✅ TODOS OS TESTES CRÍTICOS PASSARAM!")
        print("Você pode prosseguir com confiança.")
    else:
        print("\n❌ ALGUNS TESTES FALHARAM!")
        print("Revise os erros acima antes de continuar.")
    
    sys.exit(0 if all_passed else 1)
