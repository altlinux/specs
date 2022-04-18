
%define sover 1
%define libnvidia_egl_gbm libnvidia-egl-gmb%sover

Name: egl-gbm
Version: 1.1.0
Release: alt1

Group: System/Libraries
Summary: GBM EGL External Platform library
Url: https://github.com/NVIDIA/egl-gbm
License: MIT

Source0: %name-%version.tar

BuildRequires: gcc meson
BuildRequires: eglexternalplatform-devel libEGL-devel
BuildRequires: libglvnd-devel libgbm-devel libdrm-devel

%description	
%summary

%package -n %libnvidia_egl_gbm
Summary: %summary
Group: System/Libraries
Provides: libnvidia-egl-gbm = %EVR
Provides: nvidia-egl-gbm = %EVR
%description -n %libnvidia_egl_gbm
%summary

%package devel
Group: Development/Other
Summary: GBM EGL External Platform library development package
%description devel
GBM EGL External Platform library development package.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files -n %libnvidia_egl_gbm
%doc COPYING
%_libdir/libnvidia-egl-gbm.so.%sover
%_libdir/libnvidia-egl-gbm.so.*

%changelog
* Thu Apr 14 2022 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- initial build

