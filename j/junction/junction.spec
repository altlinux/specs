# github.com/sonnyp/troll required
%def_enable snapshot

%define _name Junction
%define ver_major 1.7
%define beta %nil
%define rdn_name re.sonny.Junction

Name: junction
Version: %ver_major
Release: alt1%beta

Summary: Application chooser for GNOME
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://apps.gnome.org/Junction

%if_disabled snapshot
Vcs: https://github.com/sonnyp/Junction.git
Source: https://github.com/sonnyp/%_name/archive/v%version/%name-%version%beta.tar.gz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch
##!/usr/bin/env -S XDG_DATA_DIRS=${XDG_DATA_DIRS}:/run/host/usr/share:/var/lib/snapd/desktop:/var/lib/flatpak/exports/share:${HOME}/.local/share/flatpak/exports/share gjs -m
AutoReq: noshebang

%define gjs_ver 1.76
Requires: libgjs >= %gjs_ver /usr/bin/gjs

# grep -h gi:// -r *|sort -u
Requires: typelib(Adw) = 1
Requires: typelib(Gtk) = 4.0
Requires: typelib(Xdp)
Requires: typelib(XdpGtk4)

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson /usr/bin/gjs
BuildRequires: blueprint-compiler gir(Adw) = 1
BuildRequires: desktop-file-utils /usr/bin/appstream-util

%description
Junction lets you choose the application to open files and links.

%prep
%setup -n %{?_enable_snapshot:%name}%{?_disable_snapshot:%_name}-%version%beta
#sed -i 's|\(^#!/usr/bin/\)env -S  \(gjs -m\)|\1\2|' src/bin.js

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %_name %rdn_name

%files -f %name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%rdn_name/
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Thu Nov 16 2023 Yuri N. Sedunov <aris@altlinux.org> 1.7-alt1
- first build for Sisyphus (v1.7-4-g5a322b6)

