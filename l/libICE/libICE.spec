Name: libICE
Version: 1.0.8
Release: alt1
Summary: X Inter Client Exchange Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xmlto xorg-xproto-devel xorg-xtrans-devel xorg-util-macros xorg-sgml-doctools

%description
X Inter Client Exchange Library

%package devel
Summary: X ICE Library and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

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
%_docdir/%name
%_includedir/X11/ICE
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sun Mar 04 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Thu Jun 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt3
- enabled ipv6

* Mon Feb 14 2011 Alexey Tourbin <at@altlinux.ru> 1.0.7-alt2
- rebuilt for debuginfo
- packaged docs

* Wed Oct 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Fri Aug 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Wed Jan 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Aug 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4
- drop upstream patches

* Mon May 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- added libICE-1.0.3-Double-free-Coverity1085.patch,
	libICE-1.0.3-Double-free-Coverity1086.patch,
	libICE-1.0.3-git-replace-many-malloc.patch

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt3
- CVS snapshot 2006-04-10

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial build

