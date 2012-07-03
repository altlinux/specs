%def_disable debug

Name: obex-data-server
Version: 0.4.6
Release: alt1

Summary: D-Bus service for Obex access
License: %gpl2plus
Group: System/Servers
Url: http://tadas.dailyda.com/blog/
Packager: Mobile Development Team <mobile at packages.altlinux.org>

Source: http://tadas.dailyda.com/software/%name-%version.tar.gz
Source2: obex-data-server.conf

# From configure.in
%define glib_ver 2.10.0
%define dbus_ver 0.70
%define bluez_ver 4.00
%define openobex_ver 1.3

BuildPreReq: rpm-build-licenses
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libdbus-glib-devel >= %dbus_ver
BuildPreReq: libbluez-devel >= %bluez_ver
BuildPreReq: libopenobex-devel >= %openobex_ver
BuildPreReq: libgdk-pixbuf-devel
BuildPreReq: libusb-compat-devel

BuildRequires: glib2-devel libgtk+2-devel libgio-devel libgtk+2-common-devel
BuildRequires: intltool

%description
obex-data-server is a D-Bus service to allow sending and receiving files
using the ObexFTP and Obex Push protocols, common on mobile phones and
other Bluetooth-equipped devices.

%prep
%setup -q
# cp -f %SOURCE2 data/obex-data-server.conf

%build
%configure \
	%{subst_enable debug} \
	--enable-bip=gdk-pixbuf

%make_build

%install
%make_install install DESTDIR=%buildroot
install -D -m644 data/obex-data-server.conf %buildroot%_sysconfdir/dbus-1/system.d/obex-data-server.conf

%files
%doc COPYING dbus-api.txt ChangeLog AUTHORS NEWS
# %doc test/ods-dbus-test.c test/ods-server-test.py test/ods-session-test.py
%_bindir/obex-data-server
%_datadir/dbus-1/services/obex-data-server.service
%dir %_sysconfdir/obex-data-server
%config %_sysconfdir/obex-data-server/*.xml
%config %_sysconfdir/dbus-1/system.d/obex-data-server.conf
%_man1dir/*.gz

%changelog
* Tue Jan 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Wed Dec 01 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.5-alt2
- fix buildreq

* Thu Sep 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.5-alt1
- 0.4.5

* Tue Apr 07 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.4-alt4
- changed libusb-devel to libusb-compat-devel for buildrequires

* Mon Mar 02 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.4-alt3
- build without --enable-system-config, but install dbus config manually

* Mon Feb 16 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.4-alt2
- use original dbus config

* Mon Feb 09 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.4-alt1
- 0.4.4
- build with --enable-system-config
- add config for dbus (thx to shrek@)

* Sat Feb 07 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Thu Jun 26 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt1
- Initial package for ALTLinux (based on fedora spec)

