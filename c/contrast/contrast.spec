%define APP_ID org.gnome.design.Contrast
%def_enable check

Name: contrast
Version: 0.0.11
Release: alt1

Summary: Check contrast between two colors
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/World/design/contrast
Vcs: https://gitlab.gnome.org/World/design/contrast
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.59
BuildRequires: rust-cargo
BuildRequires: pkgconfig(glib-2.0) >= 2.56
BuildRequires: pkgconfig(gio-2.0) >= 2.56
BuildRequires: pkgconfig(gtk4) >= 4.13.0
BuildRequires: pkgconfig(libadwaita-1) >= 1.5.alpha
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
%endif

%description
Contrast checks whether the contrast between two colors meet the WCAG
requirements.

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
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Fri Nov 08 2024 Oleg Shchavelev <oleg@altlinux.org> 0.0.11-alt1
- Initial build
