#!/usr/bin/env python3
from pathlib import Path
import sys
p = Path(sys.argv[1])
s = p.read_text(errors='ignore')
old = '{ HDTV_VMODE,"HDTV 1080p @60Hz ", GS_NONINTERLACED, GS_MODE_DTV_1080P, GS_FRAME, (u64)make_display_magic_number( 1079, 1919, 1, 2, 48, 238), 0x0150E00201C00005}'
new = '{ HDTV_VMODE,"HDTV 1080p LISO SEM LINHAS       ", GS_NONINTERLACED, GS_MODE_DTV_1080P, GS_FRAME, (u64)make_display_magic_number( 1079, 1919, 1, 2, 48, 238), 0x0150E00201C00005}'
if old not in s:
    print('Entrada exata não encontrada. Tentando patch por trecho...')
    s2 = s.replace('"HDTV 1080p @60Hz "', '"HDTV 1080p LISO SEM LINHAS       "')
    if s2 == s:
        raise SystemExit('Falhou: não achei a string 1080p no source baixado.')
    s = s2
else:
    s = s.replace(old, new)
p.write_text(s)
print('Patch aplicado no 1080p. Mantido GS_MODE_DTV_1080P + GS_NONINTERLACED + GS_FRAME.')
