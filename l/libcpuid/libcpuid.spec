# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libcpuid
Version: 0.4.1
Release: alt2.20200518
Summary: Provides CPU identification for x86, x86_64, aarch64, armh
License: BSD-2-Clause
Group: Development/C
Url: https://github.com/anrieff/libcpuid
Source: libcpuid-%version.tar

ExclusiveArch: %ix86 x86_64 aarch64 armh

%description
Libcpuid provides CPU identification for the x86 and x86_64.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.
For details about the programming API, please see the docs
on the project's site (http://libcpuid.sourceforge.net/)

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm %buildroot%_libdir/*.a

%files
%_libdir/%name.so.*

%files devel
%_bindir/cpuid_tool
%_includedir/%name
%_libdir/*.so
%_libdir/pkgconfig/%name.pc

%changelog
* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 0.4.1-alt2.20200518
- new snapshot

* Wed Apr 17 2019 Anton Midyukov <antohami@altlinux.org> 0.4.1-alt1
- new version 0.4.1

* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- new version 0.4.0

* Mon Oct 24 2016 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- Initial build for Alt Linux Sisyphus.
