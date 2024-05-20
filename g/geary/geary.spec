%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define ver_major 46
%define beta %nil
%define xdg_name org.gnome.Geary
# see meson_options.txt
%define profile release

# Elementary OS-specific
%def_disable contractor
%def_enable valadoc
%def_enable libunwind

Name: geary
Version: %ver_major.0
Release: alt1%beta

Summary: Email client
License: LGPL-2.1-or-later
Group: Networking/Mail
Url: https://wiki.gnome.org/Apps/Geary

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.66
%define vala_ver 0.48.11
%define gtk_ver 3.24.24
%define sqlite_ver 3.24
%define gcr_ver 3.10.1
%define webkit_ver 2.30
%define gmime_ver 3.2.4
%define peas_ver 1.24
%define icu_ver 60
%define gee_ver 0.8.5
%define handy_ver 1.2.1
%define webkit_api_ver 4.1

Requires: dconf gnome-keyring gcr

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools >= %vala_ver
BuildRequires: desktop-file-utils yelp-tools libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
BuildRequires: libsqlite3-devel >= %sqlite_ver
BuildRequires: libpeas-devel >= %peas_ver
BuildRequires: iso-codes-devel libgmime3.0-devel >= %gmime_ver
BuildRequires: libnotify-devel libcanberra-devel libgee0.8-devel >= %gee_ver
BuildRequires: pkgconfig(libsoup-3.0) libwebkit2gtk%webkit_api_ver-devel >= %webkit_ver
BuildRequires: libgnome-online-accounts-devel libjson-glib-devel
BuildRequires: libenchant-devel libsecret-devel libxml2-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: gir(Soup) = 3.0 libwebkit2gtk%webkit_api_ver-gir-devel libcanberra-vala
BuildRequires: gcr-libs-devel >= %gcr_ver gcr-libs-vala
BuildRequires: libfolks-devel libfolks-vala libenchant2-devel
BuildRequires: libytnef-devel libdbus-devel libgspell-devel
BuildRequires: pkgconfig(icu-uc) >= %icu_ver
BuildRequires: libgsound-devel libstemmer-devel
%{?_enable_libunwind:BuildRequires: libunwind-devel}
%{?_enable_valadoc:BuildRequires: valadoc}

%description
Geary is an email client built for the GNOME desktop environment.  It
allows you to read and send email with a simple, modern interface.

Visit http://www.yorba.org to read about the current state of.
Geary's development.

%prep
%setup -n %name-%version%beta

%build
%add_optflags -I%_includedir/libytnef
%meson  -Dprofile=%profile \
    %{?_enable_contractor:-Dcontractor=true} \
    %{?_disable_libunwind:-Dlibunwind_optional=true}
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%{?_enable_contractor:%_bindir/%name-attach}
%_libdir/%name/
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_desktopdir/%name-autostart.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/*/*/apps/*
%_iconsdir/hicolor/scalable/actions/*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%{?_enable_contractor:%_datadir/contractor/geary-attach.contract}
%doc AUTHORS NEWS README* THANKS

%changelog
* Mon May 20 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Fri Aug 18 2023 Yuri N. Sedunov <aris@altlinux.org> 44.1-alt1
- 44.1

* Wed Jul 05 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Apr 19 2023 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt2
- updated to 43.0-87-g10f9c133a

* Fri Sep 30 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Thu Mar 24 2022 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt2
- updated to 40.0-52-gc8c7e5e8c from mainline branch
  (fixed build with vala-0.56, updated translations)

* Fri Apr 23 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Wed Apr 14 2021 Yuri N. Sedunov <aris@altlinux.org> 40-alt0.8.rc
- 40

* Tue Mar 16 2021 Yuri N. Sedunov <aris@altlinux.org> 40-alt0.1.alpha
- 40.alpha

* Sun Feb 07 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Sun Oct 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0.1-alt1
- 3.38.0.1

* Thu Aug 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3.1-alt1
- 3.36.3.1

* Sun May 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Sun Mar 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Fri Mar 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Sun Sep 22 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun Aug 04 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Sun Apr 28 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Sun Mar 17 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.13.3-alt1
- 0.13.3

* Thu Mar 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.13.2-alt1
- 0.13.2

* Thu Feb 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- updated to geary-0.13.1-1-g618d33eb

* Sun Feb 17 2019 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0

* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1.1
- updated to 0.12.4-12-gefca27c7
- fixed BR

* Wed Aug 29 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- 0.12.4

* Sat Jul 14 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- 0.12.3

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12.2-alt1
- 0.12.2

* Tue Feb 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.11.3-alt2
- updated to 0.11.0-761-g2f145ac from master branch
- build against gnome-3.23.x libraries

* Sun Dec 25 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.3-alt1
- 0.11.3

* Mon Dec 12 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.2-alt2
- updated to geary-0.11.2-14-gd02629c

* Sun Aug 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.2-alt1
- 0.11.2

* Mon Jun 27 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt1
- 0.11.1

* Sun May 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0

* Sat May 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt2
- updated to 0.10.0-75-g2d9e9b2 (also fixed BGO #763203 and ALT #32058)

* Tue Mar 31 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Tue Feb 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Sat Dec 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Wed Nov 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Wed Oct 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Sat Sep 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Sep 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Thu Aug 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sat Jul 19 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Wed Jul 02 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Mar 03 2014 Igor Zubkov <icesik@altlinux.org> 0.4.3-alt1
- 0.4.3

* Sat Nov 23 2013 Igor Zubkov <icesik@altlinux.org> 0.4.2-alt1
- 0.4.2

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.4.1-alt1
- 0.4.1 trunk (r1119)

* Mon Aug 26 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt3
- Cleanup build requires

* Sat Jun 22 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt2
- Fix desktop file

* Sat Apr 13 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt1
- 0.3.0 -> 0.3.1

* Fri Mar 29 2013 Igor Zubkov <icesik@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

