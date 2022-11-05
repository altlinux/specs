%define srcname pixman

Name: libpixman
Version: 0.42.2
Release: alt1
Epoch: 3
Summary: Pixel manipulation library
License: MIT
Group: System/Libraries
Url: http://xorg.freedesktop.org

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %srcname-%version.tar
Patch: %srcname-%version-%release.patch
Patch2000: %name-e2k.patch

BuildRequires: libpng-devel

%description
Pixman is a pixel manipulation library for X and cairo

%package devel
Summary: Pixel manipulation library development package
Group: Development/C
Requires: %name = %epoch:%version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup -q -n %srcname-%version
%patch -p1
%ifarch %e2k
%patch2000 -p1
%endif

%build
%autoreconf
%configure \
	--disable-static
%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sat Nov 05 2022 Valery Inozemtsev <shrek@altlinux.ru> 3:0.42.2-alt1
- 0.42.2 (fixed CVE-2022-44638)

* Wed Oct 19 2022 Valery Inozemtsev <shrek@altlinux.ru> 3:0.42.0-alt1
- 0.42.0

* Wed Jul 28 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3:0.40.0-alt2
- added patch for Elbrus

* Mon Apr 27 2020 Valery Inozemtsev <shrek@altlinux.ru> 3:0.40.0-alt1
- 0.40.0

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 3:0.38.4-alt1
- 0.38.4

* Tue Feb 12 2019 Valery Inozemtsev <shrek@altlinux.ru> 3:0.38.0-alt1
- 0.38.0

* Wed Jan 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 3:0.36.0-alt1
- 0.36.0

* Tue Nov 29 2016 Valery Inozemtsev <shrek@altlinux.ru> 3:0.34.0-alt1
- 0.34.0

* Sun Nov 15 2015 Valery Inozemtsev <shrek@altlinux.ru> 3:0.32.8-alt1
- 0.32.8 (closes: #31472)

* Fri Sep 05 2014 Valery Inozemtsev <shrek@altlinux.ru> 3:0.32.6-alt1
- 0.32.6

* Mon Nov 18 2013 Valery Inozemtsev <shrek@altlinux.ru> 3:0.32.4-alt1
- 0.32.4

* Tue Nov 12 2013 Valery Inozemtsev <shrek@altlinux.ru> 3:0.32.2-alt1
- 0.32.2

* Thu Aug 08 2013 Valery Inozemtsev <shrek@altlinux.ru> 3:0.30.2-alt1
- 0.30.2

* Mon May 13 2013 Valery Inozemtsev <shrek@altlinux.ru> 3:0.30.0-alt1
- 0.30.0

* Tue Dec 11 2012 Valery Inozemtsev <shrek@altlinux.ru> 3:0.28.2-alt1
- 0.28.2

* Thu Nov 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 3:0.28.0-alt1
- 0.28.0

* Sun Jul 01 2012 Valery Inozemtsev <shrek@altlinux.ru> 3:0.26.2-alt1
- 0.26.2

* Sun May 27 2012 Valery Inozemtsev <shrek@altlinux.ru> 3:0.26.0-alt1
- 0.26.0

* Mon Apr 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 3:0.24.4-alt1
- 0.24.4

* Thu Jan 19 2012 Valery Inozemtsev <shrek@altlinux.ru> 3:0.24.2-alt1
- 0.24.2

* Mon Nov 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 3:0.24.0-alt1
- 0.24.0

* Tue Jul 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 3:0.22.2-alt1
- 0.22.2

* Mon May 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 3:0.22.0-alt1
- 0.22.0

* Tue Apr 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 3:0.21.8-alt1
- 0.21.8

* Thu Feb 24 2011 Valery Inozemtsev <shrek@altlinux.ru> 3:0.21.6-alt1
- 0.21.6

* Thu Feb 10 2011 Alexey Tourbin <at@altlinux.ru> 3:0.21.4-alt2
- rebuilt for debuginfo
- disabled symbol versioning

* Wed Jan 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 3:0.21.4-alt1
- 0.21.4

* Sun Nov 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:0.21.2-alt1
- 0.21.2

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:0.20.0-alt1
- 0.20.0

* Sun Oct 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:0.18.4-alt2
- rebuild

* Mon Aug 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:0.18.4-alt1
- 0.18.4

* Wed Jun 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:0.18.2-alt1
- 0.18.2

* Mon Apr 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 3:0.18.0-alt1
- 0.18.0

* Mon Jan 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:0.17.4-alt1
- 0.17.4

* Tue Dec 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:0.17.2-alt2
- ARM: added '.arch armv7a' directive to NEON assembly file

* Sun Nov 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:0.17.2-alt1
- 0.17.2

* Fri Oct 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:0.16.2-alt1
- 0.16.2

* Thu Sep 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:0.16.0-alt2
- enabled the x888_8_8888 sse2 fast path

* Sun Aug 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:0.16.0-alt1
- 0.16.0

* Wed Aug 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:0.15.20-alt1
- 0.15.20

* Tue Jul 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:0.15.18-alt1
- 0.15.18

* Tue Jul 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:0.15.16-alt1
- 0.15.16

* Thu Jun 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:0.15.14-alt1
- 0.15.14

* Sun Jun 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:0.15.10-alt2
- 0.15.10 (closes: #20516)

* Wed Jun 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.12-alt1
- 0.15.12

* Fri Jun 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.10-alt1
- 0.15.10

* Sun May 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.8-alt1
- 0.15.8

* Fri May 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.6-alt1
- 0.15.6

* Fri May 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.4-alt1
- 0.15.4

* Fri Apr 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.2-alt1
- 0.15.2

* Sun Feb 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.14.0-alt1
- 0.14.0

* Wed Nov 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.13.2-alt1
- 0.13.2

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.12.0-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.12.0-alt2
- rebuild with gcc4.3

* Fri Sep 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.12.0-alt1
- 0.12.0

* Sun Sep 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.11.10-alt1
- 0.11.10

* Wed Aug 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.11.8-alt1
- 0.11.8

* Wed Jun 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.11.6-alt1
- 0.11.6

* Fri Jun 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.0-alt3
- rollback to 0.10.0 (0.11.4 memory leaked)

* Wed Jun 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.11.4-alt1
- 0.11.4

* Thu May 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.0-alt2
- introduced PIXMAN_0.10.0 ABI interface for new functions in libpixman-1.so.0.10.0

* Fri Mar 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Wed Mar 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt3
- pixman-0.9.6-x-offset.patch: fix computation of x_offset in pixman_add_traps

* Wed Jan 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt2
- avoid use of C++ keyword xor in header (close #13899)

* Wed Oct 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Mon Oct 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9.5-alt2
- GIT snapshot 2007-09-29 (39a67d35f05aa47cf50191e0837a2125593a7bbc)

* Thu Sep 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9.5-alt1
- initial release
