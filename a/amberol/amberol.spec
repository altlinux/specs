%def_disable snapshot
%define ver_major 0.10
%define rdn_name io.bassi.Amberol

%def_disable bootstrap

Name: amberol
Version: %ver_major.3
Release: alt1.1

Summary: A small and simple sound and music player that is well integrated with GNOME
License: GPL-3.0
Group: Sound
Url: https://apps.gnome.org/Amberol

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/amberol.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar
Patch1: %name-0.10.3-alt-vendored-nix-loongarch64-support.patch

%define glib_ver 2.76
%define gtk_ver 4.10
%define adwaita_ver 1.2
%define gst_ver 1.20

Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-plugins-bad1.0 >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-player-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires: pkgconfig(gstreamer-bad-audio-1.0)
BuildRequires: pkgconfig(dbus-1)

%description
Amberol aspires to be as small, unintrusive, and simple as possible.
It does not manage your music collection; it does not let you manage
playlists, smart or otherwise; it does not let you edit the metadata for
your songs; it does not show you lyrics for your songs, or the Wikipedia
page for your bands.

Amberol plays music, and nothing else.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%patch1 -p1

# allow patching vendored rust code
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
        ./vendor/nix/.cargo-checksum.json

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
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%doc CHANGES* README*


%changelog
* Thu Nov 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1.1
- fixed build for loongarch64 (iv@)
- fixed Url and Group tags

* Tue Jun 20 2023 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- first build for Sisyphus


