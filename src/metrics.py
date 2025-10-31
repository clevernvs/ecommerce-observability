from prometheus_client import Counter

cart_addition_total = Counter (
    'ecommerce_cart_addition_total',
    'Total de adicões ao carrinho por produto.',
    ['product_id']
)

errors_total = Counter(
    'ecommerce_cart_errors_total',
    'Total de erros.',
    ['error_type', 'endpoint', 'status_code']
)