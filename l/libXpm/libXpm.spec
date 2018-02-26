Name: libXpm
Version: 3.5.10
Release: alt1
Summary: X Pixmap Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: xpm = %version-%release
Obsoletes: xpm < %version-%release

BuildRequires: libSM-devel libXext-devel libXt-devel xmlto xorg-util-macros xorg-sgml-doctools

%description
This package contains the XPM pixmap library for the X Window System.
The XPM library allows applications to display color, pixmapped images,
and is used by many popular X programs.

%package devel
Summary: Xpm Libraries and Header Files
Group: Development/C
Requires: %name = %version-%release
Provides: xpm-devel = %version-%release
Obsoletes: xpm-devel < %version-%release

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
%_bindir/*
%_libdir/*.so.*
%_man1dir/*

%files devel
%doc doc/README.html doc/FAQ.html doc/xpm.PS.gz
%_includedir/X11/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.10-alt1
- 3.5.10

* Wed Mar 02 2011 Alexey Tourbin <at@altlinux.ru> 3.5.9-alt2
- rebuilt for debuginfo

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.5.9-alt1
- 3.5.9

* Fri Oct 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.5.8-alt1
- 3.5.8

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.5.7-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Aug 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.5.7-alt1
- 3.5.7

* Fri Feb 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.5.6-alt2
- added documentations (close #8991)

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 3.5.6-alt1
- 3.5.6

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 3.5.5-alt1
- 3.5.5

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 3.5.4.2-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 3.5.4.2-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 3.5.4.2-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 3.5.4.1-alt1
- Xorg-7.0RC3

* Sun Nov 20 2005 Valery Inozemtsev <shrek@altlinux.ru> 3.5.4-alt0.1
- initial build

