%def_enable snapshot

%define _name Refine
%define __name refine
%define ver_major 0.2
%define beta %nil
%define rdn_name page.tesk.%_name
%def_enable check

Name: gnome-%__name
Version: %ver_major.0
Release: alt1.1%beta

Summary: Tweak various aspects of GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/TheEvilSkeleton/Refine

Vcs: https://gitlab.gnome.org/TheEvilSkeleton/Refine.git

%if_disabled snapshot
Source: %url/-/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildArch: noarch

%add_python3_path %_datadir/%__name

%define adw_ver 1.6

Requires: typelib(Adw) = 1 typelib(XdpGtk4) dconf

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler
BuildRequires: libadwaita-gir-devel >= %adw_ver
%{?_enable_check:BuildRequires: desktop-file-utils /usr/bin/appstreamcli}

%description
Refine helps discover advanced and experimental features in GNOME.

%prep
%setup -n %_name-%version

%build
%meson -Dprofile=default
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name %rdn_name

# conflicts with /usr/bin/refine from argyllcms
mv %buildroot%_bindir/%__name %buildroot%_bindir/%rdn_name
sed -i 's|\(Exec=\)%__name|\1%rdn_name|' %buildroot%_desktopdir/%rdn_name.desktop

%check
%__meson_test -v

%files -f %name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%__name/
%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%{rdn_name}*.svg
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Mon Jan 06 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1.1
- explicitly required typelib(XdpGtk4)

* Mon Jan 06 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus (0.2.0-4-gf0c5802)

