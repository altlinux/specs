%define srcName xkeyval

Name: tetex-latex-xkeyval
Version: 2.6a
Release: alt4
Summary: A LaTeX macro package
Summary(ru_RU.UTF-8): LaTeX макропакет расширяющий keyval
License: LPPL (LaTeX Project Public License)
Group: Publishing
Url: http://www.ctan.org/tex-archive/macros/latex/contrib/xkeyval/

BuildArchitectures: noarch

BuildRequires(pre): rpm-build-texmf
Requires: tetex-core tetex-latex

Packager: %packager

Source: %srcName-%version.tar.bz2

%description
This package is an extension of the keyval package by David Carlisle
and offers additional macros for setting keys and declaring and
setting class or package options.

%prep
%setup -q -n %srcName-%version

#%build

%install
mkdir -p %buildroot{%_datadir/texmf/tex/{generic,latex}/xkeyval,%_datadir/texmf/doc/latex/xkeyval,%_docdir}
install -pD -m644 doc/xkeyval.pdf %buildroot%_datadir/texmf/doc/latex/xkeyval/
install -pD -m644 run/pst-xkey.sty %buildroot%_datadir/texmf/tex/latex/xkeyval/
install -pD -m644 run/xkeyval.sty %buildroot%_datadir/texmf/tex/latex/xkeyval/
install -pD -m644 run/xkvview.sty %buildroot%_datadir/texmf/tex/latex/xkeyval/
install -pD -m644 run/xkvltxp.sty %buildroot%_datadir/texmf/tex/latex/xkeyval/
install -pD -m644 run/keyval.tex %buildroot%_datadir/texmf/tex/generic/xkeyval/
install -pD -m644 run/pst-xkey.tex %buildroot%_datadir/texmf/tex/generic/xkeyval/
install -pD -m644 run/xkeyval.tex %buildroot%_datadir/texmf/tex/generic/xkeyval/
install -pD -m644 run/xkvtxhdr.tex %buildroot%_datadir/texmf/tex/generic/xkeyval/

%files
%dir %_datadir/texmf/tex/generic/xkeyval/
%dir %_datadir/texmf/tex/latex/xkeyval/
%dir %_datadir/texmf/doc/latex/xkeyval/

%_datadir/texmf/tex/generic/xkeyval/*
%_datadir/texmf/tex/latex/xkeyval/*
%_datadir/texmf/doc/latex/xkeyval/*

%doc README

%changelog
* Sat Nov 14 2009 Andrey Bergman <vkni@altlinux.org> 2.6a-alt4
- Removed post and pre sections.

* Fri Nov 13 2009 Andrey Bergman <vkni@altlinux.org> 2.6a-alt3
- Added dependence on rpm-build-texmf.

* Fri Mar 06 2009 Andrey Bergman <vkni@altlinux.org> 2.6a-alt2
- resolved directory problem (BUG 19074)

* Thu Jan 15 2009 Andrey Bergman <vkni@altlinux.org> 2.6a-alt1
- update to version 2.6a

* Mon Jan 29 2008 Andrey (Vkni) Bergman <vkni at yandex.ru> 2.5f-alt1
- initial release for Sisyphus
