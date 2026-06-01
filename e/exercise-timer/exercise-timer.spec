%def_enable snapshot

%define _name exercise-timer
%define __name hiit
%define ver_major 1.10
%define beta %nil
%define rdn_name xyz.safeworlds.%__name

%def_enable check

Name: %_name
Version: %ver_major.0
Release: alt1%beta

Summary: Exercise Timer
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://apps.gnome.org/ru/Hiit

Vcs: https://gitlab.gnome.org/World/exercise-timer.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/exercise-timer/-/archive/v%version/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif

%define gtk_ver 4.20
%define adwaita_ver 1.8

Provides: %__name = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(alsa)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Exercise Timer is a simple utility to conduct interval training. It is
built for the GNOME desktop using Libadwaita.

%prep
%setup -n %name-%version%beta

%build
%meson \
    -Dprofile=default
%nil
%meson_build

%install
%meson_install
%find_lang %__name

%check
%__meson_test

%files -f %__name.lang
%_bindir/%__name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* CHANGELOG*


%changelog
* Sun May 31 2026 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Thu Mar 26 2026 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt1
- 1.9.1

* Sun Aug 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt1
- 1.8.5

* Sun Jun 08 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1
- 1.8.4

* Tue Apr 22 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Wed Apr 02 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- first build for Sisyphus (v1.8.1-23-gefa1c7a)



