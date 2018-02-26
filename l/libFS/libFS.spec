Name: libFS
Version: 1.0.4
Release: alt1
Summary: Library Interface to the X Font Server
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-fontsproto-devel xorg-xproto-devel xorg-xtrans-devel xorg-util-macros

%description
Library Interface to the X Font Server

%package devel
Summary: X Font Server Library and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%def_enable ipv6

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	%{subst_enable ipv6} \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/X11/fonts
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sun Mar 04 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Thu Jun 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- enabled ipv6

* Wed Oct 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Wed Jul 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri May 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial build

