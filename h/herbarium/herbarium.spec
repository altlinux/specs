%define _unpackaged_files_terminate_build 1
%define app_id ru.ximper.Herbarium

Name: herbarium
Version: 0.4.0
Release: alt1

Summary: Utility for managing mods for the game Everlasting Summer
License: MIT
Group: Games/Other

URL: https://github.com/X1mper/Herbarium
VCS: https://github.com/X1mper/Herbarium
Source0: %name-%version.tar
Source1: %name-vendor.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: meson
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(graphene-1.0)
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)

Requires: %name-common

%description
Utility for managing mods for the game Everlasting Summer, written in Go. It
allows you to enable/disable mods, automatically detect mod information, launch
the game with selected mods.

%package cli
Summary: CLI version of %name
Group: Games/Other

Requires: %name-common

%description cli
%summary.

%package common
Summary: Common files for %name
Group: Other

%description common
%summary.

%prep
%setup -a1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files
%_bindir/%name-gui
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/scalable/apps/%app_id.svg
%_datadir/metainfo/%app_id.metainfo.xml

%files cli
%_bindir/%name-cli
%_datadir/zsh/site-functions/_herbarium-cli
%_datadir/bash-completion/completions/herbarium-cli
%_datadir/fish/vendor_completions.d/herbarium-cli.fish

%files common -f %name.lang

%changelog
* Sat Jan 24 2026 David Sultaniiazov <x1z53@altlinux.org> 0.4.0-alt1
- Update to 0.4.0.

* Thu Dec 25 2025 David Sultaniiazov <x1z53@altlinux.org> 0.3.0-alt1
- Initial build.
