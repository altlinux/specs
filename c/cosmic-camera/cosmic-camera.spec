%def_disable snapshot

%define _name camera
%define binary_name %_name
%define rdn_name io.github.cosmic_utils.%_name
%define ver_major 0.3
%define beta %nil

%def_disable bootstrap
%def_enable check

Name: cosmic-%_name
Version: %ver_major.0
Release: alt1%beta

Summary: COSMIC Camera
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/cosmic-utils/camera

Vcs: https://github.com/cosmic-utils/camera.git

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif
Source1: %_name-%version%beta-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: just gcc-c++
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libcamera)
BuildRequires: cmake clang-devel nasm
BuildRequires: pkgconfig(gstreamer-video-1.0)

Requires: gst-plugins-base1.0
Requires: icon-theme-cosmic

ExcludeArch: %ix86 armh

%description
Camera is a third-party camera application for the COSMIC desktop
environment. Whether you need to snap a quick photo, record a
video, or scan a QR code, Camera provides a clean and intuitive
interface that stays out of your way.

%prep
%setup -n %_name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version%beta-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
just rootdir=%buildroot install

%check
%rust_test

%files
%_bindir/%binary_name
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/*/*.*
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Tue Mar 24 2026 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Fri Jan 30 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.23-alt1
- 0.1.23

* Thu Jan 29 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.21-alt1
- 0.1.21

* Fri Jan 09 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.20-alt1
- 0.1.20

* Thu Jan 08 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.19-alt1
- 0.1.19

* Wed Dec 17 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.18-alt1
- first build for Sisyphus


