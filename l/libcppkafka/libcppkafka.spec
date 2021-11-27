%define _unpackaged_files_terminate_build 1

Name: libcppkafka
Version: 0.4.0
Release: alt1
Summary: High level C++ wrapper for rdkafka
Group: Development/C++
License: BSD-2-Clause
Url: https://github.com/mfontanini/cppkafka

# https://github.com/mfontanini/cppkafka
Source: %name-%version.tar
Patch0: %name-alt-install.patch

BuildRequires: gcc-c++ rpm-macros-cmake boost-devel cmake librdkafka-devel
# missing from librdkafka-devel
BuildRequires: libssl-devel zlib-devel

%description
cppkafka allows C++ applications to consume and produce messages using the
Apache Kafka protocol. The library is built on top of librdkafka, and provides
a high level API that uses modern C++ features to make it easier to write code
while keeping the wrapper's performance overhead to a minimum.

%package devel
Group: Development/C++
Summary: Development environment for %name
Requires: %name = %EVR

%description devel
Development environment for %name, %summary

%prep
%setup
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE
%doc README.md
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_datadir/pkgconfig/*.pc
%_libdir/cmake/*

%changelog
* Sat Nov 27 2021 Anton Farygin <rider@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Mon Oct 12 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.1-alt1.git.5e4b350
- Updated to current snapshot.

* Tue Jun 25 2019 Anton Farygin <rider@altlinux.ru> 0.3.1-alt1
- first build for ALT

