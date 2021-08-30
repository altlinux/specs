Name: libpki
Version: 0.8.9
Release: alt6.git20180603

Summary: Library for PKI enabled application development.
License: %asl
Group: System/Libraries
Url: https://pki.openca.org/projects/libpki/
Packager: Vladimir Didenko <cow@altlinux.ru>
ExclusiveArch: i586 x86_64 %e2k

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: libssl-devel
BuildRequires: libxml2-devel
BuildRequires: libldap-devel
BuildRequires: libmysqlclient-devel
BuildRequires: postgresql-devel
BuildRequires: liblzma-devel zlib-devel

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

%prep
%setup -n %name-%version
%patch0 -p1
%ifarch %e2k
sed -i "s|\\*amd64)|e2k)|" configure.ac
sed -i "s|MYLDADD =|& @openssl_ldadd@|" src/tools/Makefile.am
%endif

%build
%autoreconf
%configure --disable-static
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

%changelog
* Mon Aug 30 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.8.9-alt6.git20180603
- Fixed build for Elbrus

* Thu Aug 26 2021 Vladimir Didenko <cow@altlinux.ru> 0.8.9-alt5.git20180603
- Don't build static library

* Fri Nov 8 2019 Vladimir Didenko <cow@altlinux.ru> 0.8.9-alt4.git20180603
- Fix build deps

* Wed Aug 29 2018 Vladimir Didenko <cow@altlinux.ru> 0.8.9-alt3.git20180603
- Specify build arches (aarch64 is not supported)

* Wed Aug 29 2018 Vladimir Didenko <cow@altlinux.ru> 0.8.9-alt2.git20180603
- New version (fixes build with openssl 1.1)

* Mon Jan 25 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.9-alt1
- New version
- Fix build deps

* Mon Jul 6 2015 Vladimir Didenko <cow@altlinux.ru> 0.8.8-alt1
- Initial build
