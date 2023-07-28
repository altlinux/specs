%def_enable snapshot
%define ver_major 0.2
%define _name audio-sharing
%define rdn_name de.haeckerfelix.AudioSharing

%def_disable bootstrap

Name: audiosharing
Version: %ver_major.2
Release: alt1

Summary: Audio Sharing application for GNOME
License: GPL-3.0
Group: Sound
Url: https://gitlab.gnome.org/World/audiosharing

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/amberol.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define glib_ver 2.66
%define gtk_ver 4.0
%define adwaita_ver 1.2
%define gst_ver 1.16

Requires: gst-plugins-base1.0 >= %gst_ver
Requires: libgst-rtsp-server >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo git yelp-tools
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-rtsp-server-1.0)
BuildRequires: pkgconfig(dbus-1)

%description
Running Audio Sharing will automatically share the current audio playback
in the form of an RTSP stream. This stream can then be played back by
other devices, for example using VLC.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %_name

%check
%__meson_test

%files -f %name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Thu Jul 06 2023 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- first build for Sisyphus


