%define sover 0

Name:    libfreenect
Version: 0.7.5
Release: alt3

Summary: Drivers and libraries for the Xbox Kinect device
License: Apache-2.0
Group:   System/Libraries
Url:     https://github.com/OpenKinect/libfreenect
VCS:     https://github.com/OpenKinect/libfreenect.git

Source: %name-%version.tar
Patch: libfreenect-0.4.2-libdir.patch
Patch1: libfreenect-0.5.7-videogroup.patch
Patch2: libfreenect-openni2.patch
Patch3: secarch.patch
Patch4: libfreenect-python3-sitelib.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake gcc-c++
BuildRequires: libglvnd-devel libfreeglut-devel libopencv-devel libusb-devel
BuildRequires: python3-dev python3-module-distutils-extra python3-module-numpy
BuildRequires: python3-module-setuptools python3-module-Cython libnumpy-py3-devel
BuildRequires: rpm-build-python3
Requires: udev

%description
libfreenect is a userspace driver for the Microsoft Kinect.
It runs on Linux, OSX, and Windows and supports

RGB and Depth Images
Motors
Accelerometer
LED
Audio

%package -n %name%sover
Summary: Shared library for %name
Group:   System/Libraries
Conflicts: %name < 0.7.5-alt3

%description -n %name%sover
This package contains the shared library for %name.

%package devel
Summary: Development files for %name
Group:   Development/C++
Requires: %name%sover = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package utils
Summary: Example utilities for %name
Group:   Video

%description utils
This package contains example utilities and demos for libfreenect.

%package opencv
Summary: OpenCV bindings for %name
Group:   System/Libraries

%description opencv
The %name-opencv package contains the libfreenect binding
library for OpenCV development

%package fakenect
Summary: Library to play back recorded data for %name
Group:   System/Libraries

%description fakenect
Fakenect consists of a "record" program to save dumps from the kinect sensor
and a library that can be linked to, providing an interface compatible with
freenect.  This allows you to save data and repeat for experiments, debug
problems, share datasets, and experiment with the kinect without having one.

%package -n python3-module-%name
Summary: Python 3 bindings for %name
Group:   Development/Python3

%description -n python3-module-%name
The python3-module-%name package contains python 3 bindings for %name.

%package openni
Summary: OpenNI2 driver for the Kinect
Group:   System/Libraries

%description openni
The OpenNI2-FreenectDriver is a bridge to libfreenect implemented as an
OpenNI2 driver. It allows OpenNI2 to use Kinect hardware on Linux and OSX.
It was originally a separate project but is now distributed with libfreenect.

%prep
%setup
rm -rf platform/windows

%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
find -type f -exec grep -l '#!/usr/bin/env python' {} \; | \
    xargs sed -i 's|#!/usr/bin/env python|#!%__python3|g'

%cmake \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DPROJECT_INCLUDE_INSTALL_DIR=%_includedir \
    -DBUILD_AUDIO=ON \
    -DBUILD_C_SYNC=ON \
    -DBUILD_CV=ON \
    -DBUILD_REDIST_PACKAGE=ON \
    -DBUILD_EXAMPLES=ON \
    -DBUILD_FAKENECT=ON \
    -DBUILD_PYTHON=OFF  \
    -DBUILD_PYTHON2=OFF \
    -DBUILD_PYTHON3=ON \
    -DBUILD_OPENNI2_DRIVER=ON \
    -DOpenGL_GL_PREFERENCE=GLVND \
    -Wno-dev

%cmake_build

%install
%cmake_install

rm -f %buildroot%_libdir/libfreenect*.a

# Install the kinect udev rule
mkdir -p %buildroot%_udevrulesdir
mkdir -p %buildroot%_libdir/openni2
mkdir -p %buildroot%python3_sitelibdir
mkdir -p %buildroot%_datadir/%name
install -p -m 644 platform/linux/udev/51-kinect.rules \
    %buildroot%_udevrulesdir
mv %buildroot%_datadir/fwfetcher.py %buildroot%_bindir/freenect-fwfetcher

# Delete libtool archives
find %buildroot -name '*.la' -exec rm -f {} ';'

# Move openni plugin: rhbz#1094787
mv %buildroot%_libdir/OpenNI2-FreenectDriver \
    %buildroot%_libdir/openni2/Drivers

# Move cmake config to proper location
mkdir -p %buildroot%_datadir/cmake/Modules
mv %buildroot%_datadir/%name/libfreenectConfig.cmake \
    %buildroot%_datadir/cmake/Modules/

%files -n %name%sover
%_libdir/%name.so.%sover
%_libdir/%name.so.%sover.*
%_libdir/%{name}_sync.so.%sover
%_libdir/%{name}_sync.so.%sover.*

%files
%doc APACHE20 GPL2 README.md CONTRIB
%_udevrulesdir/51-kinect.rules

%files devel
%doc examples/*.c wrappers/cpp/cppview.cpp
%_includedir/libfreenect
%_libdir/libfreenect.so
%_libdir/libfreenect_sync.so
%_libdir/libfreenect_cv.so
%_libdir/pkgconfig/*
%_libdir/fakenect/*.so
%_datadir/cmake/Modules/libfreenectConfig.cmake

%files utils
%_bindir/freenect-camtest
%_bindir/freenect-chunkview
%_bindir/freenect-cpp_pcview
%_bindir/freenect-cppview
%_bindir/freenect-glpclview
%_bindir/freenect-glview
%_bindir/freenect-hiview
%_bindir/freenect-micview
%_bindir/freenect-regtest
%_bindir/freenect-regview
%_bindir/freenect-tiltdemo
%_bindir/freenect-wavrecord
%_bindir/freenect-fwfetcher

%files opencv
%_bindir/freenect-cvdemo
%_libdir/libfreenect_cv.so.*

%files fakenect
%_bindir/fakenect-record
%_bindir/fakenect
%dir %_libdir/fakenect/
%_libdir/fakenect/*.so.*
%_mandir/man1/fakenect*1.*

%files -n python3-module-%name
%python3_sitelibdir/freenect.so

%files openni
%dir %_libdir/openni2/
%dir %_libdir/openni2/Drivers/
%_libdir/openni2/Drivers/libFreenectDriver.so

%changelog
* Wed May 20 2026 Sergey Palcheh <minergenon@altlinux.org> 0.7.5-alt3
- split out libfreenect0 shared library package

* Tue May 19 2026 Sergey Palcheh <minergenon@altlinux.org> 0.7.5-alt2
- spec cleanup
- new libfreenect-utils package has been released
- added patch libfreenect-python3-sitelib.patch

* Wed Mar 05 2025 Sergey Palcheh <minergenon@altlinux.org> 0.7.5-alt1
- initial build for ALT Sisyphus
