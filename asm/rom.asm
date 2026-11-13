times 0xfff0 - ($ - $$) db 0xff
 
mov ax, 0x3335
mov dx, 0xf0cc

out dx, ax
out dx, al

mov dx, 0xf055

out dx, al
out dx, ax

times 0x10000 - ($ - $$) db 0xff