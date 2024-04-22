%def_enable snapshot
%define _name Footage
%define ver_major 1.3
%define xdg_name io.gitlab.adhami3310.Footage

%def_enable check
%def_disable bootstrap

Name: footage
Version: %ver_major.2
Release: alt0.2

Summary: Simple video editor for GNOME
License: GPL-3.0
Group: Video
Url: https://gitlab.com/adhami3310/Footage.git

%if_disabled snapshot
Source: https://gitlab.com/adhami3310/Footage/releases/download/v%version/%name-%version.tar.xz
%else
Vcs: https://gitlab.com/adhami3310/Footage.git
Source: %_name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.10.0
%define adwaita_ver 1.5
%define gst_ver 1.22.8

Requires: gstreamer1.0-utils
Requires: gst-plugins-bad1.0 >= 1.22.8
Requires: gst-plugins-ugly1.0
Requires: gstreamer-editing-services
Requires: gstreamer-vaapi
Requires: gst-libav
Requires: gst-plugin-gtk4
Requires: ffmpeg a52dec fdkaac
Requires: x264 x265
Requires: gstreamer1-svt-av1 svt-av1
Requires: libmpeg2
#Requires: vo-aacenc

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver typelib(Adw) = 1
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gst-editing-services-1.0)

%description
Footage is a useful tool for quickly editing short videos and
screencasts. It's also capable of exporting any video into a format of
your choice.

%prep
%setup -n %{?_enable_snapshot:%_name}%{?_disable_snapshot:%name}-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_iconsdir/hicolor/scalable/actions/*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README* PRESS*

%changelog
* Mon Apr 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt0.2
- updated runtime dependencies

* Fri Apr 19 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt0.1
- first build for Sisyphus (v1.3.2-1-g072c586)



