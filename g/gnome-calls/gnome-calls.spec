%define _name calls
%define ver_major 47
%define beta %nil
%define xdg_name org.gnome.Calls

%def_enable man
#12/12 sip  TIMEOUT
%def_disable check

Name: gnome-%_name
Version: %ver_major.0
Release: alt1%beta

Summary: A phone dialer and call handler
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/GNOME/calls

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version%beta.tar.xz

%define glib_ver 2.62
%define adw_ver 1.4.0
%define mm_ver 1.12.0
%define feedback_ver 0.0.1

Requires: ModemManager >= %mm_ver
Requires: gst-plugins-base1.0
Requires: feedbackd callaudiod

BuildRequires(pre): rpm-macros-meson rpm-build-xdg
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: pkgconfig(gom-1.0)
BuildRequires: pkgconfig(mm-glib) >= %mm_ver
BuildRequires: pkgconfig(libebook-contacts-1.2)
BuildRequires: pkgconfig(folks)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libcallaudio-0.1)
BuildRequires: pkgconfig(libfeedback-0.0) >= %feedback_ver
BuildRequires: pkgconfig(sofia-sip-ua-glib)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: vapi(folks) vapi(libebook-contacts-1.2)
%{?_enable_man:BuildRequires: %_bindir/rst2man}
%{?_enable_check:BuildRequires: xvfb-run /usr/bin/appstreamcli desktop-file-utils}

%description
Calls is a dialer for phone calls, initially PSTN calls but eventually
other systems like SIP in future.

%prep
%setup -n %_name-%version%beta

%build
%meson \
    -Dsystemd_user_unit_dir=%_userunitdir \
    %{subst_enable_meson_bool man manpages}
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
%_userunitdir/%_name-daemon.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%{?_enable_man:%_man1dir/%name.1*}
%_desktopdir/%xdg_name.desktop
%_datadir/icons/hicolor/scalable/apps/%xdg_name.svg
%_datadir/icons/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc NEWS README.md

%changelog
* Sat Sep 14 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0-alt1
- 47.0

* Sun Sep 01 2024 Yuri N. Sedunov <aris@altlinux.org> 47-alt0.9.rc.1
- 47.rc.1

* Sat Jun 29 2024 Yuri N. Sedunov <aris@altlinux.org> 46.3-alt1
- 46.3

* Thu Mar 14 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Fri Sep 29 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Sat Sep 02 2023 Yuri N. Sedunov <aris@altlinux.org> 45-alt0.9.rc.0
- 45.rc.0

* Sun Jun 11 2023 Yuri N. Sedunov <aris@altlinux.org> 44.2-alt1
- 44.2

* Sat Apr 22 2023 Yuri N. Sedunov <aris@altlinux.org> 44.1-alt1
- 44.1

* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

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


