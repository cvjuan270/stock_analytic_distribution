# stock analytic distribution

- Itera sobre cada línea de movimiento de stock.
- Verifica si el destino del albarán está en la lista USAGES (actualmente solo "inventory [Perdida de Inventario - Consumos]").
- Si se cumple la condición anterior:

  - Intenta obtener la cuenta analítica de gastos asociada al producto.
  - Si existe una cuenta analítica de gastos:
    Asigna una distribución del 100% a esta cuenta.
  - Si no existe una cuenta analítica de gastos:
    Utiliza el modelo account.analytic.distribution.model para obtener una distribución basada en varios criterios (producto, categoría de producto, socio, categoría de socio y compañía).
    Asigna la distribución calculada a line.analytic_distribution, manteniendo la distribución existente si no se calcula una nueva.

  # Dependencias

  Este módulo depende de dos módulos de la OCA (Odoo Community Association) https://github.com/OCA/account-analytic:

  - product_analytic: Proporciona funcionalidades para la gestión analítica a nivel de producto.
  - stock_analytic: Ofrece capacidades de análisis para operaciones de inventario.
