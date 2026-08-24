%define _unpackaged_files_terminate_build 1

%def_with check

Name: libreflection-cpp
Version: 0.4.0
Release: alt1

Summary: C++ static reflection support library
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/contour-terminal/reflection-cpp

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: gcc-c++

%if_with check
BuildRequires: ctest
BuildRequires: catch-devel
%endif

%description
%summary.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
The %{name}-devel package contains development files for %{name}.

%prep
%setup

%build
%cmake \
%if_with check
       -DREFLECTION_TESTING=ON
%else
       -DREFLECTION_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc LICENSE.txt README.md
%dir %_includedir/reflection-cpp/
%_includedir/reflection-cpp/*
%dir %_libdir/cmake/reflection-cpp/
%_libdir/cmake/reflection-cpp/*

%changelog
* Mon Aug 24 2026 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
