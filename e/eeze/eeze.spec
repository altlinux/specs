%def_disable static

Name: eeze
Version: 1.2.0
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: Enlightenment hardware manipulating library
License: BSD-like
Group: System/Libraries
Url: http://www.enlightenment.org/

Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

Requires: lib%name = %version-%release

%{?_enable_static:BuildPreReq: glibc-devel-static}
BuildRequires: libudev-devel libeina-devel >= 1.2.0 libecore-devel >= 1.2.0

%description
Eeze is a library for manipulating devices through udev with a simple
and fast api. It interfaces directly with libudev, avoiding such
middleman daemons as udisks/upower or hal, to immediately gather device
information the instant it becomes known to the system.

%package -n lib%name
Summary: Enlightenment hardware manipulating library
Group: System/Libraries

%description -n lib%name
Eeze is a library for manipulating devices through udev with a simple
and fast api. It interfaces directly with libudev, avoiding such
middleman daemons as udisks/upower or hal, to immediately gather device
information the instant it becomes known to the system.

This package contains shared library required for %name-based software.

%package -n lib%name-devel
Summary: Include files for development with Eeze Library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Eeze is a library for manipulating devices through udev with a simple
and fast api. It interfaces directly with libudev, avoiding such
middleman daemons as udisks/upower or hal, to immediately gather device
information the instant it becomes known to the system.

This package contains include files required for development %name-based software.

%package -n lib%name-devel-static
Summary: Static library for development with Eeze Library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Eeze is a library for manipulating devices through udev with a simple
and fast api. It interfaces directly with libudev, avoiding such
middleman daemons as udisks/upower or hal, to immediately gather device
information the instant it becomes known to the system.

This package contains static library required for development statically linked
%name-based software.

%prep
%ifdef beta
%setup -q -n %name-%version.%beta
%else
%setup -q
%endif

%build
%configure \
	%{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS COPYING README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Wed Aug 10 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sat Mar 19 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt4
- 1.0.0 release

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt3.beta2
- 1.0.0.beta2

* Tue Nov 09 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2.beta
- rebuild for update dependencies

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1.beta
- first build for Sisyphus

