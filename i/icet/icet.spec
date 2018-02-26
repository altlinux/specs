%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: icet
Version: 2.1.0
Release: alt3.git20120130
Summary: The Image Composition Engine for Tiles (IceT)
License: Public domain
Group: Graphics
Url: http://icet.sandia.gov/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://public.kitware.com/IceT.git
Source: %name-%version.tar.gz
Source1: http://www.cs.unm.edu/~kmorel/IceT/IceTUsersGuide.pdf
Source2: CMakeCache.txt

BuildPreReq: %mpiimpl-devel cmake libGLU-devel libGL-devel
BuildPreReq: ctest slurm-utils libICE-devel
BuildPreReq: libX11-devel libXtst-devel libXau-devel libXcomposite-devel
BuildPreReq: libXcursor-devel libXdamage-devel libXdmcp-devel
BuildPreReq: libXext-devel libXfixes-devel libXft-devel libXi-devel
BuildPreReq: libXinerama-devel libXpm-devel libXrandr-devel
BuildPreReq: libXrender-devel libXt-devel libXv-devel libXxf86misc-devel
BuildPreReq: libXxf86vm-devel libGLUT-devel libXmu-devel
BuildPreReq: libmpe2-devel libXScrnSaver-devel

%description
The Image Composition Engine for Tiles (IceT) is a high-performance
sort-last parallel rendering library. In addition to providing
accelerated rendering for a standard display, IceT provides the unique
ability to generate images for tiled displays. The overall resolution of
the display may be several times larger than any viewport that may be
rendered by a single machine.

%package -n lib%name
Summary: Shared libraries of the Image Composition Engine for Tiles (IceT)
Group: System/Libraries

%description -n lib%name
The Image Composition Engine for Tiles (IceT) is a high-performance
sort-last parallel rendering library. In addition to providing
accelerated rendering for a standard display, IceT provides the unique
ability to generate images for tiled displays. The overall resolution of
the display may be several times larger than any viewport that may be
rendered by a single machine.

This package contains shared libraries of IceT.

%package devel
Summary: Development files of the Image Composition Engine for Tiles (IceT)
Group: Development/C
BuildArch: noarch
Requires: lib%name = %version-%release

%description devel
The Image Composition Engine for Tiles (IceT) is a high-performance
sort-last parallel rendering library. In addition to providing
accelerated rendering for a standard display, IceT provides the unique
ability to generate images for tiled displays. The overall resolution of
the display may be several times larger than any viewport that may be
rendered by a single machine.

This package contains development files of IceT.

%package tests
Summary: Tests for the Image Composition Engine for Tiles (IceT)
Group: Graphics
Requires: lib%name = %version-%release

%description tests
The Image Composition Engine for Tiles (IceT) is a high-performance
sort-last parallel rendering library. In addition to providing
accelerated rendering for a standard display, IceT provides the unique
ability to generate images for tiled displays. The overall resolution of
the display may be several times larger than any viewport that may be
rendered by a single machine.

This package contains tests for IceT.

%package devel-docs
Summary: Documentation for the Image Composition Engine for Tiles (IceT)
Group: Development/Documentation
BuildArch: noarch

%description devel-docs
The Image Composition Engine for Tiles (IceT) is a high-performance
sort-last parallel rendering library. In addition to providing
accelerated rendering for a standard display, IceT provides the unique
ability to generate images for tiled displays. The overall resolution of
the display may be several times larger than any viewport that may be
rendered by a single machine.

This package contains development documentation for IceT.

%prep
%setup
install -p -m644 %SOURCE1 %SOURCE2 .

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

cmake \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DMPIDIR:PATH=%mpidir \
	.
%make_build verbose=1

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%makeinstall_std

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

install -d %buildroot%_bindir
install -m755 bin/icetTests_mpi %buildroot%_bindir

rm -f %buildroot%_libdir/*.cmake

%files -n lib%name
%doc History README
%_libdir/*.so

%files devel
%_includedir/*

%files tests
%_bindir/*
%doc tests/*.c tests/*.h

%files devel-docs
%doc *.pdf
%_man3dir/*

%changelog
* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt3.git20120130
- Rebuilt with OpenMPI 1.6

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2.git20120130
- New snapshot

* Fri Feb 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2.git20111012
- Built without OSMesa

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20111012
- New snapshot

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20110811
- Version 2.1.0

* Wed May 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20110504
- New snapshot
- Built with MPE2

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20101112.2
- Fixed build

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20101112.1
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20101112
- Version 2.0.0

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100719.1
- Rebuilt for soname set-versions

* Mon Sep 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20100719
- Initial build for Sisyphus

