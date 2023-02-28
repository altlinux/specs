Name: libnpupnp
Version: 5.0.1
Release: alt1

Summary: UPnP library derived from the pupnp
License: BSD
Group: System/Libraries
Url: https://framagit.org/medoc92/npupnp

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: libcurl-devel libexpat-devel libmicrohttpd-devel

%package devel
Summary: Development libraries and header files for libupnp
Group: Development/C

%define desc \
npupnp (new pupnp or not pupnp ?) is an UPnP library derived from the \
venerable pupnp (https://github.com/pupnp/pupnp), based on its 1.6.x \
branch (around 1.6.25).

%description %desc

%description devel %desc
This package contains libraries and header files needed to develop
applications using libnpupnp.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/libnpupnp.so.*

%files devel
%doc README.md
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Tue Feb 28 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.1-alt1
- 5.0.1 released

* Mon Aug 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0-alt1
- 5.0 released

* Mon Apr 25 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.1-alt1
- 4.2.1 released

* Tue Nov 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.5-alt1
- 4.1.5 released

* Tue Sep 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.4-alt1
- initial
