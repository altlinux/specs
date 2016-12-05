%define nm_version 1.1.90
%define nm_applet_version 1.1.90
%define nm_applet_name NetworkManager-applet-gtk
#define git_date .git20150916
%define git_date %nil
%define ppp_version 2.4.7

%def_with libnm_glib

%define _unpackaged_files_terminate_build 1

Name: NetworkManager-l2tp
Version: 1.2.4
Release: alt1%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary:  NetworkManager VPN plugin for l2tp
Url: http://www.gnome.org/projects/NetworkManager/
# git://github.com/seriyps/NetworkManager-l2tp.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Requires: NetworkManager-daemon   >= %nm_version
Requires: xl2tpd
Requires: ppp = %ppp_version
# NM-l2tp should support strongswan with patch
# 948a6acaf52d "use strongswan instead of openswan and
# add options for certificates, mru and mtu"
Requires: strongswan

BuildRequires: libgnome-keyring-devel
BuildRequires: ppp-devel
BuildRequires: rpm-build-licenses
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

%description
This package contains software for integrating the l2tp VPN software
with NetworkManager.

%package gtk
License: %gpl2plus
Summary: Applications for use %name with %nm_applet_name
Group: Graphical desktop/GNOME
Requires: gnome-keyring
Requires: %nm_applet_name >= %nm_applet_version
Requires: NetworkManager-l2tp = %version-%release

Obsoletes: %name-gnome < 0.9.8-alt2
Provides: %name-gnome = %version-%release

%description gtk
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
	--with-pppd-plugin-dir=%_libdir/pppd/%ppp_version \
%if_without libnm_glib
	--without-libnm-glib \
%endif
	--enable-more-warnings=yes
%make_build

%install
%makeinstall_std
%find_lang %name

%files
%doc AUTHORS
%config %_sysconfdir/dbus-1/system.d/nm-l2tp-service.conf
%_libexecdir/NetworkManager/nm-l2tp-service
%_libdir/pppd/%ppp_version/*.so
%if_with libnm_glib
%config %_sysconfdir/NetworkManager/VPN/nm-l2tp-service.name
%endif
%config %_libexecdir/NetworkManager/VPN/nm-l2tp-service.name

%files gtk -f %name.lang
%if_with libnm_glib
%_libdir/NetworkManager/libnm-l2tp-properties.so
%endif
%_libexecdir/NetworkManager/nm-l2tp-auth-dialog
%_datadir/gnome-vpn-properties/l2tp
%_libdir/NetworkManager/libnm-vpn-plugin-l2tp.so
%_libdir/NetworkManager/libnm-vpn-plugin-l2tp-editor.so
%_datadir/appdata/*.xml

%exclude %_libdir/NetworkManager/*.la
%exclude %_libdir/pppd/%ppp_version/*.la

%changelog
* Mon Dec 05 2016 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1
- Don't treat warrnings as errors.
- Updated to 1.2.4.

* Tue May 24 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Wed May 04 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Fix build on i586.
- Patches from upstream:
  + service: fix critical errors in dispose().
  + all: NML2tpPlugin D-Bus fixes.
  + all: libnm and libnm-gtk can't mix; use libnma instead.
- Updated to 1.2.0.

* Thu Jan 21 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.git20150916
- Require strongswan again.
- Upstream git snapshot (master branch) (closes: #30613).

* Fri Jan 16 2015 Mikhail Efremov <sem@altlinux.org> 0.9.8.7-alt2
- Rebuild with ppp-2.4.7.
- Drop strongswan requires (see ALT bug #30613).

* Tue Jul 29 2014 Mikhail Efremov <sem@altlinux.org> 0.9.8.7-alt1
- Updated to 0.9.8.7.

* Tue Jun 24 2014 Mikhail Efremov <sem@altlinux.org> 0.9.8.6-alt2
- Update requires: NetworkManager -> NetworkManager-daemon.
- Update translations from upstream git.

* Wed Apr 02 2014 Mikhail Efremov <sem@altlinux.org> 0.9.8.6-alt1
- Temporary don't treat warrnings as errors.
- Add strongswan to requires.
- Updated to 0.9.8.6.

* Wed Oct 30 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.5-alt1
- Updated BR: Use libnm-glib-vpn-devel.
- Updated to 0.9.8.5.

* Mon Sep 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8-alt2
- Don't reload DBUS configuration during install.
- Rename 'gnome' subpackage to 'gtk'.

* Tue Apr 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8-alt1
- Own %_datadir/gnome-vpn-properties/l2tp.
- Updated to 0.9.8.

* Tue Nov 06 2012 Mikhail Efremov <sem@altlinux.org> 0.9.6-alt1
- Build with GTK+3.
- Updated to 0.9.6.

* Fri Aug 31 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt1.git20120624
- Updated to 0.9.4 + changes from upstream git (closes: #27508).

* Mon Apr 04 2011 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt2.git20110330
- Spec cleanup.
- Changed libexecdir to %%_libexecdir/NetworkManager.

* Wed Mar 30 2011 Nick S. Grechukh <gns@altlinux.ru> 0.8.2-alt1.git20110330
- first build

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

