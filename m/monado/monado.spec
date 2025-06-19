%set_verify_elf_method relaxed

Name:    monado
Version: 25.0.0
Release: alt1

Summary: Monado - XR Runtime (XRT)
License: BSL-1.0
Group:   Games/Other
Url:     https://gitlab.freedesktop.org/monado/monado
VCS:     https://gitlab.freedesktop.org/monado/monado.git

Source:  %name-%version.tar
Patch:  fix-compilation-on-latest-vulkan-headers.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake gcc-c++
BuildRequires: glslang python3-dev eigen3 libvulkan-devel glslc libhidapi-devel
BuildRequires: libbluez-devel libopenhmd-devel libopencv-devel libusb-devel
BuildRequires: libjpeg-devel librealsense-devel libSDL2-devel zlib-devel
BuildRequires: libcjson-devel libsystemd-devel libuvc-devel libudev-devel
BuildRequires: libXrandr-devel libXau-devel libXdmcp-devel libXext-devel
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel libffi-devel
BuildRequires: libpcre2-devel liborc-devel libsurvive-devel libopenvr-devel
BuildRequires: wayland-devel wayland-protocols
BuildRequires: doxygen graphviz
# Missing dependencies for the build.
# depthai  LeapV2 LeapSDK ONNXRuntime Percetto
Requires: libopenhmd
Requires: librealsense
Requires: libsurvive

ExclusiveArch: x86_64

%description
Monado is an open source XR runtime delivering immersive experiences such as
VR and AR on mobile, PC/desktop, and any other device (because gosh darn people
come up with a lot of weird hardware). Monado aims to be a complete and conforming
implementation of the OpenXR API made by Khronos.

%package devel
Summary: Header files for monado
Group: Development/C
Requires: %name = %EVR

%description devel
Development files for the Monado OpenXR runtime.

%prep
%setup
%patch -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DXRT_BUILD_DRIVER_STEAMVR_LIGHTHOUSE=ON \
    -DXRT_HAVE_WAYLAND:BOOL=ON \
    -DXRT_HAVE_WAYLAND_DIRECT:BOOL=ON \
    -DXRT_HAVE_VULKAN:BOOL=ON \
    -DDRIVER_HANDTRACKING:BOOL=ON \
    -DBUILD_DOC:BOOL=OFF \
    -Wno-dev

%install
%cmakeinstall_std

%files
%doc CONTRIBUTING.md LICENSE README.md
%_bindir/monado-cli
%_bindir/monado-ctl
%_bindir/monado-service
%_bindir/monado-gui
%_libdir/libmonado.so.*
%_libdir/libopenxr_monado.so
%dir %_datadir/openxr/
%_datadir/openxr/
%dir %_datadir/steamvr-monado/
%_datadir/steamvr-monado/
%_userunitdir/monado.service
%_userunitdir/monado.socket

%files devel
%doc LICENSE README.md
%dir %_includedir/%name
%_includedir/%name/
%_libdir/libmonado.so

%changelog
* Sun Jun 15 2025 Sergey Palcheh <minergenon@altlinux.org> 25.0.0-alt1
- initial build for ALT Sisyphus

