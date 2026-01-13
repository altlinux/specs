Name:    heatshrink
Version: 0.4.1
Release: alt1
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

%package devel-static
Summary: A data compression/decompression library for embedded/real-time systems
Group: System/Configuration/Other

%description devel-static
A data compression/decompression library for embedded/real-time systems.

%description
A data compression/decompression library for embedded/real-time systems.

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%prep
%setup
cp %SOURCE1 %SOURCE2 ./

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name

%files devel-static
%_includedir/%name/heatshrink_common.h
%_includedir/%name/heatshrink_config.h
%_includedir/%name/heatshrink_decoder.h
%_includedir/%name/heatshrink_encoder.h
%_libexecdir/libheatshrink.a
%_libexecdir/libheatshrink_dynalloc.a
%_libdir/cmake/%name/heatshrinkConfig.cmake
%_libdir/cmake/%name/heatshrinkConfigVersion.cmake
%_libdir/cmake/%name/heatshrinkTargets-noconfig.cmake
%_libdir/cmake/%name/heatshrinkTargets.cmake

%changelog
* Thu Nov 27 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 0.4.1-alt1
- Initial build.
