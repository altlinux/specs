%define _unpackaged_files_terminate_build 1

Name:    librealsense
Version: 2.58.2
Release: alt1

Summary: Cross-platform camera capture for Intel RealSense
License: Apache-2.0
Group:   System/Libraries
URL:     https://github.com/realsenseai/librealsense
VCS:     https://github.com/realsenseai/librealsense.git

Source0: %name-%version.tar
Source1: realsense-viewer.desktop

Patch0:  presets_path.patch
Patch1:  disable-pedantic.patch
Patch2:  librealsense.use-system-yaml-cpp.patch
Patch3:  librealsense.use-system-json.patch
Patch4:  librealsense.use-system-pybind11.patch
Patch5:  librealsense.realsense-file-fixes.patch
Patch6:  librealsense.rsutils-shared-library.patch
Patch7:  librealsense.use-system-fastcdr.patch
Patch8:  librealsense.use-system-sqlite3.patch
Patch9:  librealsense.fix-zstd-qsort.patch
Patch10: librealsense.fix-pybind11-keepalive.patch
Patch11: librealsense.fix-easylogging-visibility.patch
Patch12: librealsense.fix-cxx14-all.patch
Patch13: librealsense.fix-fastcdr-v2-api.patch

BuildRequires(pre): rpm-build-python3 rpm-macros-python3 rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libglfw3-devel libusb-devel libudev-devel libGL-devel libGLU-devel
BuildRequires: python3-dev python3-module-setuptools pybind11-devel libcap-devel
BuildRequires: nlohmann-json-devel doxygen libyaml-cpp-devel libsqlite3-devel
BuildRequires: fast-cdr-devel
Provides: librealsense2 = %EVR

%description
Intel RealSense SDK.
The SDK allows depth and color streaming, and provides intrinsic and extrinsic
calibration information. The library also offers synthetic streams (pointcloud,
depth aligned to color and vise-versa), and a built-in support for record and
playback of streaming sessions.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR
Provides: librealsense2-devel = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n python3-module-%name
Summary: Python bindings for %name
Group: System/Libraries
Provides: python3-module-librealsense2 = %EVR

%description -n python3-module-%name
The python3-module-%name package contains python bindings for %name.

%package -n python3-module-%name-devel
Summary: Python development files for %name
Group: System/Libraries
Requires: python3-module-%name =  %EVR
Provides: python3-librealsense2-devel = %EVR

%description -n python3-module-%name-devel
The python3-%name-devel package contains libraries and header files for
developing python applications that use %name.

%package doc
BuildArch: noarch
Summary: Documentation for %name
Group: Development/Documentation
Provides: librealsense2-doc = %EVR

%description doc
The %name-doc package contains documentation for developing applications
with %name.

%prep
%setup
%autopatch -p1

%build
%cmake \
  -DBUILD_UNIT_TESTS=NO \
  -DCHECK_FOR_UPDATES=NO \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_BINDIR=%_bindir \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DCMAKE_INSTALL_INCLUDEDIR=%_includedir \
  -DBUILD_PYTHON_BINDINGS:bool=true \
  -DCMAKE_C_FLAGS="%optflags -ffat-lto-objects" \
  -DCMAKE_CXX_FLAGS="%optflags -ffat-lto-objects" \
  -Wno-dev

%cmake_build

sed -i "s:/usr/local/bin:%_datadir/realsense:" config/*
sed -i "s/plugdev/users/g" config/*rules

pushd doc/doxygen
# Do not generate Windows help files
sed -i \
  -e "s/GENERATE_HTMLHELP[[:space:]]*=[[:space:]]*YES/GENERATE_HTMLHELP = NO/" \
  doxyfile
doxygen
popd

%install
%cmake_install
mkdir -p %buildroot/%_udevrulesdir
install -p -m644 config/99-realsense-libusb.rules %buildroot%_udevrulesdir

mkdir -p %buildroot/%_datadir/realsense
install -p -m755 config/usb-R200-in{,_udev} %buildroot%_datadir/realsense

install -Dm644 common/res/icon_512.png %buildroot%_datadir/pixmaps/realsense-viewer.png

install -Dm644 %SOURCE1 %buildroot%_desktopdir/realsense-viewer.desktop

%files
%doc LICENSE readme.md
%_bindir/realsense-viewer
%_bindir/rs-align
%_bindir/rs-align-advanced
%_bindir/rs-align-gl
%_bindir/rs-benchmark
%_bindir/rs-callback
%_bindir/rs-capture
%_bindir/rs-color
%_bindir/rs-convert
%_bindir/rs-data-collect
%_bindir/rs-depth
%_bindir/rs-depth-quality
%_bindir/rs-distance
%_bindir/rs-embed
%_bindir/rs-embedded-filters
%_bindir/rs-eth-config
%_bindir/rs-enumerate-devices
%_bindir/rs-infrared
%_bindir/rs-labeled-pointcloud
%_bindir/rs-on-chip-calib
%_bindir/rs-object-detection
%_bindir/rs-fw-logger
%_bindir/rs-fw-update
%_bindir/rs-gl
%_bindir/rs-hdr
%_bindir/rs-hello-realsense
%_bindir/rs-measure
%_bindir/rs-motion
%_bindir/rs-multicam
%_bindir/rs-pointcloud
%_bindir/rs-post-processing
%_bindir/rs-record
%_bindir/rs-record-playback
%_bindir/rs-rosbag-inspector
%_bindir/rs-save-to-disk
%_bindir/rs-sensor-control
%_bindir/rs-software-device
%_bindir/rs-terminal
%dir %_datadir/librealsense2
%_datadir/librealsense2/presets
%_datadir/pixmaps/realsense-viewer.png
%_libdir/librealsense2-gl.so.*
%_libdir/librealsense2.so.*
%_libdir/librealsense-file.so.*
%_libdir/librsutils.so.*
%_datadir/realsense
%_desktopdir/realsense-viewer.desktop
%_udevrulesdir/99-realsense-libusb.rules

%files devel
%_includedir/librealsense2
%_includedir/librealsense2-gl
%_libdir/librsutils.so
%_libdir/cmake/realsense2
%_libdir/cmake/realsense2-gl
%_libdir/librealsense-file.so
%_libdir/librealsense2-gl.so
%_libdir/librealsense2.so
%_libdir/pkgconfig/realsense2-gl.pc
%_libdir/pkgconfig/realsense2.pc
%_libdir/librs_lz4.a

%files -n python3-module-%name
%dir %python3_sitelibdir/pyrealsense2/
%python3_sitelibdir/pyrealsense2/__init__.py
%python3_sitelibdir/pyrealsense2/__pycache__/
%python3_sitelibdir/pyrealsense2/pyrealsense2*.so
%python3_sitelibdir/pyrealsense2/pyrealsense2*.so.*
%python3_sitelibdir/pyrealsense2/pyrsutils*.so
%python3_sitelibdir/pyrealsense2/pyrsutils*.so.*

%files -n python3-module-%name-devel
%_libdir/cmake/pyrealsense2

%files doc
%doc LICENSE doc/doxygen/html/*

%changelog
* Wed Jun 17 2026 Sergey Palcheh <minergenon@altlinux.org> 2.58.2-alt1
- new version 2.58.2
- fix rsutils shared library patch for upstream 2.58.2

* Sun May 31 2026 Sergey Palcheh <minergenon@altlinux.org> 2.58.1-alt1
- new version 2.58.1
- use system packages instead of bundled: yaml-cpp, nlohmann-json, pybind11,
  sqlite3, fastcdr
- fix fastcdr v2 API compatibility (ros2 reader/writer, ros2-msg-types)
- fix pybind11 keep_alive incompatibility with v3.0.2
- fix easylogging++ visibility for librsutils ELF verification
- fix zstd qsort_r compatibility (use qsort for glibc)
- fix C++14 requirement (auto in lambdas) for tools/examples

* Wed Jan 15 2025 Sergey Palcheh <minergenon@altlinux.org> 2.56.3-alt1
- initial build for ALT Sisyphus

