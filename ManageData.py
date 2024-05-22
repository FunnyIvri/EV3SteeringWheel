from typing import List
def EncryptData(data) -> bytes:
    data = str(data)
    return data.encode('utf-8')
def DecryptData(EncryptedData : bytes) -> List[float]:
    data = EncryptedData.decode('utf-8').split(' ')
    for i,x in enumerate(data):
        if x != 'q': data[i] = float(x) 
    return data
    