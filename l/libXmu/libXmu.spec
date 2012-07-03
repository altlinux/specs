Name: libXmu
Version: 1.1.1
Release: alt1
Summary: Xmu Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel libSM-devel libXt-devel xmlto xorg-sgml-doctools xorg-util-macros xorg-xtrans-devel

%description
Xmu Library

%package devel
Summary: Xmu Library and Header Files
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
%_includedir/X11/Xmu
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Tue Mar 06 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Feb 28 2011 Alexey Tourbin <at@altlinux.ru> 1.1.0-alt3
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt2
- devel: fixed pkg-config requires

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Thu Sep 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Jan 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sun Sep 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1
- fixed build dependencies

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

