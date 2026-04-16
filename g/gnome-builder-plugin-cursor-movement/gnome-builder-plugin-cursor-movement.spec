%define _unpackaged_files_terminate_build 1
%define plugname cursor-movement
%define xdg_name org.gnome.builder.%{plugname}

Name: gnome-builder-plugin-%plugname
Version: 0.3.0
Release: alt1

Summary: GNOME Builder plugin with cursor movement customizations
License: GPL-3.0-or-later
Group: Development/GNOME and GTK+
Url: https://altlinux.space/qualimock/cursor-movement
VCS: https://altlinux.space/qualimock/cursor-movement

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libdex-1)
BuildRequires: pkgconfig(libpanel-1)
BuildRequires: pkgconfig(gnome-builder-50.0)

%description
GNOME Builder plugin that enables cursor movement
using customizable modifiers and keys.

%prep
%setup

%build
%meson
%meson_build

%install
export GI_TYPELIB_PATH=%_libdir/gnome-builder/girepository-1.0
%meson_install
%find_lang %name

%files
%_libdir/gnome-builder/plugins/%plugname/lib%plugname.so
%_libdir/gnome-builder/plugins/%plugname/%plugname.plugin
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml

%changelog
* Thu Apr 16 2026 Alexey Volkov <qualimock@altlinux.org> 0.3.0-alt1
- initial build for ALT
