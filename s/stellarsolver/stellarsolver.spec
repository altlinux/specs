%global sover 2
%define libstellarsolver libstellarsolver%sover

%add_findreq_skiplist %_includedir/libstellarsolver/astrometry/*.ph

Name: stellarsolver
Version: 2.6
Release: alt1

Group: System/Libraries
Summary: SEP-based Star Extractor and Internal Astrometric Solver
Url: https://github.com/rlancaste/stellarsolver/
License: LGPL-3.0-or-later

Source: %name-%version.tar

BuildRequires: cmake qt6-base-devel
BuildRequires: libcfitsio-devel libgsl-devel wcslib-devel

%description
StellarSolver is the Cross Platform SEP-based Star Extractor
and Astrometry.net-Based Internal Astrometric Solver:
* An Astrometric Plate Solver for Mac, Linux, and Windows, built on
  Astrometry.net and SEP (sextractor)
* Meant to be an internal library for use in a program like KStars for internal
  plate solving on all supported operating systems

%package -n %libstellarsolver
Group: System/Libraries
Summary: Shared library of StellarSolver
%description -n %libstellarsolver
Shared library of Stellarsolver, meant to be an internal library for use in
a program like KStars for internal plate solving on all supported operating
systems.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%cmake \
    -DUSE_QT5=OFF \
    -DBUILD_TESTER=ON \
    -DBUILD_BATCH_SOLVER=ON \
    #
%cmake_build

%install
%cmake_install

%files
%doc README.md LICENSE
%_bindir/Stellar*
%_desktopdir/com.github.rlancaste.stellar*.desktop
%_iconsdir/*/*/*/Stellar*Solver*.*

%files -n %libstellarsolver
%doc README.md LICENSE
%_libdir/libstellarsolver.so.%sover
%_libdir/libstellarsolver.so.*

%files devel
%_includedir/*
%_libdir/lib*.so
%_libdir/cmake/StellarSolver/
%_libdir/pkgconfig/stellarsolver.pc

%changelog
* Fri Nov 08 2024 Sergey V Turchin <zerg@altlinux.org> 2.6-alt1
- initial build
