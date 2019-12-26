Name: libupnpp
Version: 0.17.1
Release: alt1

Summary: C++ wrapper for libupnp
License: LGPLv2.1
Group: System/Libraries
Url: http://www.lesbonscomptes.com/upmpdcli

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libcurl-devel libexpat-devel libupnp-devel

%description
libupnpp defines useful objects over libupnp and can be used
to create both devices and control points.
This package contains %name shared library

%package devel
Summary: C++ wrapper for libupnp
Group: Development/C++
Requires: %name = %version-%release
Requires: libupnp-devel

%description devel
libupnpp defines useful objects over libupnp and can be used
to create both devices and control points.
This package contains development part of %name

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/libupnpp
%_pkgconfigdir/libupnpp.pc

%changelog
* Tue Dec 24 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17.1-alt1
- 0.17.1 released

* Thu Sep 20 2018 Alexey Shabalin <shaba@altlinux.org> 0.16.1-alt1
- 0.16.1 released

* Mon Dec 26 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.15.1-alt1
- 0.15.1 released

* Mon Sep 05 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.1-alt1
- 0.14.1 released

* Tue Jan 26 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.1-alt1
- initial
