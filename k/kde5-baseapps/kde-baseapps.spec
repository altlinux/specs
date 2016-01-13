%define rname kde-baseapps

%def_disable text2speech

%define kf5konq_sover 6
%define libkf5konq libkf5konq%kf5konq_sover
%define konquerorprivate_sover 5
%define libkonquerorprivate libkonquerorprivate%konquerorprivate_sover
%define kbookmarkmodel_private_sover 6
%define libkbookmarkmodel_private libkbookmarkmodel_private%kbookmarkmodel_private_sover
%define konqsidebarplugin_sover 5
%define libkonqsidebarplugin libkonqsidebarplugin%konqsidebarplugin_sover

Name: kde5-baseapps
Version: 4.97.0
Release: alt7
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 base applications
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

#Requires: kde5-konqueror      = %EVR
Requires: /usr/bin/xbrowser
#
Requires: kde5-kdepasswd      = %EVR
Requires: kde5-kdialog        = %EVR
Requires: kde5-keditbookmarks = %EVR
Requires: kde5-kfind          = %EVR
#Requires: kde5-nsplugins      = %EVR
#Requires: %name-plasma-applets = %EVR

Source: %rname-%version.tar
Patch100: alt-kfmclient-loop.patch
Patch101: alt-passwd-len.patch

# Automatically added by buildreq on Wed Sep 16 2015 (-bi)
# optimized out: alternatives cmake cmake-modules desktop-file-utils docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-svg libqt5-test libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel python-base python3 python3-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kded kf5-kded-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdesu-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libtidy-devel python-module-google qt5-script-devel qt5-speech-devel qt5-x11extras-devel rpm-build-python3 rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-script-devel qt5-x11extras-devel
%if_enabled text2speech
BuildRequires: qt5-speech-devel
%endif
BuildRequires: libtidy-devel zlib-devel
BuildRequires: kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kded kf5-kded-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdesu-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel
BuildRequires: kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel
BuildRequires: kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
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

%package -n %libkbookmarkmodel_private
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkbookmarkmodel_private
KF5 library

%package -n %libkonqsidebarplugin
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkonqsidebarplugin
KF5 library

%package -n kde5-kdepasswd
Group: Graphical desktop/KDE
Summary: User account configuration
Requires: %name-common = %EVR
Requires: shadow-change
Requires: passwd
%description -n kde5-kdepasswd
User account configuration

%package -n kde5-kdialog
Group: Graphical desktop/KDE
Summary: Utility to display GUI dialog boxes from shell scripts
Requires: %name-common = %EVR
%description -n kde5-kdialog
kdialog allows you to display dialog boxes from shell scripts.
The syntax is very much inspired from the "dialog" command
(which shows text mode dialogs).

%package -n kde5-keditbookmarks
Group: Graphical desktop/KDE
Summary: Utility to edit KDE bookmarks
Requires: %name-common = %EVR
%description -n kde5-keditbookmarks
Utility to edit KDE bookmarks

%package -n kde5-kfind
Group: File tools
Summary: KDE utility to find files
Requires: %name-common = %EVR
%description -n kde5-kfind
KDE utility to find files

%package -n kde5-konqueror
Group: Networking/WWW
Summary: Web browser for KDE
PreReq(post,preun): alternatives >= 0.2
Requires: %name-common = %EVR
Requires: indexhtml
Provides: webclient %_bindir/xbrowser %_bindir/x-www-browser
Provides: kde5-www-browser
Provides: kde5-konqueror-plugins = %version-%release
Obsoletes: kde5-konqueror-plugins < %version-%release
Provides: kf5-konqueror-plugins = %version-%release
Obsoletes: kf5-konqueror-plugins < %version-%release
%description -n kde5-konqueror
Web browser easy for use.

%package -n kde5-nsplugins
Group: Graphical desktop/KDE
Summary: Netscape(R) browser plugins support for KDE
Requires: %name-common = %EVR
%description -n kde5-nsplugins
Tools used to utilize Netscape(R) browser plugins in KDE

%package plasma-applets
Group: Graphical desktop/KDE
Summary: Plasma applets
Requires: %name-common = %EVR
%description plasma-applets
Various Plasma applets

%prep
%setup -n %rname-%version
%patch100 -p1
%patch101 -p1

%build
%K5build

%install
%K5install
cp -arl %buildroot/%_K5data/konqueror/* %buildroot/%_datadir/konqueror/
rm -rf %buildroot/%_K5data/konqueror/
%K5install_move data akregator doc dolphinpart domtreeviewer fsview kcmcss kcontrol khtml konqsidebartng kwebkitpart templates konqueror

mv %buildroot/%_includedir/konqsidebarplugin.h %buildroot/%_K5inc/

# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/kde5-konqueror <<__EOF__
%_bindir/xbrowser       %_K5bin/konqueror      10
%_bindir/x-www-browser       %_K5bin/konqueror      10
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
desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
    --add-mime-type=x-scheme-handler/http \
    --add-mime-type=x-scheme-handler/https \
    %buildroot/%_K5xdgapp/kfmclient_html.desktop
#desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
#    --add-mime-type=x-scheme-handler/ftp \
#    --add-mime-type=x-scheme-handler/trash \
#    %buildroot/%_K5xdgapp/kfmclient_dir.desktop
rm -f %buildroot/%_K5xdgapp/kfmclient_dir.desktop
# add desktop categories
desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
    --add-category=X-PersonalSettings \
    %buildroot/%_K5xdgapp/org.kde.kdepasswd.desktop

%find_lang %name --with-kde --all-name

%files
%files common -f %name.lang
%doc COPYING.LIB README
%_K5tmpl/*.desktop
%_K5tmpl/.source/

%files -n kde5-konqueror
%config /%_sysconfdir/alternatives/packages.d/kde5-konqueror
%config(noreplace) %_K5xdgconf/translaterc
%config(noreplace) %_K5xdgconf/konqsidebartngrc
%_K5bin/konqueror
%_K5bin/kfmclient
%_K5bin/fsview
%_K5lib/libkdeinit5_konqueror.so
%_K5lib/libkdeinit5_kfmclient.so
%_K5start/konqy_preload.desktop
%_K5data/fsview/
%_K5data/konqueror/
%_K5data/khtml/
%_K5data/kwebkitpart/
%_K5data/kcmcss/
%_K5data/dolphinpart/
%_K5data/domtreeviewer/
%_K5data/konqsidebartng/
%_K5data/akregator/pics/*
%_K5data/kcontrol/pics/*
%_K5cfg/konqueror.kcfg
%_K5cfg/validators.kcfg
%_K5icon/*/*/apps/konqueror.*
%_K5icon/*/*/apps/fsview.*
%_K5icon/*/*/actions/htmlvalidator.*
%_K5icon/*/*/actions/validators.*
%_K5icon/*/*/actions/babelfish.png
%_K5icon/*/*/actions/cssvalidator.png
%_K5icon/*/*/actions/imagegallery.png
%_K5icon/*/*/actions/webarchiver.png
%_K5srv/kded/konqy_preloader.desktop
%_K5srv/khtml_*.desktop
%_K5srv/fsview_part.desktop
%_K5srv/*konq*.desktop
%_K5srv/kcmperformance.desktop
%_K5srv/kcmhistory.desktop
%_K5srv/filebehavior.desktop
%_K5srv/webarchivethumbnail.desktop
%_K5srvtyp/konq*.desktop
%_K5dbus_iface/org.kde.FavIcon.xml
%_K5dbus_iface/org.kde.?onqueror.*.xml
%_K5xdgapp/Home.desktop
%_K5xdgapp/kfmclient*.desktop
%_K5xdgapp/konqbrowser.desktop
%_K5xdgapp/konquerorsu.desktop
%_K5xmlgui/konqueror/
%_K5plug/akregatorkonqfeedicon.so
%_K5plug/autorefresh.so
%_K5plug/babelfishplugin.so
%_K5plug/dirfilterplugin.so
%_K5plug/domtreeviewerplugin.so
%_K5plug/fsviewpart.so
%_K5plug/kcm_konq.so
%_K5plug/kcm_konqhtml.so
%_K5plug/kcm_performance.so
%_K5plug/kcm_history.so
%_K5plug/konq_sidebar.so
%_K5plug/konqsidebar_*.so
%_K5plug/kded_konqy_preloader.so
%_K5plug/kf5/kded/favicons.so
%_K5plug/khtmlsettingsplugin.so
%if_enabled text2speech
%_K5plug/khtmlttsplugin.so
%endif
%_K5plug/kimgallery.so
%_K5plug/konq_aboutpage.so
%_K5plug/konq_shellcmdplugin.so
%_K5plug/minitoolsplugin.so
%_K5plug/rellinksplugin.so
%_K5plug/searchbarplugin.so
%_K5plug/validatorsplugin.so
%_K5plug/webarchiverplugin.so
%_K5plug/webarchivethumbnail.so

%files -n kde5-kdialog
%_K5bin/kdialog
%_K5dbus_iface/org.kde.kdialog.ProgressDialog.xml

%files -n kde5-kdepasswd
%_K5bin/kdepasswd
%_K5xdgapp/org.kde.kdepasswd.desktop

%files -n kde5-keditbookmarks
%_K5bin/kbookmarkmerger
%_K5bin/keditbookmarks
%_K5lib/libkdeinit5_keditbookmarks.so
%_K5plug/kcm_bookmarks.so
%_K5data/kbookmark/
%_K5xdgapp/org.kde.keditbookmarks.desktop
%_K5cfg/keditbookmarks.kcfg
%_K5srv/bookmarks.desktop
%_K5xmlgui/keditbookmarks/

%files -n kde5-kfind
%_K5bin/kfind
%_K5xdgapp/org.kde.kfind.desktop
%_K5icon/*/*/apps/kfind.*

#%files -n kde5-nsplugins
#%config(noreplace) %_sysconfdir/cron.daily/kde5-nsplugins
#%_K5bin/nspluginscan
#%_K5bin/nspluginviewer
#%_K5plug/libkcminit_nsplugins.so
#%_K5plug/libnsplugin.so
#%_K5data/nsplugin/
#%_K5srv/khtml_plugins.desktop

#%files plasma-applets
#%_K5plug/plasma_applet_folderview.so
#%_K5plug/plasma_applet_places.so
#%_K5srv/plasma-applet-folderview.desktop
#%_K5srv/plasma-applet-places.desktop

%files devel
#%_K5inc/kde-baseapps_version.h
%_K5inc/*konq*
%_K5link/lib*.so
%_K5lib/cmake/KF5Konq/
#%_K5archdata/mkspecs/modules/qt_kde-baseapps.pri

%files -n %libkf5konq
%_K5lib/libKF5Konq.so.%kf5konq_sover
%_K5lib/libKF5Konq.so.*
%files -n %libkonquerorprivate
%_K5lib/libkonquerorprivate.so.%konquerorprivate_sover
%_K5lib/libkonquerorprivate.so.*
%files -n %libkbookmarkmodel_private
%_K5lib/libkbookmarkmodel_private.so.%kbookmarkmodel_private_sover
%_K5lib/libkbookmarkmodel_private.so.*
%files -n %libkonqsidebarplugin
%_K5lib/libkonqsidebarplugin.so.%konqsidebarplugin_sover
%_K5lib/libkonqsidebarplugin.so.*

%changelog
* Wed Jan 13 2016 Sergey V Turchin <zerg@altlinux.org> 4.97.0-alt7
- update from frameworks branch

* Thu Nov 26 2015 Sergey V Turchin <zerg@altlinux.org> 4.97.0-alt6
- allow to replace konqueror

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 4.97.0-alt5
- update from frameworks branch

* Thu Nov 05 2015 Sergey V Turchin <zerg@altlinux.org> 4.97.0-alt4
- update from frameworks branch
- fix kfmclient openUrl

* Mon Oct 19 2015 Sergey V Turchin <zerg@altlinux.org> 4.97.0-alt3
- update from frameworks branch

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 4.97.0-alt2
- rebuild without qt5-speech

* Wed Sep 09 2015 Sergey V Turchin <zerg@altlinux.org> 4.97.0-alt1
- initial build
