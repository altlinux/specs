Name: libquantum
Version: 1.1.0
Release: alt1

Summary: The C library for quantum computing and quantum simulation

License: GPL
Group: Development/C
Url: http://www.libquantum.de

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.libquantum.de/files/%name-%version.tar

%description
libquantum is a C library for quantum computing and quantum
simulation. It provides quantum registers, unitary operations, time
evolution, and measurement functions. The main goal is a physically
precise simulation of a quantum system with high performance.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files required
in development of the %name-based applications.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std LIBDIR=%buildroot%_libdir

%files
%doc README CHANGES
%_libdir/*.so.*

%files devel
%_includedir/quantum.h
%_libdir/*.so

%changelog
* Wed Mar 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Sun Jan 25 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Mon May 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt2
- fix description
- fix build on x86_64

* Sun May 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- initial build for ALT Linux Sisyphus

