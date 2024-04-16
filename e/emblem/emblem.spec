%def_enable snapshot
%define ver_major 1.4
%define rdn_name org.gnome.design.Emblem

%def_disable bootstrap
%def_enable check

Name: emblem
Version: %ver_major.0
Release: alt1

Summary: GNOME Emblem
License: GPL-3.0-or-later
Group: Graphics
Url: https://apps.gnome.org/Emblem

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/design/emblem.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.14
%define adwaita_ver 1.5

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(libxml-2.0)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils clippy}

%description
Generate projects avatars for your Matrix rooms and git forges from a
symbolic icon.

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
%__meson_test -t 2

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Tue Apr 16 2024 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- updated to 1.4.0-2-g7de26cf

* Thu Sep 28 2023 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- first build for Sisyphus (1.3.0-1-g644fa35)


