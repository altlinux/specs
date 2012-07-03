%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl
%define somver 0
%define sover %somver.60.25

Name: libflame
Version: r6025
Release: alt1
Summary: Formal Linear Algebra Method Environment
License: LGPL v2.1
Group: System/Libraries
Url: http://www.cs.utexas.edu/users/flame/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
#Source1: http://www.cs.utexas.edu/users/flame/book/Downloads/FLAMEC/example.tar.gz
#Source2: elemental.tar.gz

BuildPreReq: gcc-fortran liblapack-devel
BuildPreReq: doxygen /usr/bin/dvips texmf(latex/draftcopy)

%description
The objective of the FLAME project is to transform the development of dense
linear algebra libraries from an art reserved for experts to a science that can
be understood by novice and expert alike. Rather than being only a library, the
project encompasses a new notation for expressing algorithms, a methodology for
systematic derivation of algorithms, Application Program Interfaces (APIs) for
representing the algorithms in code, and tools for mechanical derivation,
implementation and analysis of algorithms and implementations.

%package devel
Summary: Development files of Formal Linear Algebra Method Environment
Group: Development/Other
Requires: %name = %version-%release
Requires: liblapack-goto-devel

%description devel
The objective of the FLAME project is to transform the development of dense
linear algebra libraries from an art reserved for experts to a science that can
be understood by novice and expert alike. Rather than being only a library, the
project encompasses a new notation for expressing algorithms, a methodology for
systematic derivation of algorithms, Application Program Interfaces (APIs) for
representing the algorithms in code, and tools for mechanical derivation,
implementation and analysis of algorithms and implementations.

This package contains development files dof libflame.

%package doc
Summary: Documentation for Formal Linear Algebra Method Environment
Group: Development/Documentation
BuildArch: noarch

%description doc
The objective of the FLAME project is to transform the development of dense
linear algebra libraries from an art reserved for experts to a science that can
be understood by novice and expert alike. Rather than being only a library, the
project encompasses a new notation for expressing algorithms, a methodology for
systematic derivation of algorithms, Application Program Interfaces (APIs) for
representing the algorithms in code, and tools for mechanical derivation,
implementation and analysis of algorithms and implementations.

This package contains development documentation for FLAME.

%package example
Summary: Example of using Formal Linear Algebra Method Environment
Group: Development/Other
BuildArch: noarch

%description example
The objective of the FLAME project is to transform the development of dense
linear algebra libraries from an art reserved for experts to a science that can
be understood by novice and expert alike. Rather than being only a library, the
project encompasses a new notation for expressing algorithms, a methodology for
systematic derivation of algorithms, Application Program Interfaces (APIs) for
representing the algorithms in code, and tools for mechanical derivation,
implementation and analysis of algorithms and implementations.

This package contains example of using FLAME.

%prep
%setup
#tar -xzf %SOURCE1
#tar -xzf %SOURCE2

sed -i "s|@fla_host_cpu@|%_arch|" build/config.mk.in

%build
%add_optflags %optflags_shared
#autoreconf
#./bootstrap
%configure \
	--enable-debug \
	--enable-static-build \
	--enable-dynamic-build \
	--enable-external-lapack-for-subproblems \
	--enable-lapack2flame=no \
	--enable-external-lapack-interfaces \
	--enable-blas3-front-end-cntl-trees \
	--disable-cblas-interfaces \
	--disable-goto-interfaces \
	--disable-gpu \
	--enable-verbose-make-output \
	--enable-multithreading=pthreads \
	--enable-memory-leak-counter \
	--enable-supermatrix \
	--enable-supermatrix-visualization
%make_build HOST=%_host SOMVER=%somver SOVER=%sover

doxygen
pushd docs/libflame
%make_build
popd

%install
%makeinstall_std HOST=%_host INSTALL_PREFIX=%buildroot%prefix \
	 SOMVER=%somver SOVER=%sover

rm -f %buildroot%_includedir
mv %buildroot%prefix/include-%_arch-%version %buildroot%_includedir
%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -d %buildroot%_docdir/%name

install -m644 $(find ./ -name '*.pdf') %buildroot%_docdir/%name
mv doxygen/html %buildroot%_docdir/%name/

%files
%doc AUTHORS CHANGELOG CONTRIBUTORS LICENSE
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files doc
%_docdir/%name

%files example
%doc examples

%changelog
* Wed Apr 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r6025-alt1
- Version r6025

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r4818-alt4
- Fixed requirements for devel package

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r4818-alt3
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r4818-alt2
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r4818-alt1
- Version r4818

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r4073-alt4
- Rebuilt for soname set-versions

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r4073-alt3
- Fixed underlinking of libraries

* Tue Jun 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r4073-alt2
- Fixed Makefile instead of sed's changing

* Mon Jun 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r4073-alt1
- Version r4073
- Changed multithreading model: pthreads -> openmp
- Added shared library

* Mon Jul 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r3119-alt3
- Added texmf(latex/draftcopy) buildreq (fix build of documentation)

* Tue Jun 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r3119-alt2
- Added example

* Tue Jun 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r3119-alt1
- Initial build for Sisyphus

