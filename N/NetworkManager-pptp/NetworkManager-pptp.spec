%define nm_version 1.1.90
%define nm_applet_version 1.1.90
%define nm_applet_name NetworkManager-applet-gtk
%define git_date %nil
#define git_date .git20110314
%define ppp_version 2.4.7

%def_with libnm_glib

%define _unpackaged_files_terminate_build 1

Name: NetworkManager-pptp
Version: 1.2.4
Release: alt2%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary:  NetworkManager VPN plugin for pptp
Url: http://www.gnome.org/projects/NetworkManager/
# git://git.gnome.org/network-manager-pptp
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: ppp-devel
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnma-devel >= %nm_applet_version
%if_with libnm_glib
BuildRequires: libnm-glib-vpn-devel >= %nm_version
BuildRequires: libnm-gtk-devel >= %nm_applet_version
%endif
BuildRequires: libgtk+3-devel
BuildRequires: libsecret-devel
BuildRequires: intltool gettext

Requires: NetworkManager-daemon   >= %nm_version
Requires: NetworkManager-ppp   >= %nm_version
Requires: pptp-client
Requires: ppp = %ppp_version

%description
This package contains software for integrating the pptp VPN software
with NetworkManager.

%package gtk
License: %gpl2plus
Summary: Applications for use %name with %nm_applet_name
Group: Graphical desktop/GNOME
Requires: %nm_applet_name >= %nm_applet_version
Requires: NetworkManager-pptp = %version-%release

Obsoletes: %name-gnome < 0.9.8.4
Provides: %name-gnome = %version-%release

%description gtk
This package contains applications for use with
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
	--with-pppd-plugin-dir=%_libdir/pppd/%ppp_version \
%if_without libnm_glib
	--without-libnm-glib \
%endif
	--enable-more-warnings=error
%make_build

%install
%makeinstall_std
%find_lang %name

%files
%doc AUTHORS
%config %_sysconfdir/dbus-1/system.d/nm-pptp-service.conf
%_libexecdir/NetworkManager/nm-pptp-service
%_libdir/NetworkManager/libnm-vpn-plugin-pptp.so
%_libdir/pppd/%ppp_version/*.so
%if_with libnm_glib
%config %_sysconfdir/NetworkManager/VPN/nm-pptp-service.name
%endif
%config %_libexecdir/NetworkManager/VPN/nm-pptp-service.name

%files gtk -f %name.lang
%if_with libnm_glib
%_libdir/NetworkManager/libnm-pptp-properties.so
%endif
%_libexecdir/NetworkManager/nm-pptp-auth-dialog
%_datadir/gnome-vpn-properties/*
%_libdir/NetworkManager/libnm-vpn-plugin-pptp-editor.so
%_datadir/appdata/*.xml

%exclude %_libdir/NetworkManager/*.la
%exclude %_libdir/pppd/%ppp_version/*.la

%changelog
* Mon Feb 06 2017 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt2
- Require NetworkManager-ppp.

* Mon Oct 03 2016 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1
- Updated to 1.2.4.

* Fri May 13 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Fri Apr 22 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Thu Apr 14 2016 Mikhail Efremov <sem@altlinux.org> 1.1.92-alt2
- nm-pppd-plugin: fix crash (closes: #31966).

* Tue Mar 29 2016 Mikhail Efremov <sem@altlinux.org> 1.1.92-alt1
- Updated to 1.1.92 (1.2-beta3).

* Wed Mar 02 2016 Mikhail Efremov <sem@altlinux.org> 1.1.91-alt1
- Updated to 1.1.91 (1.2-beta2).

* Thu Jan 21 2016 Mikhail Efremov <sem@altlinux.org> 1.1.90-alt1
- Drop usepeerdns patch.
- Updated to 1.1.90.

* Mon Nov 30 2015 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt1
- Updated to 1.0.8.

* Mon Aug 31 2015 Mikhail Efremov <sem@altlinux.org> 1.0.6-alt1
- Minor spec cleanup.
- Updated to 1.0.6.

* Fri May 08 2015 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.

* Fri Feb 13 2015 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Treat warrnings as errors again.
- Updated to 1.0.0.

* Fri Jan 16 2015 Mikhail Efremov <sem@altlinux.org> 0.9.10.0-alt2
- Rebuild with ppp-2.4.7.

* Wed Jul 09 2014 Mikhail Efremov <sem@altlinux.org> 0.9.10.0-alt1
- Spec updated for new version.
- Updated to 0.9.10.0.

* Tue Jun 24 2014 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt3
- Update requires: NetworkManager -> NetworkManager-daemon.
- Update BR: Use libnm-glib-vpn-devel.

* Wed Apr 02 2014 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt2
- Temporary don't treat warrnings as errors.
- Rebuild with NetworkManager-applet-gtk-0.9.9.

* Mon Sep 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt1
- Don't reload DBUS configuration during install.
- Rename 'gnome' subpackage to 'gtk'.
- Updated to 0.9.8.4.

* Thu Jul 18 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.2-alt1
- From upstream git:
  + Fix path to connection-editor plugin in service file.
- Updated to 0.9.8.2.

* Thu Feb 21 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt1
- Treat warrnings as errors again.
- Conditionally enable 'usepeerdns' pppd option (by GalaxyMaster)
    (closes: #27665).
- Updated to 0.9.8.0.

* Mon Oct 08 2012 Mikhail Efremov <sem@altlinux.org> 0.9.6.0-alt2
- Fix build: temporary don't treat warrnings as errors.

* Wed Aug 08 2012 Mikhail Efremov <sem@altlinux.org> 0.9.6.0-alt1
- Updated to 0.9.6.0.

* Wed Jul 04 2012 Mikhail Efremov <sem@altlinux.org> 0.9.5.95-alt1
- Updated to 0.9.5.95 (0.9.6-rc1).

* Thu Apr 05 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.0-alt1
- Updated from upstream git (ae94fad666).
- 0.9.4.0.

* Fri Nov 11 2011 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Rename src.rpm package again.
- 0.9.2 release.

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.95-alt1
- 0.9.1.95 (0.9.2-rc1).

* Wed Aug 24 2011 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- 0.9.0 release.

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt2
- Build with GTK+3.
- Rename src.rpm package.

* Tue May 10 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt1
- Minor spec cleanup.
- 0.8.999 (0.9-rc2).

* Wed Mar 23 2011 Mikhail Efremov <sem@altlinux.org> 0.8.995-alt1.git20110314
- Fix password handling.
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

* Tue May 25 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt1.git20100427
- rename NMVpnPluginUiInterface fields.
- upstream git snapshot

* Wed Apr 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.git20100427
- upstream git snapshot

* Sat Feb 27 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- 0.8.0 release

* Thu Feb 04 2010 Mikhail Efremov <sem@altlinux.org> 0.7.999-alt1.git20100204
- Don't package ChangeLog.
- upstream git snapshot

* Wed Jan 13 2010 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt2.git20091124
- build with pppd 2.4.5.

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
- GNOME stuff moved to NetworkManager-pptp-gnome

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
- FC patch (Fix hang in auth dialog (rh #467007))

* Thu Aug 14 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn.r3930
- initial build

