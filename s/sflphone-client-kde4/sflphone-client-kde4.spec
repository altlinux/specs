%add_findpackage_path %_kde4_bindir

%define rname sflphone-client-kde
Name: sflphone-client-kde4
Version: 1.3.0
Release: alt1
%define sflphone_version 1.2.3

Group: Communications
Summary: KDE client for SFLphone
License: GPLv2
Url: http://www.sflphone.org/

Requires: sflphone-common = %sflphone_version
Requires: %name-common = %EVR

Provides: sflphone-client-kde = %EVR
Obsoletes: sflphone-client-kde < %EVR

Source: %rname-%version.tar
Patch1: alt-fix-compile.patch

# Automatically added by buildreq on Tue Feb 19 2013 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4libs kde4libs-devel kde4pimlibs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-test libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libsystemd-daemon libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: akonadi-devel boost-devel-headers gcc-c++ glib2-devel kde4-nepomuk-core-devel kde4pimlibs-devel libqt3-devel python-module-distribute rpm-build-ruby xorg-xf86miscproto-devel zlib-devel-static
BuildRequires: akonadi-devel boost-devel gcc-c++ glib2-devel kde4-nepomuk-core-devel kde4pimlibs-devel zlib-devel
BuildRequires: kde-common-devel

%description
KDE client for SFLphone. SFLphone is meant to be a robust enterprise-class desktop phone.

%package common
Summary: %name core files
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
Common files for %name.

%package devel
Summary: %name development files
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description devel
This package contains header files needed if you wish to build applications
based on %name.

%package -n libksflphone
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libksflphone
%name library

%package -n libqtsflphone
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqtsflphone
%name library

%prep
%setup -qn %rname-%version
%patch1 -p1

%build
%K4build \
    -DENABLE_VIDEO=true \
    -DENABLE_QT5=OFF \
    -DKDE4_BUILD_TESTS=OFF \
    #

%install
%K4install
%K4find_lang --with-kde %rname
%K4find_lang --with-kde --append --output=%rname.lang sflphone-kde

%files common

%files -f %rname.lang
%doc AUTHORS README*
%_K4bindir/%rname
%_K4xdg_apps/%rname.desktop
%_K4iconsdir/hicolor/*/apps/%rname.*
%_K4apps/%rname/
%_K4cfg/%rname.kcfg
#%_K4lib/plasma_engine_sflphone.so
#%_K4apps/plasma/plasmoids/org.kde.plasma.applet.sflphone/
#%_K4apps/plasma/services/sflphone.operations
#%_K4srv/plasma-*-sflphone.desktop

%files devel
#%_K4apps/cmake/modules/*.cmake
%_K4link/lib*.so
%_K4includedir/ksflphone
%_includedir/qtsflphone

%files -n libksflphone
%_K4libdir/libksflphone.so.*
%files -n libqtsflphone
%_K4libdir/libqtsflphone.so.*

%changelog
* Wed Jan 15 2014 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- new version

* Fri Aug 02 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt2
- fix requires

* Mon Jun 17 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt1
- new version

* Fri Apr 05 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt4
- obsolete sflphone-client-kde

* Thu Feb 21 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt3
- enable video

* Tue Feb 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt2
- fix package files

* Tue Feb 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt1
- initial build
