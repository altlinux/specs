%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define ver 5.10
Name: vtk
Version: %ver.0
Release: alt3
Summary: The Visualization Toolkit, an Object-Oriented Approach to 3D Graphics
License: BSD-like
Group: Development/Tools
Url: http://www.vtk.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
%setup_python_module vtk

Source: vtk-%version.tar
Source3: examples
Source4: CMakeCache.txt

Requires: lib%name = %version-%release

BuildRequires(pre): rpm-build-tcl rpm-build-python /proc
BuildPreReq: gcc-c++ tcl-devel tk-devel cmake libGLU-devel libXt-devel
BuildPreReq: %mpiimpl-devel libmysqlclient-devel postgresql-devel
BuildPreReq: boost-devel boost-mpi-devel boost-filesystem-devel
BuildPreReq: boost-graph-parallel-devel libmpe2-devel libsz2-devel
BuildPreReq: libfreetype-devel libnetcdf-mpi-devel libjpeg-devel
BuildPreReq: libxml2-devel libexpat-devel libftgl220-devel libpng-devel
BuildPreReq: libtiff-devel zlib-devel libhdf5-mpi-devel libsqlite3-devel
BuildPreReq: doxygen graphviz qt4-devel libgsl-devel ctest
BuildPreReq: libbfd-devel libnumpy-devel chrpath libopenmotif-devel
BuildPreReq: %name-data >= %version libavcodec53
BuildPreReq: python-devel libXxf86misc-devel libimlxx-devel libstlport-devel
BuildPreReq: libdc1394-devel ffmpeg2theora libtheora-devel
BuildPreReq: libgsm-devel libvorbis-devel libtag-devel
BuildPreReq: libslurm-devel slurm-utils gnuplot
BuildPreReq: libcgns-mpi-devel inkscape texlive-latex-base
BuildPreReq: texlive-latex-extra texlive-science
BuildPreReq: qt4-common qt4-dbus qt4-designer python-module-PyQt4-devel
BuildPreReq: phonon-devel libqt4-clucene python-module-sip-devel
BuildPreReq: libavformat-devel libpostproc-devel libswscale-devel
BuildPreReq: libavdevice-devel libavfilter-devel rpm-macros-fedora-compat

%description
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

%package -n lib%name
Summary: Shared libraries of The Visualization Toolkit (VTK)
Group: System/Libraries

%description -n lib%name
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains shared libraries of VTK.

%package -n lib%name-utils
Summary: Util libraries for The Visualization Toolkit (VTK)
Group: System/Libraries
Conflicts: lib%name-devel < %version-%release
Conflicts: lib%name < %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-utils
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains util libraries for VTK.

%package -n lib%name-devel
Summary: Development files of The Visualization Toolkit (VTK)
Group: Development/C++
Requires: %name = %version-%release
Requires: %name-tcl = %version-%release
Requires: lib%name = %version-%release
Requires: %mpiimpl-devel libstdc++4.5-devel libqt4-devel
Requires: libfreetype-devel

%description -n lib%name-devel
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains development files of VTK.

%package qt4-designer-plugin
Summary: The Visualization Toolkit (VTK) plugin for Qt4
Group: Development/KDE and QT
Requires: lib%name = %version-%release
Requires: qt4-designer

%description qt4-designer-plugin
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains VTK plugin for Qt4 Designer.

%package doc
Summary: Documentation for The Visualization Toolkit (VTK)
Group: Development/Documentation
BuildArch: noarch

%description doc
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains documentation for VTK.

%package tcl
Summary: The Visualization Toolkit (VTK) TCL bindings
Group: Development/Tcl
Requires: %name = %version-%release
Requires: lib%name = %version-%release
Requires: lib%name-tcl = %version-%release
%add_tcl_lib_path %_tcldatadir/%name-%ver
Provides: tcl(vtkbase) = %ver
Provides: tcl(vtkcommon) = %ver
Provides: tcl(vtkfiltering) = %ver
Provides: tcl(vtkgraphics) = %ver
Provides: tcl(vtkhybrid) = %ver
Provides: tcl(vtkimaging) = %ver
Provides: tcl(vtkio) = %ver
Provides: tcl(vtkrendering) = %ver
Provides: tcl(vtkwidgets) = %ver

%description tcl
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package provides TCL bindings to VTK.

%package -n lib%name-tcl
Summary: Shared libraries of VTK-TCL bindings
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-tcl
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains shared libraries for TCL bindings to VTK.

%package -n lib%name-tcl-devel
Summary: Development files of VTK-TCL bindings
Group: Development/Tcl
Requires: lib%name-devel = %version-%release
Requires: lib%name-tcl = %version-%release

%description -n lib%name-tcl-devel
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains development files for TCL bindings to VTK.

%package python
Summary: The Visualization Toolkit (VTK) Python bindings
Group: Development/Python
Requires: %name = %version-%release
Requires: lib%name = %version-%release
Requires: lib%name-python = %version-%release
Requires: python-module-%name = %version-%release

%description python
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package provides Python bindings to VTK.

%package -n lib%name-python
Summary: The Visualization Toolkit (VTK) Python shared libraries
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-python
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains Python shared libraries of VTK.

%package -n lib%name-python-devel
Summary: The Visualization Toolkit (VTK) Python development files
Group: Development/Python
Requires: lib%name-python = %version-%release

%description -n lib%name-python-devel
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains Python development files of VTK.

%package -n python-module-%name
Summary: The Visualization Toolkit (VTK) Python bindings
Group: Development/Python
Requires: lib%name-python = %version-%release
Requires: python-module-pygtkglext_git
%add_python_req_skip gtk.GDK
%py_requires gtk_git

%description -n python-module-%name
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package provides Python bindings to VTK.

%package -n python-module-%name-tests
Summary: Tests for The Visualization Toolkit (VTK) Python bindings
Group: Development/Python
Requires: python-module-%name = %version-%release

%description -n python-module-%name-tests
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains tests for Python bindings to VTK.

%package examples
Summary: The Visualization Toolkit (VTK) examples
Group: Development/Tools
Requires: %name = %version-%release
Requires: %name-tcl = %version-%release
Requires: %name-data >= %version
%add_python_req_skip numeric vtkmy vtkmycommon vtkmyimaging vtkmyunsorted
Provides: tcl(vtkmy)
Provides: tcl(vtkmycommon)
Provides: tcl(vtkmyimaging)
Provides: tcl(vtkmyunsorted)

%description examples
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains VTK examples. For correct work of all examples and tests
You need set environment variable VTK_DATA_ROOT=/usr/share/vtk-%ver.

%prep
%setup

install -m644 %SOURCE3 %SOURCE4 .
sed -i 's|@PYVER@|%_python_version|g' \
	Wrapping/CMakeLists.txt \
	Wrapping/Python/CMakeLists.txt \
	CMake/vtkWrapPython.cmake \
	CMake/KitCommonBlock.cmake \
	CMake/KitCommonPythonWrapBlock.cmake \
	Rendering/CMakeLists.txt \
	CMakeCache.txt

%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" CMakeCache.txt CMakeLists.txt \
	Utilities/vtkhdf5/src/H5make_libsettings.c

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
PATH=$PATH:%_qt4dir/bin

export VTK_DATA_ROOT=%_datadir/%name-%ver
FLAGS="%optflags %optflags_shared -I%mpidir/include -I%_includedir/gsl"
FLAGS="$FLAGS -DHAVE_SYS_TIME_H -DHAVE_SYS_TYPES_H -DHAVE_SYS_SOCKET_H"
%ifarch x86_64
FLAGS="$FLAGS -D__USE_LARGEFILE64"
%endif

cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%buildroot%prefix \
	-DCMAKE_C_FLAGS:STRING="$FLAGS" \
	-DCMAKE_CXX_FLAGS:STRING="$FLAGS" \
	-DCMAKE_Fortran_FLAGS:STRING="$FLAGS" \
	-DMPIDIR:STRING="%mpidir" \
	-DSIP_INCLUDE_DIR:PATH=%_includedir/%_python_version \
	-DVTK_INSTALL_QT_PLUGIN_DIR:PATH=%buildroot%_qt4_plugindir/designer \
	.
tar -czf src.tar.gz Examples
%make_build

%install
export VTK_DATA_ROOT=%_datadir/%name-%ver
source %mpidir/bin/mpivars.sh
%makeinstall

install -d %buildroot%_libdir
install -d %buildroot%_docdir/%name-%ver
install -d %buildroot%_datadir/%name-%ver-examples
#install -d %buildroot%_libexecdir/qt4
install -d %buildroot%_tcldatadir/%name%ver

%ifarch x86_64
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif
pushd %buildroot%_libdir/%name-%ver
mv doc/verdict %buildroot%_docdir/%name-%ver/
rmdir doc
for i in $(ls libvtk*TCL.so); do
	ln -s %_libdir/$i.%ver %buildroot%_tcldatadir/%name%ver/$i
done
mv *.so* %buildroot%_libdir/
mv pkgIndex.tcl tcl %buildroot%_tcldatadir/%name%ver/
popd
#mv %buildroot%prefix/plugins %buildroot%_libexecdir/qt4/

install -m644 src.tar.gz %buildroot%_datadir/%name-%ver-examples
pushd %buildroot%_datadir/%name-%ver-examples
tar -xf src.tar.gz
rm -f src.tar.gz
export LD_LIBRARY_PATH=%buildroot%_libdir
%make_build -C Examples
%make_install -C Examples install DESTDIR=%buildroot
popd
install -d %buildroot%_bindir
for i in $(ls bin |egrep -v '\.so'); do
	install -p -m755 bin/$i %buildroot%_bindir
done

pushd Wrapping/Python
export CFLAGS="%optflags"
%python_build
%python_install --optimize=2
popd

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

install -m644 bin/libvtkmy* \
	%buildroot%_libdir

#for i in $(cat examples); do
#	chrpath -r %mpidir/lib bin/$i
#	install -m755 bin/$i %buildroot%_bindir
#done
pushd %buildroot%_bindir
for i in $(ls); do
	chrpath -r %mpidir/lib $i ||:
done
popd
pushd %buildroot%_libdir
for i in $(ls *.so); do
	chrpath -r %mpidir/lib $i
done
popd

sed -i 's|%buildroot||g' \
	$(find %buildroot%_datadir/%name-%ver-examples/Examples -name '*.cmake')
sed -i 's|\(.*VTK_LIBRARY_DIRS.*\)/%_lib/vtk\-%ver|\1/%_lib|' \
	%buildroot%_libdir/vtk-%ver/VTKConfig.cmake
sed -i 's|/%_lib/vtk-%ver|/%_lib|' \
	%buildroot%_libdir/vtk-%ver/VTKTargets-relwithdebinfo.cmake

#install -p -m644 Hybrid/vtkExodusIIReaderPrivate.h \
install -p -m644 Hybrid/*.h \
	Common/vtkArrayIteratorIncludes.h \
	Common/vtkPointAccumulator.hxx \
	Filtering/vtkMarchingCubesCases.h \
	Infovis/vtkStatisticsAlgorithmPrivate.h \
	Utilities/vtk_netcdf.h \
	%buildroot%_includedir/%name-%ver/
install -p -m644 CMake/KitCommonPythonWrapBlock.cmake \
	%buildroot%_libdir/%name-%ver/

#install -d %buildroot%_libexecdir/qt4/plugins/designer
#mv %buildroot%_libdir/qt4/plugins/designer/* \
#	%buildroot%_libexecdir/qt4/plugins/designer/
#mv %buildroot/usr/plugins/designer/* \
#	%buildroot%_libexecdir/qt4/plugins/designer/

%post -n lib%name
if [ -h %_libexecdir/%name ]; then
	rm -f %_libexecdir/%name
fi
if [ -h %_libdir/%name ]; then
	rm -f %_libdir/%name
fi
ln -s %_libdir/%name-%ver %_libdir/%name

%postun -n lib%name
rm -f %_libexecdir/%name
rm -f %_libdir/%name

%files
%doc Copyright.txt README.html
%_bindir/lproj
%_bindir/pvtk
%_bindir/vtk
%_bindir/vtkEncodeString

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/*TCL.so.*
%exclude %_libdir/*Python*.so.*
%exclude %_libdir/libCosmo.so.*
%exclude %_libdir/libVPIC.so.*
%dir %_libdir/%name-%ver
%dir %_datadir/%name-%ver
%_datadir/%name-%ver/vtkChemistry

%files -n lib%name-utils
%_libdir/libCosmo.so.*
%_libdir/libVPIC.so.*

%files -n lib%name-devel
%_libdir/*.so
%exclude %_libdir/*TCL.so
%exclude %_libdir/*Python*.so
%exclude %_libdir/libvtkmy*.so
#exclude %_libdir/libvtkLocal.so
%_includedir/%name-%ver
%exclude %_includedir/%name-%ver/*Tcl*
%exclude %_includedir/%name-%ver/*Python*
%_libdir/%name-%ver/*
%exclude %_libdir/%name-%ver/testing/*.py*
%exclude %_libdir/%name-%ver/CMake/*TCL*
%exclude %_libdir/%name-%ver/CMake/*Tcl*
%exclude %_libdir/%name-%ver/CMake/*Python*

%files doc
%_docdir/%name-%ver

%files tcl
%_bindir/*Tcl*
%_tcldatadir/%name%ver

%files -n lib%name-tcl
%_libdir/*TCL.so.*

%files -n lib%name-tcl-devel
%_libdir/*TCL.so
%exclude %_libdir/libvtkmy*.so
%_libdir/%name-%ver/CMake/*TCL*
%_libdir/%name-%ver/CMake/*Tcl*
%_includedir/%name-%ver/*Tcl*

%files examples
%_bindir/*
%exclude %_bindir/lproj
%exclude %_bindir/pvtk
%exclude %_bindir/vtk
%exclude %_bindir/vtkEncodeString
%exclude %_bindir/*Tcl*
%exclude %_bindir/*python*
%exclude %_bindir/*Python*
%_libdir/libvtkmy*.so
#_libdir/libvtkLocal.so
%_datadir/%name-%ver-examples

%files qt4-designer-plugin
%_libdir/qt4/plugins/designer/*

%files python
%_bindir/*python*
%_bindir/*Python*
%_libdir/%name-%ver/testing/*.py*

%files -n lib%name-python
%_libdir/*Python*.so.*

%files -n lib%name-python-devel
%_libdir/*Python*.so
%exclude %_libdir/libvtkmy*.so
%_includedir/%name-%ver/*Python*
%_libdir/%name-%ver/CMake/*Python*

%files -n python-module-%name
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files -n python-module-%name-tests
%python_sitelibdir/*/test

%changelog
* Wed Jun 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt3
- Rebuilt with OpenMPI 1.6

* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt2
- Set soname version for libvtkQtPythonD.so

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt1
- Version 5.10.0

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt12
- Fixed utils subpackage
- Set soname version for libvtkNetCDF_cxx.so
- Restored qt4-designer-plugin subpackage

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt11
- Fixed build with boost 1.49.0 (thnx iv@)

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt10
- Rebuilt with python-module-sip 4.13.2

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt9
- Built without OSMesa

* Mon Feb 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt8
- Fixed build with libav 0.8

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt7
- Rebuilt with python-module-sip 4.13.1

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt6
- Fixed file name: VTKTargets-reswithdebinfo.cmake ->
  VTKTargets-relwithdebinfo.cmake

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt5
- Fixed VTKTargets-reswithdebinfo.cmake (ALT #26650)

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt4
- Added necessary headers
- Fixed VTK_LIBRARY_DIRS (ALT #26650)

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt3
- Rebuilt with Boost 1.48.0

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt2
- Set directories of data files

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.8.0-alt1.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt1
- Version 5.8.0

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.1-alt2
- Rebuilt with libnetcdf7-mpi

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.1-alt1
- Version 5.6.1

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt10
- Rebuilt with Boost 1.46.1

* Fri Mar 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt9
- Rebuilt with openmotif
- Added needed requirements

* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt8
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt7
- Rebuilt with PostgreSQL 9.0

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt6
- Rebuilt for soname set-versions

* Fri Oct 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt5
- Fixed underlinking of libraries

* Wed Sep 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt4
- Do not use off screen calls (avoid segfault)

* Wed Sep 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt3
- Rebuilt with libmysqlclient.so.16

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt2
- Removed paths to buildroot

* Tue Jul 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt1
- Version 5.6.0

* Mon Mar 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt9
- Rebuilt with postgresql 8.4

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt8
- Changed requirement for python-module-%name: pygtkglext -> pygtkglext_git

* Wed Mar 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt7
- Rebuilt with new Boost (changed position of property_maps)
- Added some functionals (interfaces with addition packages)

* Sat Jan 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt6
- Rebuilt without python-module-Numeric

* Wed Jul 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt5
- Rebuild with python 2.6

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt4
- Enabled Python module

* Tue Jun 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt3
- Rebuild with changed libpng12

* Fri Jun 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt2
- Fixed directory layout for TCL wrappers

* Thu Jun 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt1
- Initial build for Sisyphus

