Name:    tetex-latex-xymtex
Version: 2.00
Release: alt4.1
Summary: XyMTeX for Drawing Chemical Structural Formulas
Summary(ru_RU.KOI8-R): XyMTeX -- макропакет для рисования химических структур в LaTeX
License: Distributable
Group:   Publishing
URL:     ftp://ftp.dante.de/tex-archive/macros/latex/contrib/other/xymtex.tar.gz

Source0: xymtex-%version.tar.bz2

BuildArchitectures: noarch

Requires: tetex-core tetex-latex

Provides: xymtex

Obsoletes: xymtex


%package doc
Summary: Additional documentation for XyMTeX
Group: Publishing
Requires: %name = %version-%release
Obsoletes: xymtex-doc
Provides: xymtex-doc

%description 
XyMTeX for Drawing Chemical Structural Formulas

%description -l ru_RU.KOI8-R
XyMTeX -- макропакет для рисования химических структур в LaTeX

%description doc
Additional documentation for XyMTeX


%prep
%setup -q -n xymtex


%install
%__install -d $RPM_BUILD_ROOT%_datadir/texmf/tex/latex/xymtex
%__install -m 644 *.sty $RPM_BUILD_ROOT%_datadir/texmf/tex/latex/xymtex

# install doc
%__install -d $RPM_BUILD_ROOT%_docdir/%name-%version/docs
%__install -m 644 doc200/{*.tex,*.STY,*.dvi} $RPM_BUILD_ROOT%_docdir/%name-%version/
%__install -d $RPM_BUILD_ROOT%_datadir/texmf/doc/latex
ln -sf ../../../doc/%name-%version  $RPM_BUILD_ROOT%_datadir/texmf/doc/latex/xymtex


# install additional doc
%__install -m 644 drvdvi/*.dvi $RPM_BUILD_ROOT%_docdir/%name-%version/docs


%files
%_datadir/texmf/tex/latex/xymtex
%_docdir/%name-%version
%_datadir/texmf/doc/latex/*

%files doc
%_docdir/%name-%version/docs


%changelog
* Thu Nov 05 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.00-alt4.1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-xymtex

* Sun Aug 29 2004 Yury A. Zotov <yz@altlinux.ru> 2.00-alt4
- typo in summary and description corrected

* Thu May 27 2004 Yury A. Zotov <yz@altlinux.ru> 2.00-alt3
- package renamed to tetex-latex-xymtex

* Fri Feb 27 2004 Yury A. Zotov <yz@altlinux.ru> 2.00-alt2
- Requires tetex-latex
- License Distributable

* Thu Feb 26 2004 Yury A. Zotov <yz@altlinux.ru> 2.00-alt1
- first build for ALTLinux

