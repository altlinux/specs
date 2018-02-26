Name: libXdmcp
Version: 1.1.1
Release: alt1
Summary: Xdmcp Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xmlto xorg-sgml-doctools xorg-xproto-devel xorg-util-macros

%description
X Display Manager Control Protocol library

%package devel
Summary: Xau Libraries and Header Files
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
%dir %_docdir/%name
%_docdir/%name/*.html
%_includedir/X11/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Apr 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Feb 07 2011 Alexey Tourbin <at@altlinux.ru> 1.1.0-alt2
- rebuilt for debuginfo

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- rebuild

* Thu Sep 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sun Aug 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Sun Nov 20 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial build

