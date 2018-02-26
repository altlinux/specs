%define _name e_dbus
%def_disable static

Name: edbus
Version: 1.2.0
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: Enlightenment DBUS access library
License: BSD-like
Group: System/Libraries
Url: http://www.enlightenment.org/

Source: http://download.enlightenment.org/releases/%_name-%version.tar.bz2

Requires: lib%name = %version-%release

%{?_enable_static:BuildPreReq: glibc-devel-static}

BuildRequires: libdbus-devel  libevas-devel >= 1.2.0
BuildRequires: libecore-devel >= 1.2.0 libeina-devel >= 1.2.0

%description
This is the start of some basic convenience wrappers around dbus to ease
integrating dbus with EFL based applications.

%package -n lib%name
Summary: Enlightenment DBUS access library
Group: System/Libraries

%description -n lib%name
This is the start of some basic convenience wrappers around dbus to ease
integrating dbus with EFL based applications.

This package contains shared library required for %name-based software.

%package -n lib%name-devel
Summary: Include files for development with Enlightenment DBUS Library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This is the start of some basic convenience wrappers around dbus to ease
integrating dbus with EFL based applications.

This package contains include files required for development %name-based software.

%package -n lib%name-devel-static
Summary: Static library for development with Enlightenment DBUS Library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This is the start of some basic convenience wrappers around dbus to ease
integrating dbus with EFL based applications.

This package contains static library required for development statically linked
%name-based software.

%prep
%ifdef beta
%setup -q -n %_name-%version.%beta
%else
%setup -q -n %_name-%version
%endif

%build
%autoreconf
%configure \
	%{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*

%files -n lib%name
%_libdir/*.so.*
%_datadir/e_dbus/logo.png
%doc AUTHORS COPYING README

%files -n lib%name-devel
%_pkgconfigdir/*.pc
%_libdir/*.so
%_includedir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt2
- used %%autoreconf to fix RPATH problem

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt5
- rebuilt for debuginfo

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt4
- 1.0.0 release

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt3.beta2
- 1.0.0.beta2

* Tue Nov 09 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2.beta
- rebuild for update dependencies

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1.beta
- 1.0.0.beta

* Mon Jan 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.0.063-alt1
- 0.5.0.063

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 0.5.0.062-alt1
- new version
- removed obsolete %%post{,un}_ldconfig

* Sat Oct 18 2008 Yuri N. Sedunov <aris@altlinux.org> 0.5.0.050-alt1
- 0.5.0.050

* Wed Sep 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.1.0.003-alt1.20070919
- CVS from 20070919.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.1.0.002-alt1.20070731
- Initial build for Sisyphus.

