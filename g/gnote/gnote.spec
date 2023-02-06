%def_disable snapshot

%define rdn_name org.gnome.Gnote
%define _rdn_name org.gnome.gnote
%define ver_major 43
%define api_ver %ver_major
%define beta %nil
%define _libexecdir %_prefix/libexec
%def_without x11_support
%def_disable check

Name: gnote
Version: %ver_major.1
Release: alt1%beta

Summary: Note-taking application
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://wiki.gnome.org/Apps/Gnote

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

%define gtk_ver 3.22.20
%define gtkmm_ver 3.22.20
%define glibmm_ver 2.62
%define gspell_ver 1.6
%define libsecret_ver 0.8

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++
BuildRequires: yelp-tools desktop-file-utils
BuildRequires: pkgconfig(glibmm-2.4)  >= %glibmm_ver
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(gtkmm-3.0) >= %gtkmm_ver
BuildRequires: pkgconfig(glib-2.0) >= 2.32
BuildRequires: pkgconfig(libxml-2.0) pkgconfig(libxslt)
BuildRequires: pkgconfig(gspell-1) >= %gspell_ver
BuildRequires: pkgconfig(libsecret-1) >= %libsecret_ver
BuildRequires: pkgconfig(uuid)
%{?_enable_check:BuildRequires: libunittest-cpp-devel}

%description
Gnote is a desktop note-taking application which is simple and easy to use.
It lets you organize your notes intelligently by allowing you to easily link
ideas together with Wiki style interconnects. It is a port of Tomboy to C++
and consumes fewer resources.

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
%_bindir/%name
%_libdir/lib%name-%api_ver.so.*
%_libdir/%name/
%_man1dir/%name.*
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/apps/%rdn_name.*
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%_rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.appdata.xml
%_datadir/gnome-shell/search-providers/%rdn_name.search-provider.ini
%doc README* TODO NEWS AUTHORS

%exclude %_libdir/lib%name-%api_ver.so

%changelog
* Mon Feb 06 2023 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Wed Oct 05 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sun Sep 11 2022 Yuri N. Sedunov <aris@altlinux.org> 43-alt0.5.beta
- 43.beta

* Sun Jul 31 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Mon Mar 14 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.5.beta
- 42.beta

* Mon Jan 10 2022 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Sun Oct 31 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Mon Oct 04 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0 (ported to Meson build system)

* Mon Oct 04 2021 Yuri N. Sedunov <aris@altlinux.org> 40.3-alt1
- 40.3

* Sun Jun 13 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Sun May 02 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Sat Mar 27 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Sat Mar 13 2021 Yuri N. Sedunov <aris@altlinux.org> 40-alt0.8.rc
- 40.rc

* Sat Jan 23 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sat Sep 19 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sun Jun 28 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Sun May 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sun Mar 15 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Mar 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Thu Sep 26 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun Apr 14 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Sun Mar 17 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sun Sep 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sun Mar 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Thu Aug 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.0-alt1
- 3.25.0

* Sun Aug 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Sun Mar 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Sun Nov 27 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.1-alt1
- 3.21.1

* Sun May 15 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Sat Mar 26 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sat Nov 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Sun Sep 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Sun Sep 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.1-alt1
- 3.17.1

* Sun Jul 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Jun 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.16.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Mar 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Jan 19 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Sep 30 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14.0-alt1
- 3.14.0

* Wed Mar 26 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.0-alt1
- 3.12.0

* Mon Feb 24 2014 Alexey Shabalin <shaba@altlinux.ru> 3.10.3-alt1
- 3.10.3

* Tue Dec 31 2013 Alexey Shabalin <shaba@altlinux.ru> 3.10.2-alt1
- 3.10.2

* Mon Oct 28 2013 Alexey Shabalin <shaba@altlinux.ru> 3.10.1-alt1
- 3.10.1

* Tue Oct 08 2013 Alexey Shabalin <shaba@altlinux.ru> 3.10.0-alt1
- 3.10.0

* Mon May 13 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Tue Jan 22 2013 Alexey Shabalin <shaba@altlinux.ru> 3.6.2-alt1
- 3.6.2

* Wed Oct 31 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.1-alt1
- 3.6.1

* Fri Oct 26 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Fri Jul 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.1-alt1
- 0.9.1
- upstream drop support for panel applet

* Mon Oct 31 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Thu Oct 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- enable panel applet

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.4-alt2
- Disable panel applet

* Tue May 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt3.2
- Rebuilt with Boost 1.46.1

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt3.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Tue Oct 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.2-alt3
- pre 0.7.3

* Mon May 24 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.2-alt2
- git snapshot bca27f4

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Fri Jan 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Tue Oct 06 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- 0.6.2
- add packager
- update BuildRequires

* Thu Jun 18 2009 Anton Farygin <rider@altlinux.ru> 0.5.0-alt1
- first build for Sisyphus, based on RH spec
