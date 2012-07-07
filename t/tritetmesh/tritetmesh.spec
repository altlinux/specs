%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: tritetmesh
Version: 0.0.1
Release: alt3.bzr20100630
Summary: TriTetMesh provides an intuitive interface to Triangle and Tetgen
Group: Development/Tools
License: GPL v3
URL: http://www.fenics.org/
# bzr branch lp:tritetmesh
Source: %name-%version.tar.gz
Source1: triangle_mesh.pc
Source2: tetgen_mesh.pc
Source3: mpic++
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: lib%name = %version-%release

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel scons swig python-module-petsc-config
BuildPreReq: libnumpy-devel libmpfr-devel libtrilinos10-devel
BuildPreReq: libdolfin-real-devel python-module-dolfin-real

%description
TriTetMesh provides an intuitive interface to Triangle and Tetgen. These
packages produces quality mesh in 2D and 3D based on triangles and
tetrahedrons. The interface is provided as a C++/Python (through swig)
wrapper.

Structure
---------
TriTetMesh is a package that includes TriMesh and TetMesh, which are
the actuall wrappers of Triangle and Tetgen. These comes as standalone
c++ libraries and python modules.

Mesh formats
------------
TriTetMesh can save generated mesh in the native format that both Triangle
and Tetgen use and in the dolfin format. It can also read PLCs (see the
documentation of tetgen) that tetgen natively can read.

%package -n lib%name
Summary: Shared libraries of TriTetMesh
Group: System/Libraries

%description -n lib%name
TriTetMesh provides an intuitive interface to Triangle and Tetgen. These
packages produces quality mesh in 2D and 3D based on triangles and
tetrahedrons. The interface is provided as a C++/Python (through swig)
wrapper.

This package contains shared libraries of TriTetMesh.

%package -n lib%name-devel
Summary: Development files of TriTetMesh
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
TriTetMesh provides an intuitive interface to Triangle and Tetgen. These
packages produces quality mesh in 2D and 3D based on triangles and
tetrahedrons. The interface is provided as a C++/Python (through swig)
wrapper.

This package contains development files of TriTetMesh.

%package demo
Summary: Demos of TriTetMesh
Group: Development/Documentation
Requires: lib%name = %version-%release

%description demo
TriTetMesh provides an intuitive interface to Triangle and Tetgen. These
packages produces quality mesh in 2D and 3D based on triangles and
tetrahedrons. The interface is provided as a C++/Python (through swig)
wrapper.

This package contains demos of TriTetMesh.

%package -n python-module-%name
Summary: Python wrapper of TriTetMesh
Group: Development/Python
Requires: lib%name = %version-%release
%py_requires mpi

%description -n python-module-%name
TriTetMesh provides an intuitive interface to Triangle and Tetgen. These
packages produces quality mesh in 2D and 3D based on triangles and
tetrahedrons. The interface is provided as a C++/Python (through swig)
wrapper.

This package contains Python wrapper of TriTetMesh.

%prep
%setup
cp externals/tetgen/tetgen.h externals/tetgen/tetgen_mesh.h
cp externals/triangle/triangle.h externals/triangle/triangle_mesh.h
sed -i "s|@TOPDIR@|$PWD|g" SConstruct

install -m644 %SOURCE1 %SOURCE2 .
sed -i 's|@BUILDLIB@|%buildroot%_libdir|g' *.pc
sed -i 's|^libdir.*|libdir=%_libdir|' *.pc
install -m755 %SOURCE3 .

%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" mpic++

%install
# Prepare environments

source %_bindir/petsc-real.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export PATH=$PWD:$PATH

install -d $PWD/pkgconfig
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:$PWD/pkgconfig

# build tetgen

cd externals/tetgen
scons
scons install prefix=%buildroot%prefix
cp -f ../../*.pc ../../pkgconfig/

# build triangle

cd ../triangle
scons
scons install prefix=%buildroot%prefix
cp -f ../../*.pc ../../pkgconfig/

cd ../..

# prepare pkg-config files

install -d  %buildroot%_pkgconfigdir
cp %_pkgconfigdir/dolfin-real.pc pkgconfig/
ln -s dolfin-real.pc pkgconfig/dolfin.pc
cp -f *.pc pkgconfig/
cp -f *.pc %buildroot%_pkgconfigdir/
ln -s tetgen_mesh.pc pkgconfig/tetgen.pc
ln -s triangle_mesh.pc pkgconfig/triangle.pc

%ifarch x86_64
install -d %buildroot%_libdir
cp -fR %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

# build TriTetMesh

scons
cp -f *.pc pkgconfig/
cp -f *.pc %buildroot%_pkgconfigdir/
sed -i 's|^libdir.*|libdir=%_libdir|' \
	%buildroot%_pkgconfigdir/*.pc pkgconfig/*.pc

# install TriTetMesh

sed -i "s|^\(libdir\).*|\1=$PETSC_DIR/lib|" pkgconfig/dolfin*
sed -i "s|^\(Libs.*\)|\1 -Wl,-R$PETSC_DIR/lib|" pkgconfig/dolfin*
scons -i install prefix=%buildroot%prefix
install -d %buildroot%python_sitelibdir/%name
install -d %buildroot%_libexecdir
install -m644 \
	tritetmesh/trimesh/swig/_trimesh.so \
	tritetmesh/tetmesh/swig/_tetmesh.so \
	tritetmesh/trimesh/swig/trimesh.py \
	tritetmesh/tetmesh/swig/tetmesh.py \
	site-packages/tritetmesh/* \
	%buildroot%python_sitelibdir/%name
install -m644 externals/triangle/libtriangle_mesh.so \
	externals/tetgen/libtetgen_mesh.so \
	%buildroot%_libexecdir
mv %buildroot%_bindir/showme %buildroot%_bindir/showme_mesh

# fix pkg-config files

%ifarch x86_64
rm -f %buildroot%_pkgconfigdir/*
rm -f %buildroot%_libdir/*.so
mv %buildroot%_libexecdir/pkgconfig/* %buildroot%_pkgconfigdir/
mv %buildroot%_libexecdir/*.so %buildroot%_libdir/
%endif
sed -i 's|^prefix.*|prefix=%prefix|' \
	%buildroot%_pkgconfigdir/tritetmesh_*.pc
sed -i 's|^libdir.*|libdir=%_libdir|' \
	%buildroot%_pkgconfigdir/*.pc
sed -i 's|dolfin|dolfin-real|' \
	%buildroot%_pkgconfigdir/tritetmesh_*.pc
sed -i 's|tetgen|tetgen_mesh|' \
	%buildroot%_pkgconfigdir/tritetmesh_tetmesh.pc
sed -i 's|triangle|triangle_mesh|' \
	%buildroot%_pkgconfigdir/tritetmesh_*.pc

rm -f %buildroot%_pkgconfigdir/tetgen.pc \
	%buildroot%_pkgconfigdir/triangle.pc

# install demos

install -d %buildroot%_libdir/%name
cp -fR demo %buildroot%_libdir/%name/

# fix Python wrappers

#pushd %buildroot%python_sitelibdir/%name
#sed -i '1a\import mpi' trimesh.py tetmesh.py
#popd

sed -i 's|%buildroot||g' %buildroot%_pkgconfigdir/*.pc

rm -fR %buildroot%prefix%prefix

%files
%doc AUTHORS COPYING LICENSE README
%_bindir/*

%files -n lib%name
%_libdir/*.so

%files -n lib%name-devel
%_includedir/*
%_pkgconfigdir/*

%files -n python-module-%name
%python_sitelibdir/*

%files demo
%_libdir/%name/

%changelog
* Sat Jul 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt3.bzr20100630
- Rebuilt with OpenMPI 1.6

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt2.bzr20100630
- Rebuilt with Dolfin 1.0.rc2

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1-alt1.bzr20100630.11
- Rebuild with Python-2.7

* Fri Oct 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100630.10
- Rebuilt with updated NumPy

* Thu Aug 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100630.9
- Rebuilt with Dolfin 0.9.11

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100630.8
- Built with GotoBLAS2 instead of ATLAS

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100630.7
- Added -g into compiler flags

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100630.6
- Rebuilt for debuginfo

* Thu Dec 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100630.5
- Removed 'import mpi' from python files (this is work of dolfin now)

* Mon Nov 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100630.4
- Fixed build

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100630.3
- Rebuilt with CGAL 3.7

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100630.2
- Fixed overlinking of libraries

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100630.1
- Removed paths to buildroot

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100630
- New snapshot

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100128.2
- Rebuilt with PETSc 3.1

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100128.1
- Rebuilt with CGAL 3.6

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20100128
- New snapshot

* Sun Dec 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.bzr20091127
- Initial build for Sisyphus

