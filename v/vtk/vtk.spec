%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define ver 9.1

Name: vtk
Version: %ver.0
Release: alt1.1
Summary: The Visualization Toolkit, an Object-Oriented Approach to 3D Graphics
License: BSD-like
Group: Development/Tools
Url: https://www.vtk.org/

# https://gitlab.kitware.com/vtk/vtk.git
Source: %name-%version.tar

# git submodules
Source1: %name-%version-ThirdParty-vtkm-vtkvtkm-vtk-m.tar

# Remote modules
Source100: %name-%version-MomentInvariants.tar
Source101: %name-%version-PoissonReconstruction.tar
Source102: %name-%version-Powercrust.tar
Source103: %name-%version-SignedTensor.tar
Source104: %name-%version-SplineDrivenImageSlicer.tar
Source105: %name-%version-vtkDICOM.tar

Patch1: %name-%version-alt-python-install-path.patch

# Fix/hack for https://gitlab.kitware.com/vtk/vtk/-/issues/18220
# Needed for itk-snap
Patch2: %name-%version-alt-modules-autoinit.patch

# Patch required libharu version (Fedora 33+ contains the needed VTK patches)
Patch3: %name-%version-fedora-libharu.patch

Patch4: %name-%version-alt-dont-fetch-remote-modules.patch

Patch5: %name-%version-alt-fix-linking.patch

Patch6: %name-%version-alt-compile-flags.patch

Patch7: %name-%version-alt-armh-compat.patch

Patch8: %name-%version-alt-PoissonReconstruction-build.patch

Patch9: %name-%version-alt-SplineDrivenImageSlicer-install-headers.patch

Requires: lib%name%ver = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++ tk-devel cmake libGLU-devel libXt-devel
BuildRequires: libmysqlclient-devel postgresql-devel
BuildRequires: boost-devel boost-filesystem-devel
BuildRequires: boost-graph-parallel-devel
BuildRequires: libfreetype-devel libjpeg-devel
BuildRequires: libxml2-devel libexpat-devel libftgl220-devel libpng-devel
BuildRequires: libtiff-devel zlib-devel libhdf5-devel libsqlite3-devel
BuildRequires: doxygen graphviz libgsl-devel
BuildRequires: libbfd-devel libopenmotif-devel
BuildRequires: libgl2ps-devel
BuildRequires: libXxf86misc-devel libimlxx-devel
BuildRequires: libdc1394-devel libtheora-devel
BuildRequires: libgsm-devel libvorbis-devel libtag-devel
BuildRequires: gnuplot
BuildRequires: libcgns-devel
BuildRequires: inkscape texlive-latex-base
BuildRequires: texlive-latex-extra texlive-science
BuildRequires: libavformat-devel libpostproc-devel libswscale-devel
BuildRequires: libavdevice-devel libavfilter-devel
BuildRequires: liblz4-devel
BuildRequires: libnetcdf-devel
BuildRequires: jsoncpp-devel
BuildRequires: qt5-base-devel qt5-x11extras-devel qt5-tools-devel
BuildRequires: qt5-base-devel-static
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-phonon-devel
BuildRequires: libharu-devel
BuildRequires: libgdal-devel
BuildRequires: eigen3-devel
BuildRequires: libdouble-conversion-devel
BuildRequires: liblzma-devel
BuildRequires: libGLEW-devel
BuildRequires: libproj-devel
BuildRequires: libpugixml-devel
BuildRequires: python3-devel python3-module-matplotlib
BuildRequires: python3-module-PyQt5-devel python3-module-sip-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: libopenslide-devel
BuildRequires: libarchive-devel
BuildRequires: libfmt-devel

%description
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

%package -n lib%name%ver
Summary: Shared libraries of The Visualization Toolkit (VTK)
Group: System/Libraries

%description -n lib%name%ver
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains shared libraries of VTK.

%package -n lib%name-devel
Summary: Development files of The Visualization Toolkit (VTK)
Group: Development/C++
Requires: %name = %EVR
Requires: %name-python3 = %EVR
Requires: lib%name%ver = %EVR
Requires: lib%name%ver-python3 = %EVR
Requires: python3-module-%name = %EVR
Requires: python3-module-%name-tests = %EVR
Requires: %name-doc = %EVR
Requires: %name-examples = %EVR
%ifnarch %arm
Requires: %name-qt5 = %EVR
%endif
# Following dependencies are duplicates from build dependencies
Requires: qt5-base-devel
Requires: qt5-declarative-devel
Requires: libfreetype-devel
Requires: eigen3-devel
Requires: libdouble-conversion-devel
Requires: python3-devel
Requires: libxml2-devel
Requires: libgdal-devel
Requires: libGLEW-devel
Requires: libarchive-devel
Requires: libcgns-devel
Requires: libfmt-devel
Conflicts: libvtk6.1-devel libvtk6.2-devel libvtk8.1-devel
Conflicts: libvtk8.2-devel

%description -n lib%name-devel
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains development files of VTK.

%package doc
Summary: Documentation for The Visualization Toolkit (VTK)
Group: Development/Documentation

%description doc
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains documentation for VTK.

%package python3
Summary: The Visualization Toolkit (VTK) Python bindings
Group: Development/Python3
Requires: %name = %EVR
Requires: lib%name%ver = %EVR
Requires: lib%name%ver-python3 = %EVR
Requires: python3-module-%name = %EVR
Conflicts: vtk6.1-python vtk6.2-python vtk8.1-python
Conflicts: vtk8.2-python vtk8.2-python3

%description python3
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package provides Python bindings to VTK.

%package -n lib%name%ver-python3
Summary: The Visualization Toolkit (VTK) Python shared libraries
Group: System/Libraries
Requires: lib%name%ver = %EVR

%description -n lib%name%ver-python3
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains Python shared libraries of VTK.

%package -n python3-module-%name
Summary: The Visualization Toolkit (VTK) Python bindings
Group: Development/Python3
Requires: lib%name%ver-python3 = %EVR
%add_python3_req_skip GDK gtk gtkgl gtk.gtkgl pygtk vtkParallelPython
%add_python3_req_skip vtk.vtkCommonCore vtk.vtkFiltersGeometry vtk.vtkRenderingCore vtk.vtkWebCore vtk.web vtk.web.camera vtk.web.query_data_model
%add_python3_req_skip wslink.websocket
%py3_requires PyQt5
Provides: python3-module-vtk8.2 = %EVR
Obsoletes: python3-module-vtk8.2 < %EVR
Conflicts: python3-module-vtk8.2 < %EVR

%add_python3_self_prov_path %buildroot%python3_sitelibdir/vtkmodules/web/wslink.py

%description -n python3-module-%name
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package provides Python bindings to VTK.

%package -n python3-module-%name-tests
Summary: Tests for The Visualization Toolkit (VTK) Python bindings
Group: Development/Python3
Requires: python3-module-%name = %EVR
Provides: python3-module-vtk8.2-tests = %EVR
Obsoletes: python3-module-vtk8.2-tests < %EVR
Conflicts: python3-module-vtk8.2-tests < %EVR

%description -n python3-module-%name-tests
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains tests for Python bindings to VTK.

%package examples
Summary: The Visualization Toolkit (VTK) examples
Group: Development/Tools
Requires: %name = %EVR
%add_python3_req_skip numeric

%description examples
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains VTK examples.

%package qt5
Summary: The Visualization Toolkit (VTK) QML plugin
Group: System/Libraries

%description qt5
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains VTK QML plugin.

%prep
%setup -a1 -a100 -a101 -a102 -a103 -a104 -a105
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

pushd Remote/PoissonReconstruction
%patch8 -p1
popd

pushd Remote/SplineDrivenImageSlicer
%patch9 -p1
popd

# remove bundled libraries
for x in constantly expat freetype gl2ps hdf5 hyperlink incremental jpeg jsoncpp libharu libxml2 lz4 netcdf oggtheora png tiff Twisted txaio zlib ZopeInterface ; do
	rm -rf ThirdParty/${x}/vtk${x}
done

rm -rf \
	ThirdParty/AutobahnPython/vtkAutobahn

%build
PATH=$PATH:%_qt5_bindir

export PYTHON=%__python3
%add_optflags -I%_includedir/gsl
%add_optflags -DHAVE_SYS_TIME_H -DHAVE_SYS_TYPES_H -DHAVE_SYS_SOCKET_H
%add_optflags -D__USE_LARGEFILE64 -DH5_HAVE_SIGSETJMP -D__USE_POSIX
%add_optflags -DH5_HAVE_SETJMP_H
%add_optflags -D_FILE_OFFSET_BITS=64

# remote module flags go last
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DCMAKE_INSTALL_QMLDIR=%_qt5_qmldir \
	-DVTK_BUILD_DOCUMENTATION=ON \
	-DVTK_BUILD_EXAMPLES=OFF \
	-DVTK_BUILD_TESTING=OFF \
	-DVTK_EXTRA_COMPILER_WARNINGS=ON \
	-DVTK_GROUP_ENABLE_Imaging:STRING=YES \
	-DVTK_GROUP_ENABLE_Rendering:STRING=YES \
	-DVTK_GROUP_ENABLE_StandAlone:STRING=YES \
	-DVTK_GROUP_ENABLE_Views:STRING=YES \
	-DVTK_GROUP_ENABLE_Web:STRING=YES \
	-DCMAKE_INSTALL_LICENSEDIR:PATH=share/doc/%name-%ver/licenses \
	-DVTK_MODULE_ENABLE_VTK_CommonArchive:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_DomainsMicroscopy:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_GeovisGDAL:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_ImagingOpenGL2:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_InfovisBoost:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_InfovisBoostGraphAlgorithms:STRING=YES \
%ifnarch %arm
	-DVTK_GROUP_ENABLE_Qt:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_RenderingContextOpenGL2:STRING=YES \
%else
	-DVTK_GROUP_ENABLE_Qt:STRING=NO \
	-DVTK_MODULE_ENABLE_VTK_RenderingContextOpenGL2:STRING=NO \
	-DVTK_MODULE_ENABLE_VTK_GUISupportQt:STRING=NO \
	-DVTK_MODULE_ENABLE_VTK_GUISupportQtQuick:STRING=NO \
	-DVTK_MODULE_ENABLE_VTK_GUISupportQtSQL:STRING=NO \
%endif
	-DVTK_USE_EXTERNAL=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_expat=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_exprtk=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_freetype=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_gl2ps=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_hdf5=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_ioss=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_jpeg=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_jsoncpp=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_libharu=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_libproj=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_libxml2=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_lz4=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_netcdf=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_png=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_tiff=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_zlib=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_utf8=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_pegtl=OFF \
%ifarch %arm
	-DVTK_OPENGL_USE_GLES=ON \
	-DVTK_OPENGL_HAS_EGL=ON \
%endif
	-DVTK_PYTHON_VERSION=3 \
	-DVTK_PYTHON_OPTIONAL_LINK=OFF \
	-DVTK_SMP_IMPLEMENTATION_TYPE="Sequential" \
	-DVTK_USE_X=ON \
	-DVTK_WRAP_PYTHON=ON \
	-DVTK_MODULE_ENABLE_VTK_ParallelMomentInvariants:STRING=NO \
	-DVTK_MODULE_ENABLE_VTK_MomentInvariants:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_PoissonReconstruction:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_Powercrust:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_SignedTensor:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_SplineDrivenImageSlicer:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_vtkDICOM:STRING=YES \
	%nil

export LD_LIBRARY_PATH=$PWD/%_cmake__builddir/%_lib
%cmake_build
%cmake_build -t DoxygenDoc

%install
%cmakeinstall_std

%files
%doc Copyright.txt README.md
%_bindir/vtkParseJava-%ver
%_bindir/vtkWrapHierarchy-%ver
%_bindir/vtkWrapJava-%ver
%ifnarch %arm
%_bindir/vtkProbeOpenGLVersion-%ver
%endif

%files -n lib%name%ver
%_libdir/*.so.*
%exclude %_libdir/libvtk*Python*-%ver.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name-%ver
%_libdir/cmake/%name-%ver
%_libdir/%name

%files doc
%_docdir/%name-%ver

%files examples
%doc Examples

%files python3
%_bindir/*python*
%_bindir/*Python*

%files -n lib%name%ver-python3
%_libdir/libvtk*Python*-%ver.so.*

%files -n python3-module-%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/__pycache__
%exclude %python3_sitelibdir/vtkmodules/test

%files -n python3-module-%name-tests
%python3_sitelibdir/vtkmodules/test

%ifnarch %arm
%files qt5
%_qt5_qmldir/VTK.%ver
%endif

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 9.1.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Jan 19 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 9.1.0-alt1
- Updated to upstream version 9.1.0.

* Thu Sep 30 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt6
- Renamed vtk-data package to vtk-data9.0.

* Thu Jun 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt5
- Fixed crash in uninitialized memory in OpenSlide wrapper (Closes: #40280, #40282).

* Wed Jun 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt4
- Updated build dependencies.

* Fri Jun 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt3
- Added compatibility to p9.

* Thu May 20 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt2
- Built remote modules.
- Fixed 'duplicate target OpenSlide::OpenSlide' error using patch from upstream.
- Fixed build with new cmake macros.

* Tue May 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt1
- Updated to upstream version 9.0.1.

* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 8.2.0-alt9
- Updated build dependencies.

* Thu Jan 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 8.2.0-alt8
- Fixed build with gcc-10 and new cmake.

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 8.2.0-alt7
- NMU: fix build with freetype 2.10.3

* Fri Aug 21 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 8.2.0-alt6
- Fixed build with new qt version and architectures.

* Thu Mar 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.2.0-alt5
- fix packaging on armh arch

* Tue Feb 25 2020 Slava Aseev <ptrnine@altlinux.org> 8.2.0-alt4
- Fixed build with Python 3.8

* Mon Oct 07 2019 Vladislav Zavjalov <slazav@altlinux.org> 8.2.0-alt3
- Use internal libproj 4.4 instead of libproj 6.2.0

* Mon Jul 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 8.2.0-alt2
- Rebuilt with python-3.

* Wed May 15 2019 Slava Aseev <ptrnine@altlinux.org> 8.2.0-alt1
- Updated to upstream version 8.2.0.

* Thu Oct 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.1.1-alt3
- fixed build on armh

* Wed Oct 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8.1.1-alt2
- Updated build dependencies.

* Mon Sep 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8.1.1-alt1
- Updated to upstream version 8.1.1.

* Wed Aug 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt4
- Rebuilt without openpdt.

* Sun Jun 24 2018 Anton Midyukov <antohami@altlinux.org> 6.2.0-alt3
- Rebuilt for aarch64
- Fix FTBFS

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.2.0-alt2.qa1
- NMU: rebuilt against Tcl/Tk 8.6

* Thu Mar 23 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.2.0-alt2
- NMU: fixed build

* Fri Mar 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2.0-alt1
- Version 6.2.0

* Tue May 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.0-alt1
- Version 6.1.0

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt2
- Fixed cmake files

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt1
- Version 6.0.0

* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt6
- Rebuilt with new python-module-sip

* Tue Jul 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt5
- Fixed build

* Thu Jun 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt4
- Rebuilt with new libhdf5

* Fri Apr 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt3
- Rebuilt without MPI

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt2
- Rebuilt with Boost 1.53.0

* Fri Feb 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt1
- Version 5.10.1

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt7
- Rebuilt with new qscintilla2

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt6
- Rebuilt with Boost 1.52.0

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt5
- Rebuilt with libpng15

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt4
- Rebuilt with Boost 1.51.0 (thnx iv@)

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

