%define rname libkcddb

%define sover 5
%define libkcddb libkcddb%sover
%define libkcddbwidgets libkcddbwidgets%sover


Name: kde5-%rname
Version: 4.90.0
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: KDE CDDB library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Mon May 23 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel python-module-google python3-dev rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
KDE CDDB library.

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
Conflicts: libkcddb4-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkcddb
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkcddb
KF5 library

%package -n %libkcddbwidgets
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkcddbwidgets
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_K5cfg/libkcddb.kcfg

%files devel
%_K5inc/libkcddb/
%_K5link/lib*.so
%_K5lib/cmake/libkcddb/

%files -n %libkcddb
%_K5lib/libkcddb.so.%sover
%_K5lib/libkcddb.so.*
%_K5plug/kcm_cddb.so
%_K5srv/libkcddb.desktop
%files -n %libkcddbwidgets
%_K5lib/libkcddbwidgets.so.%sover
%_K5lib/libkcddbwidgets.so.*

%changelog
* Mon May 23 2016 Sergey V Turchin <zerg@altlinux.org> 4.90.0-alt1
- initial build
