%define _unpackaged_files_terminate_build 1

%def_without doc

Name: blitz
Summary: C++ class library for scientific computing
Version: 1.0.2
Release: alt1.1
Group: Sciences/Mathematics
License: LGPLv3 or BSD-3-Clause or Artistic-2.0
URL: https://github.com/blitzpp/blitz

# https://github.com/blitzpp/blitz.git
Source: %name-%version.tar

Patch1: %name-%version-alt-build.patch

Requires: lib%name = %EVR

BuildRequires: gcc-c++ gcc-fortran liblapack-devel
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: rpm-build-python3
%if_with doc
BuildRequires: doxygen graphviz
# explicitly added texinfo for info files
BuildRequires: texinfo
BuildRequires: /usr/bin/pdflatex
%endif

%description
Blitz++ is a C++ class library for scientific computing which provides
performance on par with Fortran 77/90. It uses template techniques to achieve
high performance. Blitz++ provides dense arrays and vectors, random number
generators, and small vectors.

%package -n lib%name
Summary: Shared libraries of Blitz++
Group: System/Libraries

%description -n lib%name
Blitz++ is a C++ class library for scientific computing which provides
performance on par with Fortran 77/90. It uses template techniques to achieve
high performance. Blitz++ provides dense arrays and vectors, random number
generators, and small vectors.

This package contains shared libraries of Blitz++.

%package -n lib%name-devel
Summary: Development files of Blitz++
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Blitz++ is a C++ class library for scientific computing which provides
performance on par with Fortran 77/90. It uses template techniques to achieve
high performance. Blitz++ provides dense arrays and vectors, random number
generators, and small vectors.

This package contains development files of Blitz++.

%if_with doc
%package -n lib%name-devel-doc
Summary: Documentation for Blitz++
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Blitz++ is a C++ class library for scientific computing which provides
performance on par with Fortran 77/90. It uses template techniques to achieve
high performance. Blitz++ provides dense arrays and vectors, random number
generators, and small vectors.

This package contains development documentation for Blitz++.
%endif

%package examples
Summary: Examples for Blitz++
Group: Development/Documentation
BuildArch: noarch

%description examples
Blitz++ is a C++ class library for scientific computing which provides
performance on par with Fortran 77/90. It uses template techniques to achieve
high performance. Blitz++ provides dense arrays and vectors, random number
generators, and small vectors.

This package contains examples for Blitz++.

%prep
%setup
%patch1 -p1

%build
export CC="gcc -pthread"
export CXX="g++ -pthread"

%cmake \
	-DBUILD_DOC:BOOL=%{with doc} \
	-DBUILD_TESTING:BOOL=ON \
	-DBZ_THREADSAFE:BOOL=ON \
	%nil

%cmake_build
%if_with doc
%cmake_build -t blitz-doc
%endif

%cmake_build -t testsuite
%cmake_build -t examples

%install
export CC="gcc -pthread"
export CXX="g++ -pthread"

%cmake_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir

%cmake_build -t check-testsuite
%cmake_build -t check-examples

%files
%doc COPYING* COPYRIGHT LEGAL LICENSE
%doc AUTHORS ChangeLog* README.md
%if_with doc
%_infodir/*
%endif

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/cmake/*
%_includedir/*
%_pkgconfigdir/*

%if_with doc
%files -n lib%name-devel-doc
%doc %_docdir/%name
%endif

%files examples
%doc examples

%changelog
* Tue Jun 01 2021 Arseny Maslennikov <arseny@altlinux.org> 1.0.2-alt1.1
- NMU:
  + Built with python3 as a build requirement.
  + Adapted spec to new cmake macros.

* Wed Feb 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Updated to upstream version 1.0.2.

* Fri May 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Updated to upstream version 1.0.1.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1.hg20120703.1
- NMU: added BR: texinfo

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.hg20120703
- New snapshot

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.hg20120125
- New snapshot

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.cvs20110820
- New snapshot

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.cvs20110418
- Version 0.10

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20100803.4
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20100803.3
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20100803.2
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20100803.1
- Rebuilt for soname set-versions

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20100803
- New snapshot

* Tue Jul 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20090702
- Initial build for Sisyphus

