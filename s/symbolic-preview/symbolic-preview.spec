%define APP_ID org.gnome.design.SymbolicPreview
%def_enable check

Name: symbolic-preview
Version: 0.0.9
Release: alt1

Summary: Symbolics made easy
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/World/design/symbolic-preview/
Vcs: https://gitlab.gnome.org/World/design/symbolic-preview/
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: pkgconfig(glib-2.0) >= 2.66
BuildRequires: pkgconfig(gio-2.0) >= 2.66
BuildRequires: pkgconfig(libadwaita-1) >= 1.0.0
BuildRequires: libxml2-devel
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstream-util
%endif

ExcludeArch: %ix86 ppc64le

%description
Symbolic Preview is a utility that helps you create, preview and export your
symbolic icons easily.

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
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_datadir/icons/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.appdata.xml
%_datadir/%name

%changelog
* Wed Oct 23 2024 Oleg Shchavelev <oleg@altlinux.org> 0.0.9-alt1
- Initial build
