%define _unpackaged_files_terminate_build 1

Name:          libva-v4l2_request
Version:       1.3
Release:       alt1

Summary: Video Acceleration (VA) API for Linux
License: GPL-3.0-or-later
Group:   System/Libraries
URL:     https://github.com/sofus13/libva-v4l2_request
VCS:     https://github.com/sofus13/libva-v4l2_request

Source: %name-%version.tar

ExclusiveArch: aarch64

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: libva-devel
BuildRequires: libdrm-devel

%description
This VA-API backend is designed to work with the Linux Video4Linux2
Request API that is used by a number of video codecs drivers, including
the Video Engine found in most Allwinner SoCs.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%_libdir/dri/v4l2_request_drv_video.so

%changelog
* Tue Sep 15 2026 Anton Osipov <radiolamp@altlinux.org> 1.3-alt1
- Initial build for ALT.
