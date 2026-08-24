%define _unpackaged_files_terminate_build 1

%def_with check

Name: libunicode
Version: 0.9.3
Release: alt1

Summary: Modern C++20 Unicode library
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/contour-terminal/libunicode

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: unicode-ucd

%if_with check
BuildRequires: ctest
BuildRequires: catch-devel
%endif

%description
The goal of libunicode library is to bring painless unicode support to C++
with simple and easy to understand APIs. The API naming conventions are
chosen to look familiar to those using the C++ standard libary.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %{version}-%{release}

%description devel
The %{name}-devel package contains development files for %{name}.

%package tools
Summary: Tools for %name
Group: Text tools
Requires: %name = %{version}-%{release}

%description tools
The %{name}-tools package contains tools about %name.

%prep
%setup

%build
%cmake \
       -DLIBUNICODE_UCD_DIR=/usr/share/unicode/ucd \
%if_with check
       -DLIBUNICODE_TESTING=ON
%else
       -DLIBUNICODE_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc LICENSE README.md
%_libdir/libunicode*.so.0*

%files devel
%dir %_includedir/libunicode/
%_includedir/libunicode/*
%dir %_libdir/cmake/libunicode/
%_libdir/cmake/libunicode/*
%_libdir/libunicode*.so

%files tools
%_bindir/unicode-query

%changelog
* Mon Aug 24 2026 Nikolay Strelkov <snk@altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus
