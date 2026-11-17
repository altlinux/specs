%define commit eadca9f4b13cdc75f1c9eec605844063f2782409

Name: libnaps2_jpeg
Version: 1.0.0
Release: alt1

Summary: Native JPEG encoder helper for NAPS2

License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/cyanfish/naps2-jpeg
# Source-url: https://github.com/cyanfish/naps2-jpeg/archive/%commit.tar.gz
Source: %name-%version.tar
Patch0: libnaps2_jpeg-system-shared.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake gcc-c++ pkgconfig(libjpegli)
BuildRequires: /usr/bin/python3

%description
Native C API for NAPS2 JPEG encoding using the system jpegli library.

%package -n %{name}1
Summary: Native JPEG encoder helper for NAPS2
Group: System/Libraries

%description -n %{name}1
Native C API for NAPS2 JPEG encoding using the system jpegli library.

%package devel
Summary: Development files for the NAPS2 JPEG helper
Group: Development/C

%description devel
Header and link library for the native NAPS2 JPEG encoder helper.

%prep
%setup
%patch0 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%check
python3 scripts/smoke-test.py ./%_cmake__builddir/libnaps2_jpeg.so.1

%install
%cmake_install

%files -n %{name}1
%doc LICENSE README.md
%_libdir/libnaps2_jpeg.so.1
%_libdir/libnaps2_jpeg.so.%version

%files devel
%_includedir/naps2_jpeg.h
%_libdir/libnaps2_jpeg.so

%changelog
* Fri Nov 13 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux (git eadca9f4).

