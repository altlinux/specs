%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_with check

Name: zfp
Version: 1.0.1
Release: alt1

Summary: Compressed numerical arrays that support high-speed random access
License: BSD-3-Clause
Group: Sciences/Mathematics
Url: https://computing.llnl.gov/projects/zfp
Vcs: https://github.com/LLNL/zfp

Source: %name-%version.tar
Patch: Fix-64-bit-integer-types-on-32-bit-archs.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: /proc
%if_with check
BuildRequires: ctest
%endif

%description
%summary.

%package -n lib%name
Summary: %summary
Group: System/Libraries

%description -n lib%name
%summary.

%package -n lib%name-devel
Summary: Development files for zfp
Group: Development/C++
Requires: %name = %EVR

%description -n lib%name-devel
Development package for zfp.

%prep
%setup
%patch -p1

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake
%cmake_build

%install
%cmakeinstall_std

%check
%cmake_build --target test

%files
%_bindir/zfp

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%doc README.*
%_includedir/*.h
%_includedir/*.hpp
%_includedir/zfp/
%_libdir/lib%name.so
%_libdir/cmake/zfp/

%changelog
* Wed Apr 29 2026 Anton Vyatkin <toni@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
