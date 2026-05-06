%define _unpackaged_files_terminate_build 1

%def_with check

Name: libudb
Version: 1.0
Release: alt1

Summary: Universal database library
License: GPL-3.0-only
Group: System/Libraries
Url: https://github.com/ProfessorNavigator/libudb

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
BuildRequires: doxygen
BuildRequires: graphviz

%if_with check
BuildRequires: ctest
%endif

%description
This library is suitable for UDB format databases managing.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This library is suitable for UDB format databases managing (see 
include/UDBase.h or documentation for format description).

%package doc
Summary: Documentation files for %name-devel
Group: Documentation
BuildArch: noarch

%description doc
This library is suitable for UDB format databases managing (see 
include/UDBase.h or documentation for format description).

This package includes the documentation files for the %name
development.

%prep
%setup

%build
%cmake \
       -D BUILD_DOCS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc COPYING README.md README_RU.md
%_libdir/libudb*.so.1
%_libdir/libudb*.so.1.0

%files devel
%dir %_includedir/LibUDB
%_includedir/LibUDB/*
%_libdir/libudb.so
%dir %_libdir/cmake/LibUDB
%_libdir/cmake/LibUDB/*

%files doc
%dir %_datadir/doc/LibUDB
%_datadir/doc/LibUDB/*
%_man3dir/Algorithm.3.*
%_man3dir/ByteOrder.3.*
%_man3dir/UDBElement.3.*
%_man3dir/UDBase.3.*

%changelog
* Wed May 06 2026 Nikolay Strelkov <snk@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
