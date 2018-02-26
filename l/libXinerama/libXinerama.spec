Name: libXinerama
Version: 1.1.2
Release: alt1
Summary: The Xinerama Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel xorg-xineramaproto-devel xmlto xorg-util-macros xorg-sgml-doctools

%description
The Xinerama Library

%package devel
Summary: The Xinerama Library and Header Files
Group: Development/C
Requires: %name = %version-%release
Conflicts: xorg-xineramaproto-devel < 1.2

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

* Wed Mar 02 2011 Alexey Tourbin <at@altlinux.ru> 1.1.1-alt4
- rebuilt for pkgconfig

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 1.1.1-alt3
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt2
- devel: fixed pkg-config requires

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Sat Oct 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- 1.1

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Mar 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Sep 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3.1
- rebuilt for new pkg-config dependencies.

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

