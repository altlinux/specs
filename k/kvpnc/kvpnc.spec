
Name: kvpnc
Version: 0.9.6
Release: alt1
#define beta rc1

Group: Networking/Remote access
Summary: KDE frontend for various vpn clients
Url: http://home.gna.org/kvpnc/
License: GPL

Requires: kde4libs >= %{get_version kde4libs} openssl psmisc ppp iptables

Source: %name-%version%{?beta:-%beta}-kde4.tar.bz2
Source1: %name-%version%{?beta:-%beta}-kde4-locale.tar.bz2
Patch1: kvpnc-0.9.3-kde4-alt-ppp-test.patch

# Automatically added by buildreq on Tue Dec 30 2008 (-bi)
#BuildRequires: gcc-c++ kde4base-runtime kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libgcrypt-devel libqt3-devel libxkbfile-devel xorg-xf86vidmodeproto-devel
BuildRequires: gcc-c++ kde4base-runtime-devel kde4libs-devel libgcrypt-devel

%description
KVpnc is a KDE frontend for various vpn clients.
It supports Cisco VPN (vpnc) and IPSec (FreeS/WAN, racoon).
vpnc is a replacement for the cisco VPN client and its used as client
for the cisco3000 VPN Concentrator, FreeS/WAN (OpenS/WAN) is a IPSec client
for Linux 2.4.x and racoon is a IPSec client for Linux 2.6.x and *BSD.
It supports also PPTP (pptpclient) and OpenVPN.

%prep
%setup -q -n %name-%version%{?beta:-%beta}-kde4
tar xvfj %SOURCE1 %name-%version%{?beta:-%beta}-kde4-locale/po
mv %name-%version%{?beta:-%beta}-kde4-locale/po .
rm -rf %name-%version%{?beta:-%beta}-kde4-locale

%patch1 -p1

cat >>CMakeLists.txt <<__EOF__
find_package(Msgfmt REQUIRED)
find_package(Gettext REQUIRED)
add_subdirectory( po )
__EOF__

for d in po src
do
pushd $d
    find -type f | \
    while read f
    do
	sed -i "s|replacedefaultroute|cleardefaultroute|g" $f
    done
popd
done


%build
%K4build


%install
%K4install
%K4find_lang --with-kde %name


%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
#
%_K4bindir/%name
%_K4apps/%name/
%_K4xdg_apps/kvpnc.desktop
%_K4iconsdir/*/*/apps/kvpnc.*
%_K4iconsdir/*/*/actions/fritzboximport.*

%changelog
* Wed May 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt1
- new version

* Mon Dec 14 2009 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt1.M51.1
- built for M51

* Mon Dec 14 2009 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt2
- fix start ppp during testing options to don't change /dev/null permissions

* Tue Dec 08 2009 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt0.M51.1
- built for M51

* Tue Dec 08 2009 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt1
- new version

* Fri Aug 07 2009 Sergey V Turchin <zerg@altlinux.org> 0.9.2-alt1
- new version

* Tue Dec 30 2008 Sergey V Turchin <zerg at altlinux dot org> 0.9.1-alt2
- built KDE4 version

* Tue Dec 30 2008 Sergey V Turchin <zerg at altlinux dot org> 0.9.1-alt1
- new version

* Tue Dec 02 2008 Sergey V Turchin <zerg at altlinux dot org> 0.9.1-alt0.1.rc2
- 0.9.1-RC2

* Wed Apr 30 2008 Sergey V Turchin <zerg at altlinux dot org> 0.9.0-alt1
- new version

* Fri Jun 22 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.9-alt2
- change replacedefaultroute ppp option to cleardefaultroute

* Mon May 07 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.9-alt1
- new version

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.7-alt1
- new version

* Wed Nov 01 2006 Sergey V Turchin <zerg at altlinux dot org> 0.8.6.1-alt1
- new version

* Thu Mar 16 2006 Sergey V Turchin <zerg at altlinux dot org> 0.8.3-alt1
- new version

* Tue Feb 07 2006 Sergey V Turchin <zerg at altlinux dot org> 0.8.2.1-alt1
- new version

* Wed Oct 05 2005 Sergey V Turchin <zerg at altlinux dot org> 0.8-alt1
- initial spec

