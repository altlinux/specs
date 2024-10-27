%define APP_ID org.gnome.World.Citations
%def_disable check

Name: citations
Version: 0.7.0
Release: alt1

Summary: Manage your bibliography
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://apps.gnome.org/Citations/
Vcs: https://gitlab.gnome.org/World/citations
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: pkgconfig(glib-2.0) >= 2.76
BuildRequires: pkgconfig(gio-2.0) >= 2.76
BuildRequires: pkgconfig(libadwaita-1) >= 1.6
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(poppler-glib)
BuildRequires: pkgconfig(gtksourceview-5)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
BuildRequires: clippy
%endif

%description
Manage your bibliographies using the BibTeX format.

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
%_datadir/%name
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Wed Oct 23 2024 Oleg Shchavelev <oleg@altlinux.org> 0.7.0-alt1
- Initial build
