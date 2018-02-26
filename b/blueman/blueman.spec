%define _libexecdir %_prefix/libexec

Name: blueman
Version: 1.23
Release: alt1
Summary: The GTK+ bluetooth management utility
License: GPLv3
Group: System/Libraries
Url: http://%name.tuxfamily.org/

Requires: bluez >= 4.35 obex-data-server >= 0.4.3
Requires: GConf polkit-gnome
Provides: bluez-gnome

Source: %name-%version.tar

BuildRequires: intltool libbluez-devel libgtk+2-devel libstartup-notification-devel python-module-Pyrex
BuildRequires: python-module-dbus python-module-pygobject-devel python-module-pygtk-devel python-module-notify

%description
Blueman is a GTK+ bluetooth management utility for GNOME using bluez
dbus backend.  The aim is to create a full featured graphical bluetooth
manager for Linux.

Features:

    * Easy to use interface
    * Storing Favourite devices
    * Send files
    * Browse files on devices
    * List all seen devices
    * View Local/Remote Device information
    * View transfer speeds and link quality
    * Configure local devices
    * Manage Pairing (Bonding)
    * Host/Connect to Personal Area Networks
    * Bind services to /dev/rfcomm ports, for eg. connecting via gprs
    * Connect and receive connections from: audio, network, input and serial devices 

%prep
%setup

subst 's/DBusServiceUnknownError/DBusException/' blueman/*/*.py
find -name Makefile.am | xargs sed -i 's,pythondir,pyexecdir,'

%build
%autoreconf
%configure \
	--with-dhcp-config=%_sysconfdir/dhcp/dhcpd.conf \
	--libexecdir=%_libexecdir \
	--enable-polkit \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%python_sitelibdir -name \*.la -delete

mkdir -p %buildroot%_altdir
cat > %buildroot%_altdir/%name <<EOF
%_bindir/bluetooth-sendto	%_bindir/blueman-sendto	20
EOF

%find_lang %name

%files -f %name.lang
%_altdir/%name
%_sysconfdir/dbus-1/system.d/org.%name.Mechanism.conf
%_sysconfdir/xdg/autostart/%name.desktop
%_bindir/blue*
%_libexecdir/%name-mechanism
%_libdir/nautilus-sendto/plugins/libnstblueman.so
%python_sitelibdir/blueman
%python_sitelibdir/_blueman.so
%exclude %python_sitelibdir/blueman/plugins/applet/AppIndicator.py*
%_desktopdir/%name-manager.desktop
%_datadir/%name
%_datadir/dbus-1/services/%name-applet.service
%_datadir/dbus-1/system-services/org.%name.Mechanism.service
%_datadir/polkit-1/actions/org.blueman.policy
%_iconsdir/hicolor/*/apps/%name.*
%_man1dir/%name-*.1*

%changelog
* Wed Jun 20 2012 Mikhail Pluzhnikov <amike@altlinux.ru> 1.23-alt1
- New release 1.23
- Build "sendto" plugin for nautilus
- Do not package AppIndicator.py

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.21-alt4.1
- Rebuild with Python-2.7

* Sun Aug 07 2011 Mykola Grechukh <gns@altlinux.ru> 1.21-alt4
- dependency on notification-daemon dropped (closes: #25995)

* Thu Apr 07 2011 Mykola Grechukh <gns@altlinux.ru> 1.21-alt3
- merely rebuilt

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.21-alt2.1
- Rebuilt with python 2.6

* Fri Nov 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.21-alt2
- enabled polkit-1

* Wed Oct 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.21-alt1
- 1.21

* Sun Oct 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.20-alt2
- enabled hal

* Sun Oct 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.20-alt1
- 1.20

* Thu Aug 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt9
- removed PulseAudio plugin

* Mon Aug 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt8
- updated russian translation

* Sat Aug 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt7
- fixed dhcpd.conf path

* Sun Jul 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt6
- added requires notification-daemon (closes: #20424)

* Thu Jun 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt5
- added alternatives for bluetooth-sendto

* Thu Jun 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt4
- removed requires python-module-pybluez

* Sat May 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt3
- obsoletes bluez-gnome (closes: #20155)

* Fri May 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt2
- provides /usr/bin/bluetooth-sendto, bluez-gnome

* Sun Apr 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt1
- 1.10

* Sat Apr 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.02-alt5
- updated translations

* Wed Apr 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.02-alt4
- To configure bluetooth modems it is authorised to all

* Tue Apr 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.02-alt3
- fixed NetworkManager support

* Wed Mar 18 2009 Alexey Rusakov <ktirf@altlinux.org> 1.02-alt2
- Replaced libbluez4 with bluez runtime dependency.

* Thu Mar 12 2009 Alexey Rusakov <ktirf@altlinux.org> 1.02-alt1
- New version (1.0.2).
- Updated dependencies.
- Updated download link, build and install sequence, files list.

* Fri Dec 05 2008 Alexey Rusakov <ktirf@altlinux.org> 0.5-alt1
- New version (0.5).
- Dropped post/postun scripts, since they are no more needed.
- Updated download URL.
- Pybluez dependency is back, fixing ALT Bug 17417.
- Repocop warnings fixed:
  + Packager tag added;
  + additional fd.o categories in the desktop file appended.

* Mon Mar 03 2008 Alexey Rusakov <ktirf@altlinux.org> 0.3-alt3
- Removed pybluez requirement, looks like it's not needed.

* Sat Mar 01 2008 Alexey Rusakov <ktirf@altlinux.org> 0.3-alt2
- Added %%update_menus/%%clean_menus to the package scripts (thanks to
  repokop).

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.3-alt1.1
- Rebuilt with python-2.5.

* Sat Dec 29 2007 Alexey Rusakov <ktirf@altlinux.org> 0.3-alt1
- The first package for Sisyphus.

