from prometheus_client import Counter, Gauge

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

active_sessions_gauge = Gauge(
    'ecommerce_active_sessions',
    'Número atual de sessões com carrinho ativo'
)

cpu_usage_gauge = Gauge(
    'ecommerce_cpu_usage_percent',
    'Percentual atual de uso de CPU do sistema'
)

def update_cpu_usage():
    try:
        cpu_percent = psutil.cpu_percent()
        cpu_usage_gauge.set(cpu_percent)
        print(f"CPU atualizada: {cup_percent}%")
    except Exception as e:
        print(f"Erro ao atualizar CPU: {e}")

def update_active_sessions():
    try:
        from models.order import Order
        active_count = Order.query.filter_by(is_open=True).count()
        active_sessions_gauge.set(active_count)
        print(f"Sessões ativas atualizadas: {active_count}")
    except Exception as e:
        print(f"Erro ao atualizar sessões ativas: {e}")