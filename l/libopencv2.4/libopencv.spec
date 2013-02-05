%def_disable debug
%def_enable apps
%def_disable openmp
%def_without unicap
%def_with swig
%def_with python
%def_with xine
%def_without octave
%def_without gstreamer
%def_with ffmpeg
%def_with 1394libs
%def_with v4l
%def_with gtk
%def_with gthread
%def_without carbon
%def_without imageio
%def_without quicktime
%def_with pic
#----------------------------------------------------------------------
%define set_without() %{expand:%%force_without %{1}} %{expand:%%undefine _with_%{1}}

%{?_with_ffmpeg:%set_without gstreamer}
%{?_with_ffmpeg:%set_without quicktime}
%{?_with_xine:%set_without quicktime}
%{?_with_1394libs:%set_without quicktime}
%{?_with_v4l:%set_without quicktime}

%define bname opencv
%define Name OpenCV
%define sover 2.4
Name: lib%bname%sover
Version: 2.4.9
%define trunk 20130204
Release: alt3.git%trunk
Summary:  Intel(R) Open Source Computer Vision Library
License: Distributable
Group: System/Libraries
URL: http://opencv.org
# git://code.opencv.org/opencv.git
Source: %bname-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: chrpath libavformat53 libavcodec53 libcvmser
BuildRequires: gcc-c++ libjasper-devel libjpeg-devel libtiff-devel
BuildRequires: openexr-devel graphviz libpng-devel libpixman-devel
BuildPreReq: cmake libnumpy-devel eigen3 doxygen zlib-devel
BuildPreReq: libucil-devel libv4l-devel libtbb-devel bzlib-devel
BuildPreReq: pkgconfig(glproto) pkgconfig(dri2proto) pkgconfig(xext)
BuildPreReq: pkgconfig(xdamage) pkgconfig(xxf86vm)
BuildPreReq: libGLU-devel libXau-devel libXdmcp-devel libgtkglext-devel
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: texlive-latex-base
%{?_enable_openmp:BuildRequires: libgomp-devel}
%{?_with_unicap:BuildRequires: libunicap-devel}
%{?_with_ffmpeg:BuildRequires: libavformat-devel libswscale-devel}
%{?_with_gstreamer:BuildRequires: gstreamer-devel}
%{?_with_gtk:BuildRequires: libgtk+2-devel}
%{?_with_xine:BuildRequires: libxine-devel}
%{?_with_python:BuildRequires: python-devel}
%{?_with_octave:BuildRequires: octave-devel}
%{?_with_swig:BuildRequires: swig}
%{?_with_1394libs:BuildRequires: libdc1394-devel}

%description
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.


%package -n lib%bname-devel
Group: Development/C++
Summary: Development files for %name
Requires: %name = %version-%release
Provides: lib%{bname}2.2-devel = %version-%release
Provides: lib%{bname}2-devel = %version-%release
Conflicts: lib%{bname}2.2-devel < %version-%release
Obsoletes: lib%{bname}2.2-devel < %version-%release
Conflicts: lib%bname-devel < %version-%release
Obsoletes: lib%bname-devel < %version-%release
Conflicts: lib%{bname}2-devel < %version-%release
Obsoletes: lib%{bname}2-devel < %version-%release

%description -n lib%bname-devel
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains header files and documentation needed to develop
applications with %name.


%package doc
Summary: %name documentation
Group: Development/Documentation
BuildArch: noarch

%description doc
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains API Reference for develop with %name.


%package tests
Group: Video
Summary: %Name tests
Requires: %name = %version-%release

%description tests
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains %Name tests applications.

%package utils
Group: Video
Summary: %Name utils
Provides: lib%bname-utils = %version-%release
Conflicts: lib%bname-utils < %version-%release
Obsoletes: lib%bname-utils < %version-%release
Provides: lib%{bname}2-utils = %version-%release
Conflicts: lib%{bname}2-utils < %version-%release
Obsoletes: lib%{bname}2-utils < %version-%release

%description utils
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains %Name demo applications.


%package -n python-module-%bname%sover
Group: Development/Python
Summary: Python modules for %Name
Provides: python-module-%bname = %version-%release
Conflicts: python-module-%bname < %version-%release
Obsoletes: python-module-%bname < %version-%release
Provides: python-module-%{bname}2 = %version-%release
Conflicts: python-module-%{bname}2 < %version-%release
Obsoletes: python-module-%{bname}2 < %version-%release
Conflicts: python-module-%{bname}2.3
Obsoletes: python-module-%{bname}2.3

%description -n python-module-%bname%sover
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains an extension module for python that provides a
Python language mapping for the %Name.

%package examples
Group: Video
Summary: %Name samples
BuildArch: noarch
Conflicts: lib%bname-examples
Conflicts: lib%{bname}2-examples

%description examples
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains %Name examples.

%prep
%setup

rm -fR 3rdparty/{ffmpeg,lib,libjasper,libjpeg,libpng,libtiff,openexr,tbb,zlib}

for i in $(egrep -R cxtypes interfaces/swig/|awk -F : '{print $1}')
do
	sed -i 's|.*cxtypes.*||' $i
done
for i in $(egrep -R cvtypes interfaces/swig/|awk -F : '{print $1}')
do
	sed -i 's|.*cvtypes.*||' $i
done

rm -f interfaces/swig/python/_*.cpp interfaces/swig/python/cv.py \
	interfaces/swig/python/highgui.py interfaces/swig/python/ml.py
#rm -fR interfaces/swig/general

%prepare_sphinx .
cp -f doc/conf.py ./
cp doc/opencv-logo2.png ./

%build
SWIG_FEATURES="-I$PWD/include/opencv"
for i in core ml imgproc video features2d flann calib3d objdetect \
	legacy highgui photo
do
	SWIG_FEATURES="$SWIG_FEATURES -I$PWD/modules/$i/include"
done
export SWIG_FEATURES
%add_optflags $SWIG_FEATURES
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DBUILD_PACKAGE:BOOL=ON \
	-DBUILD_TESTS:BOOL=OFF \
	-DBUILD_EXAMPLES:BOOL=ON \
	-DINSTALL_C_EXAMPLES:BOOL=ON \
	-DINSTALL_PYTHON_EXAMPLES:BOOL=ON \
	-DENABLE_OPENMP:BOOL=OFF \
	-DWITH_TBB:BOOL=ON \
	-DBUILD_PYTHON_SUPPORT:BOOL=ON \
	-DCMAKE_VERBOSE:BOOL=ON \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DPYTHON_PLUGIN_INSTALL_PATH:PATH=%python_sitelibdir/%bname \
	-DWITH_UNICAP:BOOL=ON \
	-DWITH_QUICKTIME:BOOL=ON \
	-DWITH_XINE:BOOL=ON \
	-DWITH_OPENGL:BOOL=ON \
	-DINSTALL_PYTHON_EXAMPLES:BOOL=ON \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
%ifarch x86_64
	-DLIB_SUFFIX:STRING=64 \
%endif
	.
%make_build VERBOSE=1

%install
%makeinstall_std

%makeinstall_std -C interfaces/swig/python

rm -f	%buildroot%python_sitelibdir/%bname/matlab_syntax.py*

install -d %buildroot%_docdir/%name
mv %buildroot%_datadir/%Name/doc/* %buildroot%_docdir/%name/

cp -fR samples/python* %buildroot%_datadir/%Name/samples/

sed -i \
	's|\(Libs:\)\(.*\)|\1 ${exec_prefix}/%_lib/libopencv_legacy.so \2|' \
	%buildroot%_pkgconfigdir/opencv.pc

%files
%doc README
%_libdir/*.so.*
%dir %_datadir/%bname
%dir %_datadir/%Name
%_datadir/%Name/haarcascades
%_datadir/%Name/lbpcascades

%files -n lib%bname-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_datadir/%Name/*.cmake

%files doc
%doc doc/vidsurv
%_docdir/%name

%files utils
%_bindir/*

%files -n python-module-%bname%sover
%python_sitelibdir/*

%files examples
%dir %_datadir/%bname
%dir %_datadir/%Name
%_datadir/*/samples

%changelog
* Tue Feb 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.9-alt3.git20130204
- New snapshot

* Thu Sep 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.9-alt3.git20120917
- Built python%_python_version(%bname)

* Thu Sep 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.9-alt2.git20120917
- Fixed pkg-config file

* Mon Sep 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.9-alt1.git20120917
- Version 2.4.9

* Mon Feb 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.2-alt2.svn20111203
- Fixed build with libav 0.8

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.2-alt1.svn20111203
- Version 2.3.2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.1-alt1.svn20110813.1.1
- Rebuild with Python-2.7

* Sun Aug 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.svn20110813.1
- Fixed headers: rename classes True -> cvTrue and False -> cvFalse

* Sat Aug 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.svn20110813
- Version 2.3.1

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.svn20110120.2
- Rebuilt for debuginfo

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.svn20110120.1
- Rebuilt with python-module-sphinx-devel

* Sat Jan 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.svn20110120
- New snapshot
- Added tracker3D and extra subpackages

* Wed Jan 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.svn20101222.1
- Disabled OpenMP (ALT #24934)

* Wed Dec 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.svn20101222
- New snapshot
- Fixed support of PNG images (ALT #24800)

* Wed Dec 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.svn20101206.1
- Rebuilt for soname set-versions

* Tue Dec 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.svn20101206
- Version 2.2
- Fixed build of python module

* Fri Nov 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.svn20101118.2
- libopencv2-devel provides libopencv-devel now

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.svn20101118.1
- Avoid conflict with libml10-devel

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.svn20101118
- New soname version

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.svn20100626.3
- Fixed underlinking of libraries

* Mon Aug 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.svn20100626.2
- Avoid requirement on lib%bname-devel for python-module-%bname (ALT #23887)

* Tue Jun 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.svn20100626.1
- Added explicit conflict with libml10-devel
- Renamed python packages

* Tue Jun 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.svn20100626
- New snapshot

* Thu Jun 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.svn20091116
- Version 2.1.0

* Fri Mar 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20091116.1
- Version 2.0.0 (ALT #23126)
- Added examples and tests packages, and pickles for python-module-%name
- Reformed with SharedLibraries Policy

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2.svn20090728.1
- Rebuilt with python 2.6

* Wed Jul 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2.svn20090728
- Enabled OpenEXR support

* Tue Jul 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.svn20090728
- Version 1.2.1

* Fri Jul 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.svn20090630
- Replaced demo data files into separate package
- Added explicit conflict with old utils package

* Wed Jul 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20090630
- New snapshot
- Soname changed

* Mon Feb 23 2009 Led <led@altlinux.ru> 1.1-alt0.1
- 1.1pre1
- enabled openmp

* Sun Feb 22 2009 Led <led@altlinux.ru> 1.0.0-alt2
- Added libswscale support to avoid the deprecated img_convert
- updated BuildRequires
- fixed Group

* Sun Mar 16 2008 Led <led@altlinux.ru> 1.0.0-alt1
- initial build
