%define _unpackaged_files_terminate_build 1

%def_with check

Name: libboxed-cpp
Version: 1.4.3
Release: alt1

Summary: Boxing primitive types in C++
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/contour-terminal/boxed-cpp

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
       -DBOXED_TESTING=ON
%else
       -DBOXED_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc LICENSE.txt README.md
%dir %_includedir/boxed-cpp/
%_includedir/boxed-cpp/*
%dir %_libdir/cmake/boxed-cpp/
%_libdir/cmake/boxed-cpp/*

%changelog
* Mon Aug 24 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.3-alt1
- Initial build for Sisyphus
