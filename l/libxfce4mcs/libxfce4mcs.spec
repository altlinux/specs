Name: libxfce4mcs
Version: 4.4.3
Release: alt3

Summary: Multi-channel settings management support for XFce
License: LGPL
Group: Development/C
Url: http://www.xfce.org
Packager: Eugene Ostapets <eostapets@altlinux.ru>

Source: ftp://ftp.berlios.de/pub/xfce-goodies/%version/%name-%version.tar.bz2

Requires: libxfce4util >= %version

# Automatically added by buildreq on Sun Nov 09 2008
BuildRequires: gcc-c++ gtk-doc imake libSM-devel libX11-devel libstartup-notification-devel libxfce4util-devel xfce4-dev-tools xorg-cf-files

%description
Multi-channel settings management support for XFce.

%package devel
Summary: Development files for %name
Group: Development/C
License: LGPL
PreReq: %name = %version-%release

%description devel
Header files for the %name library.

%prep
%setup

%build
libtoolize --force --copy
aclocal -I %_datadir/xfce4/dev-tools/m4macros
automake -acf
autoconf
%configure \
	--enable-gtk-doc \
	--enable-startup-notification \
	--disable-debug
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog
%_libdir/*.so.*

%files devel
%doc %_datadir/gtk-doc/html/%name
%dir %_includedir/xfce4/libxfce4mcs
%_includedir/xfce4/libxfce4mcs/*
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.3-alt3
- Rebuilt for debuginfo

* Wed Nov 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.3-alt2
- Rebuilt for soname set-versions

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 4.4.3-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libxfce4mcs
  * postun_ldconfig for libxfce4mcs

* Sun Nov 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 4.4.3-alt1
- Xfce 4.4.3 release

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  4.3.99.1-alt2
- Fix buildreq and cleanup spec

* Wed Sep 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- new version 4.4rc1

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.3-alt1.1
- Rebuilt for new pkg-config dependencies.

* Thu Nov 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Thu Mar 17 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Fri Dec 24 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.99.3-alt1
- 4.1.99.3

* Mon Nov 01 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.91-alt1
- 4.1.91

* Wed Jul 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Sat Apr 17 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 16 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Mon Dec 22 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.2-alt1
- 4.0.2
- Do not package %name-devel-static by default.

* Sun Dec 07 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.1-alt2
- *.la files removed.

* Tue Nov 18 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Fri Sep 26 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt1
- 3.99.4

* Fri Aug 29 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt0.9
- 3.99.3

* Sun Aug 17 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.2-alt0.9
- 3.99.2

* Mon Jul 14 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.1-alt0.9
- 3.99.1

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 3.90.0-alt0.9
- First version of RPM package for Sisyphus.
- Spec derived from original version.
