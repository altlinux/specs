%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.1.16

%define pname gasnet
Name: GASNet
Version: 1.16.2
Release: alt3
Summary: Network- and language-independent high-performance communication
License: MIT
Group: Networking/Other
Url: http://gasnet.cs.berkeley.edu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://gasnet.cs.berkeley.edu/%name-%version.tar.gz

Requires: lib%pname = %version-%release
Provides: %pname = %version-%release

BuildPreReq: %mpiimpl-devel

%description
GASNet is a language-independent, low-level networking layer that
provides network-independent, high-performance communication primitives
tailored for implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran. The interface is primarily
intended as a compilation target and for use by runtime library writers
(as opposed to end users), and the primary goals are high performance,
interface portability, and expressiveness. GASNet stands for
"Global-Address Space Networking".

The design of GASNet is partitioned into two layers to maximize porting
ease without sacrificing performance: the lower level is a narrow but
very general interface called the GASNet core API - the design is based
heavily on Active Messages, and is implemented directly on top of each
individual network architecture. The upper level is a wider and more
expressive interface called the GASNet extended API, which provides
high-level operations such as remote memory access and various
collective operations.

%package -n %pname-doc
Summary: Documentation for GASNet
Group: Documentation
BuildArch: noarch

%description -n %pname-doc
GASNet is a language-independent, low-level networking layer that
provides network-independent, high-performance communication primitives
tailored for implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran. The interface is primarily
intended as a compilation target and for use by runtime library writers
(as opposed to end users), and the primary goals are high performance,
interface portability, and expressiveness. GASNet stands for
"Global-Address Space Networking".

This package contains documentation for GASNet.

%package -n lib%pname
Summary: Shared libraries of GASNet
Group: System/Libraries

%description -n lib%pname
GASNet is a language-independent, low-level networking layer that
provides network-independent, high-performance communication primitives
tailored for implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran. The interface is primarily
intended as a compilation target and for use by runtime library writers
(as opposed to end users), and the primary goals are high performance,
interface portability, and expressiveness. GASNet stands for
"Global-Address Space Networking".

This package contains shared libraries of GASNet.

%package -n lib%pname-devel
Summary: Development files of GASNet
Group: Development/C++
Requires: lib%pname = %version-%release

%description -n lib%pname-devel
GASNet is a language-independent, low-level networking layer that
provides network-independent, high-performance communication primitives
tailored for implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran. The interface is primarily
intended as a compilation target and for use by runtime library writers
(as opposed to end users), and the primary goals are high performance,
interface portability, and expressiveness. GASNet stands for
"Global-Address Space Networking".

This package contains development files of GASNet.

%package -n lib%pname-devel-static
Summary: Static libraries of GASNet
Group: Development/C++
Requires: lib%pname-devel = %version-%release
Conflicts: libberkeley_upc-devel

%description -n lib%pname-devel-static
GASNet is a language-independent, low-level networking layer that
provides network-independent, high-performance communication primitives
tailored for implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran. The interface is primarily
intended as a compilation target and for use by runtime library writers
(as opposed to end users), and the primary goals are high performance,
interface portability, and expressiveness. GASNet stands for
"Global-Address Space Networking".

This package contains static libraries of GASNet.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags %optflags_shared -DGASNETI_BUG1389_WORKAROUND=1

./Bootstrap -y
%configure \
	--enable-pthreads \
	--disable-full-path-expansion \
	--enable-allow-libcpp \
	--enable-segment-everything \
	--enable-par \
	--enable-mpi \
	--enable-ibv \
	--with-max-pthreads-per-node=32 \
	--with-mpi-cflags="-I%mpidir/include %optflags_shared" \
	--with-mpi-libs="-Wl,-R%mpidir/lib -lmpi_cxx" \
	--with-target-cxxflags="%optflags_shared"
sed -i '10a\#define GASNETI_BUG1389_WORKAROUND 1' gasnet_config.h

%make_build all MPIDIR=%mpidir TOPDIR=$PWD \
	SOVER=%sover SOMVER=%somver

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%make_install install-all DESTDIR=%buildroot \
	TOPDIR=$PWD SOMVER=%somver

%files
%_bindir/*

%files -n %pname-doc
%_docdir/%pname

%files -n lib%pname
%_libdir/*.so.*

%files -n lib%pname-devel
%_libdir/*.so
%_includedir/*
%dir %_libdir/valgrind
%_libdir/valgrind/*

%files -n lib%pname-devel-static
%_libdir/*.a

%changelog
* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.2-alt3
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.2-alt2
- Fixed RPATH

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.2-alt1
- Version 1.16.2

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.0-alt3
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.0-alt2
- Rebuilt for debuginfo

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.0-alt1
- Version 1.16.0

* Fri Oct 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.2-alt4
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.2-alt3
- Fixed overlinking of libraries

* Fri Sep 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.2-alt2
- Built with GASNETI_BUG1389_WORKAROUND

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.2-alt1
- Version 1.14.2

* Fri Oct 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.0-alt1
- Initial build for Sisyphus

