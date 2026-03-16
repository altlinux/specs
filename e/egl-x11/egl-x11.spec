
%define sover 1
%define libnvidia_egl_x11 libnvidia-egl-x11_%sover

Name: egl-x11
Version: 1.0.5
Release: alt1

Group: System/Libraries
Summary: X11 EGL External Platform library
Url: https://github.com/NVIDIA/egl-x11
License: Apache-2.0

Source0: %name-%version.tar

BuildRequires: gcc meson
BuildRequires: eglexternalplatform-devel libEGL-devel
BuildRequires: libglvnd-devel libgbm-devel libdrm-devel
BuildRequires: pkgconfig(xcb) pkgconfig(xcb-dri3) pkgconfig(xcb-present)

%description
This is an EGL platform library for the NVIDIA driver to support XWayland via
xlib (using EGL_KHR_platform_x11) or xcb (using EGL_EXT_platform_xcb).

%package -n %libnvidia_egl_x11
Summary: %summary
Group: System/Libraries
Provides: libnvidia-egl-x11 = %EVR
Provides: nvidia-egl-x11 = %EVR
%description -n %libnvidia_egl_x11
This is an EGL platform library for the NVIDIA driver to support XWayland via
xlib (using EGL_KHR_platform_x11) or xcb (using EGL_EXT_platform_xcb).

%package devel
Group: Development/Other
Summary: X11 EGL External Platform library development package
%description devel
X11 EGL External Platform library development package.

%prep
%setup

%build
%meson \
  -D xcb=true \
  -D xlib=enabled \
  #
%meson_build

%install
%meson_install

%files -n %libnvidia_egl_x11
%doc LICENSE
%_libdir/libnvidia-egl-xlib.so.%sover
%_libdir/libnvidia-egl-xlib.so.*
%_libdir/libnvidia-egl-xcb.so.%sover
%_libdir/libnvidia-egl-xcb.so.*
%_datadir/egl/egl_external_platform.d/*_nvidia_x*.json

%changelog
* Mon Mar 16 2026 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt1
- new version

* Mon Jan 26 2026 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt1
- new version

* Thu Aug 21 2025 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- new version

* Fri Jun 27 2025 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- new version

* Fri May 23 2025 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- new version

* Tue Mar 04 2025 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- initial build
