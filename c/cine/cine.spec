%def_disable snapshot

%define __name Cine
%define _name cine
%define ver_major 1.7
%define rdn_name io.github.diegopvlk.%__name

%def_enable check

Name: %_name
Version: %ver_major.1
Release: alt1

Summary: MPV-based Video Player for Linux
License: GPL-3.0-or-later
Group: Video
Url: https://github.com/diegopvlk/Cine

Vcs: https://github.com/diegopvlk/Cine.git

BuildArch: noarch

%if_disabled snapshot
Source: https://github.com/diegopvlk/%__name/archive/v%version/%__name-%version.tar.gz
%else
Source: %__name-%version.tar
%endif

BuildArch: noarch

%add_python3_path %_datadir/%_name

%define adw_ver 1.9

Requires: python3-module-pygobject3
Requires: dconf
Requires: typelib(Adw) = 1
Requires: libadwaita-gir >= %adw_ver
#Requires: mpv

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: /usr/bin/glib-compile-resources /usr/bin/gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Cine combines a clean interface with a high-performance engine to
deliver a seamless viewing experience.

%prep
%setup -n %__name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%_datadir/dbus-1/services/%rdn_name.service
%doc README.*

%changelog
* Tue Jul 07 2026 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Sun Jun 28 2026 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Tue Jun 23 2026 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Thu Jun 11 2026 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Wed Jun 10 2026 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Fri Jun 05 2026 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Wed Jun 03 2026 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Thu May 28 2026 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Sat May 23 2026 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Fri May 22 2026 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Wed May 06 2026 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Fri May 01 2026 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sun Apr 19 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5

* Tue Apr 14 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Sun Apr 12 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Fri Apr 10 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Mon Mar 16 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Fri Mar 06 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sat Feb 21 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt1
- 1.0.9

* Sat Feb 07 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Thu Feb 05 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Wed Feb 04 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- first build for Sisyphus


