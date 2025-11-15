#Permasalahan Modul 3

bahan_bakar_awal = 120       
bahan_bakar_isi_ulang = 20    
pemakaian_per_putaran = 5      
putaran_per_pitstop = 10      
jumlah_ban_per_ganti = 4     

total_bahan_bakar = bahan_bakar_awal
total_putaran = 0
total_ban_digunakan = 0
jumlah_pitstop = 0
putaran_saat_ini = 0

print(f"--- START ---")
print(f"Bahan Bakar Awal: {bahan_bakar_awal}L, Pemakaian: {pemakaian_per_putaran}L/Putaran.")

while total_bahan_bakar >= pemakaian_per_putaran:
    total_putaran += 1                  
    putaran_saat_ini += 1                
    total_bahan_bakar -= pemakaian_per_putaran 
    
    status_putaran = (f"Putaran {total_putaran:}: Bahan Bakar berkurang {pemakaian_per_putaran}L. Bahan Bakar tersisa: {total_bahan_bakar:}L.")

    if putaran_saat_ini == putaran_per_pitstop:
        jumlah_pitstop += 1
        putaran_saat_ini = 0             
        total_bahan_bakar += bahan_bakar_isi_ulang
        total_ban_digunakan += jumlah_ban_per_ganti
status_putaran += (f" PIT STOP KE-{jumlah_pitstop:} (+{bahan_bakar_isi_ulang}L Bahan Bakar, +{jumlah_ban_per_ganti} Ban). Bahan Bakar baru: {total_bahan_bakar:}L.")

    else:
        status_putaran += " Tidak ada Pit Stop."
    print(status_putaran)
        
print("--- FINISH ---")
print(f"Total Putaran yang ditempuh: {total_putaran} putaran")
print(f"Total Ban yang digunakan: {total_ban_digunakan} ban")
print(f"Jumlah Pit Stop (Pengisian Bahan Bakar & Ganti Ban): {jumlah_pitstop} kali")

