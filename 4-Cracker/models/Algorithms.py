
from passlib.hash import md5_crypt, sha256_crypt, sha512_crypt, bcrypt


class Algorithms:

    @staticmethod
    def verify_md5(user_hash, password, salt):
        generated_hash = md5_crypt.hash(password, salt=salt)
        return user_hash == generated_hash.split('$')[3]

    @staticmethod
    def verify_sha256(user_hash, password, salt, rounds=5000):
        generated_hash = sha256_crypt.hash(password, salt=salt, rounds=5000)
        return user_hash == generated_hash.split('$')[3]

    @staticmethod
    def verify_sha512(user_hash, password, salt, rounds=5000):
        generated_hash = sha512_crypt.hash(password, salt=salt, rounds=rounds)
        return user_hash == generated_hash.split('$')[3]

    @staticmethod
    def verify_blowfish(user_hash, password, salt, ident='2', rounds=5000):
        generated_hash = bcrypt.hash(password, salt=salt, ident=ident, rounds=rounds)
        return user_hash == generated_hash.split('$')[3]

    @staticmethod
    def verify_eksblowfish(user_hash, password, salt, ident='2a', rounds=5000):
        generated_hash = bcrypt.hash(password, salt=salt, ident=ident, rounds=rounds)
        return user_hash == generated_hash.split('$')[3]

    __algorithm_map = {
        '1': verify_md5.__get__(object),
        '2': verify_blowfish.__get__(object),
        '2a': verify_eksblowfish.__get__(object),
        '5': verify_sha256.__get__(object),
        '6': verify_sha512.__get__(object)
    }

    @staticmethod
    def get_algorithm(hash_id):
        try:
            return Algorithms.__algorithm_map.get(hash_id)
        except:
            print("Hashing algorithm not found")
            return
