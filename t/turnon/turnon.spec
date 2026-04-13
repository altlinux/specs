%def_disable snapshot
%define _name turnon
%define ver_major 3.0
%define rdn_name de.swsnr.%_name

Name: %_name
Version: %ver_major.2
Release: alt1

Summary: Turn on devices in your network

License: EUPL-1.2
Group: Networking/Other
Url: https://codeberg.org/swsnr/turnon

Vcs: https://codeberg.org/swsnr/turnon.git

%if_disabled snapshot
Source: https://codeberg.org/swsnr/turnon/archive/v%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

%define adw_ver 1.8

Requires: dconf

BuildRequires(pre): rpm-build-python3
BuildRequires: blueprint-compiler python3(wheel) python3(hatchling)
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
A small GNOME application to send Wake On LAN (WoL) magic packets to
devices in a network.

%prep
%setup -n %name%{?_enable_snapshot:-%version}
# use full path for binary
sed -i 's|\(Exec=\)\(%rdn_name\)|\1%_bindir/\2|' dbus-1/de.swsnr.turnon.service

%build
%pyproject_build

%install
%pyproject_install
%find_lang %rdn_name

%files -f %rdn_name.lang
%_bindir/%rdn_name
%python3_sitelibdir_noarch/%_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %_name}/
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/gnome-shell/search-providers/%rdn_name.search-provider.ini
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Mon Apr 13 2026 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Sat Apr 11 2026 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Mar 06 2026 Yuri N. Sedunov <aris@altlinux.org> 2.9.6-alt1
- 2.9.6

* Thu Jan 22 2026 Yuri N. Sedunov <aris@altlinux.org> 2.9.5-alt1
- 2.9.5

* Sat Nov 29 2025 Yuri N. Sedunov <aris@altlinux.org> 2.9.4-alt1
- 2.9.4

* Tue Oct 14 2025 Yuri N. Sedunov <aris@altlinux.org> 2.9.3-alt1
- 2.9.3

* Tue Sep 02 2025 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt1
- 2.8.1

* Wed Aug 13 2025 Yuri N. Sedunov <aris@altlinux.org> 2.7.4-alt1
- 2.7.4

* Tue Jun 17 2025 Yuri N. Sedunov <aris@altlinux.org> 2.7.2-alt1
- 2.7.2

* Thu Jun 05 2025 Yuri N. Sedunov <aris@altlinux.org> 2.7.1-alt1
- 2.7.1
- use full path in dbus service file (ALT #53609)

* Wed May 21 2025 Yuri N. Sedunov <aris@altlinux.org> 2.6.7-alt1
- 2.6.7

* Tue Apr 22 2025 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Sun Apr 06 2025 Yuri N. Sedunov <aris@altlinux.org> 2.5.2-alt1
- 2.5.2

* Thu Apr 03 2025 Yuri N. Sedunov <aris@altlinux.org> 2.5.1-alt1
- 2.5.1

* Tue Apr 01 2025 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Tue Mar 25 2025 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Mon Mar 24 2025 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Mon Feb 17 2025 Yuri N. Sedunov <aris@altlinux.org> 2.3.4-alt1
- 2.3.4

* Sat Feb 15 2025 Yuri N. Sedunov <aris@altlinux.org> 2.3.3-alt1
- 2.3.3

* Thu Jan 30 2025 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Sun Jan 12 2025 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Thu Jan 09 2025 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Mon Jan 06 2025 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Fri Jan 03 2025 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- first build for Sisyphus

