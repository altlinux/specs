%define _unpackaged_files_terminate_build 1
%global target_name qbase

Name: libqbase
Version: 0.1.0
Release: alt3

Summary: Common BaseALT Qt projects library
License: GPLv2+
Group: System/Libraries
Vcs: https://github.com/mchernigin/libqbase

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake cmake-modules
BuildRequires: qt6-base-common qt6-base-devel qt6-declarative-devel qt6-tools-devel

Source0: %name-%version.tar

%description
Common BaseALT Qt projects library.

%package devel
Summary: Development headers and libraries for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package includes the header and library files necessary
for developing applications to use %name.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/%target_name/
%_libdir/cmake

%changelog
* Mon Feb 24 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt3
- Move to qt6

* Thu Jan 25 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt2
- Introduce devel package

* Wed Sep 13 2023 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build
