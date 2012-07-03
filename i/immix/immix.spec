%define origrel 2

Name: immix
Version: 1.3
Release: alt8

Summary: Aligns and merges a set of similar images
License: GPLv3+
Group: Graphics

Url: http://immix.sourceforge.net
Source: http://download.sourceforge.net/immix/immix-%version-%origrel.tar.gz
Patch1: immix-1.3-desktop.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Jul 22 2009
BuildRequires: gcc-c++ libexiv2-devel libfftw3-devel libqt4-devel

%description
Immix aligns and merges a set of similar images
in order to decrease their noise.

%prep
%setup
%patch1 -p1

%build
export PATH=%_qt4dir/bin:$PATH
qmake immix.pro
%make_build CXX="g++ %optflags"

%install
install -pD -m755 immix %buildroot%_bindir/immix
install -pD -m644 immix.svg %buildroot%_pixmapsdir/immix.svg
install -pD -m644 immix16.png %buildroot%_miconsdir/immix.png
install -pD -m644 immix32.png %buildroot%_niconsdir/immix.png
install -pD -m644 packaging/immix.desktop %buildroot%_desktopdir/immix.desktop

%files
%_bindir/*
%_pixmapsdir/immix.svg
%_miconsdir/immix.png
%_niconsdir/immix.png
%_desktopdir/immix.desktop

%changelog
* Tue Nov 01 2011 Michael Shigorin <mike@altlinux.org> 1.3-alt8
- Rebuild with libexiv2.so.11.

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 1.3-alt7
- Rebuild with libexiv2.so.9.

* Mon Jan 04 2010 Victor Forsyuk <force@altlinux.org> 1.3-alt6
- Rebuild with libexiv2.so.6.

* Wed Jul 22 2009 Victor Forsyuk <force@altlinux.org> 1.3-alt5
- Rebuild with libexiv2.so.5.

* Wed Dec 03 2008 Michael Shigorin <mike@altlinux.org> 1.3-alt4
- applied repocop patch

* Fri Jun 13 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.3-alt3.qa1.1
- Automated rebuild due to libexiv2.so.2 -> libexiv2.so.4 soname change.

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.3-alt3.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for immix

* Sat Mar 29 2008 Michael Shigorin <mike@altlinux.org> 1.3-alt3
- rebuild

* Sat Mar 29 2008 Michael Shigorin <mike@altlinux.org> 1.3-alt2
- 1.3-2
- whoops, specified License: (it's GPLv3)
- buildreq

* Sat Jan 05 2008 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- built for ALT Linux (thanks Fedor Zuev for pointing to it)

