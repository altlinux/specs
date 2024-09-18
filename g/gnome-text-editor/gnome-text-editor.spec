%def_disable snapshot
%define ver_major 47
%define beta %nil
%define xdg_name org.gnome.TextEditor

%def_enable check

Name: gnome-text-editor
Version: %ver_major.0
Release: alt1%beta

Summary: A simple Text Editor for GNOME
Group: Editors
License: GPL-3.0-or-later
Url: https://apps.gnome.org/TextEditor

Vcs: https://gitlab.gnome.org/GNOME/gnome-text-editor.git

%if_disabled snapshot
Source: https://download.gnome.org/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.80
%define gtk_ver 4.15
%define gtksource_ver 5.10
%define spelling_ver 0.3.1
%define adwaita_ver 1.6

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson yelp-tools
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk4-devel >= %gtk_ver
BuildRequires: libgtksourceview5-devel >= %gtksource_ver
BuildRequires: pkgconfig(libspelling-1) >= %spelling_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: libeditorconfig-devel
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Text Editor is a simple editor for GNOME focused on being a good
general purpose default editor.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name --with-gnome

%check
%__meson_test

%files -f %name.lang
%_bindir/*
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README* NEWS

%changelog
* Sat Sep 14 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0-alt1
- 47.0

* Fri May 10 2024 Yuri N. Sedunov <aris@altlinux.org> 46.3-alt1
- 46.3

* Thu Apr 11 2024 Yuri N. Sedunov <aris@altlinux.org> 46.1-alt1
- 46.1

* Sat Mar 16 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Mon Jan 22 2024 Yuri N. Sedunov <aris@altlinux.org> 45.3-alt1
- 45.3

* Tue Jan 16 2024 Yuri N. Sedunov <aris@altlinux.org> 45.2-alt1
- 45.2

* Mon Oct 30 2023 Yuri N. Sedunov <aris@altlinux.org> 45.1-alt1
- 45.1

* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Sat Mar 18 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Jan 11 2023 Yuri N. Sedunov <aris@altlinux.org> 43.2-alt1
- 43.2

* Tue Oct 04 2022 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Thu Sep 22 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sun Jun 12 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Thu Apr 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Thu Aug 26 2021 Yuri N. Sedunov <aris@altlinux.org> 41-alt0.2.beta1
- first build for Sisyphus


