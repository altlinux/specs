%define oname meshbuilder
%define scalar_type real
%define ldir %_libdir/petsc-%scalar_type
%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: %oname-%scalar_type
Version: 0.2.0
Release: alt4.bzr20110620
Summary: A tool for viewing and marking meshes, especially for use with DOLFIN
License: LGPL v2.1
Group: Graphics
Url: http://www.fenics.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch lp:meshbuilder
Source: %oname-%version.tar.gz

BuildPreReq: cmake python-module-Pyro4 libtrilinos10-devel
BuildPreReq: gcc-c++ libqt4-devel libOpenSceneGraph-devel
BuildPreReq: libtetgen-devel libtriangle-devel libvtk-devel
BuildPreReq: libdolfin-%scalar_type-devel libmpfr-devel
BuildPreReq: libXtst-devel libXcomposite-devel libXdamage-devel
BuildPreReq: libXdmcp-devel libXft-devel libXpm-devel chrpath
BuildPreReq: libXScrnSaver-devel libXxf86misc-devel libXxf86vm-devel

%description
MeshBuilder is a tool for viewing and marking meshes, especially for use
with DOLFIN.

%package -n %oname-example-data
Summary: Example data for %oname
Group: Graphics
BuildArch: noarch

%description -n %oname-example-data
Sample data for MeshBuilder, a tool for viewing and marking meshes,
especially for use with DOLFIN.

%prep
%setup
#sed -i 's|@PETSC_DIR@|%ldir|g' %oname.pro
#sed -i 's|@SCALAR_TYPE@|%scalar_type|g' %oname.pro

%build
mpi-selector --set %mpiimpl
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib:%ldir/lib -L%mpidir/lib:%ldir/lib"

FLAGS="%optflags"
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="$FLAGS" \
	-DCMAKE_CXX_FLAGS:STRING="$FLAGS" \
	-DCMAKE_Fortran_FLAGS:STRING="$FLAGS" \
	-DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DCMAKE_EXE_LINKER_FLAGS:STRING='-L%ldir/lib' \
	.
%make all VERBOSE=1

%install
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib:%ldir/lib -L%mpidir/lib:%ldir/lib"
%makeinstall_std

chrpath -r %mpidir/lib:%ldir/lib src/%oname
cp -f src/%oname %buildroot%_bindir/%name
rm -f %buildroot%_bindir/%oname

%if "%scalar_type" == "real"
install -d %buildroot%_datadir/%oname
cp -fR sample_data %buildroot%_datadir/%oname/
%endif

%brp_strip_none %_bindir/*

%files
%doc COPYING README TODO
%_bindir/*
%_man1dir/*

%if "%scalar_type" == "real"
%files -n %oname-example-data
%dir %_datadir/%oname
%_datadir/%oname/sample_data
%endif

%changelog
* Sun Jul 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt4.bzr20110620
- Rebuilt with OpenMPI 1.6

* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt3.bzr20110620
- Rebuilt with updated NumPy

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.bzr20110620
- Fixed build with Boost 1.48.0

* Mon Oct 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20110620.1
- Fixed build

* Wed Sep 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20110620
- New snapshot

* Thu Aug 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20110313.1
- Rebuilt with Dolfin 0.9.11

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20110313
- New snapshot

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20100825.3
- Built with GotoBLAS2 instead of ATLAS

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20100825.2
- Rebuilt for debuginfo

* Fri Dec 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20100825.1
- Rebuilt with dolfin 0.9.9-alt1.bzr20101201

* Fri Nov 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20100825
- New snapshot

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20100423.3
- Rebuilt with CGAL 3.7

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20100423.2
- Rebuilt with PETSc 3.1

* Wed Jul 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20100423.1
- Rebuilt with reformed ParMetis

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20100423
- New snapshot

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20091020.1
- Rebuilt with CGAL 3.6

* Wed Dec 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20091020
- Initial build for Sisyphus

