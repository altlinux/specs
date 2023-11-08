%def_disable snapshot

%define ver_major 3.3
%define rdn_name org.kop316.antispam

%def_enable check

Name: phosh-antispam
Version: %ver_major.1
Release: alt1

Summary: Phosh Anti-Spam
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://gitlab.com/kop316/phosh-antispam

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.com/kop316/phosh-antispam.git
Source: %name-%version.tar
%endif

%define gtk_ver 4.6
%define adwaita_ver 1.2

Requires: gnome-calls

BuildRequires(pre): rpm-macros-meson rpm-build-xdg
BuildRequires: meson
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
Phosh Anti-Spam is a program that monitors Gnome calls and automatically
hangs up depending on the user's preferences.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_xdgconfigdir/autostart/%rdn_name-daemon.desktop
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS*


%changelog
* Wed Nov 08 2023 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1
- 3.3.1

* Fri Oct 06 2023 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- first build for Sisyphus


