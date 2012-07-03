%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: p4est
Version: 0.3.4
Release: alt3
Summary: Parallel AMR on Forests of Octrees
License: GPLv2+
Group: Sciences/Mathematics
Url: http://www.p4est.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: %mpiimpl-devel liblapack-devel splint
BuildPreReq: pkgconfig(lua) zlib-devel chrpath

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

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

mkdir _ex
cp -fR example _ex/

%configure \
	--with-blas=-lgoto2 \
	--enable-vtk-doubles \
	--enable-mpi \
	--enable-mpiio \
	--enable-shared \
	--enable-static=no
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

rm -f %buildroot%_libdir/*.a

chrpath -r %mpidir/lib %buildroot%_bindir/* ||:

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_sysconfdir/*
%_includedir/*
%_aclocaldir/*
%_libdir/*.so

%files -n lib%name-devel-doc
%doc doc/*
%doc _ex/*

%changelog
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

