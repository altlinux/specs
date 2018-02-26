%def_disable static

Name: edje
Version: 1.2.1
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: Complex Graphical Design/Layout Engine
License: BSD
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org

Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2
# temporarily fix for
# /usr/include/bits/string3.h:52:3: error: call to __builtin___memcpy_chk will always overflow destination buffer
# at edje_calc.c
Patch: edje-1.1.0-alt-buffer-overflow.patch

%{?_enable_static:BuildPreReq: glibc-devel-static}

Requires: shared-mime-info
Requires: lib%name = %version-%release

BuildRequires: libeina-devel >= 1.2.0
BuildPreReq: libecore-devel >= 1.2.0
BuildPreReq: libembryo-devel >= 1.2.0
BuildPreReq: libevas-devel >= 1.2.0
BuildPreReq: libeet-devel >= 1.6.0
BuildRequires: liblua5-devel libsndfile-devel

%description
Edje purpose is to be a sequel to "Ebits" which to date has serviced the
needs of Enlightenment development for version 0.17. The original design
paramteres under which Ebits came about were a lot more restricted than
the resulting use of them, thus Edje was born. A graphical layout and
animation library for animated resizable, compressed and scalable themes.

%package -n lib%name
Summary: edje library
Group: System/Libraries

%description -n lib%name
Edje purpose is to be a sequel to "Ebits" which to date has serviced the
needs of Enlightenment development for version 0.17. The original design
paramteres under which Ebits came about were a lot more restricted than
the resulting use of them, thus Edje was born. A graphical layout and
animation library for animated resizable, compressed and scalable themes.

This package contains shared Edje library.

%package -n lib%name-devel
Summary: Edje headers and development libraries
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Edje purpose is to be a sequel to "Ebits" which to date has serviced the
needs of Enlightenment development for version 0.17. The original design
paramteres under which Ebits came about were a lot more restricted than
the resulting use of them, thus Edje was born. A graphical layout and 
animation library for animated resizable, compressed and scalable themes.

This package contains edje headers and development libraries

%package -n lib%name-devel-static
Summary: Edje static libraries
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Edje purpose is to be a sequel to "Ebits" which to date has serviced the
needs of Enlightenment development for version 0.17. The original design
paramteres under which Ebits came about were a lot more restricted than
the resulting use of them, thus Edje was born. A graphical layout and 
animation library for animated resizable, compressed and scalable themes.

This package contains static libraries

%prep
%ifdef beta
%setup -q -n %name-%version.%beta
%else
%setup -q
%endif

%patch

%build
%autoreconf
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure %{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n %name
%_bindir/*
%_datadir/%name/
%_datadir/mime/packages/edje.xml
%dir %_libdir/%name/
%dir %_libdir/%name/utils
%_libdir/%name/utils/epp
%doc AUTHORS COPYING README

%files -n lib%name
%_libdir/*.so.*
%dir %_libdir/%name/modules
%dir %_libdir/%name/modules/multisense_factory
%dir %_libdir/%name/modules/multisense_factory/*
%_libdir/%name/modules/multisense_factory/*/module.so
%exclude %_libdir/%name/modules/multisense_factory/*/module.la

%files -n lib%name-devel
%_includedir/*
%_pkgconfigdir/%name.pc
%_libdir/*.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif


%changelog
* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.1
- Rebuild with Python-2.7

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt5
- rebuilt for debuginfo

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt4
- 1.0.0 release

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt3.beta2
- 1.0.0.beta

* Tue Nov 09 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2.beta
- rebuild for update dependencies

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1.beta
- 1.0.0.beta

* Mon Jan 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.93.063-alt1
- 0.9.93.063

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 0.9.92.062-alt1
- new version
- removed obsolete %%post{,un}_ldconfig

* Sat Oct 18 2008 Yuri N. Sedunov <aris@altlinux.org> 0.9.9.050-alt1
- 0.9.9.050

* Mon Sep 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0.041-alt1.20070917
- CVS from 20070917.

* Thu Sep 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0.041-alt1.20070905
- CVS from 20070905.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0.040-alt1.20070731
- CVS from 20070731.
- Minor spec cleanup.
- Stricted BR.

* Wed May 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0.038-alt1.20070509
- CVS from 20070509.
- Fix BuildRequires.

* Wed Sep 20 2006 Igor Zubkov <icesik@altlinux.org> 0.5.0.032-alt1.20060920
- 20060910 -> 20060920

* Tue Sep 12 2006 Igor Zubkov <icesik@altlinux.org> 0.5.0.032-alt1.20060910
- update from cvs (0.5.0 20060327 -> 0.5.0.32 20060910)
- buildreq

* Mon Apr 10 2006 Igor Zubkov <icesik@altlinux.ru> 0.5.0-alt0.2_003_20060327
- updated from cvs
- buildreq

* Mon May 30 2005 Denis Klykvin <nikon@altlinux.ru> 0.5.0-alt0.2_003_20050530
- updated from cvs.

* Tue May 24 2005 Denis Klykvin <nikon@altlinux.ru> 0.5.0-alt0.2_003_20050524
- updated from cvs.

* Mon May 16 2005 Denis Klykvin <nikon@altlinux.ru> 0.5.0-alt0.2_003_20050516
- updated from cvs.

* Sat May 14 2005 Denis Klykvin <nikon@altlinux.ru> 0.5.0-alt0.2_003_20050514
- updated from cvs.

* Thu Apr 28 2005 Denis Klykvin <nikon@altlinux.ru> 0.5.0-alt0.2_003_20050428
- updated from cvs.
- minor spec fixes.

* Mon Apr 25 2005 Denis Klykvin <nikon@altlinux.ru> 0.5.0-alt0.2_003_20050425
- updated from cvs.

* Thu Apr 21 2005 Denis Klykvin <nikon@altlinux.ru> 0.5.0-alt0.2_003_20050421
- updated from cvs

* Tue Mar 29 2005 Alex Murygin <murygin@altlinux.ru> 0.5.0-alt0.2_003_20050329
- updated from cvs.

* Sat Jan 22 2005 Alex Murygin <murygin@altlinux.ru> 0.5.0-alt0.1_20050122
- updated from cvs.

* Tue Dec 28 2004 Alex Murygin <murygin@altlinux.ru> 0.5.0-alt0.1_20041228
- updated from cvs.

* Fri Dec 17 2004 Alex Murygin <murygin@altlinux.ru> 0.5.0-alt0.1_20041216
- updated from cvs.

* Sun Oct 24 2004 Alex Murygin <murygin@altlinux.ru> 0.5.0-alt0.1_20041022
- First build for Sisyphus.

