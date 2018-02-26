Name: libXt
Version: 1.1.3
Release: alt1
Summary: X Toolkit Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libSM-devel libX11-devel xmlto xorg-util-macros xorg-sgml-doctools

%description
X Toolkit Library

%package devel
Summary: X Toolkit Library and Header Files
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
	--with-appdefaultdir=%_sysconfdir/X11/app-defaults \
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
%_man3dir/*

%changelog
* Fri Mar 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Wed Mar 14 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt2
- fixed regressions (closes: #27071)

* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Mon Mar 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Feb 14 2011 Alexey Tourbin <at@altlinux.ru> 1.0.9-alt3
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.9-alt2
- devel: fixed pkg-config requires

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Tue Mar 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Fri Oct 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Thu Jul 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sun Jan 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sun Sep 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- added libXt-1.0.2-git-memleak.patch

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial build

