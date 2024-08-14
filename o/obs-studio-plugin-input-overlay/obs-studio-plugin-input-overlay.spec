# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: obs-studio-plugin-input-overlay
Summary: Show keyboard, gamepad and mouse input on stream (plugin for OBS studio)
Version: 5.0.5
Release: alt2
License: GPL-2.0
Group: Video
Url: https://github.com/univrsal/input-overlay

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: obs-studio-plugin-input-overlay-5.0.5-alt-add-sdl-disable-lsx-flag.patch

ExcludeArch: ppc64le

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libobs-devel
BuildRequires: libXtst-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbfile-devel
BuildRequires: libXt-devel
BuildRequires: libXinerama-devel
BuildRequires: qt6-base-devel
BuildRequires: libSDL2-devel

Requires: obs-studio-base

%description
%summary.

%prep
%setup
%patch0 -p1
%patch1 -p1
rmdir deps/libuiohook
mv libuiohook deps/ 

%build
%add_optflags
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_libdir/obs-plugins %buildroot%_datadir/obs/obs-plugins
mv %buildroot/usr/data/obs-plugins/input-overlay %buildroot%_datadir/obs/obs-plugins
mv %buildroot/usr/obs-plugins/*/input-overlay.so %buildroot%_libdir/obs-plugins

%files
%_datadir/obs/obs-plugins/input-overlay
%_libdir/obs-plugins/input-overlay.so

%changelog
* Wed Aug 14 2024 Ivan A. Melnikov <iv@altlinux.org> 5.0.5-alt2
- Fix fbtbfs on loongarch64 (thx k0tran@).

* Mon Mar 18 2024 Anton Midyukov <antohami@altlinux.org> 5.0.5-alt1
- new version 5.0.5

* Mon Aug 21 2023 Anton Midyukov <antohami@altlinux.org> 5.0.4-alt1
- initial build (Closes: 47310)
