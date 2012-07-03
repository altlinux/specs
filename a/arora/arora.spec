Name: arora
Version: 0.11.0
Release: alt2

Summary: Arora is a cross platform web browser built using Qt and WebKit.
License: GPLv2
Group: Networking/WWW

Url: http://www.arora-browser.org/
Source: %name-%version.tar
Patch0: arora-0.11.0-alt-startpage.patch
Patch1: arora-0.11.0-fake-certificate-issuer.patch
Packager: Alexey Morsov <swi@altlinux.ru>

BuildRequires: libqt4-devel gcc-c++ libqt4-webkit

%description
Arora is a simple cross platform web browser. Currently Arora is a very
basic browser whose feature list includes things like "History" and
"Bookmarks".

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
qmake-qt4 \
	"QMAKE_CFLAGS+=%optflags" \
	"QMAKE_CXXFLAGS+=%optflags" \
	"PREFIX=%_prefix" \
	%name.pro
%make_build

%install
%make INSTALL_ROOT=%buildroot install

%files
%doc AUTHORS ChangeLog GPLHEADER LICENSE.GPL2 LICENSE.GPL3 README
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/apps/%name.*
%_man1dir/*
%_pixmapsdir/%name.*

%changelog
* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 0.11.0-alt2
- reverted a commit breaking startpage (closes: #26937)
- applied a fedora patch sanitizing SSL issuer string

* Tue Feb 01 2011 Alexey Morsov <swi@altlinux.ru> 0.11.0-alt1
- new version (closes: 24986)

* Tue Aug 10 2010 Alexey Morsov <swi@altlinux.ru> 0.10.2-alt3.10082010
- new git version (commit 301487da75c659ea3157fc7793568cd6aaea9ba4)

* Wed Feb 17 2010 Alexey Morsov <swi@altlinux.ru> 0.10.2-alt2.17022010
- new git version (commit 0405e8693e18ec5f28ac81478f567f9c973ca602)

* Sun Dec 20 2009 Alexey Morsov <swi@altlinux.ru> 0.10.2-alt1.20122009
- new git version (commit eac2ce94e11e311e8c9039cd9558d258d70198eb)

* Mon Nov 09 2009 Alexey Morsov <swi@altlinux.ru> 0.10.1-alt1.09112009
- new git version (commit 1193ab397b1e220d96080a6b9275f7eb605aa8b2)

* Fri Oct 02 2009 Alexey Morsov <swi@altlinux.ru> 0.10-alt1.02102009
- new git version (commit ad1852ef4d7e74f38fdb0645919bf580da14dfc7)

* Sat Sep 26 2009 Alexey Morsov <swi@altlinux.ru> 0.9.0-alt1.26092009
- new git version (commit 138994e74d1637c4d3efbaa98538ff0b5daa05bb)

* Mon Sep 07 2009 Alexey Morsov <swi@altlinux.ru> 0.9.0-alt1.07092009
- new git version (commit b965244805d2176a7ddcfe052df07a4d7b5cf7e0)

* Wed Aug 05 2009 Alexey Morsov <swi@altlinux.ru> 0.8.0-alt1.05082009
- new git version (commit b181a799ac1671a4c853b505f746bc1bf3299770)

* Wed Jun 17 2009 Alexey Morsov <swi@altlinux.ru> 0.7.1-alt1.17062009
- new git version (commit 792e62f1468d8681f541c8f52dcc18b21ca30164)

* Tue Mar 31 2009 Alexey Morsov <swi@altlinux.ru> 0.6-alt1
- new version 

* Mon Feb 23 2009 Alexey Morsov <swi@altlinux.ru> 0.5-alt1.1
- fix build flags

* Sat Feb 21 2009 Alexey Morsov <swi@altlinux.ru> 0.5-alt1
- initial built
