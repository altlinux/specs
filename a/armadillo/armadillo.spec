Name:           armadillo
Version:        2.4.2
Release:        alt1.svn20111208
Summary:        Fast C++ matrix library with interfaces to LAPACK and ATLAS
Group:          Sciences/Mathematics
License:        LGPLv3+
URL:            http://arma.sourceforge.net/
# fragment from .git/config :
#[svn-remote "svn"]
#  url = https://arma.svn.sourceforge.net/svnroot/arma
#  fetch = trunk:refs/remotes/trunk
#  branches = branches/*:refs/remotes/*
#  tags = tags/*:refs/remotes/tags/*
Source:         %name-%version.tar.gz
Source1: Makefile
Source2: %name.pc
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: lib%name = %version-%release

BuildRequires:  cmake gcc-c++ liblapack-devel
BuildRequires:  boost-devel

%description
Armadillo is a C++ linear algebra library (matrix maths)
aiming towards a good balance between speed and ease of use.
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.
Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries.
A delayed evaluation approach is employed (during compile time)
to combine several operations into one and reduce (or eliminate) 
the need for temporaries. This is accomplished through recursive
templates and template meta-programming.
This library is useful if C++ has been decided as the language
of choice (due to speed and/or integration capabilities), rather
than another language like Matlab (TM) or Octave.
The library is distributed under a license that is useful in
both open-source and commercial contexts.

%package -n lib%name
Summary:        Shared library for the Armadillo C++ library
Group:          System/Libraries
Conflicts: %name < %version-%release

%description -n lib%name
Armadillo is a C++ linear algebra library (matrix maths)
aiming towards a good balance between speed and ease of use.
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.
Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries.
A delayed evaluation approach is employed (during compile time)
to combine several operations into one and reduce (or eliminate) 
the need for temporaries. This is accomplished through recursive
templates and template meta-programming.
This library is useful if C++ has been decided as the language
of choice (due to speed and/or integration capabilities), rather
than another language like Matlab (TM) or Octave.
The library is distributed under a license that is useful in
both open-source and commercial contexts.

This package contains shared library for the Armadillo C++ library.

%package -n lib%name-devel
Summary:        Development files for the Armadillo C++ library
Group:          Development/C++
Requires:       lib%name = %version-%release

%description -n lib%name-devel
Armadillo is a C++ linear algebra library (matrix maths)
aiming towards a good balance between speed and ease of use.
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.
Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries.
A delayed evaluation approach is employed (during compile time)
to combine several operations into one and reduce (or eliminate) 
the need for temporaries. This is accomplished through recursive
templates and template meta-programming.
This library is useful if C++ has been decided as the language
of choice (due to speed and/or integration capabilities), rather
than another language like Matlab (TM) or Octave.
The library is distributed under a license that is useful in
both open-source and commercial contexts.

This package contains files necessary for development using the
Armadillo C++ library.

%package -n lib%name-devel-doc
Summary:        Documentation for the Armadillo C++ library
Group:          Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Armadillo is a C++ linear algebra library (matrix maths)
aiming towards a good balance between speed and ease of use.
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.
Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries.
A delayed evaluation approach is employed (during compile time)
to combine several operations into one and reduce (or eliminate) 
the need for temporaries. This is accomplished through recursive
templates and template meta-programming.
This library is useful if C++ has been decided as the language
of choice (due to speed and/or integration capabilities), rather
than another language like Matlab (TM) or Octave.
The library is distributed under a license that is useful in
both open-source and commercial contexts.

This package contains documentation for development using the
Armadillo C++ library.


%prep
%setup

install -p -m644 %SOURCE2 .
sed -i -e 's|@LIBDIR@|%_libdir|' %name.pc
sed -i -e 's|@VERSION@|%version|' %name.pc

%build
INCS="-include boost/math/complex/acos.hpp"
INCS="$INCS -include boost/math/complex/asin.hpp"
INCS="$INCS -include boost/math/complex/atan.hpp"
%add_optflags -std=c++0x $INCS
%configure
%make_build VERBOSE=1

#pushd examples
#install -m644 %SOURCE1 .
#make_build
#mv example1 %name-example1
#mv example2 %name-example2
#popd

%install
%makeinstall_std

install -d %buildroot%_pkgconfigdir
install -p -m644 %name.pc %buildroot%_pkgconfigdir

#pushd examples
#install -d %buildroot%_bindir
#install -m755 %name-example? %buildroot%_bindir
#popd

%files -n lib%name
%doc LICENSE* README.txt
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
#_datadir/Armadillo

%files -n lib%name-devel-doc
%doc examples docs_user/*

%changelog
* Tue Dec 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1.svn20111208
- Version 2.4.2

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.svn20110804
- Version 2.3.0

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.svn20110504
- Version 1.2.0

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.90-alt1.svn20101014.4
- Built with GotoBLAS2 instead of ATLAS

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.90-alt1.svn20101014.3
- Rebuilt with Boost 1.46.1

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.90-alt1.svn20101014.2
- Rebuilt for debuginfo

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.90-alt1.svn20101014.1
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.90-alt1.svn20101014
- Version 0.9.90

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.svn20100611.1
- Added pkg-config file

* Fri Jun 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.svn20100611
- Version 0.9.10

* Sun May 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt1.svn20090409
- Initial build for Sisyphus

* Wed Apr 02 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Updated description

* Wed Mar 24 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Added explicit dependence on libstdc++-devel

* Wed Mar 17 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Simplified specification of directories
- Removed library packages specified by "Requires",
  as library dependencies are detected automatically

* Wed Mar 12 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Modified to generate separate devel package (subsumes previous doc package)
- Removed redundant packages specified by "BuildRequires"
- Added CMake installation prefixes to allow for x86_64

* Wed Feb  4 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Modified to generate separate doc package

* Thu Jan 28 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Added argument to cmake: -DCMAKE_INSTALL_PREFIX=/usr 

* Thu Jan 22 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Initial spec file prepared

