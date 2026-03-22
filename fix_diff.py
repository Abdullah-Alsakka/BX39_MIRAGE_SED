import re

with open('diff/new_diff.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove \DIFaddbeginFL \midrule \DIFaddendFL etc. and just leave \midrule
content = re.sub(r'\\DIFdelbeginFL\s*%DIFDELCMD\s*<\s*\\(?:midrule|toprule|bottomrule|hline|cmidrule|rowcolor)(?:.*?)(?:\n\s*%DIFDELCMD.*?)*\\DIFdelendFL\s*', '', content)
content = re.sub(r'\\DIFaddbeginFL\s*(\\(?:midrule|toprule|bottomrule|hline|cmidrule|rowcolor)(?:.*?))\s*\\DIFaddendFL\s*', r'\1\n', content)

# Remove any stray \DIFdelbeginFL %DIFDELCMD < & and %%% \DIFdelendFL that are left behind in tables
content = re.sub(r'\\DIFdelbeginFL\s*%DIFDELCMD\s*<\s*&\s*%%%\s*\\DIFdelendFL\s*', '', content)

with open('diff/new_diff.tex', 'w', encoding='utf-8') as f:
    f.write(content)
