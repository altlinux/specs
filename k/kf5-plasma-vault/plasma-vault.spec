%define rname plasma-vault

Name: kf5-%rname
Version: 5.11.4
Release: alt1%ubt
%K5init altplace

Group: Graphical desktop/KDE
Summary: Encrypted vaults support for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: fuse
#Requires: fuse-encfs >= 1.9.1
#Requires: fuse-cryfs >= 0.9.6

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Dec 26 2017 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules qt5-base-common qt5-base-devel rpm-build-qml
#BuildRequires: extra-cmake-modules kf5-kactivities-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kpackage-devel kf5-libksysguard-devel kf5-plasma-framework-devel libssl-devel qt5-declarative-devel
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: qt5-declarative-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kactivities-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel
BuildRequires: kf5-kpackage-devel kf5-libksysguard-devel kf5-plasma-framework-devel

%description
%name provides encrypted vaults.

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

%package -n libkf5plasma-vault
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkf5plasma-vault
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files -f %name.lang
%doc COPYING*
%_K5plug/kf5/kded/*vault*.so
%_K5plug/plasma/applets/*vault*.so
%_K5data/plasma/plasmoids/*vault*/
%_K5srv/*vault*.desktop

%changelog
* Tue Dec 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1%ubt
- initial build
