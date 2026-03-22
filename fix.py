import re

with open('diff/default_diff.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix \hline, \rowcolor inside \DIFaddbeginFL ... \DIFaddendFL and inline
# Wait, sometimes \DIFaddbeginFL is on one line, \hline is on another, \DIFaddendFL is on another.

text = re.sub(
    r'\\DIF(add|del)begin(?:FL)?\s*(\\rowcolor\{.*?\})\s*\\DIF(add|del)end(?:FL)?',
    r'\2', text
)
text = re.sub(
    r'\\DIF(add|del)begin(?:FL)?\s*(\\(?:hline|midrule|bottomrule|toprule))\s*\\DIF(add|del)end(?:FL)?',
    r'\2', text
)

# Also there might be %DIFDELCMD < \hline
# Let's remove them completely since they are deleted lines. 
text = re.sub(r'\\DIFdelbegin(?:FL)?\s*%DIFDELCMD\s*<\s*\\(?:hline|midrule|bottomrule|toprule|rowcolor.*?)\s*%.*?\\DIFdelend(?:FL)?', '', text, flags=re.DOTALL)

with open('diff/default_diff.tex', 'w', encoding='utf-8') as f:
    f.write(text)
