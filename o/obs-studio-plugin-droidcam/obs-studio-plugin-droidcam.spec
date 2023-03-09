%define git %nil

Name: obs-studio-plugin-droidcam
Summary: Droidcam plugin for OBS studio
Version: 2.0.1
Release: alt1
License: GPLv2
Group: Video
Url: https://github.com/dev47apps/droidcam-obs-plugin

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libturbojpeg-devel libusbmuxd-devel libimobiledevice-devel
BuildRequires: libobs-devel >= 24.0

Requires: obs-studio-base

%description
The new 'DroidCam OBS' app + plugin let you connect to your phone and get high
quality audio & video just like a regular camera source. And you can connect as
many devices as you want, over WiFi or USB!

%prep
%setup
%patch -p1

%build
mkdir build
%ifarch ppc64le
OPTFLAGS="%optflags %optflags_shared -DNO_WARN_X86_INTRINSICS -mvsx" \
%else
OPTFLAGS="%optflags %optflags_shared" \
%endif
ALLOW_STATIC=no %make_build

%install
mkdir -p %buildroot{%_libdir/obs-plugins,%_datadir/obs/obs-plugins/droidcam-obs}
install -m644 build/droidcam-obs.so %buildroot%_libdir/obs-plugins/
cp -ar data/locale %buildroot%_datadir/obs/obs-plugins/droidcam-obs/

%files
%_libdir/obs-plugins/droidcam-obs.so
%_datadir/obs/obs-plugins/droidcam-obs/

%changelog
* Thu Mar 09 2023 L.A. Kostis <lakostis@altlinux.ru> 2.0.1-alt1
- 2.0.1.

* Thu Dec 29 2022 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt1
- 2.0.0.

* Sun Jan 30 2022 L.A. Kostis <lakostis@altlinux.ru> 1.3-alt1
- 1.3.

* Thu Dec 10 2020 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt2.gc9ca053.1
- Extend ppc64 build flags (libobs knows how to handle them).

* Wed Dec 09 2020 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt2.gc9ca053
- Fix build on ppc64le.

* Wed Dec 09 2020 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt1.gc9ca053
- GIT gc9ca053.
- Initial build for Sisyphus.
