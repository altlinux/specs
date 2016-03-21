%define _libexecdir %_prefix/libexec
%define ver_major 3.18
%define httpd /usr/sbin/httpd2
%define modules_path %_sysconfdir/httpd2/modules

Name: gnome-user-share
Version: %ver_major.1
Release: alt1

Summary: Gnome user file sharing
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://www.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: apache2 >= 2.2
Requires: apache2-mod_dnssd >= 0.6

BuildRequires: gnome-common intltool yelp-tools desktop-file-utils
BuildRequires: libgtk+3-devel libnotify-devel libcanberra-gtk3-devel
BuildRequires: libnautilus-devel libselinux-devel libgudev-devel
BuildRequires: apache2 apache2-mod_dnssd

%description
gnome-user-share is a small package that binds together various free
software projects to bring easy to use user-level file sharing to the
masses.

The program is meant to run in the background when the user is logged
in, and when file sharing is enabled a webdav server is started that
shares the $HOME/Public folder. The share is then published to all
computers on the local network using mDNS/rendezvous, so that it shows
up in the Network location in Gnome.

The dav server used is apache, so you need that installed. Avahi or
Howl is used for mDNS support, so you need to have that installed and
mDNSResolver running.

%prep
%setup

%build
%autoreconf
%configure  --with-httpd=%httpd \
	--with-modules-path=%modules_path
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f gnome-user-share.lang
%_libexecdir/%name-webdav
%_desktopdir/%name-webdav.desktop
%_datadir/%name/
%_libdir/nautilus/extensions-3.0/libnautilus-share-extension.so
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/org.gnome.desktop.file-sharing.gschema.xml
#%_sysconfdir/xdg/autostart/%name-*.desktop
%doc README NEWS

%exclude %_libdir/nautilus/extensions-3.0/*.la

%changelog
* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Thu Dec 18 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Fri Nov 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Thu Oct 02 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- first build for Sisyphus

