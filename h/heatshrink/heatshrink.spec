Name:    heatshrink
Version: 0.4.1
Release: alt2
Summary: A data compression/decompression library for embedded/real-time systems
License: ISC
Group:   System/Base
URL:     https://github.com/atomicobject/heatshrink
VCS:     https://github.com/atomicobject/heatshrink
Source:  %name-%version.tar
# https://github.com/prusa3d/libbgcode/tree/main/deps/heatshrink/CMakeLists.txt
Source1: CMakeLists.txt
# https://github.com/prusa3d/libbgcode/tree/main/deps/heatshrink/Config.cmake.in
Source2: Config.cmake.in

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++

%package devel
Summary: A data compression/decompression library for embedded/real-time systems
Group: System/Configuration/Other
Requires: libheatshrink%version = %EVR
Requires: libheatshrink_dynalloc%version = %EVR
Conflicts: heatshrink-devel-static < %EVR

%description devel
A data compression/decompression library for embedded/real-time systems.

%description
A data compression/decompression library for embedded/real-time systems.

%package -n libheatshrink%version
Summary: A data compression/decompression library for embedded/real-time systems
Group: System/Libraries

%description -n libheatshrink%version
A data compression/decompression library for embedded/real-time systems.

%package -n libheatshrink_dynalloc%version
Summary: A data compression/decompression library for embedded/real-time systems
Group: System/Libraries

%description -n libheatshrink_dynalloc%version
A data compression/decompression library for embedded/real-time systems.

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%prep
%setup
cp %SOURCE1 %SOURCE2 ./

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_LIBDIR=%_lib
%cmake_build

%install
%cmake_install

%files
%_bindir/%name

%files -n libheatshrink%version
%_libdir/libheatshrink.so.%version

%files -n libheatshrink_dynalloc%version
%_libdir/libheatshrink_dynalloc.so.%version

%files devel
%_libdir/libheatshrink.so
%_libdir/libheatshrink_dynalloc.so
%_includedir/%name/heatshrink_common.h
%_includedir/%name/heatshrink_config.h
%_includedir/%name/heatshrink_decoder.h
%_includedir/%name/heatshrink_encoder.h
%_libdir/cmake/%name/heatshrinkConfig.cmake
%_libdir/cmake/%name/heatshrinkConfigVersion.cmake
%_libdir/cmake/%name/heatshrinkTargets-noconfig.cmake
%_libdir/cmake/%name/heatshrinkTargets.cmake

%changelog
* Tue Jan 20 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 0.4.1-alt2
- Build as shared libraries instead static (Closes: 57532).

* Thu Nov 27 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 0.4.1-alt1
- Initial build.
