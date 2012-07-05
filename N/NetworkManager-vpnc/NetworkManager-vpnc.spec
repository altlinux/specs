%define nm_version 0.9.5.95
%define nm_applet_version 0.9.5.95
%define git_date %nil
#define git_date .git20110510
%define gtkver 3

Name: NetworkManager-vpnc
Version: 0.9.5.95
Release: alt1%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary: NetworkManager VPN plugin for vpnc
Url: http://www.gnome.org/projects/NetworkManager/
# git://git.gnome.org/network-manager-vpnc
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgnome-keyring-devel perl-XML-Parser
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: NetworkManager-glib-devel >= %nm_version
BuildRequires: libgtk+%gtkver-devel
BuildRequires: libdbus-devel             >= 1.1
BuildRequires: libpng-devel
BuildRequires: intltool gettext

Requires: NetworkManager   >= %nm_version
Requires: vpnc             >= 0.4

%description
This package contains software for integrating the vpnc VPN software
with NetworkManager and the GNOME desktop

%package gnome
License: %gpl2plus
Summary: GNOME applications for %name
Group: Graphical desktop/GNOME
Requires: shared-mime-info >= 0.16
Requires: gnome-keyring
Requires: NetworkManager-gnome >= %nm_applet_version
Requires: NetworkManager-vpnc = %version-%release

%description gnome
This package contains GNOME applications for use with
NetworkManager panel applet.

%prep
%setup
%patch -p1

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
%doc AUTHORS
%config(noreplace) %_sysconfdir/dbus-1/system.d/nm-vpnc-service.conf
%config(noreplace) %_sysconfdir/NetworkManager/VPN/nm-vpnc-service.name
%_libexecdir/NetworkManager/nm-vpnc-service
%_libexecdir/NetworkManager/nm-vpnc-service-vpnc-helper

%files gnome -f %name.lang
%_libdir/NetworkManager/lib*.so*
%_libexecdir/NetworkManager/nm-vpnc-auth-dialog
%_datadir/gnome-vpn-properties/*
%_desktopdir/nm-vpnc-auth-dialog.desktop
#_datadir/applications/nm-vpnc.desktop

# Seems unused.
%exclude %_datadir/icons/hicolor/48x48/apps/gnome-mime-application-x-cisco-vpn-settings.png

%exclude %_libdir/NetworkManager/*.la

%changelog
* Wed Jul 04 2012 Mikhail Efremov <sem@altlinux.org> 0.9.5.95-alt1
- Updated from upstream git (9fb8461cc0).
- Updated to 0.9.5.95 (0.9.6-rc1).

* Thu Apr 05 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.0-alt1
- Updated from upstream git (3658221c15).
- 0.9.4.0.

* Fri Nov 11 2011 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Rename src.rpm package again.
- 0.9.2 release.

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.95-alt1
- 0.9.1.95 (0.9.2-rc1).

* Wed Aug 24 2011 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- 0.9.0 release.

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt2.git20110510
- Build with GTK+3.
- Rename src.rpm package.
- Package nm-vpnc-auth-dialog.desktop for gnome-shell (tnx aris).

* Tue May 10 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt1.git20110510
- Enable tests.
- Minor spec cleanup.
- upstream git snapshot (master branch).

* Wed Mar 23 2011 Mikhail Efremov <sem@altlinux.org> 0.8.996-alt1.git20110314
- Changed libexecdir to %%_libexecdir/NetworkManager.
- upstream git snapshot (master branch).

* Thu Nov 11 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt2.git20101106
- Fix source tarball and general patch packaging.

* Mon Nov 08 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1.git20101106
- upstream git snapshot
    (almost corresponds with 0.8.2 release, but builded from master branch).

* Tue Sep 14 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1.git20100914
- upstream git snapshot (master branch).

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt1.git20100628
- upstream git snapshot

* Tue May 25 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt1.git20100525
- rename NMVpnPluginUiInterface fields.
- upstream git snapshot

* Wed Apr 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.git20100427
- upstream git snapshot

* Sat Feb 27 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- 0.8.0 release

* Thu Feb 04 2010 Mikhail Efremov <sem@altlinux.org> 0.7.999-alt1.git20100204
- Don't package ChangeLog.
- upstream git snapshot

* Tue Nov 24 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091124
- upstream git snapshot

* Wed Oct 28 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091028
- upstream git snapshot
- fix gnome subpackage requires.

* Mon Oct 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.git20091005
- upstream git snapshot (NETWORKMANAGER_0_7 branch)

* Wed Apr 15 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Release 0.7.1

* Thu Mar 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt1
- 0.7.0.99 (0.7.1-rc3)

* Tue Mar 03 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.97-alt2
- GNOME stuff moved to NetworkManager-vpnc-gnome

* Thu Feb 19 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.97-alt1
- 0.7.0.97 (0.7.1-rc1)

* Wed Dec 03 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3
- Release NetworkManager 0.7

* Tue Nov 25 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.svn.r4326
- BuildRequires fixed

* Tue Nov 25 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn.r4326
- new svn snapshot
- removed obsolete post/postun macros calls
- update summary

* Tue Nov 11 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn.r4229
- new svn snapshot

* Wed Aug 13 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn.r3930
- new svn snapshot
- BuildRequires updated
- %post updated: D-Bus config reload

* Tue Jul 22 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080722
- new svn snapshot (3842)

* Wed May 28 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080527
- initial build

