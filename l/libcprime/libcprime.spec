%define _unpackaged_files_terminate_build 1

Name: libcprime
Version: 5.0.1
Release: alt1

Summary: Library for bookmarking, saving activities, sharing files and more
License: GPL-3.0-or-later
Group: System/Libraries
Url: https://gitlab.com/cubocore/libcprime

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Widgets)

%description
LibCPrime is a Library for bookmarking, saving recent activites, managing
settings for CuboCore Application Suite.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
Development files for libcprime.

Libcprime is a library for bookmarking, saving recent activites, managing
settings of CoreApps.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_libdir/libcprime*.so.5
%_libdir/libcprime*.so.5.0.0

%files devel
%dir %_includedir/cprime
%_includedir/cprime/*
%_libdir/libcprime*.so
%_datadir/pkgconfig/cprime*.pc

%changelog
* Wed Jan 07 2026 Nikolay Strelkov <snk@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Mon Dec 29 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
