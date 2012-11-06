%define nm_version 0.9.4
%define nm_applet_version 0.9.4
#define git_date .git20120624
%define git_date %nil
%define ppp_version 2.4.5

Name: NetworkManager-l2tp
Version: 0.9.6
Release: alt1%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary:  NetworkManager VPN plugin for l2tp
Url: http://www.gnome.org/projects/NetworkManager/
# git://github.com/seriyps/NetworkManager-l2tp.git
Source: %name-%version.tar
#Patch0: %name-%version-%release.patch
Requires: NetworkManager   >= %nm_version
Requires: xl2tpd
Requires: ppp = %ppp_version

# Automatically added by buildreq on Thu Aug 14 2008
BuildRequires: libgnome-keyring-devel
BuildRequires: ppp-devel
BuildRequires: rpm-build-licenses
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: NetworkManager-glib-devel >= %nm_version
BuildRequires: libgtk+3-devel
BuildRequires: libdbus-devel             >= 1.1
BuildRequires: libGConf-devel
BuildRequires: libpng-devel
BuildRequires: intltool gettext

%description
This package contains software for integrating the l2tp VPN software
with NetworkManager.

%package gnome
License: %gpl2plus
Summary: GNOME applications for %name
Group: Graphical desktop/GNOME
Requires: shared-mime-info >= 0.16
Requires: GConf2
Requires: gnome-keyring
Requires: NetworkManager-gnome >= %nm_applet_version
Requires: NetworkManager-l2tp = %version-%release

%description gnome
This package contains GNOME applications for use with
NetworkManager panel applet.

%prep
%setup -q
#patch0 -p1
sed -i '/m4/ d' Makefile.am

%build
%autoreconf
%configure \
	--disable-static \
	--libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
	--with-pppd-plugin-dir=%_libdir/pppd/%ppp_version
%make_build

%install
%makeinstall_std
%find_lang %name

%post
if /sbin/service messagebus status &>/dev/null; then
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig &>/dev/null ||:
else
echo "%name requires running messagebus service." >&2
fi

%files
%doc AUTHORS
%config(noreplace) %_sysconfdir/dbus-1/system.d/nm-l2tp-service.conf
%config(noreplace) %_sysconfdir/NetworkManager/VPN/nm-l2tp-service.name
%_libexecdir/NetworkManager/nm-l2tp-service
%_libdir/pppd/%ppp_version/*.so

%files gnome -f %name.lang
%_libdir/NetworkManager/lib*.so*
%_libexecdir/NetworkManager/nm-l2tp-auth-dialog
%_datadir/gnome-vpn-properties/l2tp/nm-l2tp-dialog.ui

%exclude %_libdir/NetworkManager/*.la
%exclude %_libdir/pppd/%ppp_version/*.la

%changelog
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

