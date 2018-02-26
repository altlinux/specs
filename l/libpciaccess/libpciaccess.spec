Name: libpciaccess
Version: 0.13.1
Release: alt1
Epoch: 1
Summary: X.org libpciaccess library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: pciids xorg-util-macros zlib-devel

%description
Library providing generic access to the PCI bus and devices

%package devel
Summary: The pciaccess Library and Header Files
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
	--with-pciids-path=%_datadir/misc \
	--with-zlib \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Tue Apr 10 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.13.1-alt1
- 0.13.1

* Sun Mar 04 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.13-alt1
- 0.13

* Wed Feb 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.12.1-alt2
- rebuild

* Thu Feb 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.12.1-alt1
- 0.12.1

* Sun Oct 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.12.0-alt3
- dropped version script

* Sat Sep 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.12.0-alt2
- required pciids

* Fri Jul 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.12.0-alt1
- 0.12.0

* Mon Apr 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.11.0-alt2
- introduced LIBPCIACCESS_0.11.0 ABI for new functions in libpciaccess.so.0;
  also restricted the list of symbols exported by the library

* Tue Dec 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.11.0-alt1
- 0.11.0

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.9-alt1
- 0.10.9

* Mon Aug 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.8-alt1
- 0.10.8

* Fri Aug 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.7-alt1
- 0.10.7

* Sat Apr 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.6-alt1
- 0.10.6

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.5-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Oct 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.5-alt1
- 0.10.5

* Sun Oct 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.4-alt2
- disable write combine support (close #17623)

* Sat Oct 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.4-alt1
- 0.10.4

* Wed Jun 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.3-alt1
- 0.10.3

* Thu May 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.2-alt1
- 0.10.2

* Wed May 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.1-alt1
- 0.10.1

* Fri Apr 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10-alt2
- Fix reads from "0"-sized ROMs
- Fix function prototypes for C++

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10-alt1
- 0.10 release

* Thu Nov 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.10.0-alt2
- GIT snapshot 2007-10-23 (e392082abb5696c8837224da86cc0af4f21d7010)

* Fri Sep 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Tue Aug 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Sat Mar 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.8.0-alt1
- initial release
