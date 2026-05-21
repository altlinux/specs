%def_disable snapshot

%define _name Flatseal
%define ver_major 2.4
%define beta %nil
%define rdn_name com.github.tchx84.%_name
%def_enable check

Name: flatseal
Version: %ver_major.1
Release: alt1%beta

Summary: Manage Flatpak permissions
License: GPL-3.0
Group: Development/Tools
Url: https://github.com/tchx84/Flatseal

Vcs: https://github.com/tchx84/Flatseal.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%define gjs_ver 1.73.1
%define adw_ver 1.8
%define webkit_ver 2.40
%define appstream_ver 1.0

Requires: libgjs >= %gjs_ver
Requires: flatpak
Requires: yelp

Requires: typelib(Adw) = 1
Requires: typelib(WebKit) = 6.0
Requires: typelib(AppStream) = 1.0
Requires: libappstream-gir >= %appstream_ver

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson yelp-tools
BuildRequires: libgjs-devel >= %gjs_ver /usr/bin/jasmine
BuildRequires: libadwaita-gir-devel >= %adw_ver
BuildRequires: libwebkitgtk6.0-gir-devel >= %webkit_ver
BuildRequires: pkgconfig(appstream) >= %appstream_ver
%{?_enable_check:BuildRequires: xvfb-run desktop-file-utils /usr/bin/appstreamcli}

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
xvfb-run %__meson_test -v

%files -f %name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%{rdn_name}*.svg
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* DOCUMENTATION* CHANGELOG*

%changelog
* Thu May 21 2026 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Tue Sep 30 2025 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Fri Apr 25 2025 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Wed Oct 02 2024 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Mon May 20 2024 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt2
- applied AUR patch for AppStream-1.0.0 (ALT #50396)

* Fri Apr 19 2024 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 2.1.2-alt1
- 2.1.2

* Wed Feb 07 2024 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Wed Oct 18 2023 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- first build for Sisyphus

