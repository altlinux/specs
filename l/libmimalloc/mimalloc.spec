%define _unpackaged_files_terminate_build 1

Group: System/Libraries

BuildRequires(pre): rpm-macros-cmake

%define oldname mimalloc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Name:           libmimalloc
Version:        2.0.7
Release:        alt1
Summary:        A general purpose allocator with excellent performance

License:        MIT
URL:            https://github.com/microsoft/mimalloc
Source:         %name-%version.tar

BuildRequires:  ctest cmake
BuildRequires:  gcc-c++

%description
mimalloc (pronounced "me-malloc")
is a general purpose allocator with excellent performance characteristics.
Initially developed by Daan Leijen for the run-time systems.

%package -n libmimalloc2
Summary:        Shared library for the %oldname library
Group:          System/Libraries

%description -n libmimalloc2
mimalloc (pronounced "me-malloc")
is a general purpose allocator with excellent performance characteristics.
Initially developed by Daan Leijen for the run-time systems.

This package contains the shared library.

%package -n libmimalloc-devel
Group: Development/C
Summary:        Development files for %oldname
Requires:       libmimalloc2 = %EVR
Provides: %oldname-devel = %EVR

%description -n libmimalloc-devel
Development package for mimalloc.

%prep
%setup

# Remove unneeded binaries from source tree.
rm -rf bin

%build
%cmake \
    -DMI_BUILD_OBJECT=OFF \
    -DMI_OVERRIDE=OFF \
    -DMI_INSTALL_TOPLEVEL=ON \
    -DMI_BUILD_STATIC=OFF \
    -DMI_BUILD_TESTS=ON \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install


%check
cd %_cmake__builddir; ctest -V; cd -


%files -n libmimalloc2
%doc --no-dereference LICENSE
%doc readme.md
%_libdir/libmimalloc.so.2
%_libdir/libmimalloc.so.2.*

%files -n libmimalloc-devel
%_libdir/libmimalloc.so
%_libdir/cmake/%oldname
%_includedir/*
%_pkgconfigdir/*


%changelog
* Sun Dec 04 2022 Arseny Maslennikov <arseny@altlinux.org> 2.0.7-alt1
- 2.0.6 -> 2.0.7.

* Mon Oct 31 2022 Arseny Maslennikov <arseny@altlinux.org> 2.0.6-alt1
- 2.0.3 -> 2.0.6.

* Sat Nov 27 2021 Igor Vlasenko <viy@altlinux.org> 2.0.3-alt1_1
- new version

* Tue Jun 01 2021 Arseny Maslennikov <arseny@altlinux.org> 1.0-alt1.1
- NMU: spec: adapted to new CMake macros.

* Sun Jun 23 2019 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build for ALT

