import random
from main. redis import redis_client

def save_code(user_id: int) -> str:
    """
    Генерирует и сохраняет 6-значный код подтверждения в Redis
    
    Args: 
        user_id: ID пользователя
    
    Returns:
        str:  Сгенерированный код (6 цифр)
    """
    code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    
    key = f"confirm_code:{user_id}"
    
    redis_client.setex(key, 300, code)
    
    return code


def verify_code(user_id: int, code: str) -> bool:
    """
    Проверяет код подтверждения и удаляет его при успехе
    
    Args:  
        user_id: ID пользователя
        code:  Код для проверки
    
    Returns:  
        bool: True если код верный, False если нет
    """
    key = f"confirm_code:{user_id}"
    
    saved_code = redis_client.get(key)
    
    if saved_code is None:
        return False
    
    if isinstance(saved_code, bytes):
        saved_code = saved_code.decode('utf-8')
    
    if saved_code == code:
        redis_client.delete(key)
        return True
    
    return False