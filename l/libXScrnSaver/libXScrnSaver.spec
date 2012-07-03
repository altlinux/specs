Name: libXScrnSaver
Version: 1.2.2
Release: alt1

Summary: X11 Screen Saver extension client library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel xorg-scrnsaverproto-devel xmlto xorg-util-macros xorg-sgml-doctools

%description
X.Org X11 Screen Saver extension client runtime library.

%package devel
Summary: XScrnSaver Library and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains library, header file and documentation
needed to develop programs which make use of %name.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/X11/extensions/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sat Mar 19 2011 Alexey Tourbin <at@altlinux.ru> 1.2.1-alt4
- Rebuilt for pkgconfig.

* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt3
- Rebuilt for debuginfo.

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt2
- devel: fixed pkg-config requires

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Mar 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Sat Apr 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial build

