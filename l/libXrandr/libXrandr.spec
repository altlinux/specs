Name: libXrandr
Version: 1.3.2
Release: alt1

Summary: X RandR Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXext-devel libXrender-devel xorg-randrproto-devel xorg-util-macros

%description
X RandR Library

%package devel
Summary: X RandR Library and Header Files
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
%_includedir/X11/extensions
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Thu Jun 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Wed Mar 02 2011 Alexey Tourbin <at@altlinux.ru> 1.3.1-alt5
- rebuilt for pkgconfig

* Wed Feb 16 2011 Alexey Tourbin <at@altlinux.ru> 1.3.1-alt4
- disabled symbol versioning

* Thu Feb 10 2011 Alexey Tourbin <at@altlinux.ru> 1.3.1-alt3
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt2
- devel: fixed pkg-config requires

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt2
- GIT snapshot 2010-03-29 (7a7bac907ac15033c0ddb979202c7f3ddc368726)

* Fri Mar 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Mon Feb 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.99.4-alt2
- fixed XRRGetOutputPrimary

* Tue Jan 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.99.4-alt1
- 1.3 RC4

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.3-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Jul 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Tue Jun 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt2
- Ignore ConfigureNotify on non-root windows in UpdateConfiguration (fd.o #16430)

* Thu Sep 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Tue Mar 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0.2-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0.2-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0.2-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0.1-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial build

