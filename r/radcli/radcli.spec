%define _unpackaged_files_terminate_build 1

Name: radcli
Version: 1.3.1
Release: alt1
Summary: RADIUS protocol client library
Group: System/Libraries
License: MIT AND BSD-2-Clause
Url: http://radcli.github.io/radcli/
Source: %name-%version.tar

BuildRequires: libnettle-devel >= 2.4
BuildRequires: libgnutls-devel >= 3.1.0

%description
The radcli library is a library for writing RADIUS Clients. The library's
approach is to allow writing RADIUS-aware application in less than 50 lines
of C code. It was based originally on freeradius-client and is source compatible
with it.

%package -n lib%name
Summary: RADIUS protocol client library
Group: System/Libraries

%description -n lib%name
The radcli library is a library for writing RADIUS Clients. The library's
approach is to allow writing RADIUS-aware application in less than 50 lines
of C code. It was based originally on freeradius-client and is source compatible
with it.

%package -n lib%name-devel
Summary: Development files for radcli
Group: Development/C
Requires: lib%name = %EVR
Conflicts: freeradius-client-devel radiusclient-ng-devel
Conflicts: libfreeradius-client-devel libradiusclient-ng-devel

%description -n lib%name-devel
This package contains libraries and header files for developing applications
that use %name.

%prep
%setup
rm -f lib/md5.c

%build
touch config.rpath
%autoreconf
%configure --disable-static --disable-rpath --with-nettle --with-tls --enable-legacy-compat
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.la
cp -p %buildroot%_datadir/%name/dictionary %buildroot%_sysconfdir/%name/dictionary

%check
%make_build check

%files -n lib%name
%doc README.md NEWS
%_libdir/*.so.*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_datadir/%name

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_man3dir/*
%_pkgconfigdir/*.pc

%changelog
* Sun Mar 26 2023 Alexey Shabalin <shaba@altlinux.org> 1.3.1-alt1
- New version 1.3.1.

* Wed Nov 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Tue Sep 24 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.11-alt1
- initial build for ALT
