%ifarch %e2k ppc64le
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%define rname ktorrent
%define sover 16
%define libktcore libktcore%sover

%add_findreq_skiplist %_K5data/%rname/scripts/*.py

Name: kde5-%rname
Version: 22.08.3
Release: alt1
%K5init

Group:     Networking/File transfer
Summary:   KDE client for BitTorrent network 
License:   GPL-2.0-or-later
URL:       http://ktorrent.org

Provides: ktorrent = %version-%release
Requires: kde5-kross-python

Source: %rname-%version.tar

# ALT
Patch10: alt-defaults.patch
Patch11: alt-short-date.patch
Patch12: alt-find-taglib.patch

# Automatically added by buildreq on Tue Apr 19 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgcrypt-devel libgpg-error libjson-c libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-svg libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel qt5-webkit-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-libktorrent-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kplotting-devel kf5-kross-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-workspace-devel kf5-solid-devel kf5-sonnet-devel libGeoIP-devel libgmp-devel libtag-devel python-module-google python3-dev qt5-phonon-devel qt5-script-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: boost-devel extra-cmake-modules
BuildRequires: qt5-phonon-devel qt5-script-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%endif
BuildRequires: libGeoIP-devel libgmp-devel libtag-devel
BuildRequires: kde5-libktorrent-devel kde5-syndication-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdnssd-devel
BuildRequires: kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kplotting-devel kf5-kross-devel
BuildRequires: kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-workspace-devel kf5-solid-devel kf5-sonnet-devel

%description
ktorrent - KDE BitTorrent client. It comes with many useful plugins.

%package -n %libktcore
Summary: KTorrent library
Group: System/Libraries
#Requires: %name-common
%description -n %libktcore
KTorrent library

%prep
%setup -q -n %rname-%version
%patch10 -p1 -b .defaults
%patch11 -p1
%patch12 -p1

sed -i 's|^add_subdirectory(plasma)||' CMakeLists.txt

%build
%K5build \
 -DWITH_SYSTEM_GEOIP:BOOL=ON \
 #


%install
%K5install
%K5install_move data ktorrent
for f in %buildroot/%_K5xmlgui/%rname/*.rc ; do
    ln -sr $f %buildroot/%_K5data/
done

%find_lang --with-kde %rname


%files -f %rname.lang
%doc LICENSES/*
%_K5bin/*
%_K5icon/hicolor/*/*/kt*.*
%_K5xdgapp/org.kde.%rname.desktop
%_K5plug/ktorrent_plugins/
%_K5xmlgui/%rname/
%_K5data/*torrent*.rc
%_K5notif/%rname.notifyrc
%if_enabled qtwebengine
%_K5data/%rname/
%endif

%files -n %libktcore
%_libdir/libktcore.so.%sover
%_libdir/libktcore.so.%sover.*


%changelog
* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Thu Sep 15 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Fri May 13 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri May 06 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt2
- fix find xmlgui files

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Thu Feb 03 2022 Oleg Solovyov <mcpain@altlinux.org> 21.12.1-alt3
- backport plugin loader fix (Closes: #41853)

* Mon Jan 31 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt2
- build without qtbebengine on e2k and ppc64le

* Mon Jan 17 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Mon Aug 23 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Thu Jun 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Wed May 19 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Thu Mar 11 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Tue Jan 19 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Wed Sep 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt2
- fix find taglib

* Fri Jul 17 2020 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt1
- new version

* Thu Sep 19 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.2-alt1
- new version

* Tue Jul 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- add upstream fix against memory corruption in ScanFolder plugin

* Fri Oct 19 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- new version

* Tue Apr 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt4
- add upstream fixes against KDEBUG#384371, KDEBUG#390605

* Wed Nov 15 2017 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt3
- don't suppress power saving by default

* Tue Oct 03 2017 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt2
- build without kwebkit

* Mon Oct 02 2017 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt4.M80P.1
- build for M80P

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt5
- short date in Added column

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt4
- fix using mimetypes

* Mon May 23 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt3
- fix provides

* Tue Apr 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt2
- fix requires

* Tue Apr 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt1
- initial build
