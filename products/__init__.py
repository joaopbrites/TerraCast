"""
Config Package - Modularização do sistema de configuração TerraCast

Este pacote contém:
- products_list: Define todos os produtos disponíveis
- processing_products: Lógica de processamento de produtos
"""

from .products_list import products
from .product_processor import process_product

__all__ = ['products', 'process_product']
