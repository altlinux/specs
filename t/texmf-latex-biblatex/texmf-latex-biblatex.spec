%define srcName biblatex

Name: texmf-latex-%srcName
Version: 1.7
Release: alt1
Summary: complete reimplementation of LaTeX's bibliographic facilities
License: LPPL (LaTeX Project Public License)
Group: Publishing
Url: http://www.ctan.org/tex-archive/macros/latex/exptl/biblatex/
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildRequires(pre): rpm-build-texmf

BuildArch: noarch

Source0: %srcName.tar

%description
The biblatex package is a complete reimplementation of the
bibliographic facilities provided by LaTeX in conjunction with
BibTeX. It redesigns the way in which LaTeX interacts with BibTeX at
a fairly fundamental level. With biblatex, BibTeX is only used to
sort the bibliography and to generate labels. Instead of being
implemented in BibTeX's style files, the formatting of the
bibliography is entirely controlled by TeX macros. Good working
knowledge in LaTeX should be sufficient to design new bibliography
and citation styles. There is no need to learn BibTeX's postfix stack
language. Just like the bibliography styles, all citation commands
may be freely (re)defined.


%prep
%setup %srcName.tar

%build

%install
mkdir -p %buildroot%_texmfmain/tex/latex/%srcName
mkdir -p %buildroot%_texmfmain/bibtex/bst/%srcName
mkdir -p %buildroot%_texmfdoc/latex/%srcName
cp -a latex/* %buildroot%_texmfmain/tex/latex/%srcName
cp -a bibtex/* %buildroot%_texmfmain/bibtex/bst/%srcName
cp -a doc/* %buildroot/%_texmfdoc/latex/%srcName

%files
%_texmfmain/tex/latex/%srcName
%_texmfmain/bibtex/bst/%srcName
%_texmfdoc/latex/%srcName
%doc README RELEASE 

%changelog
* Mon Dec 05 2011 Kirill Maslinsky <kirill@altlinux.org> 1.7-alt1
- 1.7
- NB: support for Russian language

* Tue Nov 01 2011 Kirill Maslinsky <kirill@altlinux.org> 1.6-alt1
- 1.6

* Wed Mar 31 2010 Kirill Maslinsky <kirill@altlinux.org> 0.9a-alt1
- 0.9a

* Mon Sep 14 2009 Kirill Maslinsky <kirill@altlinux.org> 0.8h-alt1
- Initial build for Sisyphus
