from matplotlib import pyplot as plt

plt.plot([0.13, 0.19, 0.28, 0.50, 0.73], [27.76, 29.08, 30.42, 32.37, 34.24], marker='o', label='32-bit (fp)')
plt.plot([0.16, 0.26, 0.38, 0.55, 0.90], [27.42, 28.65, 30.21, 31.53, 32.73], marker='o', label='LSQ 8-bit')
# plt.plot([0.16, 0.25, 0.39, 0.56], [27.20, 28.72, 30.04, 31.31], marker='o', label='LSQ+ 8-bit')
# plt.plot([0.16, 0.24, 0.39, 0.56, 0.79], [27.19, 28.83, 29.85, 31.48, 32.02], marker='o', label='int offset 8-bit')
# plt.plot([0.15, 0.24, 0.37, 0.54], [27.25, 28.61, 30.00, 31.58], marker='o', label='cubic STE 8-bit')
# plt.plot([0.16, 0.25, 0.39, 0.56, 0.79], [27.18, 28.66, 29.85, 31.47, 32.02], marker='o', label='fp & int offset 8-bit')
plt.plot([0.17, 0.26, 0.40, 0.60, 0.91], [26.25, 27.53, 28.63, 29.72, 30.94], marker='o', label='LSQ 4-bit')
# plt.plot([0.17, 0.26, 0.39, 0.61, 0.90], [26.22, 27.51, 28.41, 29.58, 31.00], marker='o', label='int offset 4-bit')
# plt.plot([0.16, 0.25, 0.38, 0.57, 0.84], [26.93, 28.48, 29.57, 31.42, 32.62], marker='o', label='LSQ 6-bit')
plt.plot([0.18, 0.28, 0.42, 0.65, 1.00], [24.16, 24.88, 25.37, 26.03, 26.96], marker='o', label='LSQ 2-bit')

# plt.plot([0.13, 0.28, 0.50], [27.76, 30.42, 32.37], marker='o', label='low bpp (32-bit)')
# plt.plot([0.26, 0.92], [27.53, 30.29], marker='o', label='high bpp (4-bit)')
# plt.hlines(27.53, 0.1, 0.3, color='gray', linestyle='--', linewidth=2)
# plt.hlines(30.29, 0.25, 1, color='gray', linestyle='--', linewidth=2)

plt.xlabel('bits per pixel (bpp)')
# plt.ylabel('PSNR (dB)')
plt.ylabel('MS-SSIM')
plt.legend()
plt.show()
