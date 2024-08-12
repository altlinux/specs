%define _unpackaged_files_terminate_build 1

Name: trompeloeil
Version: 48
Release: alt1
Summary: Header only C++14 mocking framework
Group: Development/C++
License: BSL-1.0

Url: https://github.com/rollbear/trompeloeil

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

BuildArch: noarch

%description
Header only C++14 mocking framework

%package devel
Summary: Header only C++14 mocking framework
Group:   Development/C++

%description devel
Header only C++14 mocking framework

%package docs
Summary: Header only C++14 mocking framework documentation
Group:   Documentation

%description docs
Header only C++14 mocking framework documentation

%prep
%setup

%build
%cmake \
  -DTROMPELOEIL_INSTALL_DOCS=OFF \
  -DCMAKE_INSTALL_LIBDIR:PATH=%_datadir \
  -DTROMPELOEIL_BUILD_TESTS=OFF
%cmake_build

%install
%cmakeinstall_std

%files devel
%doc LICENSE*.txt
%_includedir/*
%_datadir/cmake/*

%files docs
%doc docs

%changelog
* Mon Aug 12 2024 L.A. Kostis <lakostis@altlinux.ru> 48-alt1
- v48.

* Sat Mar 23 2024 L.A. Kostis <lakostis@altlinux.ru> 47-alt1
- Initial build for ALTLinux.

