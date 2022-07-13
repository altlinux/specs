%define git a4fb2d6

Name: nvidia-vaapi-driver
Version: 0.0.6
Release: alt2.g%{git}

Summary: VA-API implementation that uses NVDEC as a backend
License: MIT/X11
Group: System/Libraries
Url: https://github.com/elFarto/nvidia-vaapi-driver

ExclusiveArch: %ix86 x86_64

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libva-devel gst-plugins-bad1.0-devel nv-codec-headers

# just to make sure
Conflicts: libva-driver-vdpau

%description
This is an VA-API implementation that uses NVDEC as a backend. This
implementation is specifically designed to be used by Firefox for accelerated
decode of web content, and may not operate correctly in other applications.

This library requires that the nvidia_drm kernel module is configured with the
parameter nvidia-drm.modeset=1

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md COPYING
%_libdir/dri/nvidia_drv_video.so

%changelog
* Wed Jul 13 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.6-alt2.ga4fb2d6
- v0.0.6-13-ga4fb2d6.

* Fri May 27 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.6-alt1.1
- Add ExclusiveArch.

* Fri May 27 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.6-alt1
- Initial build for ALTLinux.
