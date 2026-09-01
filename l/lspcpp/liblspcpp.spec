%define _unpackaged_files_terminate_build 1
%define abiversion 1

Name: lspcpp
Version: 1.0.3
Release: alt1.60.g19150d1

Summary: A Language Server Protocol implementation in C++
License: MIT
Group: Development/C++
Url: https://github.com/kuafuwang/LspCpp
Vcs: https://github.com/kuafuwang/LspCpp

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: rapidjson-devel
BuildRequires: asio-devel
BuildRequires: zlib-devel
BuildRequires: python3
BuildRequires: libixwebsocket-devel
BuildRequires: libutfcpp-devel

%description
A Language Server Protocol implementation in C++.

%package -n liblspcpp%abiversion
Summary: Library liblspcpp of lspcpp
Group: Development/C++

%description -n liblspcpp%abiversion
This package contains library liblspcpp of lspcpp.

%package devel
Summary: Development files of liblspcpp
Group: Development/C++

%description devel
This package contains development files for liblspcpp.

%prep
%setup
rm -rf third_party/

%build
%cmake -Wno-dev \
  -DBoost_NO_BOOST_CMAKE=ON \
  -DUSE_SYSTEM_RAPIDJSON=ON \
  -DUSE_SYSTEM_UTFCPP=ON \
  -DUSE_EXTERNAL_ASIO=ON \
  -DUSE_EXTERNAL_IXWEBSOCKET=ON \
  -DLSPCPP_INSTALL=ON \
  -DCMAKE_BUILD_TYPE=Release \
  -DLSPCPP_BUILD_EXAMPLES=OFF \
  -DLSPCPP_BUILD_MINIMAL_EXAMPLE=ON \
  -DLSPCPP_BUILD_WEBSOCKETS=ON \
  -DLSPCPP_BUILD_SHARED_LIBRARY=ON \
  #
%cmake_build

%install
%cmake_install

%files -n liblspcpp%abiversion
%_libdir/liblspcpp.so.%abiversion
%_libdir/liblspcpp.so.%version

%files devel
%_includedir/LibLsp
%_includedir/LibLsp
%_cmakedir/lspcpp
%_libdir/liblspcpp.so
%_pkgconfigdir/lspcpp.pc
%_includedir/LibLsp/LspCpp.h

%changelog
* Fri Aug 28 2026 Pavel Petrykin <silverducks@altlinux.org> 1.0.3-alt1.60.g19150d1
- Initial build for Alt Linux.
