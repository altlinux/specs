Name: libmd
Version: 1.0.4
Release: alt1

Summary: Message Digest functions from BSD systems

License: BSD and ISC and Copyright only and Public Domain
Group: System/Libraries
Url: http://libbsd.freedesktop.org/

# Source-url: https://libbsd.freedesktop.org/releases/libmd-%version.tar.xz
Source: %name-%version.tar

%description
This library provides message digest functions found on BSD systems either
on their libc or libmd libraries and lacking on others like GNU systems,
thus making it easier to port projects with strong BSD origins, without
needing to embed the same code over and over again on each project

%package devel
Summary: Development files for libbsd
Group: Development/Other
Requires: %name = %EVR
Requires: pkg-config

%description devel
Development files for the libbsd library.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc COPYING README ChangeLog
%_libdir/%name.so.*

%files devel
%_man3dir/*
%_includedir/*.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Sat Feb 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- new version 1.0.4 (with rpmrb script)

* Sat Sep 04 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- initial build for ALT Sisyphus
