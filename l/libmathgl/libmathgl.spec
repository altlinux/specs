%define oname mathgl
Name: lib%oname
Version: 2.2.2.1
Release: alt1

Summary: Library of fast C++ routines for the plotting of the data

License: LGPL
Group: System/Libraries
Url: http://www.sf.net/projects/mathgl/

Source: http://prdownloads.sf.net/%oname/%oname-%version.tar
Source1: %oname-2.2.2.eng.pdf

# Automatically added by buildreq on Fri Jan 08 2010
BuildRequires: gcc-c++ glibc-devel libGL-devel libGLUT-devel libgif-devel libgsl-devel libhdf5-devel libjpeg-devel libpng-devel python-devel libnumpy-devel swig

BuildPreReq: cmake libICE-devel libSM-devel libXres-devel libXext-devel
BuildPreReq: libXtst-devel libxkbfile-devel libXau-devel libfltk-devel
BuildPreReq: libXcomposite-devel libXcursor-devel libXdamage-devel
BuildPreReq: libXdmcp-devel libXfixes-devel libXft-devel
BuildPreReq: libXi-devel libXinerama-devel libxkbfile-devel libXpm-devel
BuildPreReq: libXrandr-devel libXrender-devel libXScrnSaver-devel
BuildPreReq: libXt-devel libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildPreReq: libXmu-devel gcc-fortran libltdl-devel libharu-devel
BuildPreReq: hdf5-tools libqt4-devel ImageMagick-tools

%description
MathGL is a free library of fast C++ routines for the plotting of the data
varied in one or more dimensions. It uses OpenGL (www.opengl.org)
for the plotting. Also there is a simple window interface based on
GLUT. This provides high compatibility with any operating system
(really any which has OpenGL-like libraries).

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for %name library.

%package -n python-module-mathgl
Summary: Python module for %name
Group: System/Libraries
Requires: %name = %version-%release

%description -n python-module-mathgl
Python module for %name.

%package devel-doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
Development documentation for %name.

%package examples
Summary: Examples for %name
Group: Development/Documentation
Requires: %name = %version-%release

%description examples
Examples for %name.

%package -n %oname-udav
Summary: UDAV is program for data visualization based on MathGL
Group: Sciences/Mathematics
Requires: %name = %version-%release
Conflicts: udav
Obsoletes: udav

%description -n %oname-udav
UDAV is program for data arrays visualization based on MathGL library.
It support wide spectrum of graphics, simple script language and
visual data handling and editing. It has windows interface for data
viewing, changing and plotting. Also it can execute MGL scripts, setup
and rotate graphics and so on. MathGL is a free library of fast C++
routines for the plotting.

%prep
%setup -n %oname-%version
install -p -m644 %SOURCE1 .

%build
%add_optflags `pkg-config --cflags hdf5`
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_C_FLAGS="%optflags" \
	-DCMAKE_CXX_FLAGS="%optflags" \
	-DCMAKE_Fortran_FLAGS="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DHDF5_DIR:PATH="%_libdir/hdf5-seq" \
	-DFLTK_DIR:PATH=%prefix \
	-Denable-double:BOOL=ON \
	-Denable-fltk:BOOL=ON \
	-Denable-gif:BOOL=ON \
	-Denable-glut:BOOL=ON \
	-Denable-gsl:BOOL=ON \
	-Denable-hdf5_18:BOOL=ON \
	-Denable-jpeg:BOOL=ON \
	-Denable-ltdl:BOOL=ON \
	-Denable-pdf:BOOL=ON \
	-Denable-pthread:BOOL=ON \
	-Denable-python:BOOL=ON \
	-Denable-qt:BOOL=ON \
	-Denable-qt4:BOOL=ON \
	-Denable-openmp:BOOL=OFF \
%ifarch x86_64
	-DLIB_SUFFIX=64 \
%endif
	-DDESTDIR=%buildroot \
	.
%make_build VERBOSE=1

%install
%makeinstall_std

install -d %buildroot%_liconsdir
mv %buildroot%_pixmapsdir/udav.png %buildroot%_liconsdir/

install -m755 examples/mgl*example %buildroot%_bindir/

%files
#_bindir/mgl2*
%_bindir/mglconv
%_bindir/mglview
%doc AUTHORS README* ChangeLog.txt
%_libdir/*.so.*
%_datadir/mathgl/
%_libdir/mathgl

%files devel
%_libdir/*.so
%_includedir/*

%files -n python-module-mathgl
%python_sitelibdir/*

%files devel-doc
%doc texinfo/*.pdf *.pdf todo.txt

%files examples
%doc examples/*.cpp examples/CMakeLists.txt
%_bindir/mgl*example

%files -n %oname-udav
%_bindir/udav
%_desktopdir/udav.*
%_liconsdir/udav.*
%_datadir/udav

%changelog
* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2.1-alt1
- Version 2.2.2.1

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt4
- Rebuilt with new libhdf5

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt3
- Rebuilt with new libfltk

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt2
- Added %oname-udav

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1.1
- rebuild with libharu 2.2.1

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1
- Version 2.0.3

* Thu May 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Version 2.0

* Wed Feb 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0.1-alt1.2
- Removed bad RPATH

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.11.0.1-alt1.1.1
- Rebuild with Python-2.7

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0.1-alt1.1
- Rebuilt with libhdf5-7

* Mon Jan 24 2011 Vitaly Lipatov <lav@altlinux.ru> 1.11.0.1-alt1
- new version 1.11.0.1 (with rpmrb script)

* Tue Nov 09 2010 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- new version 1.11 (with rpmrb script) (ALT bug #24481)

* Mon Feb 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt2.1
- Rebuilt with reformed NumPy

* Fri Jan 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt2
- cleanup spec, update buildreqs
- build with hdf5 support

* Sun Jan 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt1
- new version 1.10 (with rpmrb script)

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1.1
- Rebuilt with python 2.6

* Thu Jul 09 2009 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt1
- new version (1.9) import in git

* Wed Jun 03 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt2
- rebuild with libhdf5 v1.8.3

* Thu Apr 23 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)
- enable python module build

* Wed Dec 24 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- new version 1.8 (with rpmrb script)
- update buildreq, cleanup spec

* Wed Oct 31 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- new version 1.4 (with rpmrb script)
- soname changed

* Mon Oct 08 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Sun Sep 16 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
