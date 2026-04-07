import base64

def base16(text: str) -> str:
    return base64.b16encode(text.encode()).decode()

def base32(text: str) -> str:
    return base64.b32encode(text.encode()).decode()

def base64_encode(text: str) -> str:
    return base64.b64encode(text.encode()).decode()

def base64_decode(text: str) -> str:
    return base64.b64decode(text.encode()).decode()
