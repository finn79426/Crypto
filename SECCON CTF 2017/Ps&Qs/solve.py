# Source：bamboofox OAlienO
# Usage: python3

from Crypto.Util.number import inverse, GCD 
from Crypto.PublicKey import RSA
pub1 = RSA.importKey(open("pub1.pub").read())
pub2 = RSA.importKey(open("pub2.pub").read())

n = pub1.n
e = pub1.e
p = GCD(pub1.n, pub2.n)
q = n // p
phi_n = (p-1) * (q-1)
d = inverse(e,phi_n)

private = RSA.construct((n,e,d))
c = open("cipher", "rb").read()
c_int = int.from_bytes(c, "big")
print(private.decrypt(c_int).to_bytes(512, "big"))

