%def_enable snapshot

%define ver_major 0.6
%define rdn_name app.drey.EarTag

%def_enable check

Name: eartag
Version: %ver_major.1
Release: alt1

Summary: Small and simple audio file tag editor
License: MIT
Group: Sound
Url: https://gitlab.gnome.org/World/eartag

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/eartag.git
Source: %name-%version.tar
%endif

%define gtk_ver 4.9
%define adwaita_ver 1.4

Requires: typelib(Adw) = 1
Requires: yelp

BuildArch: noarch

%add_python3_path %_datadir/%name

Requires: python3(acoustid)

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver typelib(Adw)
%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3-module-pygobject3
BuildRequires: python3(mutagen) python3(magic) python3-module-Pillow
BuildRequires: python3(acoustid)}
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %rdn_name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Sat May 04 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Sat Feb 24 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Sun Oct 29 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Sun Sep 24 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0-2-gd87ddf6

* Fri Aug 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Tue Jul 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Thu Jun 29 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- first build for Sisyphus (0.4.1-16-g8004cf4)


