# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: obs-studio-plugin-input-overlay
Summary: Show keyboard, gamepad and mouse input on stream (plugin for OBS studio)
Version: 5.1.3
Release: alt1
License: GPL-2.0
Group: Video
URL: https://github.com/univrsal/input-overlay
VCS: https://github.com/univrsal/input-overlay

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

ExcludeArch: ppc64le

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libobs-devel
BuildRequires: libSDL3-devel
BuildRequires: extra-cmake-modules
BuildRequires: libinput-devel
BuildRequires: libXtst-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXt-devel
BuildRequires: libXrandr-devel
BuildRequires: libwayland-client-devel
BuildRequires: wayland-protocols
BuildRequires: qt6-base-devel

Requires: obs-studio-base

%description
%summary.

%prep
%setup
%patch0 -p1
rmdir deps/libuiohook
mv libuiohook deps/ 

%build
%cmake -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%_datadir/obs/obs-modules/plugins/input-overlay/
%_libdir/obs-modules/plugins/input-overlay.so
%dir %_libdir/input-overlay
%_libdir/input-overlay/libuiohook.so
%_libdir/input-overlay/libuiohook-x11.so
%_libdir/input-overlay/libuiohook-wayland.so
%_libdir/input-overlay/libuiohook-xrecord.so

%changelog
* Tue Nov 03 2026 Evgeniy Serov <scala@altlinux.org> 5.1.3-alt1
- New version 5.1.3.

* Wed Aug 14 2024 Ivan A. Melnikov <iv@altlinux.org> 5.0.5-alt2
- Fix fbtbfs on loongarch64 (thx k0tran@).

* Mon Mar 18 2024 Anton Midyukov <antohami@altlinux.org> 5.0.5-alt1
- new version 5.0.5

* Mon Aug 21 2023 Anton Midyukov <antohami@altlinux.org> 5.0.4-alt1
- initial build (Closes: 47310)
