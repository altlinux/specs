Name:     libmed
Version:  4.1.0
Release:  alt3

Summary:  Library to store and exchange meshed data or computation result in MED format
License:  GPLv3 and LGPLv3
Group:    System/Libraries
Url:      https://www.salome-platform.org/downloads/current-version

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   med-%version.tar

Patch1: med-4.1.0-fedora-cmake.patch
Patch2: med-4.1.0-gentoo-build-against-hdf5-1.14.patch

BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: libhdf5-devel
BuildRequires: hdf5-tools
BuildRequires: gcc-fortran

%description
Library to store and exchange meshed data or computation result in MED format.

%package devel
Group: Development/C
Summary: Development files for libmed

%description devel
Development files for libmed.

%package tools
Group: Development/C
Summary: Utilities for work with MED format

%description tools
Utilities for work with MED format.

%prep
%setup -n med-%{version}_SRC
%patch1 -p1
%patch2 -p1

%build
%cmake \
	-DMEDFILE_BUILD_PYTHON:BOOL=OFF \
	%nil

%cmake_build

%install
%cmake_install

# Remove test-suite files
rm -rf %buildroot%_bindir/testc
rm -rf %buildroot%_bindir/testf
rm -rf %buildroot%_bindir/testpy

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
pushd %_cmake__builddir
ctest
popd

%files
%doc AUTHORS README
%doc %_defaultdocdir/med
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_libdir/cmake/*
%_includedir/*

%files tools
%_bindir/*

%changelog
* Mon Apr 01 2024 Anton Farygin <rider@altlinux.ru> 4.1.0-alt3
- NMU: added patch from Gentoo against hdf5 1.14

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 4.1.0-alt2.1
- NMU: spec: adapted to new cmake macros.

* Fri Apr 23 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.0-alt2
- Fixed build dependencies.

* Mon Apr 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.0-alt1
- Updated to upstream version 4.1.0.
- Enabled tests.

* Tue Jan 12 2021 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt3
- FTBFS: disable tests.

* Mon Sep 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.1-alt2
- NMU: rebuilt for aarch64.

* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt1
- Initial build in Sisyphus.
