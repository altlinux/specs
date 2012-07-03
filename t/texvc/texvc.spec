Name: texvc
Summary: TeX support for MediaWiki
Group: Networking/WWW
Version: 1.14.0
Release: alt4
License: GPL

Url: http://www.mediawiki.org/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Sat Feb 28 2009 (-bb)
BuildRequires: ocaml

Requires: texlive-latex-recommended
Requires: /usr/bin/latex
Requires: dvipng

%description
%summary

%prep
%setup
%build
%make
%install
install -D -m 755 texvc %buildroot%_bindir/texvc
install -D -m 755 texvc_tex %buildroot%_bindir/texvc_tex
install -D -m 755 texvc_tex %buildroot%_bindir/texvc_test

%files
%_bindir/texvc
%_bindir/texvc_tex
%_bindir/texvc_test
%changelog
* Sat Jan 30 2010 Denis Smirnov <mithraen@altlinux.ru> 1.14.0-alt4
- fix requires (ALT #22620)

* Wed Sep 23 2009 Denis Smirnov <mithraen@altlinux.ru> 1.14.0-alt3
- fix requires

* Mon Apr 27 2009 Denis Smirnov <mithraen@altlinux.ru> 1.14.0-alt2
- add Url tag

* Sat Feb 28 2009 Denis Smirnov <mithraen@altlinux.ru> 1.14.0-alt1
- first build for Sisyphus

