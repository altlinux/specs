%define _unpackaged_files_terminate_build 1

Name: libmtxclient
Version: 0.6.1
Release: alt1

Summary: Client API library for the Matrix protocol, built on top of Boost.Asio

Group: Development/Other
License: MIT
Url: https://nheko.im/nheko-reborn/mtxclient.git

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ libstdc++-devel-static
BuildRequires: boost-asio-devel nlohmann-json-devel boost-signals-devel
BuildRequires: libgtest-devel libssl-devel zlib-devel
BuildRequires: libolm-devel libsodium-devel libspdlog-devel
BuildRequires: libevent-devel libcurl-devel libcoeurl-devel

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
# Undefined references from_json/to_json:
%define optflags_lto %nil

%cmake -DUSE_BUNDLED_BOOST=OFF   \
       -DUSE_BUNDLED_SPDLOG=OFF  \
       -DUSE_BUNDLED_OLM=OFF     \
       -DUSE_BUNDLED_GTEST=OFF   \
       -DUSE_BUNDLED_JSON=OFF    \
       -DUSE_BUNDLED_OPENSSL=OFF \
       -DUSE_BUNDLED_COEURL=OFF  \
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
* Mon Jan 10 2022 Paul Wolneykien <manowar@altlinux.org> 0.6.1-alt1
- Use the external 'coeurl' lib.
- Switch to https://nheko.im/nheko-reborn/mtxclient.git.
- Explicitly use external JSON and OpenSSL libs.
- Version 0.6.1.

* Thu Nov 18 2021 Paul Wolneykien <manowar@altlinux.org> 0.6.0-alt1
- new version 0.6.0

* Tue Sep 14 2021 Paul Wolneykien <manowar@altlinux.org> 0.5.1-alt1
- Updated to v0.5.1.

* Wed May 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.1-alt2
- Rebuilt with boost-1.76.0.

* Sun Feb 14 2021 Paul Wolneykien <manowar@altlinux.org> 0.4.1-alt1
- Explicitly require stdc++fs (patch).
- Added libstdc++-devel-static to build dependencies.
- Fresh up to v0.4.1.

* Thu Jul 02 2020 Paul Wolneykien <manowar@altlinux.org> 0.3.1-alt1
- Release 0.3.1 (thx Nicolas Werner).

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 0.2.1-alt1
- New upstream: https://github.com/Nheko-Reborn/mtxclient.
- New upstream version 0.2.1.

* Fri Dec 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt2
- Rebuilt with boost-1.71.0.

* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.2.0-alt1
- Initial release.
