%def_enable snapshot
%define ver_major 8.0

Name: noise
%define _name music
%define xdg_name org.pantheon.%name
%define rdn_name io.elementary.%_name
Version: %ver_major.0
Release: alt1

Summary: The official elementary music player
Group: Sound
License: LGPL-3.0-or-later
Url: https://elementary.io

Vcs: https://github.com/elementary/music.git

%if_disabled snapshot
Source: https://launchpad.net/%name/%{ver_major}.x/%version/+download/%name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Provides: %rdn_name = %EVR
Provides: elementary-%_name = %EVR

%define gst_api_ver 1.0
%define adw_ver 1.4

Requires: elementary-icon-theme
# gstreamer
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(gstreamer-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-pbutils-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-tag-%gst_api_ver)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Quickly queue up and listen to your local music files without any extra
frills. See embedded album artwork. Control playback with media keys or
in the system audio indicator.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %rdn_name

%check
%__meson_test

%files -f %name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%rdn_name.svg
%_datadir/metainfo/%rdn_name.metainfo.xml

%changelog
* Sat Nov 09 2024 Yuri N. Sedunov <aris@altlinux.org> 8.0.0-alt1
- 8.0.0-52-gd7fbb4fc (ported to Granite-7/Libadwaita)

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 5.1.1-alt2
- updated to 5.1.1-148-g4d974d7f (fixed build with meson >= 0.61)

* Mon Jul 19 2021 Yuri N. Sedunov <aris@altlinux.org> 5.1.1-alt1
- updated to 5.1.1-16-g7667b8e5

* Sun Mar 28 2021 Yuri N. Sedunov <aris@altlinux.org> 5.0.5-alt3
- updated to 5.0.5-105-g645684a5
- built against libgranite.so.6

* Sat Oct 31 2020 Yuri N. Sedunov <aris@altlinux.org> 5.0.5-alt2
- updated to 5.0.5-63-g6a112438

* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 5.0.5-alt1
- updated to 5.0.5-7-gc2e1c535

* Thu Apr 25 2019 Yuri N. Sedunov <aris@altlinux.org> 5.0.4-alt1
- updated to 5.0.4-4-gb759f4ba

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 5.0.3-alt1
- updated to 5.0.3-12-g80bcdfda

* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 5.0.2-alt1
- updated to 5.0.2-5-gc49dd991

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt3
- updated to 0.4.2-439-g64bccda
- built against libgranite.so.5

* Thu May 24 2018 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt2
- updated to 0.4.2-382-g7a90c49

* Thu Nov 30 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Wed Aug 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Mon Apr 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.3-alt1
- 0.4.0.3

* Tue Jan 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.2-alt1
- 0.4.0.2

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Fri Sep 13 2013 Igor Zubkov <icesik@altlinux.org> 0.2.4-alt2
- fix build on x86_64

* Thu Sep 12 2013 Igor Zubkov <icesik@altlinux.org> 0.2.4-alt1
- build for Sisyphus

