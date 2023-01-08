%define git %nil

Name: nvidia-vaapi-driver
Version: 0.0.8
Release: alt2

Summary: VA-API implementation that uses NVDEC as a backend
License: MIT/X11
Group: System/Libraries
Url: https://github.com/elFarto/nvidia-vaapi-driver

ExclusiveArch: %ix86 x86_64

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libva-devel gst-plugins-bad1.0-devel nv-codec-headers

# minimal requires from README
Requires: libnvcuvid >= 470.57.02-alt1

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
* Sun Jan 08 2023 L.A. Kostis <lakostis@altlinux.ru> 0.0.8-alt2
- Added dependency to libnvcuvid (closes #44841).

* Thu Dec 22 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.8-alt1
- 0.0.8.

* Sun Dec 11 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.7-alt5.ge2d256e
- GIT e2d256e.

* Thu Dec 08 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.7-alt4.gcd1f6a9
- GIT cd1f6a9.

* Thu Dec 01 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.7-alt3.g0a8c315
- GIT 0a8c315 (to fix https://github.com/elFarto/nvidia-vaapi-driver/issues/126).

* Mon Oct 24 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.7-alt2.g03d5a28
- GIT 03d5a28.

* Wed Oct 19 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.7-alt1
- v0.0.7.

* Wed Jul 13 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.6-alt2.ga4fb2d6
- v0.0.6-13-ga4fb2d6.

* Fri May 27 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.6-alt1.1
- Add ExclusiveArch.

* Fri May 27 2022 L.A. Kostis <lakostis@altlinux.ru> 0.0.6-alt1
- Initial build for ALTLinux.
