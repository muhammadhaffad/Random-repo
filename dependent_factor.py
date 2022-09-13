from gmpy2 import *
from Crypto.Util.number import *

"""
Contoh dependent factor, jadi faktor berikutnya bergantung pada faktor sebelumnya, pada kasus ini faktor berikutnya digenerate menggunakan operasi XOR.
pada contoh berikut ini, nilai q dibangkitkan dari nilai p dengan bit-bit yang dibalik pada urutan 255 sampai 0 (top bits dari p dan q sama).
"""

p = getPrime(512)
q = p ^ ((1<<256) - 1)
n = p*q

# pertama mendapatkan top_bits (bit urutan 512 sampai 256) dengan cara dapatkan 512 (256+256) top bits dari n, kemudian diakar 2
top_bits = iroot(n >> 512, 2)[0]

#brute force bit-bit selanjutnya
P = top_bits << 256 | (2**256 - 1)
Q = top_bits << 256
for i in range(255, -1, -1):
  curr = 1 << i
  if (P^curr) * (Q^curr) < n:
    P ^= curr
    Q ^= curr

print(n % P+1)
