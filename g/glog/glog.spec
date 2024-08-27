%ifarch ppc64le
%define relax ||:
%else
%define relax %nil
%endif

%define soname 2
Name: glog
Version: 0.7.1
Release: alt1
Summary: C++ implementation of Google logging module
License: BSD
Group: Development/C++
Url: https://github.com/google/glog

Source: %name-%version.tar
BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: ctest /proc
BuildRequires: libunwind-devel libgflags-devel

%description
C++ implementation of Google logging module

%package -n lib%name%soname
Group: Development/C++
Summary: C++ implementation of Google logging module

%description -n lib%name%soname
C++ implementation of Google logging module.

%package -n lib%name-devel
Summary: Development tools for programs which will use Google logging library
Group: Development/C++
Requires: lib%name%soname = %EVR

%description -n lib%name-devel
C++ implementation of Google logging module.
Development tools.

%prep
%setup

%build
%cmake -DWITH_PKGCONFIG=ON

%cmake_build

%check
%cmake_build --target test %relax

%install
%cmakeinstall_std

%files -n lib%name%soname
%doc README.rst ChangeLog AUTHORS COPYING
%_libdir/lib%name.so.%soname
%_libdir/lib%name.so.%version

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/%name
%_libdir/cmake/%name

%changelog
* Fri Aug 16 2024 Anton Farygin <rider@altlinux.ru> 0.7.1-alt1
- 0.7.0 -> 0.7.1

* Mon Jun 03 2024 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1
- 0.6.0 -> 0.7.0
- relaxed check on ppc64le

* Wed Apr 06 2022 Anton Farygin <rider@altlinux.ru> 0.6.0-alt1
- 0.5.0 -> 0.6.0

* Sun Dec 05 2021 Anton Farygin <rider@altlinux.ru> 0.5.0-alt1
- 0.5.0
- enabled tests

* Tue Feb 13 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.4-alt4
- Fixed build on non-x86 architectures.

* Thu Jul 02 2015 Dmitry Derjavin <dd@altlinux.org> 0.3.4-alt3
- Fixed typo in devel package requirements.

* Mon Jun 22 2015 Dmitry Derjavin <dd@altlinux.org> 0.3.4-alt2
- Unused files removed.

* Mon Jun 22 2015 Dmitry Derjavin <dd@altlinux.org> 0.3.4-alt1
- Initial ALT Linux build.

