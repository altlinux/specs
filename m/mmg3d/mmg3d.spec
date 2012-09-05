Name: mmg3d
Version: 4.0
Release: alt1
Summary: Anisotropic Tetrahedral Remesher/Moving Mesh Generation
License: GPLv3+
Group: Graphics
Url: http://www.math.u-bordeaux1.fr/~cdobrzyn/logiciels/mmg3d.php
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: cmake gcc-c++ libscotch-devel

Requires: lib%name = %version-%release

%description
Mmg3d is an anisotropic fully tetrahedral automatic remesher. Beginning
with a tetrahedral mesh, it modifies it iteratively to be in agreement
with prescribed sizes (and directions) and/or to move all or a part of
the domain boundary (rigid bodies displacement).

The software reads a mesh and it is possible to prescribe a map for
edges sizes/directions and/or a displacement vector for the mesh nodes.

The mesh is then modified by using local mesh modifications of which an
insertion procedure based on anisotropic Delaunay kernel.

NB: For the moment, only volumic mesh (i.e. the tetrahedra) is treated.
No modification of the surface triangulation made (except for the rigid
bodies movements and global splitting).

%package -n lib%name
Summary: Shared library of Mmg3d
Group: System/Libraries

%description -n lib%name
Mmg3d is an anisotropic fully tetrahedral automatic remesher. Beginning
with a tetrahedral mesh, it modifies it iteratively to be in agreement
with prescribed sizes (and directions) and/or to move all or a part of
the domain boundary (rigid bodies displacement).

This package contains shared library of Mmg3d.

%package -n lib%name-devel
Summary: Development files of Mmg3d
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Mmg3d is an anisotropic fully tetrahedral automatic remesher. Beginning
with a tetrahedral mesh, it modifies it iteratively to be in agreement
with prescribed sizes (and directions) and/or to move all or a part of
the domain boundary (rigid bodies displacement).

This package contains development files of Mmg3d.

%package test
Summary: Test for Mmg3d
Group: Graphics
Requires: lib%name = %version-%release

%description test
Mmg3d is an anisotropic fully tetrahedral automatic remesher. Beginning
with a tetrahedral mesh, it modifies it iteratively to be in agreement
with prescribed sizes (and directions) and/or to move all or a part of
the domain boundary (rigid bodies displacement).

This package contains test for Mmg3d.

%prep
%setup

rm -f build/{mmg3d4.0,testlib}

%build
pushd build
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	.
%make_build VERBOSE=1
popd

%install
install -d %buildroot%_bindir
install -d %buildroot%_includedir/%name
install -d %buildroot%_libdir

pushd build
install -m755 mmg3d4.0 %buildroot%_bindir
install -m755 testlib %buildroot%_bindir/test_%name
install -p -m644 sources/*.h %buildroot%_includedir/%name
cp -P libmmg3d.so* %buildroot%_libdir
popd

%check
pushd build
export LD_LIBRARY_PATH=$PWD
./testlib
popd

%files
%_bindir/mmg3d4.0

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files test
%_bindir/test_%name

%changelog
* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1
- Initial build for Sisyphus

