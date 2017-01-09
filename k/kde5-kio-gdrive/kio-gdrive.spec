
%define rname kio-gdrive
%define sover 16
%define libktcore libktcore%sover

%add_findreq_skiplist %_K4apps/%rname/scripts/*.py

Name: kde5-%rname
Version: 1.0.4
Release: alt1%ubt
%K5init

Group:     Networking/File transfer
Summary:   KIO-client for Google Drive
License:   GPLv2
URL:       https://quickgit.kde.org/?p=kio-gdrive.git

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5

# Automatically added by buildreq on Mon Nov 07 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ kde5-kcalcore-devel kde5-kcontacts-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libgpg-error libgst-plugins1.0 libical-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-sensors libqt5-sql libqt5-svg libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-libkgapi-devel libqtkeychain-qt5-devel python-module-google python3-dev rpm-build-ruby
BuildRequires(pre): rpm-build-ubt
BuildRequires: extra-cmake-modules
BuildRequires: libqtkeychain-qt5-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-libkgapi-devel

%description
Now you are ready to use the slave. Either click on "Google Drive File Manager"
in the application launcher (which will open Dolphin with the `gdrive:/` URL) or run:
    $ kioclient5 exec gdrive:/

%prep
%setup -q -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang --with-kde --all-name %rname

%files -f %rname.lang
%_K5xdgapp/org.kde.kio-gdrive.desktop
%_K5plug/kf5/kio/gdrive.so

%changelog
* Mon Jan 09 2017 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt1%ubt
- new version

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt0.M80P.1
- build for M80P

* Wed Nov 02 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- initial build
