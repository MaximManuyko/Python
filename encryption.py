def encrypt(text):
    """
    Принимает на вход текст и возвращает его зашифрованную версию, в которой каждые два подряд идущих символа переставлены.
    """
    # Преобразуем строку в список символов для удобства манипуляций.
    chars = list(text)
    
    # Пройдемся по списку и будем переставлять каждые два подряд идущих символа.
    for i in range(0, len(chars)-1, 2):
        chars[i], chars[i+1] = chars[i+1], chars[i]
    
    # Склеим символы обратно в строку и вернем ее.
    return ''.join(chars)


print(encrypt("attack"), "taatkc")
print(encrypt("go!"), "og!")