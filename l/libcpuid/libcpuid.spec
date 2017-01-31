Name: libcpuid
Version: 0.4.0
Release: alt1
Summary: Provides CPU identification for x86
License: BSD-2-Clause
Group: Development/C
Url: https://github.com/anrieff/libcpuid
Source: libcpuid-%version.tar

%description
Libcpuid provides CPU identification for the x86 (and x86_64).

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

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
* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- new version 0.4.0

* Mon Oct 24 2016 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- Initial build for Alt Linux Sisyphus.
