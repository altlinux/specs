%define sover   8
%define libname lib%name%sover

Name: itpp
Version: 4.3.1
Release: alt1%ubt
Summary: C++ library of math, signal processing and communication routines
License: GPL-2.0+
Group: Development/C
Url: http://itpp.sourceforge.net/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
# Source: https://sourceforge.net/projects/itpp/files/itpp/%version/itpp-%version.tar.bz2
Patch: libitpp-4.0.7-namespace.patch
Patch1: gtest_support.patch
#PATCH-FIX-UPSTREAM memmove.patch [deb#741814] cristeab@gmail.com -- Corrected multilateration algorithm
Patch2: itpp-4.3.1_memmove.patch
# PATCH-FIX-UPSTREAM itpp-respect_dlib_suffix.diff mardnh@gmx.de -- http://sourceforge.net/p/itpp/bugs/236/
Patch3: itpp-respect_dlib_suffix.diff
# PATCH-FIX-UPSTREAM itpp-reproducible.patch bmwiedemann -- https://sourceforge.net/p/itpp/git/merge-requests/3/
Patch4: itpp-reproducible.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-ubt
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
BuildRequires: pkgconfig(lapack)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: libblas-devel
BuildRequires: libgtest-devel
BuildRequires: doxygen
BuildRequires: ghostscript
BuildRequires: texlive-latex-base
BuildRequires: fdupes

%description
IT++ is a C++ library of mathematical, signal processing and
communication classes and functions. Its main use is in simulation of
communication systems and for performing research in the area of
communications. The kernel of the library consists of generic vector and
matrix classes, and a set of accompanying routines. Such a kernel makes
IT++ similar to MATLAB or GNU Octave.

%package -n %libname
Summary: C++ library of math, signal processing and communication routines
Group: System/Libraries

%description -n %libname
IT++ is a C++ library of mathematical, signal processing and
communication classes and functions. Its main use is in simulation of
communication systems and for performing research in the area of
communications. The kernel of the library consists of generic vector and
matrix classes, and a set of accompanying routines. Such a kernel makes
IT++ similar to MATLAB or GNU Octave.

%package devel
Summary: Header files for %name
Group: Development/C
Requires: %libname = %version
Provides: %libname-devel = %version
Obsoletes: %libname-devel < %version

%description devel
Theis package contains the header files for the IT++ library.

IT++ is a C++ library of mathematical, signal processing and
communication classes and functions. Its main use is in simulation of
communication systems and for performing research in the area of
communications. The kernel of the library consists of generic vector and
matrix classes, and a set of accompanying routines. Such a kernel makes
IT++ similar to MATLAB or GNU Octave.

%package doc
Summary: Documentation for %name
Group: Documentation
Requires: %libname = %version

%description doc
This package contains the documentation for the IT++ as html and man pages.

IT++ is a C++ library of mathematical, signal processing and
communication classes and functions. Its main use is in simulation of
communication systems and for performing research in the area of
communications. The kernel of the library consists of generic vector and
matrix classes, and a set of accompanying routines. Such a kernel makes
IT++ similar to MATLAB or GNU Octave.

%prep
%setup
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# fix wrong permission in the source tarball for lapack.h
chmod 664 itpp/base/algebra/lapack.h

%build
%cmake \
  -DGTEST_DIR=%_includedir/gtest \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
build/gtests/itpp_gtests |:

%install
%cmakeinstall_std
# find dupes in docs
fdupes -s %buildroot%_docdir

%files -n %libname
%_libdir/lib%name.so.%{sover}*

%files devel
%_bindir/%name-config
%_man1dir/%name-config*
%_datadir/%name
%_includedir/%name
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%files doc
%_docdir/%name

%changelog
* Thu Jan 25 2018 Anton Midyukov <antohami@altlinux.org> 4.3.1-alt1%ubt
- Initial build for ALT Sisyphus.
