%define _unpackaged_files_terminate_build 1

Name:    libdivide
Version: 5.3.0
Release: alt1
Summary: Header-only C/C++ library for optimizing integer division
Group:   Development/C++
License: zlib-acknowledgement AND BSL-1.0
URL:     http://libdivide.com/
Vcs:     https://github.com/ridiculousfish/libdivide

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ ctest

%description
libdivide.h is a header-only C/C++ library for optimizing integer division.
Integer division is one of the slowest instructions on most CPUs e.g. on
current x64 CPUs a 64-bit integer division has a latency of up to 90 clock
cycles whereas a multiplication has a latency of only 3 clock cycles. libdivide
allows you to replace expensive integer division instructions by a sequence of
shift, add and multiply instructions that will calculate the integer division
much faster.

%package devel
Summary: Header-only C/C++ library for optimizing integer division
Group:   Development/C++

%description devel
libdivide.h is a header-only C/C++ library for optimizing integer division.
Integer division is one of the slowest instructions on most CPUs e.g. on
current x64 CPUs a 64-bit integer division has a latency of up to 90 clock
cycles whereas a multiplication has a latency of only 3 clock cycles. libdivide
allows you to replace expensive integer division instructions by a sequence of
shift, add and multiply instructions that will calculate the integer division
much faster.

%prep
%setup

%build
%cmake \
  -DLIBDIVIDE_BUILD_TESTS=ON \
  -DCMAKE_INSTALL_LIBDIR:PATH=%_datadir \
  %nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files devel
%doc LICENSE.txt *.md
%doc doc
%_includedir/*
%_datadir/cmake/*

%changelog
* Wed Apr 01 2026 L.A. Kostis <lakostis@altlinux.ru> 5.3.0-alt1
- Initial build for ALTLinux.
