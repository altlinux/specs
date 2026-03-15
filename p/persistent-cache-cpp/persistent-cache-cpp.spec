%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: persistent-cache-cpp
Version: 1.0.10
Release: alt1

Summary: Cache of key-value pairs with persistent storage for C++ 11
License: LGPL-3.0-only
Group: System/Libraries
Url: https://gitlab.com/ubports/development/core/lib-cpp/persistent-cache-cpp

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-filesystem-devel
BuildRequires: pkgconfig(leveldb)
BuildRequires: ayatana-cmake-modules
BuildRequires: doxygen
BuildRequires: pkgconfig(gtest)

%if_with check
BuildRequires: ctest
%endif

%description
%summary

%package -n lib%{name}-devel
Summary: Cache of key-value pairs with persistent storage for C++ 11
Group: Development/Other

%description -n lib%{name}-devel
This API provides a cache of key-value pairs with a backing store. It is
intended for caching arbitrary (possibly large) amounts of data, such as
might be needed by a web browser cache. The cache supports both
least-recently-used and time-to-live expiration policies. It scales to
large numbers (millions) of entries and is very fast. The implementation
is based on leveldb and typically provides throughput many times larger
than the I/O bandwidth to disk.

The cache is robust in the face of crashes and power loss. After a
re-start, it is guaranteed to be in a consistent state with correct
data. Some number of updates that were made just prior to a power loss
or kernel crash can be lost; however, if just the calling process
crashes, all updates that were made prior to the crash are guaranteed to
be on disk.

%package -n lib%{name}-doc
Summary: Documentation for persistent-cache-cpp-dev
Group: Documentation

%description -n lib%{name}-doc
This API provides a cache of key-value pairs with a backing store. It is
intended for caching arbitrary (possibly large) amounts of data, such as
might be needed by a web browser cache. The cache supports both
least-recently-used and time-to-live expiration policies. It scales to
large numbers (millions) of entries and is very fast. The implementation
is based on leveldb and typically provides throughput many times larger
than the I/O bandwidth to disk.

The cache is robust in the face of crashes and power loss. After a
re-start, it is guaranteed to be in a consistent state with correct
data. Some number of updates that were made just prior to a power loss
or kernel crash can be lost; however, if just the calling process
crashes, all updates that were made prior to the crash are guaranteed to
be on disk.

This package provides examples and the API reference.

%prep
%setup
%patch -p1

%build
%cmake \
       -W no-dev \
       -DBUILD_SHARED_LIBS=OFF \
       -DCMAKE_INSTALL_LIBDIR=%_libdir \
%if_with check
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%check
%ctest -j1 VV

%files -n lib%{name}-devel
%doc AUTHORS ChangeLog COPYING.LGPL HACKING
%_includedir/core/cache_codec.h
%_includedir/core/cache_discard_policy.h
%_includedir/core/cache_events.h
%_includedir/core/optional.h
%_includedir/core/persistent_cache.h
%_includedir/core/persistent_cache_stats.h
%_includedir/core/persistent_string_cache.h
%_libdir/libpersistent-cache-cpp.a
%_pkgconfigdir/libpersistent-cache-cpp.pc

%files -n lib%{name}-doc
%dir %_datadir/doc/persistent-cache-cpp
%_datadir/doc/persistent-cache-cpp/*

%changelog
* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.10-alt1
- New version 1.0.10.

* Fri Sep 12 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.9-alt1
- New version 1.0.9.

* Thu Jul 17 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus
