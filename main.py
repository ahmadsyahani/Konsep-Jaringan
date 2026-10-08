from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 5000)
f0 = 1
batas_harmonik = [1, 3, 5, 7, 9, 10]
fig, ax = plt.subplots(figsize=(10, 6))

for batas in batas_harmonik:
    sinyal = np.zeros_like(t)
    for n in range(1, batas + 1, 2):
        sinyal += np.sin(2 * np.pi * n * f0 * t) / n

    label = f"Harmonik 1 s/d {batas}"
    if batas == 10:
        sinyal += np.sin(2 * np.pi * 10 * f0 * t) / 10
        label += " (genap)"

    ax.plot(t, sinyal, label=label, linewidth=1.2)

ax.set_title("Simulasi Pembentukan Sinyal Digital di "
             "Physical Layer (Fourier Series)")
ax.set_xlabel("Waktu (detik)")
ax.set_ylabel("Amplitudo")
ax.axhline(0, color="black", linestyle="--", linewidth=0.7)
ax.set_xticks(np.arange(0, 2.01, 0.25))
ax.set_ylim(-1.1, 1.1)
ax.grid(True, linestyle=":", alpha=0.5)
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
output = Path(__file__).resolve().with_name("visualisasi_square.png")
fig.savefig(output, dpi=180)
print(f"Grafik disimpan: {output}")
plt.show()