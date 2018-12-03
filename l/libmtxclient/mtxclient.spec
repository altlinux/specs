Name: libmtxclient
Version: 0.2.0
Release: alt1

Summary: Client API library for the Matrix protocol, built on top of Boost.Asio

Group: Development/Other
License: MIT
Url: https://github.com/mujx/mtxclient

Source: %name-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: boost-asio-devel json-cpp boost-signals-devel
BuildRequires: libgtest-devel libssl-devel zlib-devel
BuildRequires: libolm-devel libsodium-devel libspdlog-devel

%description
Client API library for the Matrix protocol, built on top of Boost.Asio.

%package devel
Summary: Development files for %name
Group: Development/Other
#Requires: %name = %version-%release

%description devel
Client API library for the Matrix protocol, built on top of Boost.Asio.

This package contains C++ header files for developing and the static
library.

%prep
%setup

%build
%cmake -DUSE_BUNDLED_BOOST=OFF  \
       -DUSE_BUNDLED_SPDLOG=OFF \
       -DUSE_BUNDLED_OLM=OFF    \
       -DUSE_BUNDLED_GTEST=OFF
%cmake_build

%install
%cmakeinstall_std

# Testing needs a local Synapse server instance
#%check
#%make_build test

#%files

%files devel
%doc README.md examples
%doc LICENSE
%_libdir/*.a
%_includedir/*.hpp
%_includedir/mtx
%_includedir/mtxclient
%_libdir/cmake/MatrixClient

%changelog
* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.2.0-alt1
- Initial release.
