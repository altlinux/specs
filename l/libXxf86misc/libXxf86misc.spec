Name: libXxf86misc
Version: 1.0.3
Release: alt1
Summary: XFree86 Misc Extension Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel xorg-xf86miscproto-devel xorg-util-macros

%description
XFree86 Misc Extension Library

%package devel
Summary: XFree86 Misc Extension Library and Header Files
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
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Mon Nov 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt4
- devel: fixed pkg-config requires

* Sun Sep 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3
- updated build dependencies

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial build

