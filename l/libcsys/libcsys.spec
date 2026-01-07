%define _unpackaged_files_terminate_build 1

Name: libcsys
Version: 5.0.1
Release: alt1

Summary: Library for managing drive and getting system resource information in real time.
License: GPL-3.0-or-later
Group: System/Libraries
Url: https://gitlab.com/cubocore/libcsys

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)

%description
Library for managing drive and getting system resource information in
real time for C Suite. It uses some parts of Stacer project.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
Development files for %{name}.

Library for managing drive and getting system resource information in
real time for C Suite. It uses some parts of Stacer project.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_libdir/libcsys.so.5
%_libdir/libcsys.so.5.0.0

%files devel
%dir %_includedir/csys
%_includedir/csys/*
%_libdir/libcsys.so
%_datadir/pkgconfig/csys.pc

%changelog
* Wed Jan 07 2026 Nikolay Strelkov <snk@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Mon Dec 29 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
