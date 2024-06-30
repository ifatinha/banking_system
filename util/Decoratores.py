from datetime import datetime


def log_operations(type_operation):
    def log_decorator(operation):
    
        def wrapper(*args, **kwargs):
        
            print(f"=== Tipo de transação: {type_operation} ===")
            operation(*args, **kwargs)
            print(f"=== Realizado em {datetime.now().strftime("%d/%m/%Y %H:%M")} ===")

        return wrapper
    return log_decorator

