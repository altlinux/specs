%def_enable snapshot
%define _name video-trimmer
%define ver_major 0.8
%define rdn_name org.gnome.gitlab.YaLTeR.VideoTrimmer

%def_disable bootstrap

Name: gnome-%_name
Version: %ver_major.2
Release: alt1

Summary: GNOME Video Trimmer
License: GPL-3.0-or-later
Group: Video
Url: https://gitlab.gnome.org/YaLTeR/video-trimmer

%if_disabled snapshot
Source: %url/archive/-/v%version/%_name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/YaLTeR/video-trimmer.git
Source: %_name-%version.tar
%endif
Source1: %_name-%version-cargo.tar

%define gtk_ver 4.0.0
%define adwaita_ver 1.4

Requires: ffmpeg ffprobe

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: typelib(Adw)

%description
Video Trimmer cuts out a fragment of a video given the start and end
timestamps. The video is never re-encoded, so the process is very fast
and does not reduce the video quality.

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

%build -n %_name-%version
%meson
%meson_build

%install
%meson_install
%find_lang %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Sat Oct 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- updated to v0.8.2-3-g4259123

* Fri Aug 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- first build for Sisyphus (v0.8.1-23-ge116fc9)


