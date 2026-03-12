import re

def is_valid_corporate_email(email: str) -> bool:
    """
    Valida un correo electrónico corporativo asegurando una estructura correcta 
    y bloqueando dominios genéricos conocidos.

    Args:
        email (str): La dirección de correo electrónico a validar.

    Returns:
        bool: True si el correo tiene formato corporativo válido, False en caso contrario.
    """
    # Lista de dominios genéricos a rechazar (se asume que un corporativo no los usa)
    generic_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com"]
    
    # Expresión regular para validar el formato del correo
    # Requiere un nombre de usuario, seguido de '@', seguido de un dominio con al menos un punto
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if not re.match(pattern, email):
        return False
        
    domain = email.split('@')[1].lower()
    
    if domain in generic_domains:
        return False
        
    return True

if __name__ == "__main__":
    # Pruebas de correos válidos (corporativos)
    print("Testing Valid Corporate Emails:")
    print("1. carlos.ceo@empresa.com ->", is_valid_corporate_email("carlos.ceo@empresa.com"))
    print("2. jsmith@startup-dev.io ->", is_valid_corporate_email("jsmith@startup-dev.io"))
    
    print("\nTesting Invalid / Generic Emails:")
    # Pruebas de correos genéricos
    print("3. carlos@gmail.com ->", is_valid_corporate_email("carlos@gmail.com"))
    print("4. jsmith@outlook.com ->", is_valid_corporate_email("jsmith@outlook.com"))
    
    # Pruebas de correos mal formados
    print("5. carlos.ceo_empresa.com ->", is_valid_corporate_email("carlos.ceo_empresa.com"))
    print("6. jsmith@startup ->", is_valid_corporate_email("jsmith@startup"))