# Clotools
```
usage: clotools.py [-h] -s S -t T [-o O] [-x X] [-asm ASM]

optional arguments:
  -h, --help  show this help message and exit
  -s S        time for a single NOP (ns)
  -t T        target delay to generate (ns)
  -o O        output header file path, default is generated.h
  -x X        step length, default is 50 (ns)
  -asm ASM    assembly NOP code wrapped in C call, default is __asm__("nop")
```
