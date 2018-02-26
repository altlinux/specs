%add_findpackage_path %_kde4_bindir

%define rname kdegraphics-strigi-analyzer
Name: kde4-graphics-strigi-analyzer
Version: 4.8.2
Release: alt1

Group: Graphics
Summary: Strigi analyzers for various graphics types
Url: http://projects.kde.org/projects/kdegraphics/kdegraphics-strigi-analyzer
License: LGPLv2 and GPLv2

Provides: kde4graphics-core = %version-%release
Obsoletes: kde4graphics-core < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Sep 12 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-network libqt4-xml libssl-devel libstdc++-devel libstrigi-devel libtiff-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel zlib-devel

%description
Strigi analyzers for various graphics types

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%package -n libkdegraphics-strigi-analyzer4
Summary: KDE 4 core library
Group: System/Libraries
%description -n libkdegraphics-strigi-analyzer4
KDE 4 core library.

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install


%files
%_K4libdir/strigi/*.so
#%_K4srv/ksane_scan_service.desktop

#%files -n libkdegraphics-strigi-analyzer4
#%_K4libdir/libkdegraphics-strigi-analyzer.so.*

#%files devel
#%_K4includedir/kdegraphics-strigi-analyzer/
#%_K4link/lib*.so


%changelog
* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Mon Jan 23 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
