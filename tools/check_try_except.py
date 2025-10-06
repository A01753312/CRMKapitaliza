import sys
from pathlib import Path
p = Path(r"c:\Users\vilua\OneDrive\Documents\Escritorio\KAPITALIZA\kapitaliza-app\CRMKapitaliza\CRM_cliente.py")
text = p.read_text(encoding='utf-8')
lines = text.splitlines()
stack = []
problems = []
for i, line in enumerate(lines, start=1):
    stripped = line.lstrip()
    indent = len(line) - len(stripped)
    if stripped.startswith('try:'):
        stack.append((i, indent))
    elif stripped.startswith(('except', 'finally')):
        # pop the last try with same or greater indent
        # find last try with indent <= current indent
        for j in range(len(stack)-1, -1, -1):
            try_line, try_indent = stack[j]
            if try_indent <= indent:
                stack.pop(j)
                break
# After parsing
for try_line, try_indent in stack:
    problems.append((try_line, try_indent))
if problems:
    print('Found try without except/finally:')
    for ln, ind in problems:
        print(f'  line {ln}, indent {ind}:', lines[ln-1].rstrip())
    sys.exit(2)
else:
    print('All try blocks have except/finally pairing (per simple indent heuristic).')
    sys.exit(0)
