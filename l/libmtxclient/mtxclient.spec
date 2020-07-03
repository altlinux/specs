%define _unpackaged_files_terminate_build 1

Name: libmtxclient
Version: 0.3.1
Release: alt1

Summary: Client API library for the Matrix protocol, built on top of Boost.Asio

Group: Development/Other
License: MIT
Url: https://github.com/Nheko-Reborn/mtxclient

Source: %name-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: boost-asio-devel nlohmann-json-devel boost-signals-devel
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
       -DUSE_BUNDLED_GTEST=OFF  \
       -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmakeinstall_std

# Testing needs a local Synapse server instance
#%check
#%make_build test

%files
%doc README.md
%doc LICENSE
%_libdir/*.so.*

%files devel
%doc examples
%_includedir/*.hpp
%_includedir/mtx
%_includedir/mtxclient
%_libdir/cmake/MatrixClient
%_libdir/*.so

%changelog
* Thu Jul 02 2020 Paul Wolneykien <manowar@altlinux.org> 0.3.1-alt1
- Release 0.3.1 (thx Nicolas Werner).

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 0.2.1-alt1
- New upstream: https://github.com/Nheko-Reborn/mtxclient.
- New upstream version 0.2.1.

* Fri Dec 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt2
- Rebuilt with boost-1.71.0.

* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.2.0-alt1
- Initial release.
