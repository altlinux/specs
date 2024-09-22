%def_disable snapshot
%define ver_major 2024
%define rdn_name io.bassi.Amberol

%def_enable check
%def_disable bootstrap

Name: amberol
Version: %ver_major.1
Release: alt1

Summary: A small and simple sound and music player that is well integrated with GNOME
License: GPL-3.0-or-later
Group: Sound
Url: https://apps.gnome.org/Amberol

Vcs: https://gitlab.gnome.org/World/amberol.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/amberol/-/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar
Patch1: %name-0.10.3-alt-vendored-nix-loongarch64-support.patch

%define glib_ver 2.76
%define gtk_ver 4.14
%define adwaita_ver 1.5
%define gst_ver 1.20

Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-plugins-bad1.0 >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo 
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-player-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires: pkgconfig(gstreamer-bad-audio-1.0)
BuildRequires: pkgconfig(dbus-1)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Amberol is a music player with no delusions of grandeur. If you just
want to play music available on your local system then Amberol is the
music player you are looking for.

Amberol plays music, and nothing else.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

#%%patch1 -p1

# allow patching vendored rust code
#sed -i -e 's/"files":{[^}]*}/"files":{}/' \
#        ./vendor/nix/.cargo-checksum.json

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
* Sun Sep 22 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.1-alt1
- 2024.1

* Thu Nov 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1.1
- fixed build for loongarch64 (iv@)
- fixed Url and Group tags

* Tue Jun 20 2023 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- first build for Sisyphus


