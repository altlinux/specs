%define _unpackaged_files_terminate_build 1
%def_disable snapshot

%define _name nibbles
%define __name gnome-%_name
%define xdg_name org.gnome.Nibbles
%define ver_major 4.0
%define beta %nil
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.0
Release: alt1%beta

Summary: Guide a worm around a maze
Group: Games/Boards
License: GPL-3.0-or-later
Url: https://wiki.gnome.org/Apps/Nibbles

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version%beta.tar.xz
%else
Source: %__name-%version%beta.tar
%endif

Provides:  %__name = %EVR
Obsoletes: gnome-games-gnibbles
Provides:  gnome-games-gnibbles = %EVR

%define glib_ver 2.78.0
%define gtk_ver 4.6.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: yelp-tools gsettings-desktop-schemas-devel
BuildRequires: desktop-file-utils /usr/bin/appstreamcli
BuildRequires: libgio-devel >= %glib_ver libgtk4-devel >= %gtk_ver
BuildRequires: libgsound-devel
BuildRequires: pkgconfig(libgnome-games-support-2)

%description
Control a worm in its quest to eat bonuses and become longer.
Outmaneuver enemy worms while eating apples and bananas to increase your
length. Each worm has six lives and loses one by running into a wall,
another worm, or itself. The enemy worms are after the same bonuses that
you are, so be careful. If the worms become too large, you won't have
much room to move.

%prep
%setup -n %__name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %__name

%files -f gnome-%_name.lang
%_bindir/%__name
%_desktopdir/%xdg_name.desktop
%_datadir/%__name
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_man6dir/%__name.*
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS

%changelog
* Fri Dec 15 2023 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Wed Nov 22 2023 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt0.9.rc
- updated to 4.0.rc-5-g495a5a0 (ported to GTK4)

* Mon May 01 2023 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Mon Mar 01 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt2
- updated to 3.38.2-8-g374f9bd (fixed build with vala-0.50.4)

* Sun Nov 01 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Sat Oct 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sun Sep 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sat Jul 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sun Mar 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Fri Jan 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Tue Oct 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Thu Sep 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0 (ported to Meson build system)

* Tue Aug 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Aug 21 2018 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt2
- rebuilt against libgnome-games-support-1.so.3

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2.2-alt1
- 3.22.2.2

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2.1-alt1
- 3.20.2.1

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Wed Mar 23 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



