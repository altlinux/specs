%define rname konqueror

%def_disable text2speech
%ifarch %not_qt5_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%define kf5konq_sover 6
%define libkf5konq libkf5konq%kf5konq_sover
%define konquerorprivate_sover 5
%define libkonquerorprivate libkonquerorprivate%konquerorprivate_sover
%define konqsidebarplugin_sover 5
%define libkonqsidebarplugin libkonqsidebarplugin%konqsidebarplugin_sover

Name: kde5-%rname
Version: 22.08.3
Release: alt1
%K5init no_appdata

Group: Networking/WWW
Summary: Web browser for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires(post,preun): alternatives >= 0.2
Requires: indexhtml
Provides: webclient %_bindir/xbrowser %_bindir/x-www-browser
Provides: kde5-www-browser
Provides: kde5-konqueror-plugins = %version-%release
Obsoletes: kde5-konqueror-plugins < %version-%release
Provides: kf5-konqueror-plugins = %version-%release
Obsoletes: kf5-konqueror-plugins < %version-%release

Source: %rname-%version.tar
Patch1: alt-cleanup-webengine.patch

# Automatically added by buildreq on Wed Mar 29 2017 (-bi)
# optimized out: alternatives cmake cmake-modules desktop-file-utils docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-svg libqt5-test libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel perl python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: extra-cmake-modules kf5-kactivities-devel kf5-kcmutils-devel kf5-kded kf5-kded-devel kf5-kdelibs4support-devel kf5-kdesu-devel kf5-kdoctools-devel kf5-khtml-devel kf5-kio-devel kf5-kjs-devel kf5-kpty-devel libXres-devel libtidy-devel python-module-google python3-dev qt5-script-devel qt5-webengine-devel qt5-x11extras-devel rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-kf5 rpm-macros-qt5-webengine
BuildRequires: extra-cmake-modules qt5-base-devel qt5-script-devel qt5-x11extras-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%else
BuildRequires: qt5-webkit-devel
%endif
BuildRequires: libXres-devel libtidy-devel zlib-devel
BuildRequires: kf5-kactivities-devel kf5-kcmutils-devel kf5-kded kf5-kded-devel kf5-kdelibs4support-devel
BuildRequires: kf5-kdesu-devel kf5-kdoctools-devel kf5-khtml-devel kf5-kio-devel kf5-kjs-devel kf5-kpty-devel
BuildRequires: kf5-kwallet-devel

%if_enabled text2speech
BuildRequires: qt5-speech-devel
%endif

%description
Web browser for KDE

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kf5-filesystem
Conflicts: kde5-baseapps-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkf5konq
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkf5konq
KF5 library

%package -n %libkonquerorprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkonquerorprivate
KF5 library

%package -n %libkonqsidebarplugin
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkonqsidebarplugin
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%if_disabled qtwebengine
sed -i '/add_subdirectory.*webenginepart/d' CMakeLists.txt
sed -i '/find_package.*WebEngineWidgets/s|WebEngineWidgets||' CMakeLists.txt
rm -rf webenginepart
%endif

%build
%K5build \
%if_disabled qtwebengine
    -DTHUMBNAIL_USE_WEBKIT:BOOL=TRUE \
%endif
    #

%install
%K5install
#if [ -d %buildroot/%_K5data/konqueror ] ; then
#    cp -arl %buildroot/%_K5data/konqueror/* %buildroot/%_datadir/konqueror/
#    rm -rf %buildroot/%_K5data/konqueror/
#fi
%K5install_move data kconf_update akregator doc dolphinpart fsview kcmcss kcontrol khtml kwebkitpart templates konqueror webenginepart konqsidebartng

# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/kde5-konqueror <<__EOF__
%_bindir/xbrowser       %_K5bin/konqueror      0
%_bindir/x-www-browser       %_K5bin/konqueror      0
__EOF__

# terminate nspluginviewer
install -d %buildroot/%_sysconfdir/cron.daily/
cat > %buildroot/%_sysconfdir/cron.daily/kde5-nsplugins <<__EOF__
#!/bin/sh
killall nspluginviewer >/dev/null 2>&1 ||:
sleep 2s
killall -9 nspluginviewer >/dev/null 2>&1 ||:
__EOF__
chmod 0755 %buildroot/%_sysconfdir/cron.daily/kde5-nsplugins

# add mime types categories
#
desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
    --add-mime-type=x-scheme-handler/http \
    --add-mime-type=x-scheme-handler/https \
    %buildroot/%_K5xdgapp/kfmclient_html.desktop
#
#desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
#    --add-mime-type=x-scheme-handler/ftp \
#    --add-mime-type=x-scheme-handler/trash \
#    %buildroot/%_K5xdgapp/kfmclient_dir.desktop
rm -f %buildroot/%_K5xdgapp/kfmclient_dir.desktop

# remove InitialPreference
for f in %buildroot/%_K5xdgapp/*.desktop ; do
    sed -i 's|^InitialPreference=.*|InitialPreference=-25|' $f
done

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_K5icon/*/*/apps/*.*
%_K5icon/*/*/actions/babelfish.*
%_K5icon/*/*/actions/imagegallery.*
%_K5icon/*/*/actions/webarchiver.*
%_datadir/qlogging-categories5/*.*categories

%files
%config /%_sysconfdir/alternatives/packages.d/kde5-konqueror
%config(noreplace) %_K5xdgconf/*rc
%_K5bin/konqueror
%_K5bin/kcreatewebarchive
%_K5bin/kfmclient
%_K5bin/fsview
%_K5lib/libkdeinit5_konqueror.so
%_K5lib/libkdeinit5_kfmclient.so
%if_enabled qtwebengine
%_K5lib/libkwebenginepart.so
%_K5conf_up/*.upd
%_K5data/webenginepart/
%endif
%_K5plug/*.so
%_K5plug/konqueror_kcms/
%_K5plug/konqueror/
%_K5plug/khtml/
%_K5plug/kwebkitpart/
%_K5plug/webenginepart/
%_K5plug/dolphinpart/
%_K5plug//
%_K5plug/kf5/kfileitemaction/*.so
%_K5plug/kf5/parts/*.so
%_K5start/*.desktop
%_K5data/konqsidebartng/
%_K5data/kbookmark/
%_K5data/konqueror/
%_K5data/kcmcss/
%_K5data/akregator/pics/*
%_K5data/kcontrol/pics/*
%_K5cfg/*.kcfg
%_K5srv/*.desktop
%_K5xdgapp/*.desktop
%_K5xmlgui/*/
%if_enabled text2speech
%_K5plug/khtmlttsplugin.so
%endif

%files devel
%_K5inc/*konq*
%_K5link/lib*.so
%_K5lib/cmake/KF5Konq/
%_K5dbus_iface/*.xml

%files -n %libkf5konq
%_K5lib/libKF5Konq.so.%kf5konq_sover
%_K5lib/libKF5Konq.so.*
%files -n %libkonquerorprivate
%_K5lib/libkonquerorprivate.so.%konquerorprivate_sover
%_K5lib/libkonquerorprivate.so.*
%files -n %libkonqsidebarplugin
%_K5lib/libkonqsidebarplugin.so.%konqsidebarplugin_sover
%_K5lib/libkonqsidebarplugin.so.*

%changelog
* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Tue Sep 20 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Thu May 19 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt2
- build without qtwebengine on e2k and ppc64le

* Tue Jan 18 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Mon Sep 27 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt2
- add upstream fix against kio-5.86

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Thu Aug 26 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Fri Jun 11 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Thu May 20 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Fri Mar 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Fri Jan 15 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Mon Dec 21 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Wed Oct 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Tue Sep 22 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Wed Feb 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt2
- decrease application priority

* Tue Jan 21 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Fri Nov 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Fri Oct 25 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Mon May 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Tue Feb 19 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1
- new version

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Mon Oct 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt2
- conflict with kde5-baseapps-common

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1
- new version

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- initial build
