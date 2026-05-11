# github.com/sonnyp/troll required
%def_enable snapshot

%define _name Junction
%define ver_major 1.12
%define beta %nil
%define rdn_name re.sonny.Junction

Name: junction
Version: %ver_major
Release: alt1%beta

Summary: Application chooser for GNOME
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://apps.gnome.org/Junction

Vcs: https://github.com/sonnyp/Junction.git

%if_disabled snapshot
Source: https://github.com/sonnyp/%_name/archive/v%version/%name-%version%beta.tar.gz
%else
Source: %name-%version.tar
%endif
Patch: %name-1.12-alt-no_flatpak.patch

BuildArch: noarch

%define gjs_ver 1.76
Requires: libgjs >= %gjs_ver /usr/bin/gjs

# grep -h gi:// -r *|sort -u
Requires: typelib(Adw) = 1
Requires: typelib(Gtk) = 4.0
Requires: typelib(Soup) = 3.0
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
%patch -p1 -b .no-flatpak

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %_name %rdn_name

%files -f %name.lang
%_bindir/%name
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
* Mon May 11 2026 Yuri N. Sedunov <aris@altlinux.org> 1.12-alt1
- 1.12

* Tue Dec 23 2025 Yuri N. Sedunov <aris@altlinux.org> 1.11-alt1
- 1.11

* Sun Nov 02 2025 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt1
- 1.10

* Sun Jul 27 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9-alt1.1
- fixed start if XDG_DATA_DIRS is not set (ALT #55368)

* Tue Apr 22 2025 Yuri N. Sedunov <aris@altlinux.org> 1.9-alt1
- 1.9

* Sun Jan 21 2024 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt1
- 1.8

* Thu Nov 16 2023 Yuri N. Sedunov <aris@altlinux.org> 1.7-alt1
- first build for Sisyphus (v1.7-4-g5a322b6)

