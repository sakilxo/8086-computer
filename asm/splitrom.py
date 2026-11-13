import sys

rom = sys.stdin.buffer.read(65536)


with open("rom_low.bin", "wb") as f:
    f.write(rom[::2])

with open("rom_high.bin", "wb") as f:
    f.write(rom[1::2])