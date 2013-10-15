%define ver_major 3.10
%define gst_api_ver 1.0
%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

Name: gnome-initial-setup
Version: %ver_major.1.1
Release: alt1

Summary: Bootstrapping your OS
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://live.gnome.org/GnomeOS/Design/Whiteboards/InitialSetup

Source: http://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz

Requires: dconf gdm

%global nm_ver 0.9
%global glib_ver 2.29.4
%global gtk_ver 3.9.11

BuildRequires: intltool
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: NetworkManager-devel >= %nm_ver libnm-gtk-devel
BuildRequires: libkrb5-devel libpwquality-devel
BuildRequires: libxkbfile-devel libibus-devel
BuildRequires: libaccountsservice-devel libgnome-desktop3-devel
BuildRequires: gstreamer%gst_api_ver-devel libclutter-gst2.0-devel
BuildRequires: libgweather-devel libgnome-online-accounts-devel
BuildRequires: gdm-libs-devel iso-codes-devel libpolkit-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel

%description
GNOME Initial Setup is an alternative to firstboot, providing
a good setup experience to welcome you to your system, and walks
you through configuring it. It is integrated with gdm.

%prep
%setup

%build
pushd egg-list-box
%configure --disable-static
popd

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
%_datadir/gdm/greeter/applications/%name.desktop
%_datadir/gdm/greeter/applications/setup-shell.desktop
%_datadir/gnome-session/sessions/%name.session
%_datadir/gnome-shell/modes/initial-setup.json
%_datadir/polkit-1/rules.d/20-gnome-initial-setup.rules
%attr(1770, %name, %name) %dir %_localstatedir/lib/%name
%attr(1777, root, %name) %dir %_localstatedir/run/%name
%_sysconfdir/xdg/autostart/gnome-initial-setup-first-login.desktop
%doc README NEWS

%changelog
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

