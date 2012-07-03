Name: libXxf86dga
Version: 1.1.3
Release: alt1
Summary: XFree86 Direct Graphics Access Extension Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel xorg-xf86dgaproto-devel xorg-util-macros xorg-sgml-doctools xmlto

%description
XFree86 Direct Graphics Access Extension Library

%package devel
Summary: XFree86 Direct Graphics Access Extension Library and Header Files
Group: Development/C
Requires: %name = %version-%release
Conflicts: xorg-xf86dgaproto-devel < 2.1

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
%_includedir/X11
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt2
- devel: fixed pkg-config requires

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Tue Oct 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- 1.1

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Sep 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
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

