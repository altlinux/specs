%define rname drkonqi

Name: plasma5-%rname
Version: 5.12.3
Release: alt1%ubt
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Crash Handler
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Mar 13 2018 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3
#BuildRequires: extra-cmake-modules kf5-kcrash-devel kf5-ki18n-devel kf5-kidletime-devel kf5-kio-devel kf5-knotifications-devel kf5-kwallet-devel kf5-kxmlrpcclient-devel libssl-devel python3-dev qt5-x11extras-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-x11extras-devel
BuildRequires: libssl-devel
BuildRequires: kf5-kcrash-devel kf5-ki18n-devel kf5-kidletime-devel kf5-kio-devel kf5-knotifications-devel
BuildRequires: kf5-kwallet-devel kf5-kxmlrpcclient-devel

%description
The KDE Crash Handler.

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

%package -n libdrkonqi
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libdrkonqi
%name library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    #

%install
%K5install
%K5install_move data drkonqi
%find_lang %name --all-name

%files -f %name.lang
%doc COPYING*
%_K5exec/drkonqi
%_K5data/drkonqi/
%_K5xdgapp/*drkonqi.desktop

%changelog
* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1%ubt
- initial build
