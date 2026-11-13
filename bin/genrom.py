rom = 65536* [b"\x00"]

# 4 high, 4 low
rom[0xfff0] = b"\xf0"

# 2 high, 2 low, 2 high, 2 low
rom[0xfff1] = b"\xcc"

# high, low, high, low ...
rom[0xfff2] = b"\xaa"

# 4 low, 4 high
rom[0xfff3] = b"\x0f"

# 2 low, 2 high, 2 low, 2 high
rom[0xfff4] = b"\x33"

# low, high, low, high ...
rom[0xfff5] = b"\x55"

#with open("rom.bin", "wb") as f:
#    f.write(b"".join(rom))

with open("rom_low.bin", "wb") as f:
    f.write(b"".join(rom[::2]))

with open("rom_high.bin", "wb") as f:
    f.write(b"".join(rom[1::2]))