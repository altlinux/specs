%define rname pim-storage-service-manager

Name: kde5-%rname
Version: 16.12.3
Release: alt1%ubt
%K5init

Group: Graphical desktop/KDE
Summary: Cloud Storage Manager
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Conflicts: kde5-pim-common < 16.12

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Mar 21 2017 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-kcontacts-devel kde5-kimap-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-pimcommon-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-kitemmodels-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-ktextwidgets-devel libsasl2-devel python-module-google python3-dev ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: boost-devel libsasl2-devel
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-kcontacts-devel kde5-kimap-devel kde5-kmime-devel kde5-kpimtextedit-devel
BuildRequires: kde5-libkdepim-devel kde5-pimcommon-devel
BuildRequires: kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-kitemmodels-devel kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel kf5-ktextwidgets-devel

%description
KDE PIM Cloud Storage Manager.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kconf_update
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%config(noreplace) %_K5xdgconf/*storageservicemanager*
%_K5bin/*storageservicemanager*
%_K5conf_up/*storageservicemanager*
%_K5xdgapp/*storageservicemanager*.desktop
%_K5cfg/*storageservicemanager*
%_K5notif/*storageservicemanager*

%changelog
* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- initial build
