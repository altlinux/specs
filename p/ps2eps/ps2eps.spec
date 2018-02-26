Summary: Converts PostScript to EPS (Encapsulated PostScript) files
Name: ps2eps
Version: 1.68
Release: alt1
License: GPLv2+
Group: Publishing
Source: %name-%version.tar.gz
URL: http://www.tm.uka.de/~bless/ps2eps

Requires: ghostscript-classic

%description
ps2eps is a tool (written in Perl) to produce Encapsulated PostScript
Files (EPS/EPSF) from usual one-paged Postscript documents.  It
calculates correct Bounding Boxes for those EPS files and filters some
special postscript command sequences that can produce erroneous
results on printers. EPS files are often needed for including
(scalable) graphics of high quality into TeX/LaTeX (or even Word)
documents.

%prep
%setup -q -n %name

%build
cd src/C
gcc %optflags -o bbox bbox.c

%install
mkdir -p %buildroot%_bindir
install -m755 -s src/C/bbox %buildroot%_bindir
install -m755 bin/ps2eps %buildroot%_bindir
mkdir -p %buildroot%_man1dir
install -m644 doc/man/man1/*.1 %buildroot%_man1dir


%files
%doc Changes.txt INSTALL.txt README.txt
%doc doc/html/*.html
#doc doc/pdf/*.pdf
%_bindir/*
%_man1dir/*

%changelog
* Sat Sep 10 2011 Denis G. Samsonenko <ogion@altlinux.org> 1.68-alt1
- new version (1.68)
- build for Sisyphus

* Wed Jul 28 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 1.64-alt0.sdg1
- initial build for ALTLinux (branch-5.1)
