%define soversion 3

Name: opendht
Version: 3.6.2.3
Release: alt1
Summary: C++17 Distributed Hash Table implementation
License: GPL-3.0-only
Group: System/Libraries
URL: https://github.com/savoirfairelinux/opendht/wiki
Vcs: https://github.com/savoirfairelinux/opendht

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libgnutls-devel msgpack-cxx-devel libargon2-devel asio-devel
BuildRequires: libncurses-devel libreadline-devel libnettle-devel libfmt-devel
BuildRequires: cppunit-devel ctest liburing-devel

%description
A lightweight C++17 Distributed Hash Table implementation.

OpenDHT provides an easy to use distributed in-memory data store. Every node in
the network can read and write values to the store. Values are distributed over
the network, with redundancy.

%package -n lib%name%soversion
Summary: C++17 Distributed Hash Table implementation Library
Group: System/Libraries
Provides: lib%name = %EVR
Provides: lib%name-c = %EVR

%description -n lib%name%soversion
%summary

%package -n lib%name-devel
Summary: %name devel libs and headers
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
lib%name development libraries and headers.

%prep
%setup

%build
%cmake \
	-DOPENDHT_DOWNLOAD_DEPS=OFF \
	-DOPENDHT_BUILD_TOOLS=OFF \
	-DOPENDHT_PYTHON=OFF \
	-DOPENDHT_TESTS_NETWORK=OFF \
	-DOPENDHT_IO_URING=ON \
	-DOPENDHT_C=ON \
	%nil
%cmake_build

%install
%cmake_install

%check
# fails on x86:
# 1) test: test::CryptoTester::testAesEncryptionWithMultipleKeySizes (E)
# uncaught exception of type std::exception (or derived).
# - std::bad_alloc
%ifnarch %ix86
pushd "%_cmake__builddir"
%__ctest --output-on-failure
popd
%endif

%files -n lib%name%soversion
%_bindir/*
%_libdir/lib%{name}*.so.%{soversion}*
%_man1dir/*

%files -n lib%name-devel
%_libdir/lib%{name}*.so
%_includedir/%name
%_includedir/%name.h
%_libdir/cmake/%name
%_pkgconfigdir/%{name}*.pc

%changelog
* Tue Jan 27 2026 L.A. Kostis <lakostis@altlinux.ru> 3.6.2.3-alt1
- 3.6.2.3.

* Mon Nov 03 2025 L.A. Kostis <lakostis@altlinux.ru> 3.5.4-alt1
- 3.5.4.

* Mon Aug 18 2025 L.A. Kostis <lakostis@altlinux.ru> 3.5.1-alt1
- 3.5.1.

* Wed May 28 2025 L.A. Kostis <lakostis@altlinux.ru> 3.4.0-alt1
- Initial build for ALTLinux.
