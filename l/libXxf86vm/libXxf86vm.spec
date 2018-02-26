Name: libXxf86vm
Version: 1.1.2
Release: alt1

Summary: XFree86 Video Mode Extension Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel xorg-xf86vidmodeproto-devel xorg-util-macros xmlto xorg-sgml-doctools

%description
XFree86 Video Mode Extension Library

%package devel
Summary: XFree86 Video Mode Extension Library and Header Files
Group: Development/C
Requires: %name = %version-%release
Conflicts: xorg-xf86vidmodeproto-devel < 2.3

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
* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Sat Mar 19 2011 Alexey Tourbin <at@altlinux.ru> 1.1.1-alt4
- rebuilt for pkgconfig

* Thu Feb 10 2011 Alexey Tourbin <at@altlinux.ru> 1.1.1-alt3
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt2
- devel: fixed pkg-config requires

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Jul 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sun Jun 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- Just leave vendor and model NULL if the response didn't include them

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial build

