def initSocre():
    MD5 = "0"
    SHA1 = "0"
    SHA2 = "0"
    SHA3 = "0"
    BLAKE2 = "0"
    url_score = MD5 + "-" + SHA1 + "-" + SHA2 + "-" + SHA3 + "-" + BLAKE2
    return url_score

def addScore(url_score, new_score):
    old_md5, old_sha1, old_sha2, old_sha3, old_blake2 = getSocresfromUrl(url_score)
    new_md5, new_sha1, new_sha2, new_sha3, new_blake2 = getSocresfromUrl(new_score)
    MD5 = str(int(old_md5) + int(new_md5))
    SHA1 = str(int(old_sha1) + int(new_sha1))
    SHA2 = str(int(old_sha2) + int(new_sha2))
    SHA3 = str(int(old_sha3) + int(new_sha3))
    BLAKE2 = str(int(old_blake2) + int(new_blake2))
    return MD5 + "-" + SHA1 + "-" + SHA2 + "-" + SHA3 + "-" + BLAKE2

def getSocresfromUrl(url_score):
    MD5, SHA1, SHA2, SHA3, BLAKE2 = url_score.split('-')
    return MD5, SHA1, SHA2, SHA3, BLAKE2