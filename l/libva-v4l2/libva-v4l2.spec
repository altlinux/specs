Name: libva-v4l2
Version: 1.0.0
Release: alt1

Summary: VA-API driver backed by the Linux V4L2 stateful M2M interface

License: MIT
Group: System/Libraries
Url: https://github.com/radxa-pkg/libva-v4l2

# Source-url: https://github.com/radxa-pkg/libva-v4l2/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

Patch1: 0005-venus.patch
Patch2: 0007-packed-headers.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++
BuildRequires: pkgconfig(libva) >= 1.10
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2) >= 3.2
BuildRequires: pkgconfig(gbm)

%description
libva-v4l2 is a VA-API backend implemented on top of the Linux V4L2
stateful memory-to-memory decoder and encoder interface. It allows
applications using VA-API (FFmpeg, GStreamer, browsers) to use hardware
video codecs exposed by V4L2 M2M drivers, such as Qualcomm Venus and Iris
on Snapdragon platforms.

The driver is installed as v4l2_drv_video.so with an msm_drv_video.so
symlink, since libva falls back to the DRM driver name (msm) on Qualcomm
devices.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%_libdir/dri/v4l2_drv_video.so
%_libdir/dri/msm_drv_video.so
%doc %_datadir/doc/%name/README.md
%_datadir/licenses/%name/LICENSE

%changelog
* Wed Sep 23 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for Sisyphus
- add upstream patches for Venus support and packed headers
