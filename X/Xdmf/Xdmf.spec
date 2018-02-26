%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%def_without python3

Name: Xdmf
Version: 20100923
Release: alt18
Summary: eXtensible Data Model and Format
License: Free
Group: Sciences/Other
Url: http://www.xdmf.org/index.php/Main_Page
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -d :pserver:anonymous@public.kitware.com:/cvsroot/Xdmf login
# (respond with password xdmf)
# cvs -d :pserver:anonymous@public.kitware.com:/cvsroot/Xdmf checkout Xdmf
Source: %name-%version.tar
Source1: CMakeCache.txt

BuildPreReq: libexpat-devel libvtk-devel python-devel %mpiimpl-devel
BuildPreReq: libhdf5-mpi-devel zlib-devel bzlib-devel cmake
BuildPreReq: libX11-devel libICE-devel libXtst-devel libXau-devel
BuildPreReq: libXcomposite-devel libXcursor-devel libXdamage-devel
BuildPreReq: libXdmcp-devel libXext-devel libXfixes-devel libXi-devel
BuildPreReq: libXft-devel libXinerama-devel libXrandr-devel
BuildPreReq: libXrender-devel libXt-devel libXpm-devel libXv-devel
BuildPreReq: libXxf86misc-devel flex libxml2-devel libmetis0-devel
BuildPreReq: libmysqlclient-devel libvtk-python-devel libvtk-tcl-devel
BuildPreReq: libpq5.4-devel libjpeg-devel libtiff-devel libqt4-devel
BuildPreReq: vtk-python tcl-devel tk-devel libmpe2-devel libsz2-devel
BuildPreReq: libgomp-devel libexodusii-devel libnetcdf-mpi-devel
BuildPreReq: libXScrnSaver-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

Requires: lib%name = %version-%release

%description
The need for a standardized method to exchange scientific data between
High Performance Computing codes and tools lead to the development of
the eXtensible Data Model and Format (XDMF) . Uses for XDMF range from a
standard format used by HPC codes to take advantage of widely used
visualization programs like ParaView, to a mechanism for performing
coupled calculations using multiple, previously stand alone codes.

%package -n lib%name
Summary: Shared libraries of XDMF
Group: System/Libraries

%description -n lib%name
The need for a standardized method to exchange scientific data between
High Performance Computing codes and tools lead to the development of
the eXtensible Data Model and Format (XDMF) . Uses for XDMF range from a
standard format used by HPC codes to take advantage of widely used
visualization programs like ParaView, to a mechanism for performing
coupled calculations using multiple, previously stand alone codes.

This package contains shared libraries of XDMF.

%package devel
Summary: Development files of XDMF
Group: Development/C++
Requires: lib%name = %version-%release
Requires: libvtk-devel

%description devel
The need for a standardized method to exchange scientific data between
High Performance Computing codes and tools lead to the development of
the eXtensible Data Model and Format (XDMF) . Uses for XDMF range from a
standard format used by HPC codes to take advantage of widely used
visualization programs like ParaView, to a mechanism for performing
coupled calculations using multiple, previously stand alone codes.

This package contains development files of XDMF.

%package -n python-module-%name
Summary: Python module of XDMF
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
The need for a standardized method to exchange scientific data between
High Performance Computing codes and tools lead to the development of
the eXtensible Data Model and Format (XDMF) . Uses for XDMF range from a
standard format used by HPC codes to take advantage of widely used
visualization programs like ParaView, to a mechanism for performing
coupled calculations using multiple, previously stand alone codes.

This package contains Python module of XDMF.

%if_with python3
%package -n python3-module-%name
Summary: Python 3 module of XDMF
Group: Development/Python3
Requires: lib%name = %version-%release

%description -n python3-module-%name
The need for a standardized method to exchange scientific data between
High Performance Computing codes and tools lead to the development of
the eXtensible Data Model and Format (XDMF) . Uses for XDMF range from a
standard format used by HPC codes to take advantage of widely used
visualization programs like ParaView, to a mechanism for performing
coupled calculations using multiple, previously stand alone codes.

This package contains Python module of XDMF.
%endif

%package data
Summary: Data files for XDMF
Group: Sciences/Other
BuildArch: noarch

%description data
The need for a standardized method to exchange scientific data between
High Performance Computing codes and tools lead to the development of
the eXtensible Data Model and Format (XDMF) . Uses for XDMF range from a
standard format used by HPC codes to take advantage of widely used
visualization programs like ParaView, to a mechanism for performing
coupled calculations using multiple, previously stand alone codes.

This package contains data files for XDMF.

%package examples
Summary: Examples for XDMF
Group: Development/Documentation
BuildArch: noarch

%description examples
The need for a standardized method to exchange scientific data between
High Performance Computing codes and tools lead to the development of
the eXtensible Data Model and Format (XDMF) . Uses for XDMF range from a
standard format used by HPC codes to take advantage of widely used
visualization programs like ParaView, to a mechanism for performing
coupled calculations using multiple, previously stand alone codes.

This package contains examples for XDMF.

%prep
%setup
install -p -m644 %SOURCE1 .

%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" CMakeCache.txt

%if_with python3
rm -rf ../python3
cp -a . ../python3
sed -i 's|@PYVER@|%_python3_version|g' ../python3/CMakeCache.txt
%endif

sed -i 's|@PYVER@|%_python_version|g' CMakeCache.txt

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh

%if_with python3
pushd ../python3
cmake \
	-DVTK_CMAKE_DIR:PATH=%_libdir/vtk-5.10/CMake \
	.
for i in $(find ./ -name '*.make') $(find ./ -name link.txt); do
	sed -i 's|%_libexecdir/vtk-5.10/lib|%_libdir/lib|g' $i
done
%make_build verbose=1
popd
%endif

cmake .
for i in $(find ./ -name '*.make') $(find ./ -name link.txt); do
	sed -i 's|%_libexecdir/vtk-5.10/lib|%_libdir/lib|g' $i
done
%make_build verbose=1

%install
source %mpidir/bin/mpivars.sh
%makeinstall_std

%if_with python3
pushd ../python3
%make_install DESTDIR=$PWD/build3 install
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv build3/%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif
popd
%endif

install -d %buildroot%_libdir/vtk-5.10/CMake
mv %buildroot%prefix/vtk/* %buildroot%_libdir/vtk-5.10/CMake/
mv %buildroot%_libexecdir/XdmfCMake/* \
	%buildroot%_libdir/vtk-5.10/CMake/
rmdir %buildroot%_libexecdir/XdmfCMake
ln -s %_libdir/vtk-5.10/CMake %buildroot%_libdir/XdmfCMake

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/*.so %buildroot%_libdir/
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* %buildroot%python_sitelibdir/
%endif

install -d %buildroot%_datadir/%name
cp -fR Data/Data/* %buildroot%_datadir/%name/

rm -f $(find Examples -name '*.o')

%files
%_bindir/*

%files -n lib%name
%_libdir/*.so

%files devel
%_includedir/*
%_libdir/vtk-5.10/CMake/*
%_libdir/XdmfCMake

%files -n python-module-%name
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%files data
%_datadir/%name

%files examples
%doc Examples/*

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt18
- Rebuilt with OpenMPI 1.6

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt17
- Rebuilt with VTK 5.10.0

* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt16
- Fixed build

* Fri Feb 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt15
- Built without OSMesa

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt14
- Removed shandard library paths from RPATH

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt13
- Fixed RPATH

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt12
- Rebuilt with Boost 1.48.0

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt11
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20100923-alt10.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt10
- Rebuilt with vtk 5.8.0

* Fri Sep 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt9
- Rebuilt with metis0

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt8
- Rebuilt with libhdf5-7-mpi

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt7
- Fixed build

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt6
- Rebuilt with libnetcdf7-mpi

* Fri Apr 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt5
- Rebuilt with VTK 5.6.1

* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt4
- Rebuilt for debuginfo

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt3
- Rebuilt with metis 4.0.1-alt9

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt2
- Rebuilt with PostgreSQL 9

* Fri Sep 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100923-alt1
- Initial build for Sisyphus

