Name: libXdamage
Version: 1.1.3
Release: alt4
Summary: X Damage Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXfixes-devel xorg-damageproto-devel xorg-xextproto-devel xorg-util-macros

%description
X Damage Library

%package devel
Summary: X Damage Library and Header Files
Group: Development/C
Requires: %name = %version-%release
Conflicts: XFree86-devel < 4.4 xorg-x11-devel <= 6.9.0

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

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

%changelog
* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 1.1.3-alt4
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt3
- devel: fixed pkg-config requires

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt2
- rebuild

* Wed Jun 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Tue Oct 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Thu Jan 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- 1.1

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Tue Oct 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- added libXdamage-1.0.3-git-LockUnlockDisplay.patch

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2.2-alt4
- CVS snapshot 2006-04-02

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2.2-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2.2-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2.2-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2.1-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt0.1
- initial build

