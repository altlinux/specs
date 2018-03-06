# tmp hack til tetex is dropped
%filter_from_requires /^.usr.bin.etex/d
%filter_from_requires /^.usr.bin.pdftex/d
%filter_from_requires /^.usr.bin.pdfetex/d

Summary(ru_RU.KOI8-R): Макрос TeX для получения DVI или PDF из вывода OpenJade
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:    jadetex
Version: 3.13
Release: alt4_13
Group:   Publishing
Summary: TeX macros used by Jade TeX output
License: Freely redistributable without restriction
URL:     http://sourceforge.net/projects/jadetex

Requires: sgml-common >= 0.5
Requires: texlive-texmf
Requires: openjade
Requires(post): texlive
Requires(postun): texlive
Requires(post): texlive-texmf
Requires(postun): texlive-texmf
BuildRequires: unzip 
BuildRequires: texlive 
BuildRequires: texlive-texmf
BuildConflicts: tetex tetex-core tetex-afm tetex-context tetex-latex
Conflicts: tetex tetex-core tetex-afm tetex-context tetex-latex

BuildArch: noarch
Source0: http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: jadefmtutil.cnf
Patch0: jadetex-tetex3.patch
Patch1: jadetex-3.13-typoupstream.patch
Source44: import.info


%description
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as TeX files (to obtain DVI,
PostScript, or PDF files, for example).

%description -l ru_RU.KOI8-R
JadeTeX содержит дополнительный макрос для издательской системы LaTeX
необходимый для преобразования выходных файлов tex-модуля OpenJade в
форматы DVI, Postscript или PDF.

%prep
%setup -q
cp -p %{SOURCE1} .
%patch0 -p1 -b .tetex3
%patch1 -p1 -b .typoupstream

%build
make


%install
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/texmf-dist/tex/jadetex
cp -p *.ini %{buildroot}%{_datadir}/texmf-dist/tex/jadetex
cp -p *.sty %{buildroot}%{_datadir}/texmf-dist/tex/jadetex
cp -p *.cnf %{buildroot}%{_datadir}/texmf-dist/tex/jadetex

mkdir -p %{buildroot}%{_bindir}
ln -s etex %{buildroot}%{_bindir}/jadetex
ln -s pdfetex %{buildroot}%{_bindir}/pdfjadetex

mkdir -p %{buildroot}%{_mandir}/man1
cp -p jadetex.1 %{buildroot}%{_mandir}/man1
ln -s jadetex.1.gz %{buildroot}%{_mandir}/man1/pdfjadetex.1

# touching all ghosts; hack for rpm 4.0.4
for rpm404_ghost in %{_datadir}/texmf-dist/web2c/jadetex.fmt %{_datadir}/texmf-dist/web2c/pdfjadetex.fmt
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done


%post
%{_bindir}/env - PATH=$PATH:%{_bindir} fmtutil-sys \
	       --cnffile %{_datadir}/texmf-dist/tex/jadetex/jadefmtutil.cnf \
	       --all --fmtdir %{_datadir}/texmf-dist/web2c \
	       > /tmp/jadetex-fmtutil-sys.log 2>&1

%files
%doc index.html
%ghost %{_datadir}/texmf-dist/web2c/jadetex.fmt
%ghost %{_datadir}/texmf-dist/web2c/pdfjadetex.fmt
%dir %{_datadir}/texmf-dist/tex/jadetex
%{_datadir}/texmf-dist/tex/jadetex/*
%{_datadir}/texmf-dist/web2c/*
%{_mandir}/man1/jadetex.1*
#%{_mandir}/man1/pdfjadetex.1*
%{_bindir}/jadetex
%{_bindir}/pdfjadetex

%triggerin -- texlive
/usr/bin/env - PATH=$PATH:%{_bindir} fmtutil-sys --cnffile %{_datadir}/texmf-dist/tex/jadetex/jadefmtutil.cnf --all > /dev/null 2>&1
exit 0


%changelog
* Tue Mar 06 2018 Igor Vlasenko <viy@altlinux.ru> 3.13-alt4_13
- replaced with jadetex for texlive 2017

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

