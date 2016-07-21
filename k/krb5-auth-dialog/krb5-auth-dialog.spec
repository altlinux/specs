%define ver_major 3.20
%define gtk_api_ver 3.0
%def_with pkcs11

Name: krb5-auth-dialog
Version: %ver_major.0
Release: alt1

Summary: Kerberos 5 authentication dialog
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://redhat.com

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.28
%define gtk_ver 3.0.0
%define nm_ver 0.8.997
%define notify_ver 0.7
%define control_center_ver 3.0.0

%{?_with_pkcs11:Requires: libopensc}

BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildPreReq: NetworkManager-glib-devel >= %nm_ver
BuildRequires: flex libgio-devel libkrb5-devel libcap-devel libcap-utils libpam-devel
BuildRequires: intltool yelp-tools
BuildRequires: gnome-control-center-devel >= %control_center_ver
%{?_with_pkcs11:BuildRequires: libopensc}

%description
krb5-auth-dialog is a simple dialog that monitors kerberos tickets, and
pops up a dialog when they are about to expire.

%prep
%setup

%build
%configure \
	--disable-schemas-compile \
	--disable-static \
	--enable-network-manager \
	%{?_with_pkcs11:--with-pkcs11=%_libdir/pkcs11/opensc-pkcs11.so}

%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/libka-plugin-dummy.so
%_libdir/%name/plugins/libka-plugin-pam.so
%_libdir/%name/plugins/libka-plugin-afs.so
%_libdir/%name/plugins/libka-plugin-gnomelock.so
%_datadir/applications/%name.desktop
%_datadir/dbus-1/services/org.gnome.KrbAuthDialog.service
%_iconsdir/hicolor/*/*/*.*
%_datadir/glib-2.0/schemas/org.gnome.KrbAuthDialog.gschema.xml
%_datadir/GConf/gsettings/org.gnome.KrbAuthDialog.convert
%_datadir/appdata/%name.appdata.xml
%_sysconfdir/xdg/autostart/*.desktop
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README

%exclude %_libdir/%name/plugins/*.la

%changelog
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



