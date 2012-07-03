Name: libXaw
Version: 1.0.11
Release: alt1
Summary: X Athena Widgets Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXext-devel libXmu-devel libXpm-devel xmlto xorg-util-macros xorg-sgml-doctools

%description
X Athena Widgets Library

%package devel
Summary: X Athena Widgets Library and Header Files
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
	--disable-xaw6 \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%dir %_docdir/%name
%_docdir/%name/*.html
%_includedir/X11/Xaw
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Sat Jun 02 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Fri Mar 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.9-alt2
- rebuild for debuginfo

* Wed Jan 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt2
- devel: fixed pkg-config requires

* Tue Oct 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Sun Oct 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Thu Jul 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt3
- updated build dependencies

* Fri Nov 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Nov 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Fri Nov 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt2
- devel: drop libXaw8.so/xaw8.pc

* Wed Aug 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Thu Jan 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

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

