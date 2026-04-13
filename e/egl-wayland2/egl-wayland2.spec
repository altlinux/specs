
%define sover 1
%define libnvidia_egl_wayland libnvidia-egl-wayland2_%sover

Name: egl-wayland2
Version: 1.0.1
Release: alt1

Group: System/Libraries
Summary: Dma-buf-based Wayland external platform library
Url: https://github.com/NVIDIA/egl-wayland2
Vcs: https://github.com/NVIDIA/egl-wayland2
# src/wayland/dma-buf.h is GPL 2, rest is Apache 2.0
License: Apache-2.0 and GPL-2.0

Source0: %name-%version.tar

BuildRequires: meson ninja-build
BuildRequires: eglexternalplatform-devel libEGL-devel libdrm-devel libgbm-devel
BuildRequires: libwayland-egl-devel libwayland-client-devel wayland-devel wayland-protocols

%description
%summary

%package -n %libnvidia_egl_wayland
Summary: %summary
Group: System/Libraries
Provides: libnvidia-egl-wayland2 = %version-%release
Provides: nvidia-egl-wayland2 = %version-%release
%description -n %libnvidia_egl_wayland
%summary

%package devel
Group: Development/Other
Summary: Wayland EGL External Platform library development package
%description devel
Wayland EGL External Platform library development package

%prep
%setup

%build
%ifarch %e2k
# lcc barfs on include/wayland-eglstream-server.h:87
%add_optflags -Wno-error=signed-one-bit-field -Wno-error=maybe-uninitialized
%endif
%meson
%meson_build

%install
%meson_install

%files -n %libnvidia_egl_wayland
%doc README.md LICENSE
%_libdir/libnvidia-egl-wayland2.so.%sover
%_libdir/libnvidia-egl-wayland2.so.*
%_datadir/egl/egl_external_platform.d/*_nvidia_*.json

#%files devel
#%_libdir/lib*.so
#%_datadir/pkgconfig/wayland-eglstream*.pc
#%_datadir/wayland-eglstream/

%changelog
* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- initial build
