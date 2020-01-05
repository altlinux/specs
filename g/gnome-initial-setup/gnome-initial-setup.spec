%define _userunitdir %(pkg-config systemd --variable systemduserunitdir)

%define ver_major 3.34
%define gst_api_ver 1.0
%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

%def_disable software_sources
%def_enable cheese

Name: gnome-initial-setup
Version: %ver_major.3
Release: alt1

Summary: Bootstrapping your OS
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://live.gnome.org/GnomeOS/Design/Whiteboards/InitialSetup

Source: http://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz

%define nm_ver 1.2
%define nma_ver 1.0
%define glib_ver 2.53.0
%define gtk_ver 3.12.0
%define secret_ver 0.18
%define geoclue_ver 2.4.3
%define packagekit_ver 1.1.4

Requires: gnome-shell >= %ver_major gdm dconf geoclue2 >= %geoclue_ver
Requires: ibus gnome-keyring gnome-getting-started-docs

BuildRequires(pre): meson pkgconfig(systemd)
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libnm-devel >= %nm_ver libnma-devel >= %nma_ver
BuildRequires: libkrb5-devel libpwquality-devel
BuildRequires: libxkbfile-devel libibus-devel librest-devel
BuildRequires: libaccountsservice-devel libgnome-desktop3-devel
BuildRequires: gstreamer%gst_api_ver-devel libclutter-gst3.0-devel
BuildRequires: libgweather-devel libgnome-online-accounts-devel
BuildRequires: gdm-libs-devel iso-codes-devel libpolkit-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libsecret-devel >= %secret_ver
BuildRequires: libgeoclue2-devel >= %geoclue_ver libgeocode-glib-devel
BuildRequires: libwebkit2gtk-devel
BuildRequires: libnm-devel libnma-devel
%{?_enable_cheese:BuildRequires: libcheese-devel}
%{?_enable_software_sources:BuildRequires: pkgconfig(packagekit-glib2) >= %packagekit_ver}

%description
GNOME Initial Setup is an alternative to firstboot, providing
a good setup experience to welcome you to your system, and walks
you through configuring it. It is integrated with gdm.

%prep
%setup

%build
%meson \
	%{?_enable_software_sources:-Dsoftware-sources=enabled}
%meson_build

%install
%meson_install

mkdir -p %buildroot%_localstatedir/lib/%name
mkdir -p %buildroot%_localstatedir/run/%name

%find_lang %name

%pre
useradd -rM -d %_localstatedir/lib/%name -s /sbin/nologin %name &>/dev/null || :

%files -f %name.lang
%_libexecdir/%name
%_libexecdir/%name-copy-worker
%_libexecdir/gnome-welcome-tour
%_sysconfdir/xdg/autostart/gnome-welcome-tour.desktop
%_sysconfdir/xdg/autostart/%name-copy-worker.desktop
%_sysconfdir/xdg/autostart/%name-first-login.desktop
%_datadir/gdm/greeter/applications/%name.desktop
%_datadir/gnome-session/sessions/%name.session
%_datadir/gnome-shell/modes/initial-setup.json
%_datadir/polkit-1/rules.d/20-gnome-initial-setup.rules
%_userunitdir/*
%attr(1770, %name, %name) %dir %_localstatedir/lib/%name
%attr(1777, root, %name) %dir %_localstatedir/run/%name
%doc README NEWS

%changelog
* Sun Jan 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Sun Oct 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Fri Apr 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sun Sep 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed Aug 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.29.92-alt1
- 3.29.92

* Wed Jun 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt2
- fixed buildreqs

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Sep 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.92-alt1
- 3.21.92

* Tue Apr 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Feb 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Fri Nov 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2.1-alt1
- 3.14.2.1

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Fri Oct 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1.1-alt1
- 3.10.1.1

* Thu Sep 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Jul 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Wed Apr 17 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- 0.8

* Thu Feb 28 2013 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- first build for people/gnome

