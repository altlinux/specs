Name: esvn
Version: 0.6.12
Release: alt4

%define qtdir %_qt3dir
%define vrel 1

Summary: eSvn is a cross-platform (QT-based) GUI frontend for the Subversion revision system
Group: Development/Other
License: GPL v2 or later
URL: http://esvn.sourceforge.net/

Source0: %name-%version-%vrel.tar.gz
Source1: esvn-48x48.png
Source2: esvn-32x32.png
Source3: esvn-16x16.png

Patch0: esvn-alt-desktop-file.patch

Requires: subversion

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Mon Feb 07 2011
BuildRequires: gcc-c++ libqt3-devel

%description
eSvn is a cross-platform (QT-based) GUI frontend for the Subversion revision
system.

%prep
%setup -q -n %name
%patch0 -p1
%__subst s/doc\\/esvn/doc\\/esvn-%version/ src/mainwindow.cpp

%build
PATH=$PATH:%qtdir/bin
qmake esvn.pro
qmake esvn-diff-wrapper.pro
%__subst s/-fno-exceptions/-fexceptions/ esvn.mak
%__subst s/-fno-exceptions/-fexceptions/ esvn-diff-wrapper.mak
%__make -f esvn.mak
%__make -f esvn-diff-wrapper.mak

%install
mkdir -p %buildroot/{%_bindir,%_datadir/pixmaps,%_datadir/applications,%_docdir/%name-%version}
install -m755 %name %buildroot%_bindir/%name
install -m755 esvn-diff-wrapper %buildroot%_bindir/esvn-diff-wrapper
install -m644 %name.png %buildroot/%_datadir/pixmaps/%name.png
install -m644 eSvn.desktop %buildroot%_datadir/applications/%name.desktop
install -m644 AUTHORS COPYING LICENSE README VERSION ChangeLog %buildroot%_docdir/%name-%version
cp -f -r html-docs %buildroot/%_docdir/%name-%version/

mkdir -p %buildroot%_liconsdir/
mkdir -p %buildroot%_niconsdir/
mkdir -p %buildroot%_miconsdir/

install -m644 %SOURCE1 %buildroot%_liconsdir/%name.png
install -m644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -m644 %SOURCE3 %buildroot%_miconsdir/%name.png

sed -i -e 's,Categories=Development;,Categories=Development;RevisionControl;,' %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_bindir/esvn-diff-wrapper
%_datadir/pixmaps/%name.png
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png
%_desktopdir/%name.desktop
%dir %_docdir/%name-%version
%dir %_docdir/%name-%version/html-docs
%_docdir/%name-%version/*

%changelog
* Mon Feb 07 2011 Anatoly Lyutin <vostok@altlinux.org> 0.6.12-alt4
- Resurrect build
- Buildreq

* Sun Oct 25 2009 Igor Vlasenko <viy@altlinux.ru> 0.6.12-alt3.1
- repocop NMU: added secondary category to .desktop

* Sun Nov 16 2008 Igor Zubkov <icesik@altlinux.org> 0.6.12-alt3
- apply patch from repocop
- buildreq

* Sat Jul 12 2008 Igor Zubkov <icesik@altlinux.org> 0.6.12-alt2
- fix desktop file and icons

* Sun Nov 11 2007 Igor Zubkov <icesik@altlinux.org> 0.6.12-alt1
- 0.6.11 -> 0.6.12
- buildreq

* Sat Sep 23 2006 Alexei Takaseev <taf@altlinux.ru> 0.6.11-alt3
- fix build on x86_64

* Tue Sep 19 2006 Alexei Takaseev <taf@altlinux.ru> 0.6.11-alt2
- Fix build

* Sun Jul 17 2005 Ivan Fedorov <ns@altlinux.ru> 0.6.11-alt1
- 0.6.11

* Sat Jun 18 2005 Ivan Fedorov <ns@altlinux.ru> 0.6.9-alt2
- added require subversion (#6720)

* Sat Mar 12 2005 Ivan Fedorov <ns@altlinux.ru> 0.6.9-alt1
- 0.6.9

* Sat Jan 22 2005 Ivan Fedorov <ns@altlinux.ru> 0.6.8-alt2
- clean buildrequires

* Wed Jan 12 2005 Ivan Fedorov <ns@altlinux.ru> 0.6.8-alt1
- 0.6.8

* Thu Jan 06 2005 Ivan Fedorov <ns@altlinux.ru> 0.6.7-alt1
- 0.6.7

* Sat Dec 11 2004 Ivan Fedorov <ns@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Fri Dec 10 2004 Ivan Fedorov <ns@altlinux.ru> 0.6.5-alt2
- 0.6.5-2

* Thu Dec 09 2004 Ivan Fedorov <ns@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Thu Oct 28 2004 Ivan Fedorov <ns@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Sun Sep 26 2004 Ivan Fedorov <ns@altlinux.ru> 0.6.3-alt2
- Fixing help browser

* Sun Sep 26 2004 Ivan Fedorov <ns@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Thu Sep 16 2004 Ivan Fedorov <ns@altlinux.ru> 0.6.2-alt2
- Fixing menu
- Rewriting spec

* Tue Sep 14 2004 Ivan Fedorov <ns@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Fri Sep 03 2004 Ivan Fedorov <ns@altlinux.ru> 0.6.0-alt1
- Initial build

