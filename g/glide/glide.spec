%def_disable snapshot

%define _name Glide
%define ver_major 0.6
%define rdn_name net.base_art.%_name

%def_enable check

%def_disable bootstrap

Name: glide
Version: %ver_major.7
Release: alt1

Summary: Media player based on GStreamer and GTK
License: GPL-3.0-or-later
Group: Video
Url: https://github.com/philn/glide

Vcs: https://github.com/philn/glide.git

%if_disabled snapshot
Source: %url/releases/download/%version/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
# github tarball provides vendored sources
%{?_enable_snapshot:Source1: %name-%version-cargo.tar}

%define gst_ver 1.26.11
%define adw_ver 1.8

Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-libav
Requires: gst-plugin-gtk4 >= 0.14.3
Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-play-1.0)
BuildRequires: pkgconfig(gstreamer-gl-1.0)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Glide is a simple and minimalistic media player relying on GStreamer for
the multimedia support and GTK for the user interface. Glide should be
able to play any multimedia format supported by GStreamer, locally or
remotely hosted.

%prep
%setup -n %name-%version %{?_disable_bootstrap:%{?_enable_snapshot:-a1}}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %rdn_name

%check
%__meson_test

%files -f %rdn_name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* TODO

%changelog
* Wed Apr 01 2026 Yuri N. Sedunov <aris@altlinux.org> 0.6.7-alt1
- 0.6.7

* Fri Nov 14 2025 Yuri N. Sedunov <aris@altlinux.org> 0.6.6-alt1
- 0.6.6

* Sun Aug 25 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.5-alt1
- 0.6.5

* Tue Jul 16 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- first build for Sisyphus (0.6.3-19-g5cb2545)


