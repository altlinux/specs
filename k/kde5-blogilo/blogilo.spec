%define rname blogilo

%define sover 5
%define libnotesharedprivate libnotesharedprivate%sover
%define libcomposereditorwebengineprivate libcomposereditorwebengineprivate%sover

Name: kde5-%rname
Version: 17.08.3
Release: alt1%ubt
%K5init

Group: Networking/Other
Summary: Blogging client
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-pim-blogilo = %EVR
Obsoletes: kde5-pim-blogilo < %EVR

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Mar 16 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kde5-kcalcore-devel kde5-kcontacts-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdb4-devel libdbusmenu-qt52 libgpg-error libgst-plugins1.0 libical-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-webenginewidgets libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-kblog-devel kde5-kimap-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-messagelib-devel kde5-pimcommon-devel kde5-syndication-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-ktexteditor-devel kf5-kwallet-devel kf5-libkgapi-devel kf5-syntax-highlighting-devel libsasl2-devel python-module-google python3-dev qt5-webengine-devel ruby ruby-stdlibs selinux-policy
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-webengine-devel
BuildRequires: boost-devel libsasl2-devel
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-kblog-devel kde5-kimap-devel kde5-kmime-devel kde5-kpimtextedit-devel
BuildRequires: kde5-libkdepim-devel kde5-messagelib-devel kde5-pimcommon-devel kde5-syndication-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-ktexteditor-devel kf5-kwallet-devel
BuildRequires: kf5-libkgapi-devel kf5-syntax-highlighting-devel


%description
Blogilo is a blogging client for KDE, which supports famous blogging APIs.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Conflicts: kde5-pim-common < 16.12
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libcomposereditorwebengineprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libcomposereditorwebengineprivate
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kconf_update composereditorwebengine
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_K5icon/*/*/actions/*.*
%config(noreplace) %_K5xdgconf/*blogilo*.*categories
%_K5cfg/*blogilo*.kcfg
%_K5data/composereditorwebengine/

%files
%_K5bin/blogilo
%_K5xdgapp/org.kde.blogilo.desktop
%_K5cf_upd/*blogilo*
%_K5icon/*/*/apps/blogilo.*
#%doc %_K5doc/en/blogilo/

#%files devel
#%_K5inc/blogilo_version.h
#%_K5inc/blogilo/
#%_K5link/lib*.so
#%_K5lib/cmake/blogilo
#%_K5archdata/mkspecs/modules/qt_blogilo.pri

%files -n %libcomposereditorwebengineprivate
%_K5lib/libcomposereditorwebengineprivate.so.%sover
%_K5lib/libcomposereditorwebengineprivate.so.*

%changelog
* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.2-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Mon May 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Mon Apr 24 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- initial build
