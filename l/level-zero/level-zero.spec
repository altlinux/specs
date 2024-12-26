%define soversion 1
Name: level-zero
Version: 1.19.2
Release: alt1

Summary: OneAPI Level Zero Specification Headers and Loader
License: MIT
Group: Development/C

Url: https://github.com/oneapi-src/level-zero
# Source-url: https://github.com/oneapi-src/level-zero/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: opencl-headers
BuildRequires: libspdlog-devel

%description
The objective of the oneAPI Level-Zero Application Programming Interface
(API) is to provide direct-to-metal interfaces to offload accelerator
devices. Its programming interface can be tailored to any device needs
and can be adapted to support broader set of languages features such as
function pointers, virtual functions, unified memory,
and I/O capabilities.

%package -n libze%soversion
Summary: This package contains the shared libraries for Level Zero
Group: Development/C
Conflicts: liboneapi-level-zero1 = %EVR
Obsoletes: liboneapi-level-zero1 = %EVR

%description -n libze%soversion
This package contains the shared libraries for Level Zero.

%package -n libze-devel
Summary: The oneAPI Level Zero Specification Headers and Loader development package
Group: Development/C
Requires: libze%soversion = %EVR
Provides: oneapi-level-zero-devel = %EVR

%description -n libze-devel
The libze-devel package contains library and header files for
developing applications that use libze.

%prep
%setup

%build
%cmake -DSYSTEM_SPDLOG=ON
%cmake_build

%install
%cmake_install

%files -n libze%soversion
%doc LICENSE
%doc README.md SECURITY.md
%_libdir/libze_loader.so.%soversion.*
%_libdir/libze_loader.so.%soversion
%_libdir/libze_validation_layer.so.%soversion.*
%_libdir/libze_validation_layer.so.%soversion
%_libdir/libze_tracing_layer.so.%soversion.*
%_libdir/libze_tracing_layer.so.%soversion

%files -n libze-devel
%_includedir/level_zero
%_libdir/libze_loader.so
%_libdir/libze_validation_layer.so
%_libdir/libze_tracing_layer.so
%_pkgconfigdir/libze_loader.pc
%_pkgconfigdir/level-zero.pc

%changelog
* Fri Dec 13 2024 Andrey Kovalev <ded@altlinux.org> 1.19.2-alt1
- new version 1.19.2
- built according to shared libs policy

* Sat Aug 17 2024 Boris Yumankulov <boria138@altlinux.org> 1.17.28-alt1
- new version 1.17.28

* Wed Jul 31 2024 Boris Yumankulov <boria138@altlinux.org> 1.17.19-alt1
- initial build for ALT Sisyphus

