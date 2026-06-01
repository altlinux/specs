%def_enable snapshot

%define _name Refine
%define __name refine
%define ver_major 0.8
%define beta %nil
%define rdn_name page.tesk.%_name
%def_enable check

Name: gnome-%__name
Version: %ver_major.0
Release: alt1%beta

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

Provides: %_name = %EVR
Provides: %__name = %EVR

BuildArch: noarch

%add_python3_path %_datadir/%__name

%define adw_ver 1.8

Requires: python3-module-pygobject3
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
%find_lang --with-gnome --output=%name.lang %__name %rdn_name

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
* Sun May 31 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Mon Feb 09 2026 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sun Jan 04 2026 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Fri Nov 21 2025 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- 0.6.3-2-ge92dce0

* Tue Nov 18 2025 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Wed Oct 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0-1-g3714ecf

* Tue Jul 01 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.10-alt1
- 0.5.10

* Sat May 10 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.9-alt1
- 0.5.9

* Thu Apr 17 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt1
- 0.5.7

* Thu Apr 03 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1.1
- 0.5.6

* Mon Mar 31 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1.1
- added provides {R,r}efine

* Sat Mar 22 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Fri Mar 07 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Thu Feb 27 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.5-alt1
- 0.4.5

* Thu Feb 06 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Wed Jan 29 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Jan 23 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Mon Jan 20 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue Jan 14 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Wed Jan 08 2025 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- updated to 0.3.0-7-g6e5271f

* Mon Jan 06 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1.1
- explicitly required typelib(XdpGtk4)

* Mon Jan 06 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus (0.2.0-4-gf0c5802)

