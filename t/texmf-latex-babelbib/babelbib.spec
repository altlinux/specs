%define truename babelbib
Name: texmf-latex-%truename
Version: 1.29
Release: alt1
Summary: Multilingual bibliographies: The babelbib package for LaTeX
Summary(ru_RU.CP1251): многоязыковая поддержка (через babel) для стилей BibTeX
License: LaTeX Project Public License
Group: Publishing
Url: http://tug.ctan.org/tex-archive/biblio/bibtex/%truename
Packager: Igor Vlasenko <viy@altlinux.ru>

Source: ftp://tug.ctan.org/pub/tex-archive/biblio/bibtex/%truename/%truename.zip
Source1: babelbibtest-ru.tex
Source2: babelbibtest-ru.bib
Patch:  %truename-1.20-add-russian-alt.patch
Patch1: %truename-1.20-add-russian-alt-recoded.patch
Patch2: %truename-kill-checksum-alt.patch

Obsoletes: tetex-latex-babelbib <= 1.21

BuildArch: noarch

BuildRequires: latex2html unzip rpm-build-texmf 
#cm-super-fonts-pfb cm-super-fonts-tex-dvips /usr/bin/latex /usr/bin/pdflatex texlive-fonts-recommended

%description
This package enables to generate multilingual bibliographies in
cooperation with babel. Two approaches are possible: Each citation
may be written in another language, or the whole bibliography can 
be typeset in a language chosen by the user. The current version 
supports Afrikaans, Danish, Dutch, English, Esperanto, Finnish, French,
German, Italian, Norwegian, Portuguese, Russian, Spanish, and Swedish.
  In addition, the package supports commands to change the typography
of the bibliographies.
  Many of the standard and extended bibliography styles are available.

%prep
%setup -q -n %truename
#patch1 -p0
#patch2 -p0

%build
#cd source/latex/babelbib
#make 

%install
INSTALLDIR=%buildroot/usr/share/texmf/tex/latex/babelbib
DOCDIR=%buildroot/usr/share/texmf/doc/latex/babelbib
BSTDIR=%buildroot/usr/share/texmf/bibtex/bst/babelbib
if [ ! -d $INSTALLDIR ]; then mkdir -p $INSTALLDIR; fi
if [ ! -d $DOCDIR ]; then mkdir -p $DOCDIR; fi
if [ ! -d $BSTDIR ]; then mkdir -p $BSTDIR; fi

#cd source/latex/babelbib
#install -m644 babelbib.sty $INSTALLDIR
#install -m644 *.bdf $INSTALLDIR
#install -m644 *.bst $BSTDIR
#install -m644 babelbib.pdf $DOCDIR

install -m644 tex/latex/babelbib/babelbib.sty $INSTALLDIR
install -m644 tex/latex/babelbib/*.bdf $INSTALLDIR
install -m644 bibtex/bst/babelbib/*.bst $BSTDIR
install -m644 doc/latex/babelbib/babelbib.pdf $DOCDIR

%files
#doc README ChangeLog babelbib.xml babelbibtest.bib tugboat-babelbib.pdf babelbibtest.tex
%doc doc/latex/babelbib/README doc/latex/babelbib/ChangeLog 
%doc doc/latex/babelbib/babelbibtest.bib 
%doc doc/latex/babelbib/tugboat-babelbib.pdf 
%doc doc/latex/babelbib/babelbibtest.tex
%doc source/latex/babelbib/babelbib.xml
%dir /usr/share/texmf/bibtex/bst/babelbib
%dir /usr/share/texmf/tex/latex/babelbib
%dir /usr/share/texmf/doc/latex/babelbib
/usr/share/texmf/bibtex/bst/babelbib/*
/usr/share/texmf/tex/latex/babelbib/*
/usr/share/texmf/doc/latex/babelbib/*

%changelog
* Mon Nov 09 2009 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- renamed to texmf-latex-babelbib
- russian patch removed - merged to upstream.
- TODO: texlive includes old babelbib w/o russian.
  eventually it will update babelbib to the new version,
  so there will be no need for separate package.

* Thu Jan 05 2006 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- initial build
