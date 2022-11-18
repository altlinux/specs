Name: libupnpp
Version: 0.22.3
Release: alt1

Summary: C++ wrapper for libupnp
License: LGPLv2.1
Group: System/Libraries
Url: http://www.lesbonscomptes.com/upmpdcli

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: libcurl-devel libexpat-devel libnpupnp-devel >= 5.0

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
rm -vf %buildroot%_libdir/*.a

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/libupnpp
%_pkgconfigdir/libupnpp.pc

%changelog
* Fri Nov 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.3-alt1
- 0.22.3 released

* Mon Aug 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.2-alt1
- 0.22.2 released

* Tue Sep 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21.0-alt1
- 0.21.0 released

* Wed Sep 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17.1-alt2
- rebuilt with libupnp-1.14

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
