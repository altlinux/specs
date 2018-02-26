Name: xorg-util-macros
Version: 1.17
Release: alt1
Summary: X.Org X11 Autotools macros
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: util-macros = %version-%release
BuildArch: noarch

%description
X.Org X11 autotools macros required for building the various packages that
comprise the X Window System

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure
%make

%install
%make DESTDIR=%buildroot install

%files
%_datadir/aclocal/*.m4
%_datadir/pkgconfig/*.pc

%changelog
* Fri Mar 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.17-alt1
- 1.17

* Wed Mar 07 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.16.2-alt1
- 1.16.2

* Mon Jan 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.16.1-alt1
- 1.16.1

* Fri Jul 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.15.0-alt1
- 1.15.0

* Sun May 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Wed Apr 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.13.0-alt1
- 1.13.0

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Fri Sep 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Wed Aug 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Wed Jun 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Thu Jun 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Mon Apr 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Thu Mar 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Sun Feb 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Thu Jan 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Sat Jan 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Tue Dec 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Sat Sep 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Fri Jun 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Wed Dec 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sat Nov 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Jun 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.6-alt2
- rename xorg-x11-util-macros to xorg-util-macros

* Thu Mar 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Fri Dec 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Mon Aug 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Fri Jul 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue May 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

