Name:    OrbbecSDK_v2
Version: 2.8.7
Release: alt1

Summary: Software development kit for Orbbec 3D depth cameras and LiDARs
License: MIT
Group:   System/Libraries
URL:     https://www.orbbec.com
VCS:     https://github.com/orbbec/OrbbecSDK_v2

Source: %name-%version.tar
Patch0: OrbbecSDK_v2-2.8.7-fix-libdir.patch
Patch1: OrbbecSDK_v2-2.8.7-fix-rpath.patch
Patch2: OrbbecSDK_v2-2.8.7-fix-threads.patch
Patch3: OrbbecSDK_v2-2.8.7-fix-arch-detect.patch

# Prebuilt extension libraries are provided only for x86_64 and arm64.
ExcludeArch: i586 %arm

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ patchelf
BuildRequires: doxygen libopencv-devel libEGL-devel libGL-devel
BuildRequires: udev

Requires: udev

# Prebuilt extension libraries contain no debug information.
%add_debuginfo_skiplist %_libdir/extensions

%description
OrbbecSDK_v2 is the official software development kit for Orbbec 3D depth
cameras and LiDAR devices (Femto Bolt, Femto Mega, Gemini series, Astra 2,
Pulsar and others). It provides the core runtime libraries, udev rules and
prebuilt extension modules required to enumerate, configure and stream data
from Orbbec devices on Linux.

%package devel
Summary: Development files for OrbbecSDK_v2
Group:   Development/C++
Requires: %name = %EVR

%description devel
This package contains the C/C++ headers and CMake configuration files needed
to build applications against OrbbecSDK_v2.

%package tools
Summary: Command-line tools for OrbbecSDK_v2 devices
Group:   System/Configuration/Hardware
Requires: %name = %EVR

%description tools
This package contains command-line utilities for OrbbecSDK_v2 devices:
  - ob_benchmark: measure depth/color stream latency;
  - ob_multi_devices_firmware_update: update firmware on multiple devices.

%package examples
Summary: Example source code for OrbbecSDK_v2
Group:   Development/Documentation
ExcludeArch: i586 %arm
Requires: %name-devel = %EVR

%description examples
This package contains source code examples demonstrating how to use the
OrbbecSDK_v2 API for device enumeration, stream acquisition, post-processing,
multi-device synchronization and other tasks.

%package doc
Summary: API documentation for OrbbecSDK_v2
Group:   Development/Documentation
BuildArch: noarch

%description doc
This package contains the Doxygen-generated API reference documentation for
OrbbecSDK_v2.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake \
    -DOB_BUILD_EXAMPLES=OFF \
    -DOB_ENABLE_BOLT_OPENGL_COMPAT=ON \
    -DCMAKE_INSTALL_RPATH="" \
    -DOB_INSTALL_FILTER_DEV_HEADERS=ON

%cmake_build

%install
%cmake_install

# Remove hardcoded build-tree RUNPATH from prebuilt extension libraries and strip
# them (they ship with no .debug sections, so stripping silences both the
# debuginfo and the eu-elflint warnings).
for f in %buildroot%_libdir/extensions/*/*.so; do
    [ -f "$f" ] || continue
    patchelf --remove-rpath "$f" || true
    strip --strip-unneeded "$f" || true
done

# Make sure the main library and the shipped tools also have no RUNPATH
for f in %buildroot%_libdir/libOrbbecSDK.so.* %buildroot%_bindir/ob_*; do
    [ -f "$f" ] || continue
    patchelf --remove-rpath "$f" || true
done

# Move udev rules to the proper system location and drop upstream helpers
# that are meaningless in a system package.
mkdir -p %buildroot%_udev_rulesdir
mv %buildroot/usr/shared/99-obsensor-libusb.rules %buildroot%_udev_rulesdir/
rm -f %buildroot/usr/shared/install_udev_rules.sh
rm -f %buildroot/usr/setup.sh

# The SDK already installs runtime configs into %%_libdir; remove duplicates
# from the non-standard /usr/shared location.
rm -f %buildroot/usr/shared/OrbbecSDKConfig.xml
rm -f %buildroot/usr/shared/OrbbecSDKConfig.md
rmdir %buildroot/usr/shared >/dev/null 2>&1 || true

# Move documentation and examples to FHS locations.
mkdir -p %buildroot%_docdir/%name
mv %buildroot/usr/shared/doc/api %buildroot%_docdir/%name/
rmdir %buildroot/usr/shared/doc >/dev/null 2>&1 || true
rmdir %buildroot/usr/shared >/dev/null 2>&1 || true

mkdir -p %buildroot%_datadir/%name
mv %buildroot/usr/examples %buildroot%_datadir/%name/
# Upstream helper is Debian/Ubuntu-specific (apt-get/sudo/dpkg), not useful in ALT
rm -f %buildroot/usr/build_examples.sh
rmdir %buildroot/usr/examples >/dev/null 2>&1 || true

%files
%doc LICENSE.txt README.md LiDAR_README.md
%_udev_rulesdir/99-obsensor-libusb.rules
%_libdir/libOrbbecSDK.so.*
%_libdir/extensions/
%_libdir/OrbbecSDKConfig.xml
%_libdir/OrbbecSDKConfig.md

%files devel
%_includedir/libobsensor/
%_libdir/libOrbbecSDK.so
%_libdir/OrbbecSDKConfig.cmake
%_libdir/OrbbecSDKConfig-release.cmake
%_libdir/OrbbecSDKVersion.cmake

%files tools
%_bindir/ob_benchmark
%_bindir/ob_multi_devices_firmware_update

%files examples
%dir %_datadir/%name
%_datadir/%name/examples/

%files doc
%dir %_docdir/%name
%_docdir/%name/api/

%changelog
* Sat Jun 27 2026 Sergey Palcheh <minergenon@altlinux.org> 2.8.7-alt1
- initial build for ALT Sisyphus

