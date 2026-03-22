import sys
import os
import re

inputPattern = re.compile(r'\\(?:input|include){([^}]+)}')

def strip_comments(line):
    # Remove everything after a '%' character unless it's escaped '\%'
    parts = line.split('%')
    uncommented_line = parts[0]
    for part in parts[1:]:
        if uncommented_line.endswith('\\'):
            uncommented_line += '%' + part
        else:
            break
    return uncommented_line

def flattenLatex( rootFilename ):
    dirpath, filename = os.path.split(rootFilename)
    with open(rootFilename,'r', encoding='utf-8') as fh:
        for line in fh:
            uncommented_line = strip_comments(line)
            match = inputPattern.search( uncommented_line )
            if match:
                newFile = match.group(1)
                if not newFile.endswith('tex'):
                    newFile += '.tex'
                newFilePath = os.path.join(dirpath,newFile)
                if os.path.exists(newFilePath):
                    flattenLatex( newFilePath )
                else:
                    line = line.replace('\\endinput', '')
                    sys.stdout.buffer.write(line.encode('utf-8'))
            else:
                line = line.replace('\\endinput', '')
                sys.stdout.buffer.write(line.encode('utf-8'))

if __name__ == "__main__":
    flattenLatex( sys.argv[1] )


# Which ends up being called like this:

# # merge multiple files into the old and current versions of the document
# flatten-latex ${DIFFTREE}/thesis.tex > old.tex
# flatten-latex ${WORKINGTREE}/thesis.tex > cur.tex

# # produce the marked up document
# latexdiff old.tex cur.tex > tmp.tex

# # fix line ending problem introduced by latexdiff
# sed 's/^M//' tmp.tex > diff.tex