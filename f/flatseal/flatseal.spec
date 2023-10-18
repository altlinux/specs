%def_disable snapshot

%define _name Flatseal
%define ver_major 2.1
%define beta %nil
%define rdn_name com.github.tchx84.Flatseal
%define mozjs_ver 115

# online screenshots
%def_disable check

Name: flatseal
Version: %ver_major.0
Release: alt1%beta

Summary: Manage Flatpak permissions
License: GPL-3.0
Group: Development/Tools
Url: https://github.com/tchx84/Flatseal

%if_disabled snapshot
Vcs: https://github.com/tchx84/Flatseal.git
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%define gjs_ver 1.73.1
%define adw_ver 1.4
%define webkit_ver 2.40

Requires: libgjs >= %gjs_ver
Requires: flatpak
Requires: yelp

Requires: typelib(Adw) = 1
Requires: typelib(WebKit) = 6.0
Requires: typelib(AppStream)

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson yelp-tools
BuildRequires: desktop-file-utils /usr/bin/appstream-util
BuildRequires: libgjs-devel >= %gjs_ver
BuildRequires: libadwaita-gir-devel >= %adw_ver
BuildRequires: libwebkitgtk6.0-gir-devel >= %webkit_ver

%description
Flatseal is a graphical utility to review and modify permissions for
Flatpak applications.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name %rdn_name

%check
%__meson_test -v

%files -f %name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%{rdn_name}*.svg
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/appdata/%rdn_name.appdata.xml
%doc README* DOCUMENTATION*

%changelog
* Wed Oct 18 2023 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- first build for Sisyphus

