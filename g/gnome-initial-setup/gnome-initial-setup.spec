%define ver_major 3.14
%define gst_api_ver 1.0
%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

Name: gnome-initial-setup
Version: %ver_major.2
Release: alt1

Summary: Bootstrapping your OS
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://live.gnome.org/GnomeOS/Design/Whiteboards/InitialSetup

Source: http://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz

%define nm_ver 0.9
%define glib_ver 2.36.0
%define gtk_ver 3.11.3
%define secret_ver 0.18
%define geoclue_ver 2.1.2

Requires: dconf gdm geoclue2 >= %geoclue_ver

BuildRequires: intltool
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: NetworkManager-devel >= %nm_ver libnm-gtk-devel
BuildRequires: libkrb5-devel libpwquality-devel
BuildRequires: libxkbfile-devel libibus-devel librest-devel
BuildRequires: libaccountsservice-devel libgnome-desktop3-devel
BuildRequires: gstreamer%gst_api_ver-devel libclutter-gst2.0-devel
BuildRequires: libgweather-devel libgnome-online-accounts-devel
BuildRequires: gdm-libs-devel iso-codes-devel libpolkit-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libcheese-devel
BuildRequires: libsecret-devel >= %secret_ver
BuildRequires: geoclue2-devel >= %geoclue_ver

%description
GNOME Initial Setup is an alternative to firstboot, providing
a good setup experience to welcome you to your system, and walks
you through configuring it. It is integrated with gdm.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

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
%_datadir/gdm/greeter/applications/setup-shell.desktop
%_datadir/gnome-session/sessions/%name.session
%_datadir/gnome-shell/modes/initial-setup.json
%_datadir/polkit-1/rules.d/20-gnome-initial-setup.rules
%attr(1770, %name, %name) %dir %_localstatedir/lib/%name
%attr(1777, root, %name) %dir %_localstatedir/run/%name
%doc README NEWS

%changelog
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

