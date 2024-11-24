# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libcpuid
Version: 0.7.0
Release: alt1
Summary: libcpuid provides CPU identification for the x86 (and x86_64)
License: BSD-2-Clause
Group: Development/C
Url: https://github.com/anrieff/libcpuid
Source: libcpuid-%version.tar
Patch: 0001-CMakeLists.txt-Add-LIB_DESTINATION-variable.patch
Patch1: use_KDIR_for_kmodule_path-libcpuid-0.7.0.patch

ExclusiveArch: %ix86 x86_64

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: doxygen graphviz

%description
%summary.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.
For details about the programming API, please see the docs
on the project's site (http://libcpuid.sourceforge.net/)

%package -n kernel-source-cpuid
Summary: cpuid kernel driver for arm64
Group: Development/Kernel

%description -n kernel-source-cpuid
cpuid kernel driver for arm64.

%prep
%setup
%autopatch -p1

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%_libdir
%cmake_build

%install
%cmake_install

#%%ifarch aarch64
#mkdir -p %kernel_srcdir
#cd %buildroot%prefix/src/
#mv cpuid-%version kernel-source-cpuid-%version
#tar -cjvf %kernel_srcdir/kernel-source-cpuid-%version.tar.bz2 kernel-source-cpuid-%version
#rm -r kernel-source-cpuid-%version
#%%endif

%files
%_libdir/%name.so.*

%files devel
%_bindir/cpuid_tool
%_includedir/%name
%_man3dir/*
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc
%_prefix/lib/cmake/cpuid

#%%ifarch aarch64
#%%files -n kernel-source-cpuid
#%%attr(0644,root,root) %kernel_src/kernel-source-cpuid-%version.tar.bz2
#%%endif

%changelog
* Sun Nov 24 2024 Anton Midyukov <antohami@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Wed May 01 2024 Anton Midyukov <antohami@altlinux.org> 0.6.5-alt1
- New version 0.6.5.

* Mon Oct 09 2023 Anton Midyukov <antohami@altlinux.org> 0.6.4-alt1
- New version 0.6.4.

* Sun Apr 23 2023 Anton Midyukov <antohami@altlinux.org> 0.6.3-alt1
- New version 0.6.3.

* Sat Jan 14 2023 Anton Midyukov <antohami@altlinux.org> 0.6.2-alt1
- new version 0.6.2

* Fri Oct 28 2022 Anton Midyukov <antohami@altlinux.org> 0.6.1-alt1
- new version 0.6.1

* Mon Oct 17 2022 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt1
- new version 0.6.0

* Mon Aug 29 2022 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt3.20220828
- new snapshot
- exclusive arch ix86, x86_64
- fix description

* Wed Feb 23 2022 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt2.20220206
- new snapshot

* Fri Apr 09 2021 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt1
- new version 0.5.1

* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 0.4.1-alt2.20200518
- new snapshot

* Wed Apr 17 2019 Anton Midyukov <antohami@altlinux.org> 0.4.1-alt1
- new version 0.4.1

* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- new version 0.4.0

* Mon Oct 24 2016 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- Initial build for Alt Linux Sisyphus.
