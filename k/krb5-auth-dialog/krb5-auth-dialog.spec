%define ver_major 43
%define xdg_name org.gnome.KrbAuthDialog
%define gtk_api_ver 3.0

%def_with pkcs11

Name: krb5-auth-dialog
Version: %ver_major.0
Release: alt1

Summary: Kerberos 5 authentication dialog
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://redhat.com

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.58
%define gtk_ver 3.14
%define gcr_ver 3.5.5

%{?_with_pkcs11:Requires: libopensc}

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson flex
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: pkgconfig(gcr-3) >= %gcr_ver
BuildRequires: libkrb5-devel libpam-devel
BuildRequires: yelp-tools /usr/bin/appstream-util
%{?_with_pkcs11:BuildRequires: libopensc}

%description
krb5-auth-dialog is a simple dialog that monitors kerberos tickets, and
pops up a dialog when they are about to expire.

%prep
%setup

%build
%meson \
    %{?_with_pkcs11:-Dpkcs11='%_libdir/pkcs11/opensc-pkcs11.so'}
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/*
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/libka-plugin-afs.so
%_libdir/%name/plugins/libka-plugin-dummy.so
%_libdir/%name/plugins/libka-plugin-gnomelock.so
%_libdir/%name/plugins/libka-plugin-pam.so
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/*/*.*
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%name.metainfo.xml
%_sysconfdir/xdg/autostart/%name.desktop
%_man1dir/*
%doc AUTHORS NEWS README*


%changelog
* Wed Oct 12 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0 (ported to Meson build system)

* Sat Nov 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Thu Jul 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Oct 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Thu Jun 19 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Thu Mar 28 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Sat Feb 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.90-alt1
- 2.91.90

* Sun Sep 12 2010 Yuri N. Sedunov <aris@altlinux.org> 0.17-alt1
- 0.17

* Tue Jun 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.16-alt1
- 0.16

* Sat Apr 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt1
- 0.15

* Fri Nov 20 2009 Yuri N. Sedunov <aris@altlinux.org> 0.14-alt2
- patch to build against libnm-glib

* Sun Nov 01 2009 Yuri N. Sedunov <aris@altlinux.org> 0.14-alt1
- 0.14

* Thu Oct 29 2009 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt2
- rebuild against new NetworkManager-glib

* Mon Sep 28 2009 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13
- updated buildreqs

* Tue May 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- new version
- updated buildreqs

* Mon May 04 2009 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- first build for Sisyphus



