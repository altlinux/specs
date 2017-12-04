Name: libXcursor
Version: 1.1.15
Release: alt1%ubt
Summary: X Cursor Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: libXfixes-devel libXrender-devel xmlto xorg-util-macros xorg-sgml-doctools

%description
X Cursor Library

%package devel
Summary: X Cursor Library and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/X11/Xcursor
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Mon Dec 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.1.15-alt1%ubt
- fixes:
 + CVE-2017-16612 Fix heap overflows when parsing malicious files

* Thu May 30 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.1.14-alt1
- 1.1.14

* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.13-alt1
- 1.1.13

* Thu Jun 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.1.12-alt1
- 1.1.12

* Mon Feb 28 2011 Alexey Tourbin <at@altlinux.ru> 1.1.11-alt4
- rebuilt for pkgconfig

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 1.1.11-alt3
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.11-alt2
- devel: fixed pkg-config requires

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.11-alt1
- 1.1.11

* Fri Aug 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.10-alt1
- 1.1.10

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.9-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sat Aug 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1.9-alt1
- 1.1.9

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Sat Jun 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5.2-alt5
- CVS snapshot 2006-04-06

* Sun Mar 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5.2-alt4
- https://bugs.freedesktop.org/show_bug.cgi?id=4439

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5.2-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5.2-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5.2-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5.1-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5-alt0.1
- initial build

