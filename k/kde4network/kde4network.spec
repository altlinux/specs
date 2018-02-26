
%add_findpackage_path %_kde4_bindir

%ifdef _kde_alternate_placement
%add_findreq_skiplist %_kde4_bindir/kopete_*.sh
%add_findreq_skiplist %_kde4_bindir/winpopup-*.sh
%else
%add_findreq_skiplist %_K4bindir/kopete_*.sh
%add_findreq_skiplist %_K4bindir/winpopup-*.sh
%endif
%add_findreq_skiplist %_K4apps/kopete_skype/call_*

%ifarch arm
%def_disable desktop
%else
%def_enable desktop
%endif
%def_disable knewsticker
%def_enable kopete_irc
%def_disable kopete_telepathy
%def_enable kopete_googletalk

%define rname kdenetwork
%define major 4
%define minor 8
%define bugfix 4
Name: kde4network
Version: %major.%minor.%bugfix
Release: alt1

Packager: Sergey V Turchin <zerg at altlinux dot org>

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Network Applications
License: GPL
Url: http://www.kde.org

Requires: %name-filesharing = %version-%release
Requires: %name-kdnssd = %version-%release
%if_enabled knewsticker
Requires: %name-knewsticker = %version-%release
%endif
Requires: %name-kget = %version-%release
Requires: %name-kopete = %version-%release
Requires: %name-kppp = %version-%release
Requires: %name-krdc = %version-%release
Requires: %name-krfb = %version-%release

Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar

# ALT
Patch11: kdenetwork-4.7.1-alt-kget-newtransfer-dialog-size.patch
Patch12: kdenetwork-4.1.96-alt-find-decibel.patch
Patch13: kdenetwork-4.2.96-alt-zeroconf-autonet.patch
Patch14: kdenetwork-4.3.0-alt-def-kppp.patch
Patch15: kdenetwork-4.3.0-alt-kppp-var-lock.patch
Patch16: kdenetwork-4.6.0-alt-kppp-add-devices.patch
Patch17: kdenetwork-4.3.0-alt-kppp-search.patch
Patch18: kdenetwork-4.8.0-alt-kppp-select-modem.patch
Patch19: kdenetwork-4.3.0-alt-kppp-resolv-mods.patch
Patch20: kdenetwork-4.5.0-alt-kget-disable-bt.patch
Patch21: kdenetwork-4.7.1-alt-fix-compile.patch
Patch22: kdenetwork-4.5.1-alt-kppp-fix-statglg-close.patch
Patch23: kdenetwork-4.6.3-alt-samba-sharing.patch
Patch24: kdenetwork-4.8.3-alt-mobile.patch

BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ libqca2-devel libgmp-devel
BuildRequires: libvncserver-devel libgpgme-devel libexpat-devel
BuildRequires: soprano soprano-backend-redland libsoprano-devel
%if_enabled kopete_telepathy
BuildRequires: libtapioca-qt-devel libtelepathy-qt-devel
%endif
BuildRequires: libortp-devel >= 0.13
%if_enabled kopete_googletalk
BuildRequires: libspeex-devel libalsa-devel
BuildRequires: libmediastreamer-devel libssl-devel
BuildRequires: libmediastreamer-ilbc
%endif
BuildRequires: libsqlite3-devel libidn-devel boost-devel libopenslp-devel libjasper-devel
BuildRequires: libqimageblitz-devel libxml2-devel libxslt-devel libnxcl-devel libmms-devel
BuildRequires: libjpeg-devel libavahi-qt4-devel bzlib-devel libldap-devel
BuildRequires: libotr-devel libmeanwhile-devel libgadu-devel libv4l-devel libmsn-devel
BuildRequires: rpm-macros-browser-plugins shared-desktop-ontologies
BuildRequires: libktorrent-devel
BuildRequires: kde4libs-devel >= %version kde4pimlibs-devel >= %version
BuildRequires: kde4base-workspace-devel >= %version kde4base-devel >= %version

%description
Networking applications for the K Desktop Environment.

- kppp: Dual-up tool
- kopete: instant messenger client
%if_enabled knewsticker
- knewsticker: RDF newsticker applet
%endif
- krfb: Desktop Sharing server, allow others to access your desktop via VNC
- krdc: a client for Desktop Sharing and other VNC servers


%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kdenetwork-common <= 3.5.12-alt1
%description common
%name common package

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
Core files for %name

%package filesharing
Summary: %name filesharing
Group: Networking/File transfer
Requires: %name-core = %version-%release
%description filesharing
%name filesharing.

%package kdnssd
Summary: %name kdnssd
Group: Networking/Remote access
Requires: %name-core = %version-%release
Requires: avahi-daemon libnss-mdns
%description kdnssd
%name kdnssd.

%package knewsticker
Summary: %name knewsticker
Group: Networking/News
Requires: %name-core = %version-%release
%description knewsticker
%name knewsticker.

%package kget
Summary: %name kget
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
%description kget
%name kget.

%package kopete
Summary: Instant Messaging client
Group: Networking/Instant messaging
Requires: kde4base-runtime-core
Requires: %name-core = %version-%release
Requires: qca2-ossl
%if_enabled kopete_googletalk
Requires: libmediastreamer-ilbc
%endif
%description kopete
Kopete is an Instant Messaging client
designed to be modular and plugin based.

%package -n libkget4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkget4
%name library

%package -n libkopete4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkopete4
%name libraries

%package -n libkrdccore4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkrdccore4
%name library

%package kppp
Summary: %name kppp
Group: Networking/Remote access
Requires: %name-core = %version-%release
%description kppp
%name kppp.

%package krdc
Summary: %name krdc
Group: Networking/Remote access
Requires: %name-core = %version-%release
%description krdc
%name krdc.

%package -n libkrfbprivate4
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkrfbprivate4
%name library

%package krfb
Summary: %name krfb
Group: Networking/Remote access
Requires: %name-core = %version-%release
%description krfb
%name krfb.

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: kde4libs-devel
Requires: %name-common = %version-%release
%description devel
This package contains header files needed if you wish to build applications
based on %name.


%prep
%setup -q -n %rname-%version
%patch11 -p1
#%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
#%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%if_disabled desktop
%patch24 -p1
%endif

%build
%K4cmake \
    -DKDE4_ENABLE_FPIE:BOOL=ON \
    -DWITH_irc:BOOL=%{?_enable_kopete_irc:ON}%{!?_enable_kopete_irc:OFF} \
    -DWITH_msn:BOOL=ON \
    -DMOZPLUGIN_INSTALL_DIR:PATH=%browser_plugins_path \
    -DWITH_telepathy:BOOL=%{?_enable_kopete_telepathy:ON}%{!?_enable_kopete_telepathy:OFF} \
    -DWITH_GOOGLETALK:BOOL=%{?_enable_kopete_googletalk:ON}%{!?_enable_kopete_googletalk:OFF} \
    -DSAMBA_PACKAGE_NAME=\\\"samba\\\" \
    -DENABLE_EMBEDDED_TORRENT_SUPPORT=false
#    -DKDE4_ENABLE_FINAL:BOOL=ON \
%K4make

%install
%K4install

find %buildroot/%_K4datadir/bin -type f | \
%ifdef _kde_alternate_placement
while read f; do mv $f %buildroot/%_kde4_bindir/; done
%else
while read f; do mv $f %buildroot/%_K4bindir/; done
%endif

install -d -m 0755 %buildroot%_sysconfdir/rc.d/init.d

mkdir -p %buildroot/etc/control.d/facilities/
cat >%buildroot/etc/control.d/facilities/kppp-kde4 <<__EOF__
#!/bin/sh
. /etc/control.d/functions
%ifdef _kde_alternate_placement
BINARY=%_kde4_bindir/kppp
%else
BINARY=%_K4bindir/kppp
%endif
new_summary "KPPP dial-up tool"
new_fmode public 4711 root root
new_fmode netadmin 4710 root netadmin
new_fmode restricted 700 root root
new_help public "Any user can use KPPP"
new_help netadmin "Only \"netadmin\" group members can use KPPP"
new_help restricted "Only root can use KPPP"
control_fmode "\$BINARY" "\$*" || exit 1
__EOF__
chmod 0755 %buildroot/etc/control.d/facilities/kppp-kde4

%pre kppp
/usr/sbin/groupadd -r -f netadmin >/dev/null 2>&1
[ $1 -eq 1 ] || /usr/sbin/control-dump kppp-kde4
%post kppp
[ $1 -eq 1 ] || /usr/sbin/control-restore kppp-kde4

%files
%files common
%doc README
%dir %_K4srv/kconfiguredialog/
%_K4snd/KDE-Im-Phone-Ring.wav

%files core
%_K4iconsdir/oxygen/*/*/*.*
%_K4iconsdir/hicolor/*/*/*.*

%files filesharing
%_K4lib/sambausershareplugin.so
%_K4srv/sambausershareplugin.desktop

%files kdnssd
%_K4apps/remoteview/
#%_K4apps/zeroconf/
%_K4lib/kded_dnssdwatcher.so
%_K4lib/kio_zeroconf.so
%_K4srv/kded/dnssdwatcher.desktop
%_K4srv/zeroconf.protocol

%if_enabled knewsticker
%files knewsticker
%_K4lib/plasma_applet_knewsticker.so
%_K4srv/plasma-knewsticker-default.desktop
%_K4doc/*/knewsticker
%endif

%files kget
%_K4bindir/kget
%_K4apps/kget/
%_K4apps/dolphinpart/kpartplugins/kget*
%_K4apps/khtml/kpartplugins/kget*
%_K4apps/kwebkitpart/kpartplugins/kget*
%_K4lib/kget_*
%_K4lib/kcm_kget_*.so
%_K4lib/krunner_kget.so
%_K4lib/plasma_engine_kget.so
%_K4lib/plasma_kget_barapplet.so
%_K4lib/plasma_kget_piechart.so
%_K4conf_update/kget*
%_K4dbus_services/org.kde.kget.service
%_K4xdg_apps/kget.desktop
%_K4srv/plasma-engine-kget.desktop
%_K4srv/kgetbarapplet-default.desktop
%_K4srv/kgetpiechartapplet-default.desktop
%_K4srv/ServiceMenus/kget_download.desktop
%_K4cfg/kget*
%_K4srv/kget_*
%_K4srv/plasma-runner-kget.desktop
%_K4srvtyp/kget_*
%_K4doc/*/kget

%files kopete
%if_enabled kopete_googletalk
%_K4bindir/googletalk-call
%endif
#%_K4bindir/skype-action-handler
%_K4bindir/kopete
%_K4bindir/kopete_latexconvert.sh
%_K4bindir/winpopup-install
%_K4bindir/winpopup-send
%_K4libdir/libqgroupwise.so
%_K4lib/libchattexteditpart.so
%_K4lib/kcm_kopete_*
%_K4lib/kopete_*
%_K4plug/accessible/chatwindowaccessiblewidgetfactory.so
%browser_plugins_path/skypebuttons.so
%_K4conf_update/kopete-*
%_K4xdg_apps/kopete.desktop
%_K4conf/kopeterc
%_K4cfg/historyconfig.kcfg
%_K4cfg/kopete_otr.kcfg
%_K4cfg/kopeteappearancesettings.kcfg
%_K4cfg/kopetebehaviorsettings.kcfg
%_K4cfg/kopetestatussettings.kcfg
%_K4cfg/latexconfig.kcfg
%_K4cfg/nowlisteningconfig.kcfg
%_K4cfg/webpresenceconfig.kcfg
%_K4cfg/translatorconfig.kcfg
%_K4srv/aim.protocol
%_K4srv/chatwindow.desktop
%_K4srv/emailwindow.desktop
%_K4srv/kconfiguredialog/kopete_*
%_K4srv/kopete_*
%_K4srv/callto.protocol
%_K4srv/skype.protocol
%_K4srv/tel.protocol
%_K4srv/xmpp.protocol
%if_enabled kopete_irc
%_K4srv/irc.protocol
%endif
%_K4srvtyp/kopete*
%_K4snd/Kopete_Event.ogg
%_K4snd/Kopete_Received.ogg
%_K4snd/Kopete_Sent.ogg
%_K4snd/Kopete_User_is_Online.ogg
%_K4apps/kopete/
%_K4apps/kopete_*/
%_K4apps/kopeterichtexteditpart/
%_K4cfg/urlpicpreview.kcfg
%_K4doc/*/kopete

%files -n libkget4
%_K4libdir/libkgetcore.so.*

%files -n libkopete4
#%_K4libdir/libgadu_kopete.so.*
%if_enabled kopete_irc
%_K4libdir/libkirc.so.*
%_K4libdir/libkirc_client.so.*
%endif
%_K4libdir/libkyahoo.so.*
%_K4libdir/libkopete_videodevice.so.*
%_K4libdir/libkopeteaddaccountwizard.so.*
%_K4libdir/libkopete.so.*
%_K4libdir/libkopeteprivacy.so.*
%_K4libdir/libkopetechatwindow_shared.so.*
#%_K4libdir/libiris_kopete.so.*
%_K4libdir/libkopete_oscar.so.*
%_K4libdir/libkopete_otr_shared.so.*
#%_K4libdir/libkopete_msn_shared.so.*
%_K4libdir/liboscar.so.*
%_K4libdir/libkopeteidentity.so.*
%_K4libdir/libkopetestatusmenu.so.*
%_K4libdir/libkopetecontactlist.so.*

%files kppp
%attr(4711, root, root) %_K4bindir/kppp
%config %_sysconfdir/control.d/facilities/kppp-kde4
%_K4bindir/kppplogview
%_K4xdg_apps/Kppp.desktop
%_K4xdg_apps/kppplogview.desktop
%_K4apps/kppp
%_K4doc/*/kppp

%files -n libkrdccore4
%_K4libdir/libkrdccore.so.*

%files krdc
%_K4bindir/krdc
%_K4apps/krdc/
%_K4xdg_apps/krdc.desktop
%_K4cfg/krdc.kcfg
%_K4srv/krdc_*.desktop
%_K4srv/rdp.protocol
%_K4srv/vnc.protocol
%_K4srv/ServiceMenus/smb2rdc.desktop
%_K4srvtyp/krdc_plugin.desktop
%_K4doc/*/krdc
%_K4lib/kcm_krdc_rdpplugin.so
%_K4lib/kcm_krdc_vncplugin.so
%_K4lib/krdc_rdpplugin.so
%_K4lib/krdc_testplugin.so
%_K4lib/krdc_vncplugin.so

%files -n libkrfbprivate4
%_K4libdir/libkrfbprivate.so.*

%files krfb
%_K4bindir/krfb
%_K4lib/krfb_framebuffer_qt.so
%_K4lib/krfb_framebuffer_x11.so
%_K4apps/krfb/
%_K4xdg_apps/krfb.desktop
%_K4srv/krfb_framebuffer_qt.desktop
%_K4srv/krfb_framebuffer_x11.desktop
%_K4srvtyp/krfb-framebuffer.desktop
%_K4doc/*/krfb

%files devel
%_K4link/*.so
%_K4includedir/*/
%_K4dbus_interfaces/*

%changelog
* Wed Jun 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1.M60P.1
- build for M60P

* Fri May 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2
- fix compile on arm

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Thu Feb 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- rebuilt with new libktorrent

* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version
- don't disable bittorrent in kget

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Thu Sep 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt2
- fix kget new download dialog width

* Tue Sep 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Tue Jul 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Wed Jun 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Thu May 26 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt2
- enable "allow guests" by default in filesharing configuration dialog

* Thu May 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Thu Apr 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Mon Feb 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt3
- fix conflict with kdenetwork

* Fri Feb 25 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- move to standart place
- kopete built with googletalk jingle support

* Fri Jan 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Tue Nov 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Wed Oct 06 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Wed Sep 29 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt2
- fix closing kppp stats dialog (ALT#24168)

* Tue Aug 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Thu Aug 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Tue Jun 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Tue May 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1.M51.1
- built for M51

* Mon Apr 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt2
- rebuilt with new libmsn

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Thu Feb 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Thu Jan 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Mon Dec 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt1.1
- Rebuilt with python 2.6

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Tue Nov 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Wed Oct 14 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt2
- fix requires (ALT#21372)

* Fri Oct 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

#- don't use old netscape plugins placement
* Tue Sep 29 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt2
- using new netscape plugins placement

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version
- add kppp defaults
- add more devices to kppp
- kppp fix modem selection on setup
- add to kppp checking for /etc/sysconfig/network::RESOLV_MODS

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Thu Jul 16 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Mon Jun 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Thu May 14 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version
- fix zeroconf:/ autonet:/ integration

* Wed Apr 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Wed Mar 04 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Thu Feb 19 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt3
- remove requires to optional packages from kopete

* Mon Feb 09 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt2
- add upstream patch to fix kopete logon

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Mon Jan 19 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- fix kppp control facility file permissions
- removed deprecated macroses from specfile

* Wed Nov 12 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt2
- fix to build kopete telepathy

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Tue Oct 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Fri Sep 05 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Sat Aug 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Sat Jun 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt2
- built KGet with BitTorrent support

* Mon Jun 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Tue May 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Wed Apr 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- new version
- add patch from upstream to fix crash kopete jabber

* Thu Mar 20 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
- initial specfile

