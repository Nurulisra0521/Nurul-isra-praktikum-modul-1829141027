#import modul Rumus

import RumusVST

def main():
    print("\nKETERANGAN")
    print("s = jarak tepuh (m, km)")
    print("t = waktu tempuh (jam, sekon)")
    print("v = kecepatan (km/jam, m/sekon)")
    
    #rumus kecepatan
    s = 26
    t = 3

    kecepatan = RumusVST. kecepatan(s, t)

    print("\nKECEPATAN")
    print("jarak\t: ", s)
    print("waktu\t: ", t)
    print("kecepatan\t: ", kecepatan)

    #rumus jarak
    v = 18
    t = 2

    jarak = RumusVST.jarak(v, t)

    print("\nJARAK")
    print("kecepatan\t: ", v)
    print("waktu\t: ", t)
    print("jarak\t: ", jarak)

    #rumus waktu
    s = 20
    v = 5

    waktu = RumusVST.waktu(s, v)
    
    print("\nWAKTU")
    print("jarak\t: ", s)
    print("kecepatan\t: ", v)
    print("waktu\t: ", waktu)
    
if __name__ == "__main__":
    main()
    
