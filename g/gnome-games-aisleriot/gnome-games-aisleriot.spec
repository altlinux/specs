%define _unpackaged_files_terminate_build 1
%def_disable snapshot

%define _name aisleriot
%define ver_major 3.22
%define _libexecdir %_prefix/libexec

# fixed, kde, pysol, svg-rsvg, svg-qtsvg
# default: svg-rsvg
%define default_theme_format svg-rsvg
%def_enable theme_kde

Name: gnome-games-%_name
Version: %ver_major.28
Release: alt1

Summary: A collection of card games
Group: Games/Cards
License: GPL-3.0-or-later and GFDL-1.3-or-later
Url: https://wiki.gnome.org/Apps/Aisleriot

%if_disabled snapshot
Source: https://gitlab.gnome.org/GNOME/%_name/-/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

Obsoletes: gnome-games-sol
Provides:  gnome-games-sol = %version-%release
Provides:  %_name = %version-%release

Requires: pysol-cardsets
%{?_enable_theme_kde:Requires: kde5-carddecks}

%define glib_ver 2.32.0
%define gtk_ver 3.18.0
# guile-3.0 also supported but /usr/bin/guile points to guile22
%define guile_ver 22

BuildRequires(pre): rpm-macros-meson
BuildRequires: /proc meson guile%guile_ver guile%guile_ver-devel
BuildRequires: desktop-file-utils yelp-tools libappstream-glib-devel libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver librsvg-devel libcanberra-gtk3-devel
BuildRequires: libICE-devel libSM-devel
%{?_enable_theme_kde:BuildRequires: gcc-c++ qt5-base-devel qt5-svg-devel kde5-carddecks libxml2-devel}

%description
AisleRiot also known as Solitaire or sol is a collection of over 80 card games
which are easy to play with the aid of a mouse.

%prep
%setup -n %_name-%version

%build
%meson \
	-Ddefault_theme_format='svg-rsvg' \
	%{?_disable_theme_kde:-Dtheme_kde=false} \
	%{?_enable_theme_kde:-Dtheme_kde_path=%_datadir/kf5/carddecks}
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%files -f %_name.lang
%attr(-,root,games) %_bindir/sol
%_libdir/%_name/
%dir %_libexecdir/%_name
%_libexecdir/%_name/ar-cards-renderer
%_desktopdir/*.desktop
%_datadir/%_name/
%_iconsdir/hicolor/*/*/*.*
%_datadir/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%_datadir/metainfo/sol.metainfo.xml
%_man6dir/sol.*
%doc README* TODO COPYING.README

%exclude %_libdir/valgrind/aisleriot.supp

%changelog
* Wed Mar 22 2023 Yuri N. Sedunov <aris@altlinux.org> 3.22.28-alt1
- 3.22.28

* Sat Dec 03 2022 Yuri N. Sedunov <aris@altlinux.org> 3.22.27-alt1
- 3.22.27

* Sat Oct 22 2022 Yuri N. Sedunov <aris@altlinux.org> 3.22.26-alt1
- 3.22.26

* Sun Sep 04 2022 Yuri N. Sedunov <aris@altlinux.org> 3.22.25-alt1
- 3.22.25

* Tue Jun 28 2022 Yuri N. Sedunov <aris@altlinux.org> 3.22.24-alt1
- 3.22.24

* Sun May 29 2022 Yuri N. Sedunov <aris@altlinux.org> 3.22.23-alt1
- 3.22.23

* Fri Apr 01 2022 Yuri N. Sedunov <aris@altlinux.org> 3.22.22-alt1
- 3.22.22

* Sun Mar 06 2022 Yuri N. Sedunov <aris@altlinux.org> 3.22.21-alt1
- updated to 3.22.21-6-ge8d8bffd

* Fri Dec 10 2021 Yuri N. Sedunov <aris@altlinux.org> 3.22.20-alt1
- 3.22.20

* Wed Sep 29 2021 Yuri N. Sedunov <aris@altlinux.org> 3.22.18-alt1
- 3.22.18

* Mon Dec 16 2019 Yuri N. Sedunov <aris@altlinux.org> 3.22.10-alt1
- 3.22.10 (ported to Meson build system)

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.22.9-alt1
- 3.22.9

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.22.8-alt1
- 3.22.8

* Mon Oct 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.7-alt1
- 3.22.7

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.6-alt1
- 3.22.6

* Fri Aug 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt2
- fixed guile binary name

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt1
- 3.22.5

* Fri Nov 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt1
- 3.22.4

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Apr 18 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt0.1
- updated to 3.22.1-9-gb30db7a
- build with guile22

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Sat Mar 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.91-alt1
- 3.7.91

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Thu Oct 11 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Nov 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- first build for Sisyphus

