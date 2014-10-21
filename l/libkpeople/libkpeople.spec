
%def_enable baloo

%define kpeople_sover 4
%define libkpeople libkpeople%kpeople_sover
%define kpeoplewidgets_sover 4
%define libkpeoplewidgets libkpeoplewidgets%kpeoplewidgets_sover

Name: libkpeople
Summary: Meta-contact aggregation library
Version: 0.3.0
Release: alt2

Group: System/Libraries
Url: https://projects.kde.org/projects/playground/network/libkpeople
License: LGPLv2+

Source: %name-%version.tar

# Automatically added by buildreq on Tue Oct 21 2014 (-bi)
# optimized out: automoc boost-devel-headers cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libakonadi4-calendar libakonadi4-contact libakonadi4-kabc libakonadi4-kcal libakonadi4-kde libakonadi4-kmime libakonadi4-notes libakonadi4-socialutils libakonadi4-xml libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpgmexx4-pthread libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-sql libqt4-svg libqt4-xml libsoprano-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4-baloo-devel kde4pimlibs-devel libXxf86misc-devel libqt3-devel python-module-google qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4pimlibs-devel
%if_enabled baloo
BuildRequires: kde4-baloo-devel
%endif

%description
A library that provides access to all contacts and the people who hold them.

%package common
Summary: Common %name files
Group: System/Configuration/Other
BuildArch: noarch
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
Requires: kde4pimlibs-devel
%description devel
This package contains the development files for %name.

%package -n %libkpeople
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkpeople
%name library

%package -n %libkpeoplewidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
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
#%_K4lib/imports/org/kde/people/
%_K4srv/*.desktop
%_K4srvtyp/*.desktop

%files -n %libkpeople
%_K4libdir/libkpeople.so.%kpeople_sover
%_K4libdir/libkpeople.so.%kpeople_sover.*

%files -n %libkpeoplewidgets
%_K4libdir/libkpeoplewidgets.so.%kpeoplewidgets_sover
%_K4libdir/libkpeoplewidgets.so.%kpeoplewidgets_sover.*


%files devel
%_K4includedir/kpeople/
%_K4includedir/KPeople/
%_K4link/lib*.so
%_libdir/cmake/KPeople

%changelog
* Tue Oct 21 2014 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt2
- fix requires

* Tue Oct 21 2014 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- new version

* Wed May 21 2014 Sergey V Turchin <zerg@altlinux.org> 0.2.2-alt0.M70P.1
- built for M70P

* Tue May 20 2014 Sergey V Turchin <zerg@altlinux.org> 0.2.2-alt1
- new version

* Thu Apr 03 2014 Sergey V Turchin <zerg@altlinux.org> 0.2.1-alt0.M70P.1
- built for M70P

* Wed Mar 19 2014 Sergey V Turchin <zerg@altlinux.org> 0.2.1-alt1
- new version

* Tue Dec 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt0.M70P.1
- built for M70P

* Thu Oct 31 2013 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial package
