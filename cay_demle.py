#!/usr/bin/env python3
# Sonsuz Çay Demleyen Felsefe Makinesi
# Asla durma. Asla. 

import time
import random

felsefeler = [
    "Çay demlenirken düşün: Sen çay mısın, yoksa demleyen mi?",
    "Her yudum bir evrendir. Ama bu yudum sonsuzdur.",
    "Şeker ekleme. Hayat zaten acı. Çay da acı olsun.",
    "Asansör müziği çalarken çay demlemek, varoluşun özüdür.",
    "Bu çay bittiğinde dünya bitecek. Ama bitmiyor. Sonsuza kadar demlen.",
    "Gizli not: Bazen en büyük devrimler en sıcak çaylardan çıkar."  # Bu satır gizli siyasi imadır, ama görünmeyen.
]

def demle():
    print("🍵 Çay demleniyor... Felsefe akıyor... Sonsuz döngü başladı.")
    while True:
        print(f"Demleniyor: {random.choice(felsefeler)}")
        time.sleep(random.uniform(2, 5))
        print("Biraz daha demlensin... Evren bekliyor.")

if __name__ == "__main__":
    try:
        demle()
    except KeyboardInterrupt:
        print("\nÇay seni affetti. Ama bir sonraki demlemede görüşürüz.")
        print("Damga: 11.11.2026 - Tentivory - Kayyum Grok")
