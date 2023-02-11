%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# LTO causes errors, disable it
%global optflags_lto %nil

# TODO: remove later this fix for documentation
%define _cmake__builddir BUILD

%def_with openmp
%def_without unicap
%def_with swig
%def_with python3
%def_without xine
%def_without octave
%def_without gstreamer
%def_with ffmpeg
%def_with 1394libs
%def_with v4l
%def_with gtk
%def_without quicktime
%ifarch %{ix86} x86_64 armh
%def_with gdcm
%else
%def_without gdcm
%endif
%ifarch %{ix86} x86_64
%def_with openni
%else
%def_without openni
%endif
#----------------------------------------------------------------------
%define set_without() %{expand:%%force_without %{1}} %{expand:%%undefine _with_%{1}}

%{?_with_ffmpeg:%set_without gstreamer}
%{?_with_ffmpeg:%set_without quicktime}
%{?_with_xine:%set_without quicktime}
%{?_with_1394libs:%set_without quicktime}
%{?_with_v4l:%set_without quicktime}

%define bname opencv
%define Name OpenCV
%define sover 4.5
Name: lib%bname
Epoch: 1
Version: 4.5.5
Release: alt2
Summary: Open Source Computer Vision Library
License: Distributable
Group: System/Libraries
URL: https://opencv.org

# https://github.com/opencv/opencv.git
Source: %bname-%version.tar
# https://github.com/opencv/opencv_contrib.git
Source1: %bname-contrib-%version.tar
# https://github.com/opencv/opencv_3rdparty.git
# Exact commits are mentioned in following files from contrib repo:
# modules/xfeatures2d/cmake/download_vgg.cmake
# modules/xfeatures2d/cmake/download_boostdesc.cmake
Source2: %bname-xfeatures2d-boostdesc-%version.tar
Source3: %bname-xfeatures2d-vgg-%version.tar

Patch1: %name-%version-alt-python-paths.patch
Patch2: %name-%version-alt-linking.patch
Patch3: %name-%version-alt-build.patch
Patch4: https://github.com/opencv/opencv/commit/8d88bb06b230b5c4b5bca78d84102f5d1adf48cf.patch

Patch2000: %name-e2k-simd.patch

BuildRequires: gcc-c++ libjasper-devel libjpeg-devel libtiff-devel
BuildRequires: openexr-devel graphviz libpng-devel libpixman-devel
BuildRequires: cmake eigen3 zlib-devel
BuildRequires: python3 python3(bs4) doxygen
BuildRequires: libucil-devel libtbb-devel bzlib-devel
BuildRequires: pkgconfig(glproto) pkgconfig(dri2proto) pkgconfig(xext)
BuildRequires: pkgconfig(xdamage) pkgconfig(xxf86vm)
BuildRequires: libGLU-devel libXau-devel libXdmcp-devel
BuildRequires: python3-module-sphinx-devel python3-module-Pygments python3-module-sphinx-sphinx-build-symlink
BuildRequires: texlive-latex-base
BuildRequires: libprotobuf-devel protobuf-compiler libwebp-devel
BuildRequires: libgflags-devel
%ifarch %{ix86} x86_64 armh
BuildRequires: libglog-devel
%endif
%ifarch %{ix86} x86_64
BuildRequires: ceres-solver-devel
%endif
%{?_with_v4l:BuildRequires: libv4l-devel}
%{?_with_openmp:BuildRequires: libgomp-devel}
%{?_with_unicap:BuildRequires: libunicap-devel}
%{?_with_ffmpeg:BuildRequires: libavformat-devel libswscale-devel libavresample-devel}
%{?_with_gstreamer:BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel}
%{?_with_gtk:BuildRequires: libgtk+3-devel}
%{?_with_xine:BuildRequires: libxine-devel}
%{?_with_python3:
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libnumpy-py3-devel
}
%{?_with_octave:BuildRequires: octave-devel}
%{?_with_swig:BuildRequires: swig}
%{?_with_1394libs:BuildRequires: libdc1394-devel}
%{?_with_gdcm:BuildRequires: gdcm-devel}
%{?_with_openni:
BuildRequires: openni-devel
BuildRequires: openni-primesense
}
BuildRequires: libade-devel

%add_findprov_skiplist %_datadir/OpenCV/samples/*

%description
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

%package -n lib%bname%sover
Group: System/Libraries
Summary: Open Source Computer Vision Library

%description -n lib%bname%sover
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

%package devel
Group: Development/C++
Summary: Development files for %name
Requires: lib%bname%sover = %EVR
# generated cmake targets mention tbb, require it here explicitly
Requires: tbb-devel
Provides: lib%{bname}2.2-devel = %EVR
Provides: lib%{bname}2-devel = %EVR
Conflicts: lib%{bname}2.2-devel < %EVR
Obsoletes: lib%{bname}2.2-devel < %EVR
Conflicts: lib%{bname}2-devel < %EVR
Obsoletes: lib%{bname}2-devel < %EVR
Provides: lib%bname-devel-static = %EVR

%description devel
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
Requires: lib%bname%sover = %EVR

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
Provides: lib%{bname}2-utils = %EVR
Conflicts: lib%{bname}2-utils < %EVR
Obsoletes: lib%{bname}2-utils < %EVR
Provides: lib%{bname}3.4-utils = %EVR
Conflicts: lib%{bname}3.4-utils < %EVR
Obsoletes: lib%{bname}3.4-utils < %EVR

%description utils
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains %Name demo applications.

%if_with python3
%package -n python3-module-%bname
Group: Development/Python3
Summary: Python3 modules for %Name
Provides: python3-module-%{bname}3.4 = %EVR
Conflicts: python3-module-%{bname}3.4 < %EVR
Obsoletes: python3-module-%{bname}3.4 < %EVR

%description -n python3-module-%bname
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains an extension module for python that provides a
Python3 language mapping for the %Name.
%endif

%package examples
Group: Video
Summary: %Name samples
Conflicts: lib%bname-examples
Conflicts: lib%{bname}2-examples
Provides: lib%{bname}3.4-examples = %EVR
Conflicts: lib%{bname}3.4-examples < %EVR
Obsoletes: lib%{bname}3.4-examples < %EVR
AutoReq:no

%description examples
%Name means Intel(R) Open Source Computer Vision Library. It is a
collection of C functions and a few C++ classes that implement many
popular Image Processing and Computer Vision algorithms.
%Name provides cross-platform middle-to-high level API that includes
about 300 C functions and a few C++ classes. Also there are constantly
improving Python bindings to %Name.

This package contains %Name examples.

%prep
%setup -b 1 -b 2 -b 3
%patch1 -p1
pushd ../%bname-contrib-%version >/dev/null
%patch2 -p1
popd >/dev/null
%patch3 -p1
%patch4 -p1
%ifarch %e2k
%patch2000 -p1
%endif

rm -fR 3rdparty/{ffmpeg,libjasper,libjpeg,libpng,libtiff,openexr,tbb,zlib,protobuf,libwebp}

mkdir -pv %_cmake__builddir/downloads/xfeatures2d
cp %_builddir/%bname-xfeatures2d-boostdesc-%version/* %_cmake__builddir/downloads/xfeatures2d/
cp %_builddir/%bname-xfeatures2d-vgg-%version/* %_cmake__builddir/downloads/xfeatures2d/

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%cmake \
	-DBUILD_PACKAGE:BOOL=ON \
	-DBUILD_TESTS:BOOL=OFF \
	-DBUILD_EXAMPLES:BOOL=ON \
	-DINSTALL_C_EXAMPLES:BOOL=ON \
	-DINSTALL_PYTHON_EXAMPLES:BOOL=ON \
	-DENABLE_OPENMP:BOOL=%{?_with_openmp:ON}%{!?_with_openmp:OFF} \
	-DWITH_TBB:BOOL=ON \
	-DBUILD_PYTHON_SUPPORT:BOOL=ON \
	-DCMAKE_VERBOSE:BOOL=ON \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DWITH_UNICAP:BOOL=%{?_with_unicap:ON}%{!?_with_unicap:OFF} \
	-DWITH_QUICKTIME:BOOL=%{?_with_quicktime:ON}%{!?_with_quicktime:OFF} \
	-DWITH_XINE:BOOL=%{?_with_xine:ON}%{!?_with_xine:OFF} \
	-DWITH_FFMPEG:BOOL=%{?_with_ffmpeg:ON}%{!?_with_ffmpeg:OFF} \
	-DWITH_GSTREAMER=%{?_with_gstreamer:ON}%{!?_with_gstreamer:OFF} \
	-DWITH_OPENGL:BOOL=ON \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DBUILD_opencv_ts:BOOL=OFF \
	-DBUILD_PROTOBUF:BOOL=OFF \
	-DPROTOBUF_UPDATE_FILES:BOOL=ON \
	-DOPENCV_ENABLE_NONFREE:BOOL=ON \
	-DWITH_LIBV4L:BOOL=%{?_with_v4l:ON}%{!?_with_v4l:OFF} \
	-DOPENCV_EXTRA_MODULES_PATH=%_builddir/%bname-contrib-%version/modules \
	%{?_with_openni: -DWITH_OPENNI=ON } \
	%{?_with_gdcm: -DWITH_GDCM=ON} \
	-DBUILD_DOCS:BOOL=ON \
	-DOPENCV_DOC_INSTALL_PATH=%_docdir/%name/ \
	-DOPENCV_3P_LIB_INSTALL_PATH=%_libdir/%Name/3rdparty/%_lib \
	-DOPENCV_LICENSES_INSTALL_PATH=%_datadir/%Name-%version/licenses \
	-DOPENCV_OTHER_INSTALL_PATH=%_datadir/%Name \
	-DOPENCV_GENERATE_PKGCONFIG:BOOL=ON \
	-DOPENCV_SKIP_CMAKE_CXX_STANDARD:BOOL=ON \
	-DPYTHON_EXECUTABLE=%__python3 \
	-DPYTHON_DEFAULT_EXECUTABLE=%__python3 \
	%nil

%cmake_build
%cmake_build -t opencv_docs

%install
%cmakeinstall_std install_docs

%files -n lib%bname%sover
%doc README.md
%_libdir/*.so.*
%dir %_datadir/%Name
%dir %_datadir/%Name-%version
%_datadir/%Name-%version/licenses

%files devel
%_libdir/*.so
%_libdir/cmake/*
%_includedir/*
%_pkgconfigdir/*
%_datadir/%Name/*.supp
%ifarch %{ix86} x86_64 armh
%dir %_libdir/%Name
%dir %_libdir/%Name/3rdparty
%dir %_libdir/%Name/3rdparty/%_lib
%_libdir/%Name/3rdparty/%_lib/*.a
%endif

%files doc
%_docdir/%name

%files utils
%_bindir/*

%if_with python3
%files -n python3-module-%bname
%python3_sitelibdir/*
%endif

%files examples
%_datadir/%Name/samples
%_datadir/%Name/haarcascades
%_datadir/%Name/lbpcascades
%_datadir/%Name/quality

%changelog
* Tue Jan 10 2023 Alexey Shabalin <shaba@altlinux.org> 1:4.5.5-alt2
- The upstream fix https://github.com/opencv/opencv/pull/21614
  for build on power8

* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.5.5-alt1
- Updated to upstream version 4.5.5.

* Mon Aug 30 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.5.3-alt3
- Disabled LTO.

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1:4.5.3-alt2
- disable python2 subpackage, disable provides for python examples

* Mon Jul 26 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.5.3-alt1
- Updated to upstream version 4.5.3.

* Thu Jun 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.5.2-alt1
- Updated to upstream version 4.5.2.
- Built with openmp support.

* Tue Jun 01 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:4.5.1-alt3
- added SIMD patch for Elbrus

* Mon May 31 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.5.1-alt2
- Fixed build with new cmake macros (Closes: #40128).

* Thu Jan 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.5.1-alt1
- Updated to upstream version 4.5.1.

* Tue Dec 01 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.5.0-alt2
- Fixed build.

* Mon Oct 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.5.0-alt1
- Updated to upstream version 4.5.0.

* Thu Sep 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.4.0-alt1
- Updated to upstream version 4.4.0.

* Thu Jul 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.3.0-alt2
- Disabled any requires for examples subpackage (by Vitaly Lipatov)
- Updated build switches.

* Mon Apr 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.3.0-alt1
- Updated to upstream version 4.3.0.

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 1:3.4.6-alt2
- rebuild with new gbcm

* Fri Jul 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.6-alt1
- Updated to upstream version 3.4.6.

* Wed Jan 23 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.5-alt1
- Updated to upstream version 3.4.5.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.4.3-alt1.qa1
- NMU: applied repocop patch

* Mon Sep 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.3-alt1
- Updated to upstream version 3.4.3.
- Rebuilt with gtk+-3.

* Mon Jun 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.4.1-alt3.1
- NMU: autorebuild with libjpasper.so.4

* Thu Jun 14 2018 Anton Farygin <rider@altlinux.ru> 1:3.4.1-alt3
- rebuilt with ffmpeg-4.0

* Wed Jun 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.1-alt2
- Fixed build for aarch64, removed devel-static subpackage.

* Thu May 10 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.4.1-alt1.1
- NMU: rebuild with gdcm 2.8.4

* Thu May 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.1-alt1
- Updated to upstream version 3.4.1.

* Fri Feb 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.0-alt3
- Updated static libraries location.

* Fri Feb 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.0-alt2
- Packaged static libraries (Closes: #34504).

* Tue Jan 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.0-alt1
- Updated to upstream version 3.4.0.

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.4.13.3-alt1
- Updated to version 2.4.13.3.

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 1:2.4.13.2-alt1
- new version

* Mon Jun 22 2015 Sergey V Turchin <zerg@altlinux.org> 1:2.4.9.1-alt2.1
- rebuild with gcc5

* Mon Oct 06 2014 Sergey V Turchin <zerg@altlinux.org> 1:2.4.9.1-alt2
- enable ffmpeg
- disable gstreamer1

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 1:2.4.9.1-alt1
- new version (ALT#30150)
- disable ffmpeg
- disable xine
- enable gstreamer1

* Fri Mar 21 2014 Dmitry Derjavin <dd@altlinux.org> 1:2.4.8.1-alt4
- Added pythonX.Y(opencv) require to the python module package.

* Tue Mar 18 2014 Dmitry Derjavin <dd@altlinux.org> 1:2.4.8.1-alt3
- opencv_ts disabled;
- more spec cleanup.

* Tue Feb 11 2014 Dmitry Derjavin <dd@altlinux.org> 1:2.4.8.1-alt2
- Old (really?) SWIG related stuff removed from spec;
- Files section spec file cleanup.

* Tue Feb 04 2014 Dmitry Derjavin <dd@altlinux.org> 1:2.4.8.1-alt1
- Switched to the current upstream.

* Wed Sep 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.9-alt5.git20130204
- Fixed OpenCVConfig.cmake (ALT #29345)

* Sun Aug 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.9-alt4.git20130204
- Fixed pkg-config file (ALT #29231)

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
