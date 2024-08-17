Name: liboneapi-level-zero1
Version: 1.17.28
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

%package devel
Summary: The oneAPI Level Zero Specification Headers and Loader development package
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains library and header files for
developing applications that use %name.

%prep
%setup

%build
%cmake -DSYSTEM_SPDLOG=ON
%cmake_build

%install
%cmake_install

%files
%doc LICENSE
%doc README.md SECURITY.md
%_libdir/libze_loader.so.1.*
%_libdir/libze_loader.so.1
%_libdir/libze_validation_layer.so.1.*
%_libdir/libze_validation_layer.so.1
%_libdir/libze_tracing_layer.so.1.*
%_libdir/libze_tracing_layer.so.1

%files devel
%_includedir/level_zero
%_libdir/libze_loader.so
%_libdir/libze_validation_layer.so
%_libdir/libze_tracing_layer.so
%_pkgconfigdir/libze_loader.pc
%_pkgconfigdir/level-zero.pc

%changelog
* Sat Aug 17 2024 Boris Yumankulov <boria138@altlinux.org> 1.17.28-alt1
- new version 1.17.28

* Wed Jul 31 2024 Boris Yumankulov <boria138@altlinux.org> 1.17.19-alt1
- initial build for ALT Sisyphus

