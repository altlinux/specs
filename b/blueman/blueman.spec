# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:    blueman
Version: 2.4.3
Release: alt1

Summary: Blueman is a GTK+ Bluetooth Manager
License: GPL-3.0-or-later
Group:   System/Configuration/Hardware
URL:     https://github.com/blueman-project/blueman

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires(pre): rpm-macros-systemd
BuildRequires: meson
BuildRequires: rpm-build-python3 rpm-build-gir
BuildRequires: python3-dev
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: intltool >= 0.35.0
BuildRequires: iproute
BuildRequires: python3-module-Cython >= 0.21
BuildRequires: python3-module-dbus

Requires: bluez
Requires: typelib(Gtk) = 3.0

%add_python3_req_skip gi.repository.GObject

%description
%summary.

%prep
%setup
%patch -p1

%build
%meson  -Dsystemdsystemunitdir=%_unitdir \
	-Dsystemduserunitdir=%_user_unitdir \
	-Ddhcp-config-path=%_sysconfdir/dhcp/dhcpd.conf \
	-Dthunar-sendto=false \
	-Dpolicykit=true \
	-Dpulseaudio=true \
	-Dpythoninstalldir=%python3_sitelibdir \
	-Dsendto-plugins=[]

%meson_build

%install
%meson_install

mkdir -p %buildroot%_altdir
cat > %buildroot%_altdir/%name <<EOF
%_bindir/bluetooth-sendto	%_bindir/blueman-sendto	20
EOF

# replace config
mkdir -p %buildroot%_sysconfdir/dbus-1/system.d
mv %buildroot%_datadir/dbus-1/system.d/org.blueman.Mechanism.conf \
	%buildroot%_sysconfdir/dbus-1/system.d

mkdir -p %buildroot%_presetdir
echo 'enable blueman-mechanism.service' >%buildroot%_presetdir/80-blueman.preset

%find_lang %name

%post
%post_service blueman-mechanism.service

%preun
%preun_service blueman-mechanism.service

%files -f %name.lang
%_altdir/blueman
%doc CHANGELOG.md FAQ README.md
%_bindir/blueman-*
%_unitdir/blueman-mechanism.service
%_presetdir/80-blueman.preset
%_user_unitdir/blueman-applet.service
%_user_unitdir/blueman-manager.service
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.blueman.Mechanism.conf
%_datadir/dbus-1/system-services/org.blueman.Mechanism.service
%_datadir/dbus-1/services/org.blueman.Manager.service
%_datadir/applications/blueman-*.desktop
%_datadir/dbus-1/services/org.blueman.Applet.service
%_datadir/blueman
%_datadir/glib-2.0/schemas/org.blueman.gschema.xml
%_datadir/polkit-1/actions/org.blueman.policy
%_datadir/polkit-1/rules.d/blueman.rules
%_desktopdir/blueman-manager.desktop
%_iconsdir/hicolor/*/*/*
%_libexecdir/blueman-mechanism
%_libexecdir/blueman-rfcomm-watcher
%_man1dir/blueman-*.1*
%python3_sitelibdir/blueman
%python3_sitelibdir/_blueman.so
%_sysconfdir/xdg/autostart/blueman.desktop

%changelog
* Sun Jul 28 2024 Anton Midyukov <antohami@altlinux.org> 2.4.3-alt1
- new version 2.4.3

* Tue Jun 04 2024 Anton Midyukov <antohami@altlinux.org> 2.4.2-alt1
- new version 2.4.2

* Wed Apr 10 2024 Anton Midyukov <antohami@altlinux.org> 2.4.1-alt1
- new version 2.4.1

* Sun Mar 31 2024 Anton Midyukov <antohami@altlinux.org> 2.4-alt1
- new version 2.4
- switch to meson
- disable sendto plugins
- fix Group fiels to 'System/Configuration/Hardware'
- fix post/preun blueman-mechanism.service

* Thu Jan 25 2024 Anton Midyukov <antohami@altlinux.org> 2.3.5-alt2
- fix the location of systemd unit blueman-mechanism.service

* Thu Mar 09 2023 Anton Midyukov <antohami@altlinux.org> 2.3.5-alt1
- new version 2.3.5
- add 'Requires: typelib(Gtk) = 3.0'

* Fri Sep 09 2022 Anton Midyukov <antohami@altlinux.org> 2.3.2-alt1
- new version 2.3.2

* Thu Jul 21 2022 Anton Midyukov <antohami@altlinux.org> 2.3.1-alt1
- new version 2.3.1

* Mon Jun 20 2022 Anton Midyukov <antohami@altlinux.org> 2.2.5-alt1
- new version 2.2.5

* Tue Mar 08 2022 Anton Midyukov <antohami@altlinux.org> 2.2.4-alt1
- new version 2.2.4

* Fri Mar 04 2022 Anton Midyukov <antohami@altlinux.org> 2.2.3-alt1
- new version 2.2.3

* Fri Jan 22 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.4-alt2
- Added changes for P9 compatibility.

* Thu Jan 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.4-alt1
- new version 2.1.4 (Fixes CVE-2020-15238).

* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 2.1.3-alt1
- new version 2.1.3

* Mon Apr 20 2020 Anton Midyukov <antohami@altlinux.org> 2.1.2-alt1
- New release 2.1.2

* Mon Jul 09 2012 Mikhail Pluzhnikov <amike@altlinux.ru> 1.23-alt2
- Fix tray icon name (Closes bug: 27523)

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
