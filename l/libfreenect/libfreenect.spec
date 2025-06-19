Name:    libfreenect
Version: 0.7.5
Release: alt1

Summary: Drivers and libraries for the Xbox Kinect device
License: Apache-2.0
Group:   Other
Url:     https://github.com/OpenKinect/libfreenect
VCS:     https://github.com/OpenKinect/libfreenect.git

Source: %name-%version.tar
Patch: libfreenect-0.4.2-libdir.patch
Patch1: libfreenect-0.5.7-videogroup.patch
Patch2: libfreenect-openni2.patch
Patch3: secarch.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake gcc-c++
BuildRequires: libglvnd-devel libfreeglut-devel libopencv-devel libusb-devel
BuildRequires: python3-dev python3-module-distutils-extra python3-module-numpy
BuildRequires: python3-module-setuptools python3-module-Cython libnumpy-py3-devel
Requires: udev

ExclusiveArch: x86_64

%description
libfreenect is a userspace driver for the Microsoft Kinect.
It runs on Linux, OSX, and Windows and supports

RGB and Depth Images
Motors
Accelerometer
LED
Audio

%package devel
Summary: Development files for %name
Group:   Development/C++

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package fakenect
Summary: Library to play back recorded data for %name
Group:   Development/C++
Requires: %name = %EVR

%description fakenect
Fakenect consists of a "record" program to save dumps from the kinect sensor
and a library that can be linked to, providing an interface compatible with
freenect.  This allows you to save data and repeat for experiments, debug
problems, share datasets, and experiment with the kinect without having one.

%package opencv
Summary: OpenCV bindings for %name
Group:   Development/C++
Requires: %name = %EVR

%description opencv
The %name-opencv package contains the libfreenect binding
library for OpenCV development.

%package -n python3-module-%name
Summary: Python 3 bindings for %name
Group:   Development/Python3
Requires: %name = %EVR
Requires: python3-module-numpy

%description -n python3-module-%name
The %name-python package contains python 3 bindings for %name

%package openni
Summary: OpenNI2 driver for the Kinect
Group:   Development/C++

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

%build
find -type f -exec grep -l '#!/usr/bin/env python' {} \; | xargs sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|g'

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
%cmakeinstall_std

rm -f %buildroot%_libdir/libfreenect*.a

# Install the kinect udev rule
mkdir -p %buildroot%_udevrulesdir
mkdir -p %buildroot%_libdir/openni2
mkdir -p %buildroot%python3_sitelibdir
install -p -m 644 platform/linux/udev/51-kinect.rules %buildroot%_udevrulesdir

# Delete libtool archives
find %buildroot -name '*.la' -exec rm -f {} ';'

# Move openni plugin: rhbz#1094787
mv %buildroot%_libdir/OpenNI2-FreenectDriver %buildroot%_libdir/openni2/Drivers

mv %buildroot/usr/lib/python3/site-packages/freenect.so %buildroot%python3_sitelibdir

%files
%doc APACHE20 GPL2 README.md CONTRIB
%_libdir/libfreenect.so.0*
%_libdir/libfreenect_sync.so.0*
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
%_datadir/%name
%_udevrulesdir/51-kinect.rules

%files devel
%doc examples/*.c wrappers/cpp/cppview.cpp
%_includedir/libfreenect
%_libdir/*.so
%_libdir/pkgconfig/*
%_libdir/fakenect/*.so

%files fakenect
%_bindir/fakenect-record
%dir %_libdir/fakenect/
%_libdir/fakenect/*.so.*
%_bindir/fakenect
%_datadir/fwfetcher.py
%_mandir/man1/fakenect*1.*

%files opencv
%_bindir/freenect-cvdemo
%_libdir/libfreenect_cv.so.*

%files -n python3-module-%name
%python3_sitelibdir/freenect.so

%files openni
%dir %_libdir/openni2/
%dir %_libdir/openni2/Drivers/
%_libdir/openni2/Drivers/libFreenectDriver.so

%changelog
* Wed Mar 05 2025 Sergey Palcheh <minergenon@altlinux.org> 0.7.5-alt1
- initial build for ALT Sisyphus

