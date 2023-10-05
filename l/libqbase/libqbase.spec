%define _unpackaged_files_terminate_build 1

Name: libqbase
Version: 0.1.0
Release: alt1

Summary: Common BaseALT Qt projects library.
License: GPLv2+
Group: Other
Url: https://github.com/mchernigin/baselib

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake cmake-modules
BuildRequires: qt5-base-common qt5-base-devel qt5-declarative-devel qt5-tools-devel

Source0: %name-%version.tar

%global target_name qbase

%description
Common BaseALT Qt projects library

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_includedir/%target_name/
%_libdir/*.so
%_libdir/cmake

%changelog
* Wed Sep 13 2023 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build
