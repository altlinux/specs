Name: glog
Version: 0.5.0
Release: alt1
Summary: C++ implementation of Google logging module
License: BSD
Group: Development/C++
Url: https://github.com/google/glog

Source: %name-%version.tar
BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: ctest /proc

%description
C++ implementation of Google logging module

%package -n lib%name
Group: Development/C++
Summary: C++ implementation of Google logging module

%description -n lib%name
C++ implementation of Google logging module.

%package -n lib%name-devel
Summary: Development tools for programs which will use Google logging library
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
C++ implementation of Google logging module.
Development tools.

%prep
%setup

%build
%cmake

%cmake_build

%check
%cmake_build --target test

%install
%cmakeinstall_std

%files -n lib%name
%doc README.rst ChangeLog AUTHORS COPYING
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/%name

%changelog
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

