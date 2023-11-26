%def_enable snapshot
%define ver_major 0.3
%define rdn_name com.felipekinoshita.Wildcard

%def_disable bootstrap

Name: wildcard
Version: %ver_major.3
Release: alt1

Summary: regular expression testing app for GNOME
License: GPL-3.0-or-later
Group: Text tools
Url: https://gitlab.gnome.org/World/Wildcard

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/Wildcard.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.10
%define adwaita_ver 1.4

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: typelib(Adw)

%description
Wildcard gives a nice and simple to use interface to test/practice
regular expressions.

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
* Sun Nov 26 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Sat Nov 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Sun Oct 08 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Sun Aug 20 2023 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Sun Aug 13 2023 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus (v0.2.0-6-gff8c151)


