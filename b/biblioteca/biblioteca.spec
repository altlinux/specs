# github.com/sonnyp/troll required
%def_enable snapshot

%define _name Biblioteca
%define ver_major 1.4
%define beta %nil
%define rdn_name app.drey.%_name
%define mozjs_ver 115

# broken appdata/metainfo
%def_disable check

Name: biblioteca
Version: %ver_major
Release: alt1%beta

Summary: Read GNOME documentation offline
License: GPL-3.0
Group: Development/Tools
Url: https://github.com/workbenchdev/Biblioteca

Vcs: https://github.com/workbenchdev/Biblioteca.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Patch: Biblioteca-1.4-alt-no-flatpak.patch

BuildArch: noarch

%define gjs_ver 1.74
%define adw_ver 1.4

Requires: libgjs >= %gjs_ver
Requires: dconf

Requires: typelib(Adw) = 1
Requires: typelib(WebKit) = 6.0
Requires: typelib(Xdp)
Requires(post): glib2-doc libgtk4-devel-doc

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: libgjs-devel >= %gjs_ver
BuildRequires: meson blueprint-compiler typelib(Adw) typelib(WebKit) = 6.0
%{?_enable_check:BuildRequires: desktop-file-utils /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Biblioteca lets you browse and read GNOME documentation.

%prep
%setup -n %_name-%version
%patch -b .no-flatpak
sed -i 's|\/app\/bin\/|/usr/bin/|' src/meson.build
sed -i 's|\(^#!/usr/bin/\)env -S \(gjs -m\)|\1\2|
        s|\/app\/share/|/usr/share/|' build-aux/build-index.js \
        src/{window,Shortcuts}*
sed -i '/build-index/d' src/meson.build

%build
%meson
%meson_build

%install
%meson_install
touch %buildroot%_datadir/%rdn_name/index.json
install -pD -m755 build-aux/build-index.js %buildroot%_datadir/%rdn_name/
%find_lang --with-gnome --output=%name.lang %name %rdn_name

%check
%__meson_test -v

%post
/bin/sh -c "%_datadir/%rdn_name/build-index.js %_datadir/%rdn_name"

%files -f %name.lang
%_bindir/%name
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%dir %_datadir/%rdn_name
%_datadir/%rdn_name/%rdn_name.src.gresource
%_datadir/%rdn_name/build-index.js
%_datadir/%rdn_name/index.json
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%{rdn_name}*.svg
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Wed Aug 21 2024 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- first build for Sisyphus (v1.4-2-g90c9fd8)

