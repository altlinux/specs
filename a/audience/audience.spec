%def_enable snapshot

%define ver_major 2.8
%define gst_api_ver 1.0
%define _name videos
%define rdn_name io.elementary.%_name

Name: audience
%define xdg_name org.pantheon.%name
Version: %ver_major.4
Release: alt1

Summary: A modern media player
License: GPL-3.0
Group: Video
Url: https://launchpad.net/audience

%if_disabled snapshot
Source: https://github.com/elementary/videos/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/elementary/videos.git
Source: %_name-%version.tar
%endif

Provides: %rdn_name = %version-%release

Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gst-libav

BuildRequires(pre): meson
BuildRequires: gcc-c++ libgranite-devel libclutter-gtk3-devel
BuildRequires: libclutter-gst3.0-devel gst-plugins%gst_api_ver-devel
BuildRequires: vala-tools libgranite-vala
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: gobject-introspection-devel

%description
Audience is a simple, modern media player that makes greater use of
hardware acceleration than most players out there.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install

%find_lang %rdn_name

%files -f %rdn_name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.appdata.xml
%_iconsdir/hicolor/*x*/apps/%rdn_name.svg
%doc README.md

%changelog
* Sun Jul 17 2022 Yuri N. Sedunov <aris@altlinux.org> 2.8.4-alt1
- updated to 2.8.4-18-g6b019cb1

* Tue Mar 08 2022 Yuri N. Sedunov <aris@altlinux.org> 2.8.3-alt1
- updated to 2.8.3-7-gfb79c9ed

* Sat Jan 01 2022 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt1
- updated to 2.8.1-15-g3e4a32a8

* Tue Nov 23 2021 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- updated to 2.8.0-20-gad2924b4

* Mon Jul 19 2021 Yuri N. Sedunov <aris@altlinux.org> 2.7.3-alt1
- updated to 2.7.3-15-gcdaed46f

* Sun Mar 28 2021 Yuri N. Sedunov <aris@altlinux.org> 2.7.2-alt2
- updated to 2.7.2-63-g0607dc5d
- built against libgranite.so.6

* Tue Jul 07 2020 Yuri N. Sedunov <aris@altlinux.org> 2.7.2-alt1
- 2.7.2

* Wed Apr 22 2020 Yuri N. Sedunov <aris@altlinux.org> 2.7.1-alt1
- updated to 2.7.1-3-g3ce47b8

* Tue Dec 03 2019 Yuri N. Sedunov <aris@altlinux.org> 2.7.0-alt1
- updated to 2.7.0-6-g168d1ed

* Thu Jan 17 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- updated to 2.6.3-6-g4c4c239

* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- updated to 2.6.2-46-g635073a

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- 0.2.6

* Fri Jan 12 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt2
- rebuild against libgranite.so.4

* Mon Aug 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Mon Apr 17 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Wed Jan 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.1.2-alt1
- 0.2.1.2

* Fri Jan 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.1.1-alt1
- 0.2.1.1

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.0.2-alt1
- 0.1.0.2

* Sun Jan 05 2014 Igor Zubkov <icesik@altlinux.org> 0.1-alt3.r305
- r305

* Thu Dec 12 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt2.r302
- Make build more verbose

* Thu Dec 12 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt1.r302
- r302

* Sun Sep 22 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt1.r296
- build for Sisyphus

