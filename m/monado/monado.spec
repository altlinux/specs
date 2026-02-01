%set_verify_elf_method relaxed

%define soname 25 

Name:    monado
Version: 25.1.0
Release: alt2

Summary: Monado - XR Runtime (XRT)
License: BSL-1.0
Group:   Games/Other
Url:     https://gitlab.freedesktop.org/monado/monado
VCS:     https://gitlab.freedesktop.org/monado/monado

Source:  %name-%version.tar

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

%package -n lib%name%soname
Group: System/Libraries
Summary: %name library
%description -n lib%name%soname
%name library.

%prep
%setup

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
%doc CONTRIBUTING.md LICENSES README.md
%_bindir/%{name}*
%_libdir/libopenxr_monado.so
%_datadir/openxr
%_datadir/steamvr-monado
%_userunitdir/%name.*

%files devel
%_includedir/%name
%_libdir/libmonado.so

%files -n lib%name%soname
%_libdir/libmonado.so.%soname
%_libdir/libmonado.so.%{soname}.*

%changelog
* Sun Feb 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 25.1.0-alt2
- spec cleanup

* Wed Jan 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 25.1.0-alt1
- 25.0.0 -> 25.1.0

* Sun Jun 15 2025 Sergey Palcheh <minergenon@altlinux.org> 25.0.0-alt1
- initial build for ALT Sisyphus

