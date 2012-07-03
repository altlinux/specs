Name: libXfixes
Version: 5.0
Release: alt1
Summary: X Fixes Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel xorg-fixesproto-devel xorg-xextproto-devel xorg-util-macros

%description
X Fixes Library

%package devel
Summary: X Fixes Library and Header Files
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
%_includedir/X11/extensions
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Mon Mar 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 5.0-alt1
- 5.0

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 4.0.5-alt4
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.0.5-alt3
- devel: fixed pkg-config requires

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.0.5-alt2
- rebuild

* Thu Jun 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 4.0.3-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Tue Oct 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 4.0.2-alt2
- added libXfixes-4.0.2-git-LockUnlockDisplay.patch

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Mon Sep 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 4.0-alt2
- CVS snapshot 2006-04-02

* Tue Mar 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 4.0-alt1
- 4.0

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 3.0.1.2-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 3.0.1.2-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 3.0.1.2-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 3.0.1.1-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 3.0.1-alt0.1
- initial build

