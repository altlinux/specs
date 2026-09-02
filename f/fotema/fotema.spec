%def_disable snapshot

# required for "ring"
%define optflags_lto %nil

%define _name Fotema
%define ver_major 2.4
%define rdn_name app.fotema.%_name

%def_enable check
%def_disable bootstrap

Name: fotema
Version: %ver_major.2
Release: alt2

Summary: A photo gallery for GNOME
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/blissd/fotema

Vcs: https://github.com/blissd/fotema.git

ExclusiveArch: x86_64 aarch64 loongarch64

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

Patch: fotema-1.19.0-alt-loongarch64-size_t-ort-crate.patch
Patch1: cargo-lock-bump-ffmpeg-next.patch

%define gtk_ver 4.0
%define adwaita_ver 1.5
%define glycin_api_ver 2

# for glycin
Requires: bubblewrap glycin-%glycin_api_ver-loaders

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(shumate-1.0)
BuildRequires: libonnxruntime-devel
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

BuildRequires: pkgconfig(openssl)
BuildRequires: libopencv-devel gcc-c++
# for glycin
BuildRequires: pkgconfig(libseccomp)
# for ffmpeg-next
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libavformat) >= 61
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libswresample)
# for bindgen
BuildRequires: clang-devel
# ? for gdk-sys
BuildRequires: pkgconfig(gdk-3.0)
# for ort
BuildRequires: /proc

%description
A photo gallery for everyone who wants their photos to live locally on their devices.
Why enjoy your photo library with Fotema?
- Many supported image formats. Fotema supports the same image formats as Loupe (the GNOME image viewer).
- View iOS Live Photos.
- Play videos.
- View your library by year or month.

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%patch1 -p1
#%%patch -p2
#sed -i -e 's/"files":{[^}]*}/"files":{}/' \
#	./vendor/ort/.cargo-checksum.json

%build
%meson
%__meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* THUMBNAILS*

%changelog
* Wed Sep 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.4.2-alt2
- builded with onnxruntime from repo
- fixed FTBFS

* Sun Mar 22 2026 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Thu Jan 22 2026 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Wed Dec 17 2025 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Oct 07 2025 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Fri Sep 19 2025 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Fri Sep 12 2025 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Tue Jun 24 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Sun Jun 22 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Sun Apr 06 2025 Yuri N. Sedunov <aris@altlinux.org> 1.20.1-alt1
- 1.20.1

* Wed Apr 02 2025 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Tue Feb 11 2025 Yuri N. Sedunov <aris@altlinux.org> 1.19.2-alt1
- 1.19.2

* Wed Jan 29 2025 Yuri N. Sedunov <aris@altlinux.org> 1.19.1-alt1
- 1.19.1

* Tue Jan 14 2025 Ilya Sorochan <k0tran@altlinux.org> 1.19.0-alt2
- add patch for ort crate to fix build on loongarch64

* Wed Jan 08 2025 Yuri N. Sedunov <aris@altlinux.org> 1.19.0-alt1
- 1.19.0

* Sat Dec 28 2024 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1
- 1.18.3

* Tue Dec 24 2024 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- first build for Sisyphus (v1.18.2-21-g38ac8e9)



