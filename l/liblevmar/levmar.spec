# SOlib major and minor version
%global major 2
%global minor 6

Name: liblevmar
Version: 2.6
Release: alt2
Summary: Levenberg-Marquardt nonlinear least squares algorithm
Url: https://users.ics.forth.gr/~lourakis/levmar/
Group: System/Libraries

Source0: %name-%version.tar

# Patch to fix compilation of the shared library and compile the demo program
Patch0: levmar-cmake-shared.patch

License: GPL-2.0-or-later
BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libblas-devel
BuildRequires: ctest cmake
BuildRequires: dos2unix
BuildRequires: chrpath
BuildRequires: libblas-devel
#BuildRequires: libclapack-devel
BuildRequires: liblapack-devel

Provides: levmar = %EVR

%description
levmar is a native ANSI C implementation of the Levenberg-Marquardt
optimization algorithm.  Both unconstrained and constrained (under linear
equations, inequality and box constraints) Levenberg-Marquardt variants are
included.  The LM algorithm is an iterative technique that finds a local
minimum of a function that is expressed as the sum of squares of nonlinear
functions.  It has become a standard technique for nonlinear least-squares
problems and can be thought of as a combination of steepest descent and the
Gauss-Newton method.  When the current solution is far from the correct on,
the algorithm behaves like a steepest descent method: slow, but guaranteed
to converge.  When the current solution is close to the correct solution, it
becomes a Gauss-Newton method.

%package devel
Group: Development/Other
Summary: Development files for levmar library, and demo program
Requires: liblevmar = %EVR
Provides: levmar-devel = %EVR

%description devel
Development files for the levmar library, and demo program.

%prep
%setup
%autopatch -p1

dos2unix -k README.txt

%build
%add_optflags %optflags_shared
%cmake -DLINSOLVERS_RETAIN_MEMORY:BOOL=OFF -DNEED_F2C:BOOL=OFF
%cmake_build

%install
install -D -p -m 755 "%_cmake__builddir/liblevmar.so.%major.%minor" "%buildroot%_libdir/liblevmar.so.%major.%minor"
install -D -p -m 644 levmar.h "%buildroot%_includedir/levmar.h"
install -D -p -m 755 "%_cmake__builddir/lmdemo" "%buildroot%_bindir/lmdemo"
ln -s "liblevmar.so.%major.%minor" "%buildroot%_libdir/liblevmar.so.%major"
ln -s "liblevmar.so.%major.%minor" "%buildroot%_libdir/liblevmar.so"
chrpath --delete "%buildroot%_bindir/lmdemo"

%check
"%_cmake__builddir/lmdemo"

%files
%doc README.txt LICENSE
%_libdir/liblevmar.so.%major.%minor
%_libdir/liblevmar.so.%major

%files devel
%_includedir/levmar.h
%_libdir/liblevmar.so
%_bindir/lmdemo

%changelog
* Sat Jun 21 2025 Anton Midyukov <antohami@altlinux.org> 2.6-alt2
- use %%cmake macros (fix FTBFS)
- cleanup spec
- update URL
- convert License to SPDX format

* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 2.6-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_14
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_10
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_9
- new version

