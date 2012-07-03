Name: libXevie
Version: 1.0.3
Release: alt1
Summary: X Event Interceptor Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel xorg-evieproto-devel xorg-util-macros

%description
X Event Interceptor Library

%package devel
Summary: X Event Interceptor Library and Header Files
Group: Development/C
Requires: %name = %version-%release
Conflicts: XFree86-devel < 4.4 xorg-x11-devel <= 6.9.0

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
%_includedir/X11/extensions
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Sun Oct 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Sep 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial build

