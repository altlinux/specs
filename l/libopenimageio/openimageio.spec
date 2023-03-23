%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# TODO: dependency on Field3D

# TODO: build and run tests

%define oname openimageio
%define soname 2.3

Name:           lib%oname
Version:        2.3.21.0
Release:        alt2.1
Summary:        Library for reading and writing images
Group:          System/Libraries

License:        BSD-3-Clause
URL:            https://sites.google.com/site/openimageio/home

# https://github.com/OpenImageIO/oiio.git
Source0:        %name-%version.tar

# Images for test suite
#Source1:        oiio-images.tar.gz

Source2: %oname.watch

Patch1: %oname-alt-armh-disable-neon.patch
Patch2000: %oname-e2k.patch

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  cmake gcc-c++
BuildRequires:  txt2man
BuildRequires:  qt5-base-devel
BuildRequires:  boost-devel boost-python3-devel boost-filesystem-devel boost-asio-devel
BuildRequires:  libGLEW-devel
BuildRequires:  openexr-devel imath-devel
BuildRequires:  libpng-devel libtiff-devel libjpeg-devel libopenjpeg2.0-devel
BuildRequires:  libgif-devel
BuildRequires:  libwebp-devel
BuildRequires:  libhdf5-devel
BuildRequires:  zlib-devel
BuildRequires:  libjasper-devel
BuildRequires:  libpugixml-devel
BuildRequires:  libraw-devel
BuildRequires:  librobin-map-devel
BuildRequires:  pybind11-devel
BuildRequires:  libsquish-devel
BuildRequires:  bzip2-devel
BuildRequires:  freetype2-devel
BuildRequires:  libfmt-devel
BuildRequires:  openvdb-devel
%ifnarch %e2k
BuildRequires:  libdcmtk-devel
%endif
BuildRequires:  libopencv-devel
BuildRequires: libavcodec-devel libavformat-devel libswscale-devel
BuildRequires: libheif-devel

# WARNING: OpenColorIO and OpenImageIO are cross dependent.
# If an ABI incompatible update is done in one, the other also needs to be
# rebuilt.
BuildRequires:  libopencolorio2.0-devel

%description
OpenImageIO is a library for reading and writing images, and a bunch of related
classes, utilities, and applications. Main features include:
- Extremely simple but powerful ImageInput and ImageOutput APIs for reading and
  writing 2D images that is format agnostic.
- Format plugins for TIFF, JPEG/JFIF, OpenEXR, PNG, HDR/RGBE, Targa, JPEG-2000,
  DPX, Cineon, FITS, BMP, ICO, RMan Zfile, Softimage PIC, DDS, SGI,
  PNM/PPM/PGM/PBM, Field3d.
- An ImageCache class that transparently manages a cache so that it can access
  truly vast amounts of image data.

%package -n lib%oname%soname
Summary:        Library for reading and writing images
Group:          System/Libraries

%description -n lib%oname%soname
OpenImageIO is a library for reading and writing images, and a bunch of related
classes, utilities, and applications. Main features include:
- Extremely simple but powerful ImageInput and ImageOutput APIs for reading and
  writing 2D images that is format agnostic.
- Format plugins for TIFF, JPEG/JFIF, OpenEXR, PNG, HDR/RGBE, Targa, JPEG-2000,
  DPX, Cineon, FITS, BMP, ICO, RMan Zfile, Softimage PIC, DDS, SGI,
  PNM/PPM/PGM/PBM, Field3d.
- An ImageCache class that transparently manages a cache so that it can access
  truly vast amounts of image data.

%package -n python3-module-%oname
Summary:        Python-3 bindings for %oname
Group:          Development/Python3
Requires:       lib%oname%soname = %EVR

%description -n python3-module-%oname
Python bindings for %oname.

%package -n %oname-utils
Summary:        Command line utilities for %oname
Group:          Other
Requires:       lib%oname%soname = %EVR
Conflicts:      libxforms-demos

%description -n %oname-utils
Command-line tools to manipulate and get information on images using the
%{name} library.


%package -n %oname-iv
Summary:        %oname based image viewer
Group:          Other
Requires:       lib%oname%soname = %EVR

%description -n %oname-iv
A really nice image viewer, iv, based on %oname classes (and so will work
with any formats for which plugins are available).


%package devel
Summary:        Documentation for %oname
Group:          Development/Other
Requires:       lib%oname%soname = %EVR
Requires:       python3-module-%oname = %EVR
Requires:       %oname-utils = %EVR
%ifnarch armh
Requires:       %oname-iv = %EVR
%endif
Requires:       libopencv-devel

%description devel
Development files for package %name


%prep
%setup
%ifarch armh
%patch1 -p1
%endif
%ifarch %e2k
%patch2000 -p1
# simplifies the patch
sed -i '/#if OIIO_SIMD_SSE >= 4/{N;/_mm_dp_ps/s/#if /&!defined(__e2k__) \&\& /}' \
	src/include/OpenImageIO/simd.h
%endif

# Remove bundled pugixml
rm -fr src/include/OpenImageIO/detail/pugixml/

# Install test images
#rm -rf ../oiio-images && mkdir ../oiio-images && pushd ../oiio-images
#tar --strip-components=1 -xzf #{SOURCE1}

%ifarch armh
sed -ri '/Qt5_FOUND AND OPENGL_FOUND/ s,iv_enabled,FALSE,' src/iv/CMakeLists.txt
%endif

%build
%add_optflags -D_FILE_OFFSET_BITS=64

# disable debugging stuff
%add_optflags -DNDEBUG
%ifarch %e2k
%add_optflags -mno-sse4.2 -mno-avx
%endif

# set -DCMAKE_BUILD_TYPE=RelWithDebInfo to skip stripping debuginfo from python modules built via pybind11
%cmake \
	-DINCLUDE_INSTALL_DIR:PATH=%_includedir/%oname \
	-DPYTHON_VERSION=%_python3_version \
	-DBUILD_DOCS:BOOL=TRUE \
	-DINSTALL_DOCS:BOOL=FALSE \
	-DINSTALL_FONTS:BOOL=FALSE \
	-DUSE_EXTERNAL_PUGIXML:BOOL=TRUE \
	-DSTOP_ON_WARNING:BOOL=FALSE \
	-DJPEG_INCLUDE_DIR=%_includedir \
	-DOPENJPEG_INCLUDE_DIR=$(pkg-config --variable=includedir libopenjp2) \
	-DOpenGL_GL_PREFERENCE=GLVND \
	-DVERBOSE=TRUE \
	-DOIIO_BUILD_TESTS:BOOL=FALSE \
	-DPLUGIN_SEARCH_PATH=%_libdir/OpenImageIO-%soname \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DOIIO_USING_IMATH=3 \
	%nil

%cmake_build

%install
%cmake_install

# Move man pages to the right directory
mkdir -p %buildroot%_man1dir
cp -a %_cmake__builddir/src/doc/*.1 %buildroot%_man1dir

mkdir -p %buildroot%_libdir/OpenImageIO-%soname

%files -n lib%oname%soname
%doc CHANGES.md README.md
%doc LICENSE.md THIRD-PARTY.md
%_libdir/libOpenImageIO.so.%{soname}
%_libdir/libOpenImageIO.so.%{soname}.*
%_libdir/libOpenImageIO_Util.so.%{soname}
%_libdir/libOpenImageIO_Util.so.%{soname}.*
%_libdir/OpenImageIO-%soname

%files -n python3-module-%oname
%python3_sitelibdir/OpenImageIO

%files -n %oname-utils
%_bindir/*
%_man1dir/*.1*
%ifnarch armh
%exclude %_bindir/iv
%exclude %_man1dir/iv.1*

%files -n %oname-iv
%_bindir/iv
%_man1dir/iv.1*
%endif

%files devel
%_libdir/libOpenImageIO.so
%_libdir/libOpenImageIO_Util.so
%_includedir/*
%_libdir/pkgconfig/OpenImageIO.pc
%_libdir/cmake/*

%changelog
* Thu Mar 23 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.3.21.0-alt2.1
- Patch for Elbrus.

* Mon Mar 20 2023 Alexander Burmatov <thatman@altlinux.org> 2.3.21.0-alt2
- Fix build requires.

* Mon Nov 28 2022 Ivan A. Melnikov <iv@altlinux.org> 2.3.21.0-alt1
- Updated to upstream version 2.3.21.0
  (fixes CVE-2022-36354, CVE-2022-41977, CVE-2022-41639, CVE-2022-41988)

* Wed Sep 14 2022 Ivan A. Melnikov <iv@altlinux.org> 2.3.19.0-alt1
- Updated to upstream version 2.3.19.0.

* Thu Feb 10 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.12.0-alt1
- Updated to upstream version 2.3.12.0.

* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.11.0-alt1
- Updated to upstream version 2.3.11.0.

* Thu Dec 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.10.1-alt1
- Updated to upstream version 2.3.10.1.

* Wed Sep 29 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.3.7.2-alt2
- E2K: enabled OpenCV, fixed issue with Clang

* Mon Sep 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.7.2-alt1
- Updated to upstream version 2.3.7.2.

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.17.0-alt1
- Updated to upstream version 2.2.17.0.

* Wed Jul 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.16.0-alt1
- Updated to upstream version 2.2.16.0.

* Thu Jun 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.15.1-alt1
- Updated to upstream version 2.2.15.1.

* Fri Jun 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.15.0-alt3
- Updated dependencies.
- Specified default plugin search path.

* Thu Jun 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.15.0-alt2
- Rebuilt with opencolorio-2.0.1.

* Wed Jun 02 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.15.0-alt1
- Updated to upstream version 2.2.15.0.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 2.2.13.1-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Apr 08 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.13.1-alt1
- Updated to upstream version 2.2.13.1.

* Mon Mar 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.12.0-alt1
- Updated to upstream version 2.2.12.0.

* Mon Feb 08 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.11.1-alt1
- Updated to upstream version 2.2.11.1.

* Tue Jan 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.10.1-alt1
- Updated to upstream version 2.2.10.1.

* Wed Dec 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.9.0-alt1
- Updated to upstream version 2.2.9.0.

* Wed Oct 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.7.0-alt1
- Updated to upstream version 2.2.7.0.

* Fri Sep 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.6.1-alt1
- Updated to upstream version 2.2.6.1.

* Thu Sep 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.18.1-alt2
- Updated conflicts (Closes: #38878).

* Thu Aug 13 2020 Michael Shigorin <mike@altlinux.org> 2.1.18.1-alt1.1
- E2K: fix build of this library's clients

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.18.1-alt1
- Updated to upstream version 2.1.18.1.

* Mon Jul 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.17.0-alt1
- Updated to upstream version 2.1.17.0.

* Thu Jun 25 2020 Michael Shigorin <mike@altlinux.org> 2.1.16.0-alt4
- E2K: don't miss %%optflags while working around SIMD issue
  (thx darktemplar@)

* Mon Jun 22 2020 Michael Shigorin <mike@altlinux.org> 2.1.16.0-alt3
- E2K: avoid BR: dcmtk, opencv for now (not available yet)

* Fri Jun 19 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.16.0-alt2
- fixed packaging on armh

* Thu Jun 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.16.0-alt1
- Updated to upstream version 2.1.16.0.

* Mon Apr 13 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.13.0-alt1
- Updated to upstream version 2.1.13.0.

* Thu Jul 25 2019 Ivan A. Melnikov <iv@altlinux.org> 2.0.9-alt2
- Link with libatomic on mipsel.

* Fri Jul 12 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.9-alt1
- Updated to upstream version 2.0.9.

* Mon May 27 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.8-alt1
- Updated to upstream version 2.0.8.

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 1.8.15-alt2
- rebuilt for libdcmtk14

* Tue Oct 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.15-alt1
- Initial build for ALT.

* Tue Oct 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.15-1
- Update to 1.8.15.

* Mon Sep 24 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.14-2
- Remove python2 module and replace with python3 module.

* Mon Sep 03 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.14-1
- Update to 1.8.14.

* Wed Jul 18 2018 Simone Caronni <negativo17@gmail.com> - 1.8.12-3
- Rebuild for LibRaw update.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.12-1
- Update to 1.8.12.

* Mon Apr 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.10-1
- Update to 1.8.10.

* Fri Mar 02 2018 Adam Williamson <awilliam@redhat.com> - 1.8.9-2
- Rebuild for opencv 3.4.1

* Thu Mar 01 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.9-1
- Update to 1.8.9

* Fri Feb 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.8.8-3
- Rebuild

* Tue Feb 13 2018 Sandro Mani <manisandro@gmail.com> - 1.8.8-2
- Rebuild (giflib)

* Fri Feb 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.8-1
- Update to 1.8.8.

* Thu Jan 18 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.7-3
- Add openjpeg2 to build dependencies.
- Re-enable dcmtk for 32bit arches.

* Sat Jan 13 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.7-2
- Rebuild for OpenColorIO 1.1.0.

* Wed Jan 03 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.7-1
- Update to latest upstream release.
- Disable building with dcmtk until fixed, see:
  https://github.com/OpenImageIO/oiio/issues/1841

* Thu Nov 02 2017 Richard Shaw <hobbes1069@gmail.com> - 1.8.6-1
- Update to latest upstream release.
- Add dcmtk to build to enable DICOM plugin.
