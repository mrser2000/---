from allure import step as allure_step

def step(description: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with allure_step(description):
                return func(*args, **kwargs)
        return wrapper
    return decorator