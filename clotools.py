import argparse

# generated header file start lines
ghf_section_1='''/* 
+--------------------------------+
| THIS IS AN AUTO GENERATED FILE |
|     CREATED BY clotools.py     |
+--------------------------------+

MIT License

Copyright (c) 2026 Catium2006

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

*/
'''

# nop
ghf_section_2='''
#define nop_2() nop_1();nop_1()
#define nop_4() nop_2();nop_2()
#define nop_8() nop_4();nop_4()
#define nop_16() nop_8();nop_8()
#define nop_32() nop_16();nop_16()
#define nop_64() nop_32();nop_32()
#define nop_128() nop_64();nop_64()
#define nop_256() nop_128();nop_128()
#define nop_512() nop_256();nop_256()
#define nop_1024() nop_512();nop_512()
#define nop_2048() nop_1024();nop_1024()
#define nop_4096() nop_2048();nop_2048()

'''

# generated header file content
ghf_content=''

def devideDelay(base,target):
    macro_name = f'delay_ns_{target}()'
    total = int(target/base)
    index = 0
    nops = []
    rt = 0
    while(total > 0):
        if(total & 1):
            rt += (2**index)
            if(2**index) > 4096:
                print('delay is too long ( > 4096 nop )')
                exit(-1)
            nops.append(f'nop_{2**index}()')
        index+=1
        total = total>>1
    rt*=base
    definition = ''
    for i in range(0,len(nops)):
        definition = definition + nops[i]
        if(i != len(nops) - 1):
            definition = definition + ';'
    macro = '#define ' + macro_name + ' ' + definition
    note = f'// real time = {rt} ns'
    return note + '\n' + macro + '\n\n'

def main():
    parser = argparse.ArgumentParser()

    #parser.description=""
    parser.add_argument("-s", required=True, type=int, help="time for a single NOP (ns)")
    parser.add_argument("-t",required=True, type=int, help='target delay to generate (ns)')
    parser.add_argument("-o", default='generated.h', type=str, help='output header file path, default is generated.h')
    parser.add_argument("-x", default=50, type=int, help='step length, default is 50 (ns)')
    parser.add_argument("-asm", default='__asm__("nop")', type=str, help='assembly NOP code wrapped in C call, default is __asm__("nop")')
    args = parser.parse_args()

    ghf_content = ghf_section_1
    ghf_content += f'#define nop_1() {args.asm}'
    ghf_content += ghf_section_2

    target = args.x
    while(target <= args.t):
        ghf_content += devideDelay(args.s,target)
        target += args.x

    with open(args.o,'w') as f:
        f.write(ghf_content)
        f.close()

if __name__ == "__main__":
   main()

