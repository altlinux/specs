%define nm_version 0.9.5.95
%define nm_applet_version 0.9.5.95
%define git_date %nil
#define git_date .git20111101
%define gtkver 3

Name: NetworkManager-openvpn
Version: 0.9.5.95
Release: alt1%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary: NetworkManager VPN plugin for OpenVPN
Url: http://www.gnome.org/projects/NetworkManager
# git://git.gnome.org/network-manager-openvpn
Source0: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgnome-keyring-devel perl-XML-Parser
BuildRequires: intltool
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: NetworkManager-glib-devel >= %nm_version
BuildRequires: libgtk+%gtkver-devel

Requires: NetworkManager   >= %nm_version
Requires: openvpn          >= 2.1

%description
NetworkManager-openvpn provides VPN support to NetworkManager for
OpenVPN.

%package gnome
License: %gpl2plus
Summary: GNOME applications for %name
Group: Graphical desktop/GNOME
Requires: shared-mime-info >= 0.16
Requires: gnome-keyring
Requires: NetworkManager-gnome >= %nm_applet_version
Requires: NetworkManager-openvpn = %version-%release

%description gnome
This package contains GNOME applications for use with
NetworkManager panel applet.

%prep
%setup
#patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
	--with-gtkver=%gtkver
%make_build

%install
%makeinstall_std
%find_lang %name

%check
make check

%post
if /sbin/service messagebus status &>/dev/null; then
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig &>/dev/null ||:
else
echo "WARNING: %name requires running messagebus service." >&2
fi

%files
%doc AUTHORS README
%_libexecdir/NetworkManager/nm-openvpn-service
%_libexecdir/NetworkManager/nm-openvpn-service-openvpn-helper
%dir %_sysconfdir/NetworkManager/VPN
%_sysconfdir/NetworkManager/VPN/nm-openvpn-service.name
%_sysconfdir/dbus-1/system.d/nm-openvpn-service.conf

%files gnome -f %name.lang
%_libdir/NetworkManager/libnm-openvpn-properties.so*
%_libexecdir/NetworkManager/nm-openvpn-auth-dialog
#_datadir/applications/nm-openvpn.desktop
%_datadir/gnome-vpn-properties/*
#_datadir/icons/hicolor/*/*/*.png

%exclude %_libdir/NetworkManager/*.la

%changelog
* Wed Jul 04 2012 Mikhail Efremov <sem@altlinux.org> 0.9.5.95-alt1
- Updated to 0.9.5.95 (0.9.6-rc1).

* Thu Apr 05 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.0-alt1
- Updated from upstream git (f9b6f747e5).
- 0.9.4.0.

* Fri Nov 11 2011 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Rename src.rpm package again.
- 0.9.2 release.

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.95-alt1.git20111101
- 0.9.1.95 (0.9.2-rc1).

* Wed Aug 24 2011 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- 0.9.0 release.

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt2
- Build with GTK+3.
- Rename src.rpm package.

* Tue May 10 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt1
- Enable tests.
- Minor spec cleanup.
- 0.8.999 (0.9-rc2).

* Wed Mar 23 2011 Mikhail Efremov <sem@altlinux.org> 0.8.995-alt1.git20110314
- Changed libexecdir to %%_libexecdir/NetworkManager.
- upstream git snapshot (master branch).

* Thu Nov 11 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt2.git20101106
- Fix source tarball and general patch packaging.

* Mon Nov 08 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1.git20101106
- upstream git snapshot
    (almost corresponds with 0.8.2 release, but builded from master branch).

* Tue Sep 14 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1.git20100914
- upstream git snapshot (master branch).

* Thu Jul 22 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
- rename NMVpnPluginUiInterface fields again.
- 0.8.1 release

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt1.git20100628
- upstream git snapshot

* Tue May 25 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt1.git20100525
- rename NMVpnPluginUiInterface fields
- upstream git snapshot

* Wed Apr 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.git20100427
- upstream git snapshot

* Sat Feb 27 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- 0.8.0 release

* Thu Feb 04 2010 Mikhail Efremov <sem@altlinux.org> 0.7.999-alt1.git20100204
- Don't package ChangeLog.
- upstream git snapshot

* Sat Jan 02 2010 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt2.git20091124
- enable script-security option for OpenVPN 2.1.

* Tue Nov 24 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091124
- upstream git snapshot

* Wed Oct 28 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091028
- upstream git snapshot

* Wed Oct 21 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.git20091021
- fix 'gnome' subpackage requires
- upstream git snapshot (NETWORKMANAGER_0_7 branch)

* Mon Oct 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.git20091005
- upstream git snapshot (NETWORKMANAGER_0_7 branch)

* Wed Apr 15 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Release 0.7.1

* Thu Mar 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt1
- 0.7.0.99 (0.7.1-rc3)

* Tue Mar 03 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.97-alt2
- GNOME stuff moved to NetworkManager-openvpn-gnome

* Thu Feb 19 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.97-alt1
- 0.7.0.97 (0.7.1-rc1)

* Wed Dec 03 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt5
- Release NetworkManager 0.7

* Mon Dec 01 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt4.svn.r4326
- no OpenVPN 2.1 options (close #18034)

* Tue Nov 25 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.svn.r4326
- BuildRequires fixed

* Tue Nov 25 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.svn.r4326
- new svn snapshot
- removed obsolete post/postun macros calls
- update summary

* Tue Nov 11 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.svn.r4229
- new svn snapshot

* Wed Aug 13 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.svn.r3930
- new svn snapshot
- BuildRequires updated
- %post updated: D-Bus config reload

* Tue Jul 22 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.svn20080722
- new svn snapshot (3842)

* Thu May 29 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.svn20080527
- spec fixed

* Wed May 28 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080527
- initial build

