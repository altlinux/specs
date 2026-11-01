%global _unpackaged_files_terminate_build 1
%global appid dev.faetalize.waytator
%def_with check

Name: waytator
Version: 1.5.1
Release: alt1
Summary: Screenshots and video recording on wayland
License: GPL-3.0-or-later
Group: Graphics
URL: https://github.com/faetalize/waytator
VCS: https://github.com/faetalize/waytator

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)

%description
Waytator is an application for screenshotting and screen recording on
wlroots-based Wayland compositors, with a lightweight built-in image and
video editor.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test
desktop-file-validate %buildroot%_desktopdir/%appid.desktop

%files
%_bindir/%name
%_desktopdir/%appid.desktop
%_iconsdir/hicolor/*/apps/%appid.png

%changelog
* Sun Nov 01 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.5.1-alt1
- Initial build for ALT.
