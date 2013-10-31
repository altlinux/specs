
%define kpeople_sover 1
%define kpeople_libver 0.1
%define libkpeople libkpeople%kpeople_sover
%define kpeoplewidgets_sover 1
%define kpeoplewidgets_libver 0.1
%define libkpeoplewidgets libkpeoplewidgets%kpeoplewidgets_sover

Name: libkpeople
Summary: Meta-contact aggregation library
Version: 0.1.0
Release: alt1

Group: System/Libraries
Url: https://projects.kde.org/projects/playground/network/libkpeople
License: LGPLv2+

Source: %name-%version.tar

# Automatically added by buildreq on Thu Oct 31 2013 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-script libqt4-sql libqt4-svg libqt4-test libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base python3 python3-base ruby ruby-stdlibs shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: ctest gcc-c++ glib2-devel kde4-nepomuk-core-devel libicu50 libqt3-devel python-module-distribute rpm-build-python3 rpm-build-ruby soprano xorg-xf86miscproto-devel zlib-devel-static
BuildRequires: gcc-c++ glib2-devel
BuildRequires: kde4-nepomuk-core-devel soprano-backend-redland soprano-backend-virtuoso soprano libsoprano-devel shared-desktop-ontologies-devel
BuildRequires: kde4libs-devel kde-common-devel

%description
A library that provides access to all contacts and the people who hold them.

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Libraries
Conflicts: libktorrent1
Conflicts: libktorrent3 <= 1.1.0-alt2
%description common
Common %name files

%package core
Summary: Core files for %name package
Group: Graphical desktop/KDE
Requires: %name-common = %EVR
%description core
Core files for %name package

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description devel
This package contains the development files for %name.

%package -n %libkpeople
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkpeople
%name library

%package -n %libkpeoplewidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkpeoplewidgets
%name library

%prep
%setup

%build
%K4build

%install
%K4install
%K4find_lang libkpeople


%files common -f libkpeople.lang

%files core
%_K4apps/kpeople/
%_K4lib/*plugin.so
%_K4lib/imports/org/kde/people/
%_K4srv/*.desktop
%_K4srvtyp/*.desktop

%files -n %libkpeople
%_K4libdir/libkpeople.so.%kpeople_sover
%_K4libdir/libkpeople.so.%kpeople_libver

%files -n %libkpeoplewidgets
%_K4libdir/libkpeoplewidgets.so.%kpeoplewidgets_sover
%_K4libdir/libkpeoplewidgets.so.%kpeoplewidgets_libver


%files devel
%_K4includedir/kpeople/
%_K4includedir/KPeople/
%_K4link/lib*.so
%_K4apps/cmake/modules/*.cmake

%changelog
* Thu Oct 31 2013 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial package
