Name: libXau
Version: 1.0.7
Release: alt1
Summary: Xau Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-xproto-devel xorg-util-macros

%description
X authority database routines

%package devel
Summary: Xau Libraries and Header Files
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
%_includedir/X11/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Wed Mar 07 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Mon Feb 07 2011 Alexey Tourbin <at@altlinux.ru> 1.0.6-alt3
- rebuilt for debuginfo

* Sun Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt2
- rebuild

* Fri Jul 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Fri Aug 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Aug 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Jul 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Sun Nov 20 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial build

