%define _name calls
%define ver_major 43
%define beta %nil
%define xdg_name org.gnome.Calls

%def_enable man
#12/12 sip  TIMEOUT
%def_disable check

Name: gnome-%_name
Version: %ver_major.3
Release: alt1%beta

Summary: A phone dialer and call handler
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/GNOME/calls

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version%beta.tar.xz

%define glib_ver 2.62
%define handy_ver 1.4.0
%define mm_ver 1.12.0
%define feedback_ver 0.0.1
%define phosh_ver 0.16

Requires: ModemManager >= %mm_ver
Requires: gst-plugins-base1.0
Requires: feedbackd callaudiod
#Requires: phosh >= %phosh_ver

BuildRequires(pre): rpm-macros-meson rpm-build-xdg
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
BuildRequires: pkgconfig(libpeas-1.0)
BuildRequires: pkgconfig(gom-1.0)
BuildRequires: pkgconfig(mm-glib) >= %mm_ver
BuildRequires: pkgconfig(libebook-contacts-1.2)
BuildRequires: pkgconfig(folks)
BuildRequires: pkgconfig(libcallaudio-0.1)
BuildRequires: pkgconfig(libfeedback-0.0) >= %feedback_ver
BuildRequires: pkgconfig(sofia-sip-ua-glib)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: vapi(folks) vapi(libebook-contacts-1.2)
%{?_enable_man:BuildRequires: %_bindir/rst2man}
%{?_enable_check:BuildRequires: xvfb-run /usr/bin/appstreamcli desktop-file-utils libcmocka-devel}

%description
Calls is a dialer for phone calls, initially PSTN calls but eventually
other systems like SIP in future.

%prep
%setup -n %_name-%version%beta

%build
%meson \
%{?_disable_man:-Dmanpages=false}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %_name call-ui

%check
xvfb-run %__meson_test

%files -f %name.lang
%_xdgconfigdir/autostart/%xdg_name-daemon.desktop
%_bindir/%name
%dir %_libdir/%_name
%dir %_libdir/%_name/plugins
%dir %_libdir/%_name/plugins/provider
%_libdir/%_name/plugins/provider/dummy/
%_libdir/%_name/plugins/provider/mm/
%_libdir/%_name/plugins/provider/ofono/
%_libdir/%_name/plugins/provider/sip/
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%{?_enable_man:%_man1dir/%name.1*}
%_desktopdir/%xdg_name.desktop
%_datadir/icons/hicolor/scalable/apps/%xdg_name.svg
%_datadir/icons/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc NEWS README.md

%changelog
* Sun Jan 15 2023 Yuri N. Sedunov <aris@altlinux.org> 43.3-alt1
- 43.3

* Sun Dec 04 2022 Yuri N. Sedunov <aris@altlinux.org> 43.2-alt1
- 43.2

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sat Oct 30 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Fri Jul 16 2021 Yuri N. Sedunov <aris@altlinux.org> 41-alt0.1.alpha
- first build for Sisyphus


