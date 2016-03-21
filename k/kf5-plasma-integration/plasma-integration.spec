%define rname plasma-integration

Name: kf5-%rname
Version: 5.6.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 integration of Qt applications
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Mar 22 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libwayland-client libxcbutil-keysyms libxkbfile-devel python-base python-modules python3 qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kservice-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libXres-devel python-module-google python3-base qt5-declarative-devel qt5-x11extras-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-declarative-devel qt5-x11extras-devel
BuildRequires: libXres-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kservice-devel kf5-kwayland-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
Framework Integration is a set of plugins responsible for better integration of
Qt applications when running on a KDE Plasma workspace.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files -f %name.lang
%doc COPYING.LIB README.md
%_K5plug/platformthemes/KDEPlasmaPlatformTheme.so

%changelog
* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- initial build
