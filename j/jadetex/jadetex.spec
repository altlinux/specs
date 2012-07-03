Name: jadetex
Version: 3.13
Release: alt4
Packager: Grigory Batalov <bga@altlinux.ru>

Group: Publishing
Summary: TeX macros used by Jade TeX output
Summary(ru_RU.KOI8-R): Макрос TeX для получения DVI или PDF из вывода OpenJade
License: Distributable (C) Sebastian Rahtz <s.rahtz@elsevier.co.uk>
URL: http://jadetex.sourceforge.net/

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz
Source1:%name-ru-test-0.2.tar.bz2
Source2: ftp://ftp.ptc.spbu.ru/people/uwe/sgml/koi8r.dcl
Source3: jadefmtutil.cnf

Patch1: %name-ml-urw-alt.patch
Patch2: %name-uni-urw-alt.patch
Patch3: %name-urw-t1-hack.patch

BuildArch: noarch
Obsoletes: jadetex-urw-test

Requires: openjade sgml-common >= 0.5
%add_texmf_req_skip latex/omega
# Note: to build the test install
# netpbm docbook-style-dsssl fonts-type1-urw-tex texlive-lang-cyrillic texlive-extra-utils

# Automatically added by buildreq on Mon Oct 19 2009
BuildRequires: texlive-latex-base
BuildRequires(pre): rpm-build-texmf

%description
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as TeX files, to obtain DVI, Postscript
or PDF files for example.

%description -l ru_RU.KOI8-R
JadeTeX содержит дополнительный макрос для издательской системы LaTeX
необходимый для преобразования выходных файлов tex-модуля OpenJade в
форматы DVI, Postscript или PDF.

%prep
%setup -q -a1
%patch1 -p0
%patch2 -p0
%patch3 -p0
sed -i -e 's/{ptm}/{utm}/' jadetex.dtx
rm -f doc/.cvsignore .cvsignore

%build
%make_build

%install
mkdir -p %buildroot%_texmfmain/tex/%name
install -m644 *.ini *.sty dsssl.def jadetex.ltx %buildroot%_texmfmain/tex/%name/

mkdir -p %buildroot%_bindir
ln -s pdftex %buildroot%_bindir/jadetex
ln -s pdftex %buildroot%_bindir/pdfjadetex

mkdir -p %buildroot%_sysconfdir/texmf/{fmtutil,fmt.d}
ln -s ../fmtutil/format.jadetex.cnf %buildroot%_sysconfdir/texmf/fmt.d/20-jadetex.cnf
install -m644 %SOURCE3 %buildroot%_sysconfdir/texmf/fmtutil/format.jadetex.cnf

mkdir -p %buildroot%_man1dir
install -m644 *.1 %buildroot%_man1dir

# --------- should be moved to sgml-common ---------
#next is for processing SGML files in KOI8-R encoding.
mkdir -p %buildroot%_datadir/sgml/
install -m644 %SOURCE2 %buildroot%_datadir/sgml/
# ---------

%files
%_bindir/%name
%_bindir/pdf%name
%_man1dir/*
%_texmfmain/tex/%name
%_sysconfdir/texmf/fmt.d/*
%_sysconfdir/texmf/fmtutil/*
%doc ChangeLog doc ru-test
# --------- should be moved to sgml-common ---------
%_datadir/sgml/koi8r.dcl
# ---------

%changelog
* Fri Nov 06 2009 Grigory Batalov <bga@altlinux.ru> 3.13-alt4
- Rebuilt with generic TeX requirements checking enabled.
- Temporarily skip texmf(latex/omega) requirement.

* Mon Oct 19 2009 Grigory Batalov <bga@altlinux.ru> 3.13-alt3
- Rebuilt with texlive.
- Specfile cleaned up.
- Unnesessary texhash in %%post-script was removed.
- Formats (*.fmt) are built on install automatically.

* Thu Apr 22 2004 Yury Konovalov <yurix@altlinux.ru> 3.13-alt2
- assign common (for T1 and T2A) tex font families (URW for now) for widely
  used in dsssl stylesheets fonts (Arial, Times New Roman, Courier New,
  Palatino, etc)
- hardcoded T2A fontenc removed to reduce font substitition
- above require us to use only thouse fonts which have both T1 and T2A
  families defined (TS1 is a plus too). So URW T1 hack is added, until
  correspondent fonts packages will be updated.
- rpm scripts fixed (more accurate use of texhash and fmtutil)
- do not provide /usr/share/sgml directory

* Thu Oct 16 2003 Yury Konovalov <yurix@altlinux.org> 3.13-alt1
- 3.13
- added dependency on urw-tex and cm-super-fonts-tex fonts package (bug #2473)
- merge ru-test example with the main package
- spec clean-up
- Russian description added

* Sat Feb 01 2003 Yurix <yurix@altlinux.ru> 3.12-alt6
- Rebuild against tetex-2.0-alt1

* Fri Jan 17 2003 Alexander Bokovoy <ab@altlinux.ru> 3.12-alt5
- Rebuild against tetex-2.0-alt0.8 since plain.tex has been changed
  by D.Knuth.

* Sun Jan 12 2003 Yurix <yurix@altlinux.ru> 3.12-alt4
- add urw-tex to BuildPreReq to fix missing urw support
- move ru-test to separate package

* Sat Dec 07 2002 Yurix <yurix@altlinux.ru> 3.12-alt3
- add support for urw-tex fonts
- add example for russian users

* Wed Dec 04 2002 AEN <aen@altlinux.ru> 3.12-alt2
- rebuild with new tetex

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 3.12-alt1
- 3.12

* Mon Dec 03 2001 Stanislav Ievlev <inger@altlinux.ru> 3.11-alt1
- 3.11

* Sun Dec 24 2000 AEN <aen@logic.ru>
- adopted for RE

* Mon Oct 16 2000 Camille Begnis <camille@mandrakesoft.com> 2.20-5mdk
- use hugelatex instead of latex

* Wed Oct 11 2000 Camille Begnis <camille@mandrakesoft.com> 2.20-4mdk
- Add support for Italian with patch i18n

* Mon Sep 11 2000 Camille Begnis <camille@mandrakesoft.com> 2.20-3mdk
- Why was the binary missing?

* Mon Aug 28 2000 Camille Begnis <camille@mandrakesoft.com> 2.20-2mdk
- add buildrequires and rebuild upon new tetex release

* Wed Aug 23 2000 Camille Begnis <camille@mandrakesoft.com> 2.20-1mdk
- 2.20
- adapt spec from Eric Bischoff <ebisch@cybercable.tm.fr>
- Pre-LSB compliance

