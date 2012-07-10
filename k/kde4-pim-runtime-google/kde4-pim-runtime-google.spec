%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname kdepim-runtime-google
%define major 4
%define minor 9
%define bugfix 0
Name: kde4-pim-runtime-google
Version: %major.%minor.%bugfix
Release: alt0.1

Group: Graphical desktop/KDE
Summary: KDE Akonadi Google contacts and calendar resources
License: GPLv2
Url: http://www.kde.org

Provides: akonadi-googledata = %version-%release
Obsoletes: akonadi-googledata < %version-%release

Source: %rname-%version.tar
Source1: CMakeLists.txt

# Automatically added by buildreq on Tue Jul 10 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel kde4pimlibs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-sql libqt4-svg libqt4-webkit libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libstrigi-devel libxkbfile-devel libxml2-devel phonon-devel pkg-config python-base shared-desktop-ontologies-devel shared-mime-info soprano-backend-redland soprano-backend-virtuoso xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: akonadi-devel boost-devel-headers gcc-c++ glib2-devel kde4pimlibs-devel libkgapi4-devel libqt3-devel qjson-devel qt4-designer soprano xsltproc zlib-devel-static
BuildRequires: akonadi-devel boost-devel gcc-c++ kde4pimlibs-devel libkgapi4-devel qjson-devel xsltproc
BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano

%description
This package contains the Akonadi resources for Google contacts and calendar.

%package -n libkmindexreader4
Summary: KDE 4 library
Group: System/Libraries
License: LGPLv2
Requires: %name-common = %version-%release
%description -n libkmindexreader4
KDE 4 library

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: kde4libs-devel
Requires: %name-common = %version-%release
%description devel
This package contains header files needed if you wish to build applications
based on %name.


%prep
%setup -q -n %rname-%version

cat %SOURCE1 >CMakeLists.txt
cat >>CMakeLists.txt <<__EOF__
macro_optional_add_subdirectory(calendar)
macro_optional_add_subdirectory(contacts)
__EOF__


%build
%K4build \
    -DKDEPIM_BUILD_DESKTOP:BOOL=ON \
    -DKDEPIM_BUILD_MOBILE:BOOL=ON \
    -DAKONADI_INSTALL_PREFIX:STRING=%_prefix

%install
%K4install

%files
%_kde4_bindir/akonadi_googlecalendar_resource
%_kde4_bindir/akonadi_googlecontacts_resource
%_datadir/akonadi/agents/googlecalendarresource.desktop
%_datadir/akonadi/agents/googlecontactsresource.desktop

#%files devel
#%_K4link/*.so
#%_K4includedir/*
#%_K4apps/cmake/modules/*
#%_K4dbus_interfaces/*


%changelog
* Tue Jul 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt0.1
- initial build
