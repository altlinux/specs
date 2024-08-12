
%define sover 1
%define libnvidia_egl_wayland libnvidia-egl-wayland%sover

Name: egl-wayland
Version: 1.1.15
Release: alt1
Epoch: 1

Group: System/Libraries
Summary: Wayland EGL External Platform library
Url: https://github.com/NVIDIA/egl-wayland
License: MIT

Source0: %name-%version.tar
Source1: 10_nvidia_wayland.json
Source2: 15_nvidia_gbm.json
# ALT
Patch1: alt-ftbfs.patch
Patch2: alt-wlEglInitializeSurfaceExport.patch

# Automatically added by buildreq on Fri Jul 12 2019 (-bi)
# optimized out: elfutils glibc-devel-static glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libstdc++-devel libwayland-client libwayland-client-devel libwayland-server perl pkg-config python-base python-modules python3 python3-base python3-dev rpm-build-python3 sh4 wayland-devel xorg-proto-devel
#BuildRequires: eglexternalplatform-devel gcc-c++ libEGL-devel libstdc++-devel-static libwayland-egl-devel libwayland-server-devel python3-module-mpl_toolkits
BuildRequires: autoconf-archive
BuildRequires: eglexternalplatform-devel libEGL-devel libdrm-devel
BuildRequires: libwayland-egl-devel libwayland-server-devel libwayland-client-devel wayland-devel wayland-protocols

%description
%summary

%package -n %libnvidia_egl_wayland
Summary: %summary
Group: System/Libraries
Provides: libnvidia-egl-wayland = %version-%release
Provides: nvidia-egl-wayland = %version-%release
%description -n %libnvidia_egl_wayland
%summary

%package devel
Group: Development/Other
Summary: Wayland EGL External Platform library development package
%description devel
Wayland EGL External Platform library development package

%prep
%setup
%patch1 -p1
%patch2 -p1
%autoreconf

%build
%ifarch %e2k
# lcc barfs on include/wayland-eglstream-server.h:87
%add_optflags -Wno-error=signed-one-bit-field -Wno-error=maybe-uninitialized
%endif
%configure
%make_build

%install
%makeinstall_std
install -pDm644 %SOURCE1 \
	%buildroot/%_datadir/egl/egl_external_platform.d/10_nvidia_wayland.json
install -pDm644 %SOURCE2 \
	%buildroot/%_datadir/egl/egl_external_platform.d/15_nvidia_gbm.json

%files -n %libnvidia_egl_wayland
%doc README.md COPYING
%_libdir/libnvidia-egl-wayland.so.%sover
%_libdir/libnvidia-egl-wayland.so.*
%_datadir/egl/egl_external_platform.d/*_nvidia_*.json

%files devel
%_libdir/lib*.so
%_datadir/pkgconfig/wayland-eglstream*.pc
%_datadir/wayland-eglstream/

%changelog
* Mon Aug 12 2024 Sergey V Turchin <zerg@altlinux.org> 1:1.1.15-alt1
- new version

* Wed Nov 01 2023 Sergey V Turchin <zerg@altlinux.org> 1:1.1.13-alt1
- new version

* Wed Jul 26 2023 Sergey V Turchin <zerg@altlinux.org> 1:1.1.12-alt2
- add upstream fixes

* Wed Jul 19 2023 Sergey V Turchin <zerg@altlinux.org> 1:1.1.12-alt1
- new version

* Tue Oct 25 2022 Sergey V Turchin <zerg@altlinux.org> 1:1.1.11-alt1
- new version

* Fri Jul 08 2022 Sergey V Turchin <zerg@altlinux.org> 1:1.1.10-alt1
- new version

* Wed Dec 29 2021 Sergey V Turchin <zerg@altlinux.org> 1:1.1.9-alt3
- package icd for gbm provider

* Tue Dec 28 2021 Sergey V Turchin <zerg@altlinux.org> 1:1.1.9-alt2
- add upstream fixes from master branch

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 1:1.1.9-alt1
- new version

* Mon Sep 27 2021 Sergey V Turchin <zerg@altlinux.org> 1:1.1.8-alt1
- new version

* Fri May 14 2021 Sergey V Turchin <zerg@altlinux.org> 1:1.1.7-alt1
- new version

* Thu Apr 15 2021 Michael Shigorin <mike@altlinux.org> 1:1.1.6-alt1.2
- E2K: *workaround* ftbfs with lcc

* Thu Apr 15 2021 Michael Shigorin <mike@altlinux.org> 1:1.1.6-alt1.1
- E2K: workaround ftbfs with lcc
- minor spec cleanup

* Wed Mar 03 2021 Sergey V Turchin <zerg@altlinux.org> 1:1.1.6-alt1
- new version

* Tue Sep 22 2020 Sergey V Turchin <zerg@altlinux.org> 1:1.1.5-alt1
- new version

* Tue Nov 26 2019 Sergey V Turchin <zerg@altlinux.org> 1:1.1.4-alt3
- upstream tag 1.1.4 updated

* Tue Nov 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:1.1.4-alt2
- fix to build with new Mesa

* Wed Oct 09 2019 Sergey V Turchin <zerg@altlinux.org> 1:1.1.4-alt1
- new version

* Fri Jul 12 2019 Sergey V Turchin <zerg@altlinux.org> 1:1.1.3-alt1
- initial build

