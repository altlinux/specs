%def_disable static
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
%define sover 2.3
Name: lib%bname%sover
Version: 2.3.2
%define trunk 20111203
Release: alt2.svn%trunk
Summary:  Intel(R) Open Source Computer Vision Library
License: Distributable
Group: System/Libraries
URL: http://%{bname}library.sourceforge.net/
# https://code.ros.org/svn/opencv/trunk/opencv
Source: %bname-%version.tar
Source1: %{bname}_extra.tar
Source2: interfaces.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: chrpath libavformat53 libavcodec53
BuildRequires: gcc-c++ libjasper-devel libjpeg-devel libtiff-devel
BuildRequires: openexr-devel graphviz libpng-devel
BuildPreReq: cmake libnumpy-devel eigen2 doxygen
BuildPreReq: libucil-devel libv4l-devel libtbb-devel bzlib-devel
BuildPreReq: python-module-sphinx-devel python-module-Pygments
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


%if_enabled static
%package -n lib%bname-devel-static
Summary: Static %name
Group: Development/C++
Requires: lib%bname-devel = %version-%release
Conflicts: lib%bname-devel-static
Conflicts: lib%{bname}2-devel-static

%description -n lib%bname-devel-static
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains static library to develop applications with
%name.
%endif


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
Requires: %name-utils-data = %version-%release
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

%package utils-data
Group: Video
Summary: %Name utils data
BuildArch: noarch

%description utils-data
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains %Name demo applications data.


%package -n python-module-%bname%sover
Group: Development/Python
Summary: Python modules for %Name
Provides: python-module-%bname = %version-%release
Conflicts: python-module-%bname < %version-%release
Obsoletes: python-module-%bname < %version-%release
Provides: python-module-%{bname}2 = %version-%release
Conflicts: python-module-%{bname}2 < %version-%release
Obsoletes: python-module-%{bname}2 < %version-%release

%description -n python-module-%bname%sover
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains an extension module for python that provides a
Python language mapping for the %Name.

%package -n python-module-%bname%sover-pickles
Group: Development/Python
Summary: Pickles for Python modules for %Name
Conflicts: python-module-%bname-pickles
Conflicts: python-module-%{bname}2-pickles

%description -n python-module-%bname%sover-pickles
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains pickles for %{bname}4 for python that provides a
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

%package -n %bname-tracker3D
Group: Video
Summary: Obtain automatically training images from video or camera
Requires: %name = %version-%release
Requires: %bname-tracker3D-data = %version-%release

%description -n %bname-tracker3D
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

tracker3D application was developed to obtain automatically
training images from video or camera only by selecting an object
in one frame. To do so you need only a pre-recored video or
live input from camera.

%package -n %bname-tracker3D-data
Group: Video
Summary: Data files for tracker3D
BuildArch: noarch

%description -n %bname-tracker3D-data
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

tracker3D application was developed to obtain automatically
training images from video or camera only by selecting an object
in one frame. To do so you need only a pre-recored video or
live input from camera. This package contains data files for tracker3D.

%package -n %bname-extra
Group: Video
Summary: Extra data files for %Name
BuildArch: noarch

%description -n %bname-extra
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains extra data files for %Name.

%prep
%setup
tar -xf %SOURCE1
tar -xf %SOURCE2

for i in IlmImf Iex Half; do
	rm -f 3rdparty/lib/$i.lib
done

rm -f $(find ./ -name '*.a')

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
INCS="-I$PWD/modules/core/include -I$PWD/modules/imgproc/include"
INCS="$INCS -I$PWD/modules/video/include -I$PWD/modules/features2d/include"
INCS="$INCS -I$PWD/modules/flann/include -I$PWD/modules/calib3d/include"
INCS="$INCS -I$PWD/modules/objdetect/include -I$PWD/modules/ml/include"
INCS="$INCS -I$PWD/modules/highgui/include -I$PWD/modules/legacy/include"
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
	-DCMAKE_CXX_FLAGS:STRING="-DHAVE_PNG -fno-strict-aliasing $INCS" \
	-DCMAKE_C_FLAGS:STRING="-DHAVE_PNG -fno-strict-aliasing $INCS" \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DPYTHON_PLUGIN_INSTALL_PATH:PATH=%python_sitelibdir/%bname \
%ifarch x86_64
	-DLIB_SUFFIX:STRING=64 \
%endif
	.
%make_build VERBOSE=1

# tracker3D

pushd opencv_extra/3d/tracker3D
rm -f makefile
cmake \
	-DOpenCV_DIR=$PWD/../../.. \
	.
%make_build
popd

%install
touch AUTHORS ChangeLog COPYING INSTALL NEWS THANKS TODO

%makeinstall_std

%makeinstall_std -C interfaces/swig/python

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%python_sitelibdir_noarch/* %buildroot%python_sitelibdir/
%endif

rm -fR %buildroot%_datadir/%bname/doc \
	%buildroot%python_sitelibdir/%bname/matlab_syntax.py*

# tracker3D

install -m755 opencv_extra/3d/tracker3D/tracker3D \
	%buildroot%_bindir
install -d %buildroot%_datadir/%bname/tracker3D
install -p -m644 opencv_extra/3d/tracker3D/data/* \
	%buildroot%_datadir/%bname/tracker3D

# extra

cp -fR opencv_extra/classifiers opencv_extra/testdata \
	%buildroot%_datadir/%bname/

# no RPATH

pushd %buildroot
for i in .%_bindir/* .%python_sitelibdir/%bname/*.so \
	.%python_sitelibdir/*.so .%_libdir/*.so
do
	chrpath -d $i
done
popd

%files
%_libdir/*.so.*

%files -n lib%bname-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%dir %_datadir/%bname
%_datadir/%Name

%if_enabled static
%files -n lib%bname-devel-static
%_libdir/*.a
%endif

%files doc
%doc doc/vidsurv doc/*.pdf

%files utils
%_bindir/*
%exclude %_bindir/tracker3D

%files utils-data
%dir %_datadir/%bname
%_datadir/%bname/*
%exclude %_datadir/%bname/samples
%exclude %_datadir/%bname/tracker3D
%exclude %_datadir/%bname/classifiers
%exclude %_datadir/%bname/testdata


%files -n python-module-%bname%sover
%python_sitelibdir/*

%files examples
%dir %_datadir/%bname
%_datadir/%bname/samples

%files -n %bname-tracker3D
%doc opencv_extra/3d/tracker3D/readme.txt
%_bindir/tracker3D

%files -n %bname-tracker3D-data
%dir %_datadir/%bname
%_datadir/%bname/tracker3D

%files -n %bname-extra
%dir %_datadir/%bname
%_datadir/%bname/classifiers
%_datadir/%bname/testdata

%changelog
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
