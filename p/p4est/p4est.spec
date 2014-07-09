%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: p4est
Version: 1.0
Release: alt1
Summary: Parallel AMR on Forests of Octrees
License: GPLv2+
Group: Sciences/Mathematics
Url: http://www.p4est.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: %mpiimpl-devel liblapack-devel splint
BuildPreReq: pkgconfig(lua) zlib-devel chrpath libsc-devel
BuildPreReq: libmetis-devel doxygen graphviz

Requires: lib%name = %version-%release

%description
The p4est software library enables the dynamic management of a
collection of adaptive octrees, conveniently called a forest of octrees.
p4est is designed to work in parallel and scale to hundreds of thousands
of processor cores.

%package -n lib%name
Summary: Shared libraries of Parallel AMR on Forests of Octrees
Group: System/Libraries

%description -n lib%name
The p4est software library enables the dynamic management of a
collection of adaptive octrees, conveniently called a forest of octrees.
p4est is designed to work in parallel and scale to hundreds of thousands
of processor cores.

This package contains shared libraries of p4est.

%package -n lib%name-devel
Summary: Development files of Parallel AMR on Forests of Octrees
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
The p4est software library enables the dynamic management of a
collection of adaptive octrees, conveniently called a forest of octrees.
p4est is designed to work in parallel and scale to hundreds of thousands
of processor cores.

This package contains development files of p4est.

%package -n lib%name-devel-doc
Summary: Documentation and examples for Parallel AMR on Forests of Octrees
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The p4est software library enables the dynamic management of a
collection of adaptive octrees, conveniently called a forest of octrees.
p4est is designed to work in parallel and scale to hundreds of thousands
of processor cores.

This package contains development documentation and examples for p4est.

%prep
%setup

sed -i 's|@VERSION@|%version|' configure.ac

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

mkdir _ex
cp -fR example _ex/

%add_optflags -I%_includedir/metis
%autoreconf
%configure \
	--with-blas=-lopenblas \
	--enable-vtk-doubles \
	--enable-mpi \
	--enable-mpiio \
	--enable-shared \
	--enable-static=no \
	--enable-pthread \
	--with-metis \
	--with-sc=%prefix
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
sed -i 's|^Makefile:|Makefile_:|' Makefile
%make_build

doxygen
mv doxygen/html doxygen/doxygen

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

rm -f %buildroot%_libdir/*.a

chrpath -r %mpidir/lib %buildroot%_bindir/* ||:

%files
%doc AUTHORS NEWS README
%_bindir/*
%_datadir/data

%files -n lib%name
%_libdir/libp4est-*.so

%files -n lib%name-devel
%_sysconfdir/*
%_includedir/*
%_aclocaldir/*
%_libdir/*.so
%exclude %_libdir/libp4est-*.so

%files -n lib%name-devel-doc
%doc doc/*
%doc _ex/*
%doc doxygen/doxygen

%changelog
* Tue Jul 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Version 1.0

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4.2-alt1
- Version 0.3.4.2

* Thu Jul 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4.1-alt1
- Version 0.3.4.1

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt4
- Built with OpenBLAS instead of GotoBLAS2

* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt3
- Rebuilt with OpenMPI 1.6

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt2
- Fixed RPATH

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Version 0.3.4

* Wed May 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3.8-alt1.3d81
- Version 0.3.3.8-3d81

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1.70-alt1.e24d.3
- Rebuilt

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1.70-alt1.e24d.2
- Built with GotoBLAS2 instead of ATLAS

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1.70-alt1.e24d.1
- Rebuilt for debuginfo

* Sat Dec 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1.70-alt1.e24d
- Initial build for Sisyphus

