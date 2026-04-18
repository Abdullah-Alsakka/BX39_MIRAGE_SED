# Add glossaries support to latexmk
add_cus_dep( 'acn', 'acr', 0, 'makeglossaries' );
add_cus_dep( 'glo', 'gls', 0, 'makeglossaries' );
$clean_ext .= " acr acn alg glo gls glg";

sub makeglossaries {
     my ($base_name, $path) = fileparse( $_[0] );
     my @args = ( "-d", $path, $base_name );
     if ($silent) { unshift @args, "-q"; }
     return system "makeglossaries", @args;
}

# for compilation with latexmk
$pdflatex = 'pdflatex -shell-escape -interaction=nonstopmode %O %S';
$recorder = 1;
$pdf_mode = 1;
$bibtex_use = 2; # Use bibtex/biber if necessary
$biber = 'biber %O %S';
$force_mode = 1;

