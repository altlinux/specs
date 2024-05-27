# github.com/sonnyp/troll required
%def_enable snapshot

%define _name Tangram
%define ver_major 3.1
%define beta %nil
%define rdn_name re.sonny.Tangram
%define mozjs_ver 115

Name: tangram
Version: %ver_major
Release: alt1%beta

Summary: Browser for pinned tabs
License: GPL-3.0
Group: Networking/WWW
Url: https://apps.gnome.org/Tangram

Vcs: https://github.com/sonnyp/Tangram.git

%if_disabled snapshot
Source: https://github.com/sonnyp/Tangram/archive/v%version/%name-%version%beta.tar.gz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

%define gjs_ver 1.76

Requires: libgjs >= %gjs_ver /usr/bin/gjs

# grep -h gi:// -r *|sort -u
Requires: typelib(Adw) = 1
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gtk) = 4.0
Requires: typelib(Pango)
Requires: typelib(PangoCairo)
Requires: typelib(Soup) = 3.0
Requires: typelib(Gst) = 1.0
Requires: typelib(WebKit) = 6.0

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson /usr/bin/gjs
BuildRequires: blueprint-compiler gir(Adw) = 1
BuildRequires: desktop-file-utils libappstream-glib-devel

%description
Tangram is a new kind of browser. It is designed to organize and run
your Web applications. Each tab is persistent and independent.

You can set multiple tabs with different accounts for the same application.


%prep
%setup -n %{?_enable_snapshot:%name}%{?_disable_snapshot:%_name}-%version%beta
sed -i 's|\(^#!/usr/bin/\)env -S \(gjs -m\)|\1\2|' src/bin.js

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
%doc README* TODO*


%changelog
* Mon May 27 2024 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1

* Mon Nov 13 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- first build for Sisyphus (v3.0-1-g7de723e)

