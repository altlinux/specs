Name: libXv
Version: 1.0.12
Release: alt1
Summary: The Xv Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel xorg-proto-devel xorg-util-macros xorg-sgml-doctools xmlto

%description
The Xv Library

%package devel
Summary: The Xv Library and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup -q

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
%_includedir/X11/extensions
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Mon Dec 05 2022 Valery Inozemtsev <shrek@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Tue May 29 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Thu Jan 30 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Sun Jun 23 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Tue Jun 04 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Wed Mar 09 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt3
- rebuild

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt2
- devel: fixed pkg-config requires

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Sat Oct 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Mar 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Tue Sep 26 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sun Sep 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt4
- Coverity CID #580: XvQueryEncodings Returned without freeing storage "pes"

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial build

