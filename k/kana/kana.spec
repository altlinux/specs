%def_enable snapshot
%define ver_major 1.4
%define rdn_name com.felipekinoshita.Kana

%def_disable bootstrap

Name: kana
Version: %ver_major
Release: alt1

Summary: Learn Japanese characters
License: GPL-3.0
Group: Education
Url: https://gitlab.gnome.org/fkinoshita/kana

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/fkinoshita/kana.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define glib_ver 2.76
%define gtk_ver 4.10
%define adwaita_ver 1.3
%define gst_ver 1.20

Requires: gst-plugins-base1.0 >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-player-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-bad-audio-1.0)
BuildRequires: pkgconfig(dbus-1)

%description
Hone your Japanese skills by matching romanized characters to their
correct hiragana and katakana counterparts.

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
%doc README*


%changelog
* Sat Dec 02 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Sun Nov 26 2023 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3

* Wed Nov 08 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Mon Nov 06 2023 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Sat Nov 04 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- first build for Sisyphus (v1.0-1-g1cdd14e)


