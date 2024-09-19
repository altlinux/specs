%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define ver_major 47
%define beta %nil
%define httpd /usr/sbin/httpd2
%define modules_path %_sysconfdir/httpd2/modules

Name: gnome-user-share
Version: %ver_major.0
Release: alt1%beta

Summary: Gnome user file sharing
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later
Url: https://www.gnome.org

Vcs: https://gitlab.gnome.org/GNOME/gnome-user-share.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif

%define glib_ver 2.74

Requires: apache2 >= 2.4
Requires: apache2-mod_dnssd >= 0.6

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libselinux-devel
BuildRequires: apache2 apache2-mod_dnssd pkgconfig(systemd)

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
%setup -n %name-%version%beta

%build
%meson -Dhttpd=%httpd \
       -Dmodules_path=%modules_path
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f gnome-user-share.lang
%_libexecdir/%name-webdav
%_desktopdir/%name-webdav.desktop
%_datadir/%name/
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/org.gnome.desktop.file-sharing.gschema.xml
%_userunitdir/%name-webdav.service
%doc README* NEWS

%changelog
* Sun Sep 15 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0-alt1
- 47.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Thu Sep 08 2022 Yuri N. Sedunov <aris@altlinux.org> 43-alt0.1.alpha
- 43.alpha (removed Nautilus extension)

* Wed Mar 30 2022 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt3
- updated to 3_34_0-30-gc31b0a8 (fixed build with meson >= 0.61)

* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt2
- updated to GNOME_USER_SHARE_3_34_0-24-g3432ce7
- fixed meson options

* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0 (ported to Meson build system)

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0.1-alt1
- 3.32.0.1

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Feb 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.27.90-alt1
- 3.27.90

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Wed Aug 31 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

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

