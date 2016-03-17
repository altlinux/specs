%define rname kstars

Name: kde5-%rname
Version: 15.12.2
Release: alt1
%K5init

Group: Education
Summary: Desktop Planetarium
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: xplanet

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Mar 18 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-gir rpm-build-python3 xml-common xml-utils zlib-devel
#BuildRequires: eigen3 extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kparts-devel kf5-kplotting-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libGLU-devel libcfitsio-devel libindi-devel python-module-google python3.3-site-packages qt5-multimedia-devel qt5-svg-devel ruby ruby-stdlibs wcslib-devel xplanet zlib-devel-static
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-multimedia-devel qt5-svg-devel
BuildRequires: xplanet eigen3 libGLU-devel zlib-devel
BuildRequires: libcfitsio-devel libindi-devel wcslib-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kparts-devel kf5-kplotting-devel
BuildRequires: kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel

%description
KStars is a Desktop Planetarium for KDE. It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time. The display includes 130,000 stars, 13,000 deep-sky objects,all 8
planets, the Sun and Moon, and thousands of comets and asteroids.

%prep
%setup -n %rname-%version

sed -i 's|isnan(|std::isnan(|g' kstars/tools/horizonmanager.cpp

%build
%K5build

%install
%K5install
%K5install_move data kstars sounds
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%config(noreplace) %_K5xdgconf/kstars.knsrc
%_K5bin/kstars
%_K5data/kstars/
%_K5icon/*/*/apps/kstars.*
%_K5icon/*/*/actions/kstars_*.*
%_K5snd/KDE-KStars-*.*
%_K5xdgapp/org.kde.kstars.desktop
%_K5xmlgui/kstars/
%_K5notif/kstars.notifyrc
%_K5cfg/kstars.kcfg

%changelog
* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
