%define soname 25 

Name:    monado
Version: 25.1.0
Release: alt4

Summary: Monado - XR Runtime (XRT)
License: BSL-1.0
Group:   Games/Other
Url:     https://gitlab.freedesktop.org/monado/monado
VCS:     https://gitlab.freedesktop.org/monado/monado

Source:  %name-%version.tar
Patch:   monado-25.1.0-steamvr-libdir.patch
Patch1:  monado-25.1.0-openxr-libdir.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: glslang python3-dev eigen3-devel libvulkan-devel glslc libhidapi-devel
BuildRequires: libbluez-devel libopenhmd-devel libopencv-devel libusb-devel
BuildRequires: libjpeg-devel librealsense-devel libSDL2-devel zlib-devel
BuildRequires: libcjson-devel libsystemd-devel libuvc-devel libudev-devel
BuildRequires: libXrandr-devel libXau-devel libXdmcp-devel libXext-devel
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel libffi-devel
BuildRequires: libpcre2-devel liborc-devel libsurvive-devel libopenvr-devel
BuildRequires: wayland-devel wayland-protocols libcap-devel
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
%patch -p1
%patch1 -p1

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

%cmake_build

%install
%cmake_install

%files
%doc CONTRIBUTING.md LICENSES README.md
%_bindir/%{name}*
%_libdir/monado/libopenxr_monado.so
%_datadir/openxr
%_libdir/steamvr-monado
%_userunitdir/%name.*

%files devel
%_includedir/%name
%_libdir/libmonado.so

%files -n lib%name%soname
%_libdir/libmonado.so.%soname
%_libdir/libmonado.so.%{soname}.*

%changelog
* Sat Jun 06 2026 Sergey Palcheh <minergenon@altlinux.org> 25.1.0-alt4
- rebuild with librealsense 2.58.1

* Tue May 19 2026 Sergey Palcheh <minergenon@altlinux.org> 25.1.0-alt3
- spec cleanup
- added patch monado-25.1.0-steamvr-libdir.patch
- added patch monado-25.1.0-openxr-libdir.patch

* Sun Feb 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 25.1.0-alt2
- spec cleanup

* Wed Jan 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 25.1.0-alt1
- 25.0.0 -> 25.1.0

* Sun Jun 15 2025 Sergey Palcheh <minergenon@altlinux.org> 25.0.0-alt1
- initial build for ALT Sisyphus

