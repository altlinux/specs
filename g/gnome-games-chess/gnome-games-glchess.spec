%define _unpackaged_files_terminate_build 1

%define _name chess
%define xdg_name org.gnome.Chess
%define __name gnome-%_name
%define ver_major 43
%define beta %nil
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.1
Release: alt1%beta

Summary: A chess game for GNOME
Group: Games/Boards
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Chess

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version%beta.tar.xz

Provides:  %__name = %version-%release
Obsoletes: gnome-games-glchess
Provides:  gnome-games-glchess = %version-%release
Requires: gnuchess >= 6.2.3

%define glib_ver 2.44
%define gtk_ver 4.0
%define rsvg_ver 2.46
%define vala_ver 0.50.0
%define adwaita_ver 1.0.0

BuildRequires(pre):rpm-macros-meson
BuildRequires: meson vala-tools >= %vala_ver
BuildRequires: yelp-tools /usr/bin/appstream-util desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver libgtk4-devel >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: librsvg-devel >= %rsvg_ver gsettings-desktop-schemas-devel

%description
A chess game which supports several chess engines, with 2D and optionally
3D support if OpenGL is present.

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
%_iconsdir/hicolor/*/apps/%{xdg_name}*.*
%_man6dir/%__name.*
%_datadir/dbus-1/services/%xdg_name.service
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%config(noreplace) %_sysconfdir/%__name/engines.conf
%_datadir/metainfo/%xdg_name.appdata.xml

%changelog
* Sun Jan 08 2023 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Wed Aug 10 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Thu Mar 17 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Fri Oct 29 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Thu Sep 16 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Thu Apr 15 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Tue Mar 23 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0 (ported to GTK 4)

* Sun Dec 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sun May 31 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Fri Mar 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Sun Sep 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Feb 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Sat Sep 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed Apr 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Wed Mar 22 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Sun Nov 06 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Thu Oct 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt2
- explicitly requires gnuchess

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sat May 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Sun Mar 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Fri May 08 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Sat Feb 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Wed Dec 17 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Fri Jun 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Jan 20 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1.1-alt1
- 3.10.1.1

* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Aug 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Mon Jun 10 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2.1-alt1
- 3.8.2.1

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Mar 07 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- first build for people/gnome



