Name: libpki
Version: 0.8.9
Release: alt1

Summary: Library for PKI enabled application development.
License: %asl
Group: System/Libraries
Url: https://pki.openca.org/projects/libpki/
Packager: Vladimir Didenko <cow@altlinux.ru>

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: libssl-devel
BuildRequires: libxml2-devel
BuildRequires: libldap-devel
BuildRequires: libmysqlclient-devel
BuildRequires: postgresql-devel

%description
The LibPKI Project is aimed to provide an easy-to-use PKI library for PKI
enabled application development. The library provides the developer with
all the needed functionalities to manage certificates, from generation
to validation. The LibPKI Project enables developers with the possibility
to implement complex cryptographic operations with a few simple function
calls by implementing an high-level cryptographic API.

%package tools
Summary: Auxiliary tools for LibPKI
Group: Development/C

%description tools
This package contains auxiliary tools for PKI library

%package devel
Summary: Header files and library for development with LibPKI
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the header files and development libraries needed
to develop programs that use the PKI library.

%package devel-static
Summary: The PKI static library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains the PKI static library.

%prep
%setup -n %name-%version
%patch0 -p1

%build
%autoreconf
%configure
%make

%install
%makeinstall_std

rm -fr %buildroot%_includedir/%name/drivers/kmf

%files
%config(noreplace) %_sysconfdir/%name/*.xml
%config(noreplace) %_sysconfdir/%name/hsm.d/*.xml
%config(noreplace) %_sysconfdir/%name/profile.d/*.xml
%config(noreplace) %_sysconfdir/%name/store.d/*.xml
%config(noreplace) %_sysconfdir/%name/token.d/*.xml
%config(noreplace) %_sysconfdir/pki.conf
%_libdir/%name.so.*

%files tools
%_bindir/pki-*
%_bindir/url-tool

%files devel
%_datadir/%name
%_bindir/*-config
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%files devel-static
%_libdir/*.a

%changelog
* Mon Jan 25 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.9-alt1
- New version
- Fix build deps

* Mon Jul 6 2015 Vladimir Didenko <cow@altlinux.ru> 0.8.8-alt1
- Initial build
