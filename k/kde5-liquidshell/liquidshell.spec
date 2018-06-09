%define rname liquidshell

%define liquidshell_sover 5
%define libliquidshell liquidshell%liquidshell_sover

Name: kde5-liquidshell
Version: 0.1.0
Release: alt1%ubt
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE 5 plasma dekstop shell alternative
Url: https://cgit.kde.org/liquidshell.git/
License: GPLv3

Requires: plasma5-workspace
Requires: polkit-kde-plasma-desktop

Source: %rname-%version.tar
Patch1: alt-disable-packagekit.patch
Patch2: alt-def-quicklaunch.patch
Patch3: alt-def-date-format.patch
Patch4: alt-panel-minimum-rows.patch
Patch5: alt-widgets-order.patch

# Automatically added by buildreq on Sat Jun 09 2018 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgio-devel libgpg-error libnm-devel libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3
#BuildRequires: extra-cmake-modules git-core gtk-update-icon-cache kf5-bluez-qt-devel kf5-karchive-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kwindowsystem-devel kf5-networkmanager-qt-devel libssl-devel python3-dev qt5-x11extras-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-x11extras-devel
BuildRequires: kf5-bluez-qt-devel kf5-karchive-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-knewstuff-devel kf5-knotifications-devel
BuildRequires: kf5-kwindowsystem-devel kf5-networkmanager-qt-devel

%description
Alternative desktop replacement for Plasma, using QtWidgets instead of QtQuick to ensure hardware acceleration is not required.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kf5-plasma-desktop-common = %EVR
Obsoletes: kf5-plasma-desktop-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kf5-plasma-desktop-devel = %EVR
Obsoletes: kf5-plasma-desktop-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n polkit-kde-plasma-desktop
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: polkit-kde-kfontinst
Provides: polkit-kde-kcmclock
%description -n polkit-kde-plasma-desktop
Common polkit files for %name

%package -n %libliquidshell
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libliquidshell
%name library

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%K5build

%install
%K5install

#K5install_move data doc

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README stylesheet.css
%_K5bin/liquidshell
%_K5icon/*/*/apps/liquidshell.*
%_K5xdgapp/*liquidshell*.desktop
%_K5notif/*liquidshell*

%changelog
* Sat Jun 09 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1%ubt
- initial build
