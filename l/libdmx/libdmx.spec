Name: libdmx
Version: 1.1.2
Release: alt1
Summary: The dmx Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel xorg-dmxproto-devel xorg-util-macros xmlto xorg-sgml-doctools

%description
The dmx Library

%package devel
Summary: The dmx Library and Header Files
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
%_includedir/X11
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt2
- devel: fixed pkg-config requires

* Fri Oct 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt4
- CVS snapshot 2006-04-06

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

