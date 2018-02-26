Name: tetex-bibtex8
Version: 3.71
Release: alt1

Summary: An 8-bit Implementation of BibTeX 0.99 with multilanguage support
Summary(ru_RU.CP1251): BibTeX со встроенной многоязыковой поддержкой
License: GPL
Group: Publishing
Url: http://tug.ctan.org/tex-archive/biblio/bibtex/8-bit/
Packager: Igor Vlasenko <viy@altlinux.ru>

Source: ftp://tug.ctan.org/pub/tex-archive/biblio/bibtex/8-bit/bt371src.zip
Source1: ftp://tug.ctan.org/pub/tex-archive/biblio/bibtex/8-bit/bt371csf.zip
Patch: %name-%version-alt-Makefile.patch

# Automatically added by buildreq on Fri Dec 30 2005
BuildRequires: unzip

%description
A multilanguage implementation of BibTeX 0.99.
(v3.71) "big" BibTeX with full support of 8-bit encodings

An enhanced, portable C version of BibTeX.  
Enhanced by conversion to "big" (32-bit) 
capacity, addition of run-time selectable 
capacity and 8-bit support extensions.
National character set and sorting order
are controlled by an external configuration 
file.  Various examples are included.

It is recommended to install also a %name-gost package
with ukrainian and belarussian support
and GOST bibliography styles.

%description -l ru_RU.CP1251
(v3.71) Многоязычная реализация BibTeX 0.99 с полной поддержкой 
8-битных кодировок. Кодировка и порядок сортировки описываются в 
отдельном файле конфигурации. 

Желательно также устновить пакет %name-gost с поддержкой 
украинского и беларусского языков и стили BiBTeX для оформления 
библиографии согласно ГОСТ.

%prep
%setup -q -T -c -n %name-%version
unzip -aa -o %SOURCE1
unzip -aa -o %SOURCE0
%patch -p0

%build
make CFLAGS='%optflags -Wno-char-subscripts -funsigned-char' \
 -f unix.mak linux-gcc

# quick dirty csfs. 
# if you are looking for rus+ukr+bel csfs, 
# they are is included in separate gost package
iconv -f cp866 -t koi8-r cp866rus.csf > koi8r.csf
iconv -f cp866 -t cp1251 cp866rus.csf > cp1251rus.csf

%install
%__install -d %buildroot/usr/bin
%__install -m755 bibtex %buildroot/usr/bin/bibtex8
%__install -d %buildroot/usr/share/texmf/bibtex/csf
%__install -m644 *.csf %buildroot/usr/share/texmf/bibtex/csf/

%files
%doc 00readme.txt csfile.txt HISTORY
%_bindir/bibtex8
%dir /usr/share/texmf/bibtex/csf
/usr/share/texmf/bibtex/csf/*.csf

%changelog
* Fri Dec 30 2005 Igor Vlasenko <viy@altlinux.ru> 3.71-alt1
- initial build
