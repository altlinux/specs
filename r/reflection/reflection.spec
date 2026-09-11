%define _unpackaged_files_terminate_build 1

# Vendored sqlite3.c is compiled with LTO which rustc later links
# without -flto, so slim LTO objects from %optflags_lto
# leave sqlite3_unlock_notify unresolved in the sqlx-macros .so.
%define optflags_lto %nil

%define app_id cx.modal.Reflection

%def_with check

Name: reflection
Version: 0.5
Release: alt1

Summary: Collaborative, local-first GTK text editor
License: GPL-3.0-or-later
Group: Editors
Url: https://modal.cx/reflection/
VCS: https://github.com/p2panda/reflection

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: gobject-introspection-devel
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(libspelling-1)

%description
Collaboratively take meeting notes, even when there's no internet.

%prep
%setup -a1
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%doc README.md
%_bindir/reflection
%_datadir/reflection/
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Tue Sep 8 2026 Alexey Volkov <qualimock@altlinux.org> 0.5-alt1
- initial build for ALT
