%define APP_ID org.gnome.design.Lorem
%def_disable check

Name: lorem
Version: 1.4
Release: alt2

Summary: Generate placeholder text
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://apps.gnome.org/Lorem/
Vcs: https://gitlab.gnome.org/World/design/lorem
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.59
BuildRequires: rust-cargo
BuildRequires: pkgconfig(gio-2.0) >= 2.76
BuildRequires: pkgconfig(glib-2.0) >= 2.76
BuildRequires: pkgconfig(gtk4) >= 4.10.1
BuildRequires: pkgconfig(libadwaita-1) >= 1.5.alpha
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
BuildRequires: clippy
%endif

%description
Simple app to generate the well-known Lorem Ipsum placeholder text.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/fonts/SourceSerif4.ttf
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/%name
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Tue Nov 12 2024 Oleg Shchavelev <oleg@altlinux.org> 1.4-alt2
- Rebuild improved spec (ALT #51816)
- Add macro %%meson_build
- Update BuildRequires

* Wed Oct 16 2024 Oleg Shchavelev <oleg@altlinux.org> 1.4-alt1
- Initial build
