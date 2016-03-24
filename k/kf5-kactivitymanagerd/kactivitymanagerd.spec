%define rname kactivitymanagerd

Name: kf5-kactivitymanagerd
Version: 5.6.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Core component for the KDE Activity concept
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar


# Automatically added by buildreq on Thu Mar 17 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: boost-devel-headers extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kglobalaccel-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel python-module-google python3.3-site-packages qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel boost-devel extra-cmake-modules
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kglobalaccel-devel
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/kactivitymanagerd
%_K5lib/libkactivitymanagerd_plugin.so
%_K5plug/kactivitymanagerd/
#%_K5plug/*.so
#%_K5data/kactivitymanagerd/
#%_K5srv/*.protocol
%_K5srv/*.desktop
%_K5srvtyp/*.desktop

%changelog
* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Fri Mar 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.95-alt1
- initial build
