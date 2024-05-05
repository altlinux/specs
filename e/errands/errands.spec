%def_disable snapshot

%define _name Errands
%define ver_major 46
%define rdn_name io.github.mrvladus.List

%def_enable check

Name: errands
Version: %ver_major.0.2
Release: alt1

Summary: Todo application for GNOME
License: MIT
Group: Office
Url: https://github.com/mrvladus/Errands

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/mrvladus/Errands.git
Source: %name-%version.tar
%endif

%define adwaita_ver 1.4

Requires: typelib(Adw) = 1 typelib(GtkSource) = 5
Requires: yelp

BuildArch: noarch

%add_python3_path %_datadir/%name

Requires: python3-module-icalendar >= 5.0.11
Requires: dconf gnome-keyring gnome-online-accounts

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson yelp-tools
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(goa-1.0)
BuildRequires: pkgconfig(libportal)
%{?_enable_check:BuildRequires: python3(pytest) desktop-file-utils /usr/bin/appstreamcli}

%description
Todo application for those who prefer simplicity.

%prep
%setup %{?_disable_snapshot:-n %_name-%version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Sun May 05 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0.2-alt1
- 46.0.2

* Thu May 02 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0.1-alt1
- 46.0.1

* Thu May 02 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- updated to 46.0-1-g0b8f689

* Tue Feb 27 2024 Yuri N. Sedunov <aris@altlinux.org> 45.1.9-alt1.1
- explicitly required typelib(GtkSource) = 5 (ALT #49507)

* Thu Feb 08 2024 Yuri N. Sedunov <aris@altlinux.org> 45.1.9-alt1
- 45.1.9

* Wed Feb 07 2024 Yuri N. Sedunov <aris@altlinux.org> 45.1.8-alt1
- 45.1.8

* Sat Jan 27 2024 Yuri N. Sedunov <aris@altlinux.org> 45.1.7-alt1
- 45.1.7

* Sat Jan 06 2024 Yuri N. Sedunov <aris@altlinux.org> 45.1.4-alt1
- 45.1.4

* Mon Jan 01 2024 Yuri N. Sedunov <aris@altlinux.org> 45.1.2-alt1
- 45.1.2

* Wed Dec 13 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0.6-alt1
- updated to 45.0.6-15-gde8b47b

* Mon Nov 27 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0.5-alt1
- 45.0.5

* Sun Nov 05 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0.4-alt1
- updated to 45.0.4-27-g01e9d07

* Tue Oct 03 2023 Yuri N. Sedunov <aris@altlinux.org> 44.7.6-alt1
- first build for Sisyphus (44.7.6-7-ge26c812)


