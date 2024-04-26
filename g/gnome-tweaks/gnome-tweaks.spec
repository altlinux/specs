%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define ver_major 46
%define beta %nil
%define old_name gnome-tweak-tool
%define xdg_name org.gnome.tweaks
%define pypi_name gtweak

%def_enable check

Name: gnome-tweaks
Version: %ver_major.1
Release: alt1%beta

Summary: A tool to customize advanced GNOME 3 options
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/GNOME/gnome-tweaks

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%endif
Patch: %name-3.27.4-alt-desktop.patch

BuildArch: noarch

%define gsds_ver 46
%define adw_ver 1.4
%define pygobject_ver 3.46.0

Requires: gnome-settings-daemon >= %ver_major
Requires: gsettings-desktop-schemas-devel >= %gsds_ver
Requires: sound-theme-freedesktop
Requires: typelib(Gtk) = 4.0 typelib(Adw) = 1

Provides: %old_name = %version-%release
Obsoletes: %old_name < 3.27.4

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-python3
BuildRequires: meson
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: python3-module-pygobject3-devel >= %pygobject_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver typelib(Adw) = 1
BuildRequires: pkgconfig(gudev-1.0)
%{?_enable_check:BuildRequires:/usr/bin/appstreamcli desktop-file-utils}

%description
GNOME Tweaks is an application for changing the advanced settings
of GNOME 3.

Features:
* Install and switch gnome-shell themes
* Switch GTK+ themes
* Switch icon themes
* Change
  - The user-interface and title bar fonts
  - Icons in menus and buttons
  - Behavior on laptop lid close
  - Shell font size
  - File manager desktop icons
  - Title bar click action
  - Shell clock to show date
  - Font hinting
  - Font anti-aliasing

%prep
%setup -n %name-%version%beta
%patch -b .desktop

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
%python3_sitelibdir_noarch/%pypi_name/
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS NEWS README*

%changelog
* Fri Apr 26 2024 Yuri N. Sedunov <aris@altlinux.org> 46.1-alt1
- 46.1

* Sun Apr 07 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt2
- updated to 46.0-9-g6307804 (ALT #49758)

* Sun Mar 17 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Mon Feb 12 2024 Yuri N. Sedunov <aris@altlinux.org> 45.1-alt1
- 45.1

* Sat Sep 23 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Sun Mar 06 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.5.beta
- 42.beta

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 40.10-alt1
- 40.10

* Sun Mar 28 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Wed Feb 24 2021 Yuri N. Sedunov <aris@altlinux.org> 40-alt0.2.beta
- 40.beta

* Wed Feb 24 2021 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 15 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt2
- updated to 3.34.0
- explicitly required typelib(Handy) = 0.0

* Fri Sep 27 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun Sep 22 2019 Yuri N. Sedunov <aris@altlinux.org> 3.33.90-alt1
- 3.33.90

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Thu Sep 27 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sun Apr 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.4-alt1
- 3.26.4

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2.1-alt1
- 3.26.2.1

* Wed Sep 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Jun 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Fri Apr 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Wed Mar 23 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Wed Nov 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Nov 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Thu Mar 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Sat Nov 02 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt3
- updated to 3.10_5dce590 (fixed extension update checks)
- fixed BGO #710275

* Sun Sep 29 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt2
- updated to 3.10_a8f0982 (fixed BGO #708900)

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Jul 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Apr 08 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Feb 28 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.4-alt1
- 3.7.4

* Mon Dec 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt2
- updated to 600e101a
- moved to System menu (ALT #27896)

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Oct 03 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Thu Mar 22 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.5-alt1
- 3.3.5 snapshot

* Sat Nov 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.0-alt1.1
- Rebuild with Python-2.7

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Jun 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5

* Sun May 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Thu Apr 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Wed Apr 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Thu Apr 07 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- Initial package
