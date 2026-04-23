"""
Config Package - Modularização do sistema de configuração TerraCast

Este pacote contém:
- products_list: Define todos os produtos disponíveis
- processing_products: Lógica de processamento de produtos
"""

from .products_list import products

__all__ = ['products']
