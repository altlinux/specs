#define git_date .git20120315
%define git_date %nil

%define dbus_version 1.2.12-alt2
%define libdbus_glib_version 0.76

%define ppp_version 2.4.5
%define wpa_supplicant_version 0.7.3-alt3
%define dhcpcd_version 4.0.0

%def_enable systemd
%def_disable wimax
%def_enable introspection

Name: NetworkManager
Version: 0.9.5.95
Release: alt1%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary: Network Link Manager and User Applications
Url: http://www.gnome.org/projects/NetworkManager/
# git://git.freedesktop.org/git/NetworkManager/NetworkManager.git
Source: %name-%version.tar
Source1: %name.conf
Source2: 50-ntpd
Source3: 70-vendor-encap
Source4: 10-netfs
Source5: 20-hostname
Source6: NetworkManager.sysconfig
Source7: 30-efw
Source8: 80-etcnet-post
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

# For tests
BuildPreReq: dbus dhcpcd

BuildPreReq: intltool libgcrypt-devel libtool
BuildRequires: glibc-devel-static iproute2 libnl-devel libwireless-devel ppp-devel
BuildRequires: libdbus-glib-devel >= %libdbus_glib_version
BuildRequires: libpolkit1-devel libnss-devel libgio-devel libuuid-devel gtk-doc
BuildRequires: libgudev-devel
BuildRequires: libgnome-bluetooth-devel
BuildRequires: iptables libsoup-devel
%{?_enable_wimax:BuildRequires: libiWmxSdk-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgudev-gir-devel}
%{?_enable_systemd:BuildRequires: libsystemd-login-devel}

Requires: dbus >= %dbus_version
Requires: wpa_supplicant >= %wpa_supplicant_version
Requires: iproute2 openssl
Requires: ppp = %ppp_version
Requires: dhcpcd >= %dhcpcd_version
Requires: nss >= 3.11.7
Requires: ppp-pppoe
Requires: dnsmasq
Requires: openresolv
Requires: libshell
Requires: ModemManager >= 0.2
Requires: NetworkManager-glib = %version-%release

Conflicts: NetworkManager-vpnc < 0.9.2
Conflicts: NetworkManager-openvpn < 0.9.2
Conflicts: NetworkManager-pptp < 0.9.2
Conflicts: NetworkManager-gnome < 0.9.2

Obsoletes: nmcli

%description
NetworkManager attempts to keep an active network connection available
at all times.  The point of NetworkManager is to make networking
configuration and setup as painless and automatic as possible. If
using DHCP, NetworkManager is intended to replace default routes,
obtain IP addresses from a DHCP server, and change name servers
whenever it sees fit.

%package devel
License: %gpl2plus
Summary: Libraries and headers for adding NetworkManager support to applications
Group: Development/Other
Requires: libdbus-glib >= %libdbus_glib_version
Requires: libdbus-devel >= %dbus_version
Requires: pkgconfig

%description devel
This package contains various headers accessing some NetworkManager
functionality from applications.

%package glib
License: %gpl2plus
Summary: Libraries for adding NetworkManager support to applications that use glib
Group: Development/GNOME and GTK+
Requires: dbus >= %dbus_version

%description glib
This package contains the libraries that make it easier to use some
Network Manager functionality from applications that use glib.

%package glib-devel
Summary: Header files for adding NetworkManager support to applications that use glib.
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release
Requires: %name-glib = %version-%release
Requires: glib2-devel
Requires: pkgconfig
Requires: libdbus-glib-devel >= %libdbus_glib_version

%description glib-devel
This package contains the header and pkg-config files for development
applications using NetworkManager functionality from applications
that use glib.

%package glib-devel-doc
Summary: Development documentation for %name-glib
Group: Development/GNOME and GTK+
Conflicts: %name-glib < %version
BuildArch: noarch

%description glib-devel-doc
This package contains development documentation for %name-glib

%package glib-gir
Summary: GObject introspection data for the NetworkManager
Group: System/Libraries
Requires: %name-glib = %version-%release

%description glib-gir
GObject introspection data for the NetworkManager.

%package glib-gir-devel
Summary: GObject introspection devel data for the NetworkManager
Group: System/Libraries
BuildArch: noarch
Requires: %name-glib-gir = %version-%release
Requires: %name-glib-devel = %version-%release

%description glib-gir-devel
GObject introspection devel data for the NetworkManager.


%prep
%setup
%patch -p1

%build
# Disable remote settings client test.
# It is required X session.
#SUBDIRS=. tests
sed -i 's;^SUBDIRS=\. tests;#SUBDIRS=. tests;' libnm-glib/Makefile.am

%autoreconf
%configure \
    --libexecdir=%_libexecdir/NetworkManager \
    --localstatedir=%_var \
    --disable-static \
    --with-crypto=nss \
    --with-distro=alt \
    --with-dhclient=no \
    --with-dhcpcd=/sbin/dhcpcd \
    --with-docs=yes \
    --with-resolvconf=/sbin/resolvconf \
    --enable-concheck \
    --with-pppd-plugin-dir=%_libdir/pppd/%ppp_version \
    %{subst_enable wimax} \
    --with-tests=yes \
    %{?_enable_systemd:--with-systemdsystemunitdir=/lib/systemd/system} \
%if_enabled systemd
	--with-session-tracking=systemd \
%else
	--with-session-tracking=ck \
%endif
    --enable-introspection=auto \
    --enable-more-warnings=error

%make_build

%install
%makeinstall_std
%find_lang %name
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sysconfdir/NetworkManager/VPN
mkdir -p %buildroot%_sysconfdir/NetworkManager/system-connections
./libtool --mode=install install -m 755 test/nm-online %buildroot%_bindir/
mkdir -p %buildroot/%_var/log/
touch %buildroot/%_var/log/NetworkManager
mkdir -p %buildroot/%_var/lib/NetworkManager
touch %buildroot/%_var/lib/NetworkManager/timestamps
touch %buildroot/%_var/lib/NetworkManager/NetworkManager.state
install -m 0644 %SOURCE1 %buildroot%_sysconfdir/NetworkManager/
install -m 0755 %SOURCE2 %buildroot%_sysconfdir/NetworkManager/dispatcher.d
install -m 0755 %SOURCE3 %buildroot%_sysconfdir/NetworkManager/dispatcher.d
install -m 0755 %SOURCE4 %buildroot%_sysconfdir/NetworkManager/dispatcher.d
install -m 0755 %SOURCE5 %buildroot%_sysconfdir/NetworkManager/dispatcher.d
install -m 0755 %SOURCE7 %buildroot%_sysconfdir/NetworkManager/dispatcher.d
install -m 0755 %SOURCE8 %buildroot%_sysconfdir/NetworkManager/dispatcher.d
install -Dm0644 %SOURCE6 %buildroot%_sysconfdir/sysconfig/%name

%check
make check

%pre
# Workaround for upgrade
[ -d %_var/lib/NetworkManager/timestamps ] &&
rm -rf %_var/lib/NetworkManager/timestamps/ ||:

%post
if /sbin/service messagebus status &>/dev/null; then
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig &>/dev/null ||:
#post_service %name
	if [ $1 -eq 1 ]; then
		/sbin/chkconfig --add NetworkManager
	else
		/sbin/chkconfig NetworkManager resetpriorities ||:
	fi
else
echo "WARNING: NetworkManager requires running messagebus service." >&2
fi

%preun
%preun_service %name
if [ $1 -eq 0 ]; then
    killall -TERM nm-system-settings >/dev/null 2>&1 ||:
fi

%files -f %name.lang
%doc COPYING NEWS AUTHORS README CONTRIBUTING TODO
%_bindir/nm-tool
%_bindir/nm-online
%_bindir/nmcli
%_libdir/pppd/%ppp_version/nm-pppd-plugin.so
%_datadir/NetworkManager
%_datadir/dbus-1/system-services/*.service
%doc %_man1dir/*.*
%doc %_man5dir/*.*
%doc %_man8dir/*.*
%dir %_libexecdir/NetworkManager/
%dir %_libdir/NetworkManager/
%_libdir/NetworkManager/libnm-*.so
%_libexecdir/NetworkManager/nm-*
%_sbindir/*
%_sysconfdir/dbus-1/system.d/*.conf
%config(noreplace) %_sysconfdir/NetworkManager/%name.conf
%_initrddir/NetworkManager
%dir %_sysconfdir/NetworkManager
%dir %_sysconfdir/NetworkManager/dispatcher.d
%dir %_sysconfdir/NetworkManager/VPN
%dir %_sysconfdir/NetworkManager/system-connections
%dir %_var/lib/NetworkManager
%ghost %config(noreplace) %_var/log/NetworkManager
%ghost %config(noreplace) %_var/lib/NetworkManager/NetworkManager.state
%ghost %config(noreplace) %_var/lib/NetworkManager/timestamps
/lib/udev/rules.d/*
%_datadir/polkit-1/actions/*.policy
%_sysconfdir/NetworkManager/dispatcher.d/*
%config(noreplace) %_sysconfdir/sysconfig/%name
%{?_enable_systemd:/lib/systemd/system/%name.service}
%{?_enable_systemd:/lib/systemd/system/%name-wait-online.service}

%files devel
%doc %_datadir/gtk-doc/html/%name
%dir %_includedir/%name
%_includedir/%name/%name.h
%_includedir/%name/NetworkManagerVPN.h
%_includedir/%name/nm-version.h
%_pkgconfigdir/%name.pc

%files glib
%_libdir/libnm-glib.so.*
%_libdir/libnm-glib-vpn.so.*
%_libdir/libnm-util.so.*

%files glib-devel
%dir %_includedir/libnm-glib
%_includedir/libnm-glib/*.h
%_includedir/%name/nm-setting*.h
%_includedir/%name/nm-connection.h
%_includedir/%name/nm-utils*.h
%_pkgconfigdir/libnm-glib.pc
%_pkgconfigdir/libnm-glib-vpn.pc
%_pkgconfigdir/libnm-util.pc
%_libdir/libnm-glib.so
%_libdir/libnm-glib-vpn.so
%_libdir/libnm-util.so

%files glib-devel-doc
%dir %_datadir/gtk-doc/html/libnm-glib
%_datadir/gtk-doc/html/libnm-glib/*
%dir %_datadir/gtk-doc/html/libnm-util
%_datadir/gtk-doc/html/libnm-util/*

%if_enabled introspection
%files glib-gir
%_libdir/girepository-1.0/NMClient-1.0.typelib
%_libdir/girepository-1.0/NetworkManager-1.0.typelib

%files glib-gir-devel
%_datadir/gir-1.0/NMClient-1.0.gir
%_datadir/gir-1.0/NetworkManager-1.0.gir
%endif

%exclude %_libdir/NetworkManager/*.la
%exclude %_libdir/pppd/%ppp_version/*.la

%changelog
* Tue Jul 03 2012 Mikhail Efremov <sem@altlinux.org> 0.9.5.95-alt1
- Treat warrnings as errors again.
- Updated from upstream git (18b0ba499c).
- Updated to 0.9.5.95 (0.9.6-rc1).

* Mon May 21 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.0-alt3
- Use libsystemd-login if systemd support is enabled (closes: #27339).
- atcnet-alt: Fix test's DSO linking.
- sysconfig: Fix comment.
- Drop systemd handling from spec.

* Thu Apr 12 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.0-alt2
- Disable wimax support.
- Updated from upstream git (21bc3ab517):
  + wifi: check the driver reports any encryption caps with nl80211
    (bgo #673717).
  + Fix a few misc issues noticed by Coverity.

* Thu Apr 05 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.0-alt1
- Updated from upstream git (6a1208b526).
- 0.9.4.0.

* Wed Mar 28 2012 Mikhail Efremov <sem@altlinux.org> 0.9.3.995-alt1.git20120315
- Temporary don't treat warrnings as errors.
- initscript: Pass --nocheck to the nmcli.
- etcnet-alt: Updated according with upstream changes.
- alt backend: Updated and cleanup according with upstream changes.
- upstream git snapshot (master branch).

* Thu Mar 01 2012 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt3
- Don't try to unmount network filesystems (closes: #27013).

* Thu Feb 16 2012 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt2
- netfs hook: Fix typo in service name (closes: #26947).
- systemd support: Enable service during install (closes: #26586).

* Fri Nov 11 2011 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Rename src.rpm package again.
- 0.9.2 release.

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.95-alt1.git20111101
- 0.9.1.95 (0.9.2-rc1).

* Tue Sep 20 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.90-alt1.git20110920
- upstream git snapshot (master branch).

* Wed Aug 24 2011 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- 0.9.0 release.

* Tue Jun 07 2011 Mikhail Efremov <sem@altlinux.org> 0.8.9997-alt1.git20110607
- etcnet-alt: Fix adding/removal devices handling.
- Drop fix for env path in python scripts (fixed in upstream).
- upstream git snapshot (master branch) (closes: #21834).

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt3.git20110510
- Rename src.rpm package.

* Wed May 11 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt2.git20110510
- Package NetworkManager-wait-online.service file.
- From upstream git:
    + systemd: tweak NM-wait-online.service.
- Try to reconnect when cable is plugged.

* Tue May 10 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt1.git20110510
- etcnet-alt:
    + Added more tests.
    + Handle MAC from iplink file.
    + Handle route metric.
    + Honor current etcnet network profile (closes: #18435).
    + Various fixes.
    + Allow tab as tokens delimiter.
    + add tests for wired configuration.
    + Allow several IPv4 addresses and routes.
    + Don't send signals if it is unnecessary.
- Add 80-etcnet-post dispatcher script.
- Add 30-efw dispatcher script (closes: #21834).
- Suppress annoying messages.
- init script: Use the new Sleep() method.
- init script: Disconnect all ifaces on stop.
- ntpd hook: Don't create garbage in /tmp.
- Set cp1251 as prefered encoding for Cyrillic langs (closes: #25404).
- Handle write result in signals handler.
- Move nm-version.h to devel subpackage.
- Fix work with dnsmasq-2.57.
- Enable gobject-introspection (by aris@).
- upstream git snapshot (master branch).

* Wed Mar 23 2011 Mikhail Efremov <sem@altlinux.org> 0.8.997-alt1.git20110323
- Workaround for upgrade: remove old timestamps directory.
- etcnet-alt: Drop obsoleted timestamps handling.
- Don't use dns plugins with resolvconf support.
- etcnet-alt: cosmetic cleanup.
- etcnet-alt: Don't send signals if it is unnecessary.
- etcnet-alt: Update connections for device on dir creation.
- Disable remote settings client test.
- Fix env path in tests/examples.
- etcnet-alt: Updated for NM-0.9.
- upstream git snapshot (master branch).

* Mon Feb 21 2011 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt3.git20101126
- Enable systemd support (closes: #25118).
- Minor spec cleanup.

* Fri Nov 26 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt2.git20101126
- etcnet-alt: minor fixes.
- etcnet-alt: Use timestamps for connections.
- etcnet-alt: Fix ONBOOT option handling.
- sysconfig: Set NM_DOWN_CONTROLLED to 'yes' by default again.
- init script: Not start NM if networking is disabled..
- Rewrite and rename 10-mount -> 10-netfs.
- Drop Packager from spec.
- upstream git snapshot (master branch).

* Thu Nov 11 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt2.git20101106
- Ensure that dhcp client is exited before start an another one.
- Fix source tarball and general patch packaging.
- Add /etc/sysconfig/NetworkManager config.
- Enable tests.
- test-keyfile: drop dbus stuff.

* Sat Nov 06 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1.git20101106
- drop alt-set-iwconfig-essid.patch.
- upstream git snapshot
    (almost corresponds with 0.8.2 release, but builded from master branch).

* Tue Sep 21 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt3.git20100914
- add 20-hostname dispatcher script
    (Call update_chrooted when hostname is changed).
- Don't lost hostnames mapped to 127.0.0.1 and ::1.

* Tue Sep 14 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100914
- add versioned dependency on NetworkManager-glib.
- upstream git snapshot (master branch).

* Thu Jul 22 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100722
- spec cleanup
- upstream git snapshot
    (almost corresponds with 0.8.1 release, but builded from master branch).

* Wed Jun 30 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100628
- Allow sending sleep/wake signals for clients in active sessions (tnx shrek@)

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1.git20100628
- NetworkManager.conf: Explicitly specify dhcpcd as DHCP client.
- upstream git snapshot (master branch).

* Fri May 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt2.git20100525
- etcnet-alt: fix connectons export.

* Tue May 25 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt1.git20100525
- Not ignore modems with 'bluetooth' driver
- upstream git snapshot
- Move checking for the X server presence to _set_hostname().

* Thu Apr 29 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt3.git20100427
- fix self-inheritance of NMDHCPDhcpcd.
- rename nm-system-settings.conf -> NetworkManager.conf.
- add etcnet-alt description to man page.
- upstream git snapshot

* Fri Mar 12 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt2
- fix X server finding while changing hostname.

* Sat Feb 27 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- 0.8.0 release

* Thu Feb 04 2010 Mikhail Efremov <sem@altlinux.org> 0.7.999-alt1.git20100204
- package docs/spec.html.
- Don't package ChangeLog.
- upstream git snapshot

* Wed Jan 13 2010 Mikhail Efremov <sem@altlinux.org> 0.7.998-alt2
- build with pppd 2.4.5.

* Sat Jan 09 2010 Mikhail Efremov <sem@altlinux.org> 0.7.998-alt1
- 0.7.998 (0.8-rc2)

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 0.7.997-alt1.git20091209
- upstream git snapshot

* Tue Dec 01 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt3.git20091124
- etcnet-alt: allow connections without default gateway.
- init script: change pidfile path.
- fix localstatedir path.

* Tue Nov 24 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt2.git20091124
- init script: killall nm-system-settings again.
- upstream git snapshot

* Mon Nov 09 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt2.git20091026
- fix cooperation between dnsmasq and resolvconf.
- etcnet-alt: bind mac address to connections.

* Wed Oct 28 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091026
- Don't create default wired connection.
- init script: remove haldaemon reqiures.
- init script: remove killall system-setting.
- etcnet-alt plugin updated.
- 0.7.996 (upstream git snapshot)

* Wed Oct 21 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1.997-alt1
- 0.7.1.997 (0.7.2-rc3)

* Mon Oct 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt9.git20091005
- Build libnm-util docs again.
- kill usage of sha1 according with upstream changes.
- upstream git snapshot (NETWORKMANAGER_0_7 branch)

* Sun Aug 23 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt9.git20090716
- init script: taking down devices before NM start.
- libnm-util: fix setting wireless security.
- etcnet-alt: fixed proto WPA2 from wpa_supplicant.conf.

* Thu Aug 20 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt8.git20090716
- Don't write resolv.conf if resolvconf failed.

* Thu Jul 16 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt7.git20090716
- upstream git snapshot (NETWORKMANAGER_0_7 branch)
- added 10-mount dispatcher script

* Mon Jul 06 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt6
- build with libudev.
- etcnet-alt: fixed build without libgio.
- fixed exit status of 70-vendor-encap.

* Tue Jun 30 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt5
- cherry-picked from upstream git:
	+ wifi: don't bring device up if it's rfkilled.
	+ serial: use termios for better compatibility (rh #464760).
- added 70-vendor-encap dispatcher script.

* Wed May 13 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt4
- from upstream git:
  dns: fix handling of searches and domains in resolv.conf

* Tue Apr 28 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt3
- ignore interface if 'options' file present and NM_CONTROLLED
  not set.

* Tue Apr 21 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2
- Remove 'invalid' tag from connections when cable was unplugged
  and plugged again.

* Wed Apr 15 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Release 0.7.1

* Mon Apr 13 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt5
- etcnet-alt: fixed handling multiple networks from
  wpa_supplicant.conf.
- added 'sleep' and 'wake' init script commands.

* Fri Apr 10 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt4
- etcnet-alt: don't return secrets in the GetSettings handler
- build development documentation

* Thu Apr 09 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt3
- Set hostname if no X server present.
- etcnet-alt plugin: implement 'get hostname' property.
- use 'action' for sysctl in init script.
- use '--persist' nm-dispatcher option.
- avoid nm-dispatcher error message.

* Tue Apr 07 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt2
- use own dispatcher script for ntpd

* Mon Apr 06 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt1
- 0.7.0.100 (0.7.1-rc4)

* Fri Apr 03 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt7
- call dhcpcd hook for ntpd

* Tue Mar 24 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt6
- use /etc/net/ifaces/default for creating connections 
	even if /etc/net/ifaces/<iface> not exists.

* Mon Mar 23 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt5
- Fix possible crash when resynchronizing devices if HAL restarts
	(from upstream git)

* Tue Mar 17 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt4
- update-chrooted dispatcher script is removed

* Tue Mar 17 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt3
- enable resolvconf support
- don't backup resolv.conf anymore

* Fri Mar 13 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt2
- init script start/stop priority changed from '40 90' to '12 90'
	(close ALT bug #19002)

* Thu Mar 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt1
- 0.7.0.99 (0.7.1-rc3)

* Thu Feb 26 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.98-alt1
- 0.7.0.98 (0.7.1-rc2)
- pack source as tar instead tar.gz.

* Thu Feb 19 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.97-alt1
- 0.7.0.97 (0.7.1-rc1)
- spec cleanup
- fix keyfile plugin test build.

* Fri Feb 13 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt19
- also monitoring /etc/net/ifaces/ directory.
- fix segfault when file is deleted from /etc/net/ifaces/*/.

* Mon Jan 26 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt18
- use dhcpcd 4 

* Tue Dec 30 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt17
- enable debug message again
- not check frequency matching

* Fri Dec 26 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt16
- alt-set-iwconfig-essid.patch update.
- nm-device-wifi.c: disable debug message.

* Tue Dec 23 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt15
- alt-set-iwconfig-essid.patch updated.
- init script start/stop priority changed from '98 02' to '40 90'.

* Fri Dec 19 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt14
- save/restore resolv.conf
- some fixes in etcnet-alt plugin (close ALT bug #16736, etc)

* Mon Dec 15 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt13
- create /etc/NetworkManager/system-connections directory.
- kill nm-system-settings when service stop.

* Fri Dec 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt12
- enable keyfile plugin
- fix segmentation fault in keyfile plugin
- fix reading routes

* Mon Dec 08 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt11
- remove NetworkManager-devel -> NetworkManager requires(close #18129)
- alt-dhcp-client-pid.patch is added (close #18021).
- remove device from hash table before sending signal.
- src/nm-netlink-monitor.c: fix function call.

* Wed Dec 03 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt10
- Release NetworkManager 0.7

* Wed Nov 26 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt9.svn.r4326
- don't create default connection in nm-system-settings daemon 
	(nm-applet do it)

* Tue Nov 25 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt8.svn.r4326
- dnsmasq requires is added

* Mon Nov 24 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt7.svn.r4326
- new svn snapshot
- etcnet-alt plugin updated according to upstream code changes
- fix WEP keys reading

* Fri Nov 21 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt7.svn.r4229
- ldconfig removed (obsolete)
- don't restart service when upgrade (close #17275)
- etcnet-alt plugin can read wireless settings 
	from wpa_supplicant.conf (WPA and WEP)

* Wed Nov 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt6.svn.r4229
- fix zombies bug

* Wed Nov 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt5.svn.r4229
- new svn snapshot
- NetworkManager-0.7.0-alt-no-strict-aliasing.patch,
  NetworkManager-0.7.0-alt-no_check_dhclient.patch and
  NetworkManager-0.7.0-alt-supplicant_interface.patch
	removed (obsolete)
- alt-set-iwconfig-essid.patch	
	(dirty patch for set essid when connecting to wireless networks)
- alt-no-update-hostname.patch
- update-chrooted dispatcher script is added
- fix preun
- ppp-pppoe requires is added

* Mon Oct 27 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt5.svn.r4209
- new svn revision 

* Thu Oct 02 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt5.svn.r3930
- expiremental patch for not exposyng system connections to user
- expiremental dirty patch to not set DISCONNECTED state when there are routes 

* Tue Aug 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt4.svn.r3930
- new svn snapshot
- %post updated (D-Bus config reload; add %post_service)

* Wed Aug 06 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt4.svn20080722
- spec cleanup
- split NetworkManager-glib on NetworkManager-glib and NetworkManager-glib-devel
- NetworkManager-0.7.0-alt-kill_supplicant.patch is added
	(not kill all wpa_supplicant, only for managed interfaces)
- NetworkManager-0.7.0-alt-supplicant_interface.patch
	(release the interface when NM exit)

* Mon Jul 28 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.2.svn20080722
- update  NetworkManager-0.7.0-alt-dhcpcd_opt.patch ("-K" option is added)

* Wed Jul 23 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.1.svn20080722
- version for dhcpcd 4

* Tue Jul 22 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.svn20080722
- new svn snapshot (3842)
- .la files are not packaged (close #15840)

* Wed May 28 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.svn20080527
- new svn snapshot (3694)
- nm-system-settings plugin is completely rewritten

* Tue May 13 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.svn20080428
- reading "WPA_DRIVER" from "/etc/net/ifaces/<interface>/options" is added

* Mon May 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.svn20080428
- killall wpa_supplicant on start
- nm-system-settings plugin update

* Tue Apr 29 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080428
- new svn snapshot (3614)
- dhcpcd-1.3.x -> dhcpcd-3.0.x
- spec cleanup

* Tue Apr 22 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080419
- initial build

