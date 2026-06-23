%define optflags_lto %nil
%define _libexecdir %_prefix/libexec

%def_enable snapshot
%define __name Gitte
%define _name gitte
%define ver_major 0.8
%define rdn_name de.wwwtech.%_name

%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: A GTK4/libadwaita Git client for the GNOME desktop
License: AGPL-3.0-or-later
Group: Text tools
Url: https://codeberg.org/ckruse/Gitte

Vcs: https://codeberg.org/ckruse/Gitte.git

%if_disabled snapshot
Source: %url/archive/%name-%version.tar.gz
%else
Source: %__name-%version.tar
%endif
Source1: %__name-%version-cargo.tar

%define gtk_ver 4.20
%define adwaita_ver 1.8

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(liblzma)
BuildRequires: /usr/bin/appstreamcli desktop-file-utils

%description
A GTK4/libadwaita Git client for the GNOME desktop, written in Rust. It
is heavily inspired by [Git Tower](https://www.git-tower.com/) and
[Magit](https://magit.vc/). The name Gitte is a play on words. It is the
diminutive form of the German female first name Brigitte and is
pronounced "Git-ty" in English (with a hard G like in GIF).

%prep
%setup -n %__name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%__name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%_name
%dir %_libexecdir/%_name/
%_libexecdir/%_name/%_name-askpass
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Tue Jun 23 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Sat Jun 13 2026 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Thu May 28 2026 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu May 21 2026 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue May 19 2026 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- first build for Sisyphus


