
%add_findpackage_path %_kde4_bindir

%if_enabled kde_mobile
%def_disable desktop
%else
%def_enable desktop
%endif

%def_enable kopete_irc
%def_disable mediastreamer

%ifdef _kde_alternate_placement
%add_findreq_skiplist %_kde4_bindir/kopete_*.sh
%add_findreq_skiplist %_kde4_bindir/winpopup-*.sh
%else
%add_findreq_skiplist %_K4bindir/kopete_*.sh
%add_findreq_skiplist %_K4bindir/winpopup-*.sh
%endif
%add_findreq_skiplist %_K4apps/kopete_skype/call_*

%define rname kopete
Name: kde4-kopete
Version: 17.08.3
Release: alt1%ubt

Group: Networking/Instant messaging
Summary: Instant Messaging client
License: GPLv2

Provides: kde4network-kopete = %EVR
Obsoletes: kde4network-kopete < %EVR

Requires: qca2-ossl
%if_enabled mediastreamer
Requires: libmediastreamer-ilbc
%endif

Source: %rname-%version.tar
# ALT
Patch1: alt-mobile.patch
#Patch2: alt-xmpp-service-reg-form-layout.patch

# Automatically added by buildreq on Thu Sep 26 2013 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glib2-devel glibc-devel-static kde4libs kde4libs-devel kde4pimlibs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgcrypt-devel libgif-devel libgpg-error libgpg-error-devel libopencore-amrnb0 libopencore-amrwb0 libortp-devel libp11-kit libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-qt3support libqt4-sql libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel libxml2-devel phonon-devel pkg-config python-base python3 python3-base ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-scrnsaverproto-devel xorg-xproto-devel xsltproc zlib-devel
#BuildRequires: boost-devel-headers fonts-ttf-google-droid-kufi fonts-ttf-google-droid-sans fonts-ttf-google-droid-serif gcc-c++ kde4-nepomuk-core-devel kde4base-runtime-core kde4pimlibs-devel libexpat-devel libgadu-devel libidn-devel libjasper-devel libjpeg-devel libmeanwhile-devel libmediastreamer-devel libmsn-devel libotr-devel libqca2-devel libqimageblitz-devel libsqlite3-devel libsrtp libv4l-devel libxslt-devel python-module-distribute rpm-build-python3 rpm-build-ruby samba-client xorg-xf86miscproto-devel zlib-devel-static
BuildRequires(pre): rpm-build-ubt
BuildRequires: boost-devel gcc-c++ qjson-devel
BuildRequires: kde4base-runtime-devel kde4pim-devel
BuildRequires: kde4pimlibs-devel libgpgme-devel
BuildRequires: libexpat-devel libidn-devel libjasper-devel libjpeg-devel
BuildRequires: libgadu-devel libgnutls-devel libtasn1-devel jsoncpp-devel
BuildRequires: libmeanwhile-devel libotr5-devel libalsa-devel libmsn-devel
%if_enabled mediastreamer
BuildRequires: libmediastreamer-devel libmediastreamer-ilbc
%endif
BuildRequires: libqca2-devel libqimageblitz-devel libsqlite3-devel 
BuildRequires: libsrtp-devel libortp-devel libv4l-devel libxslt-devel python-devel
BuildRequires: kde-common-devel rpm-macros-browser-plugins

%description
Kopete is an Instant Messaging client
designed to be modular and plugin based.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
%name common package

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
Core files for %name

%package -n libkopete4
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
%description -n libkopete4
%name libraries

%package -n libkopete4_videodevice
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkopete4_videodevice
%name libraries

%package -n libkopeteaddaccountwizard4
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkopeteaddaccountwizard4
%name libraries

%package -n libkopeteprivacy4
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkopeteprivacy4
%name libraries

%package -n libkopetechatwindow4_shared
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkopetechatwindow4_shared
%name libraries

%package -n libkopete4_oscar
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkopete4_oscar
%name libraries

%package -n liboscar4
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n liboscar4
%name libraries

%package -n libkopete4_otr_shared
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkopete4_otr_shared
%name libraries

%package -n libkopeteidentity4
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkopeteidentity4
%name libraries

%package -n libkopetestatusmenu4
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkopetestatusmenu4
%name libraries

%package -n libkopetecontactlist4
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkopetecontactlist4
%name libraries

%package -n libkyahoo4
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkyahoo4
%name libraries

%package -n libkirc4_client
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkirc4_client
%name libraries

%package -n libkirc4
Summary: %name libraries
Group: System/Libraries
License: LGPLv2.1
Requires: %name-common = %version-%release
Conflicts: libkopete4 <= 4.11.1-alt1
%description -n libkirc4
%name libraries

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: kde4libs-devel
Requires: %name-common = %version-%release
Conflicts: kde4network-devel <= 4.11.1-alt1
%description devel
This package contains header files needed if you wish to build applications
based on %name.

%prep
%setup -q -n %rname-%version
%if_disabled desktop
%patch1 -p1
%endif
#%patch2 -p1

%build
%K4build \
    -DKDE4_ENABLE_FPIE:BOOL=ON \
    -DWITH_irc:BOOL=%{?_enable_kopete_irc:ON}%{!?_enable_kopete_irc:OFF} \
    -DWITH_msn:BOOL=ON \
    -DWITH_wlm:BOOL=OFF \
    -DMOZPLUGIN_INSTALL_DIR:PATH=%browser_plugins_path \
    #

%install
%K4install

%files common
%doc AUTHORS IDENTITY_REFACTORY README TODO
%dir %_K4srv/kconfiguredialog/
%_K4iconsdir/oxygen/*/*/*.*
%_K4iconsdir/hicolor/*/*/*.*

#%files core

%files
%if_enabled mediastreamer
%_K4bindir/libjingle-call
%endif
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
%_K4cfg/history2config.kcfg
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

%if_enabled kopete_irc
%files -n libkirc4
%_K4libdir/libkirc.so.*
%files -n libkirc4_client
%_K4libdir/libkirc_client.so.*
%endif
%files -n libkyahoo4
%_K4libdir/libkyahoo.so.*
%files -n libkopete4_videodevice
%_K4libdir/libkopete_videodevice.so.*
%files -n libkopeteaddaccountwizard4
%_K4libdir/libkopeteaddaccountwizard.so.*
%files -n libkopete4
%_K4libdir/libkopete.so.*
%files -n libkopeteprivacy4
%_K4libdir/libkopeteprivacy.so.*
%files -n libkopetechatwindow4_shared
%_K4libdir/libkopetechatwindow_shared.so.*
%files -n libkopete4_oscar
%_K4libdir/libkopete_oscar.so.*
%files -n libkopete4_otr_shared
%_K4libdir/libkopete_otr_shared.so.*
%files -n liboscar4
%_K4libdir/liboscar.so.*
%files -n libkopeteidentity4
%_K4libdir/libkopeteidentity.so.*
%files -n libkopetestatusmenu4
%_K4libdir/libkopetestatusmenu.so.*
%files -n libkopetecontactlist4
%_K4libdir/libkopetecontactlist.so.*

%files devel
%_K4link/*.so
%_K4includedir/*/
%_K4dbus_interfaces/*

%changelog
* Wed Feb 21 2018 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Tue Apr 25 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Wed Aug 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt2
- disable voice support in gtalk and msn

* Tue Aug 09 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Mon Jan 18 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Dec 08 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt2
- fix build requires

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt0.M70P.1
- build for M70P

* Tue Nov 03 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Tue Sep 15 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Jun 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt1
- new version

* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.0-alt1
- new version

* Thu Mar 26 2015 Andrey Cherepanov <cas@altlinux.org> 14.12.3-alt2.M70P.2
- Rebuild with new verson of libmediastreamer

* Wed Mar 25 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.3-alt2.M70P.1
- build for M70P

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.3-alt3
- rebuild with new libmediastreamer

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.3-alt2
- add patch for new libmediastreamer (ALT#29079)

* Fri Mar 13 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.3-alt1
- new version

* Fri Mar 13 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.1-alt2
- rebuild with new libmediastreamer

* Wed Jan 28 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.1-alt1
- new version

* Mon Nov 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt0.M70P.1
- built for M70P

* Mon Nov 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Thu Aug 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1.M70P.1
- built for M70P

* Wed Aug 27 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt2
- fix xmpp service register form layout (ALT#30254)

* Thu Aug 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Wed Aug 06 2014 Alexey Shabalin <shaba@altlinux.ru> 4.13.3-alt1.1
- NMU: rebuild with new samba

* Tue Jul 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.3-alt1
- new version

* Wed Jun 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Wed May 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Tue Apr 22 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt0.M70P.1
- built for M70P

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt4.M70P.1
- built for M70P

* Thu Sep 26 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt5
- split from kdenetwotk
