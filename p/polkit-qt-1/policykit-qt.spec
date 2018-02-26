
Name: polkit-qt-1
%define major 0
%define minor 103
%define bugfix 0
Version: %major.%minor.%bugfix
Release: alt1

Group: Development/KDE and QT
Summary: Qt support for applications using PolicyKit
Url: http://www.kde.org/
License: LGPLv2.1

Requires: %{get_dep libqt4-core}

Provides: policykit-qt-1 = %version-%release
Obsoletes: policykit-qt-1 < %version-%release

Source: %name-%version.tar.bz2
#Patch1: polkit-qt-0.9.2-alt-linking.patch

#BuildRequires(pre): libqt4-devel
#BuildRequires: gcc-c++ libqt4-devel xorg-devel libpolkit-devel

# Automatically added by buildreq on Wed Jun 24 2009 (-bi)
#BuildRequires: automoc cmake gcc-c++ libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libpolkit-devel libqt3-devel libqt4-devel libxkbfile-devel xorg-xf86vidmodeproto-devel
BuildRequires(pre): libqt4-devel kde-common-devel
BuildRequires: automoc cmake gcc-c++ libpolkit1-devel

%description
Qt support for applications using PolicyKit

%package -n libpolkit-qt-core-1
Summary: %name library
Group: System/Libraries
Requires: libqt4-core >= %{get_version libqt4-core}
%description -n libpolkit-qt-core-1
%name library

%package -n libpolkit-qt-gui-1
Summary: %name library
Group: System/Libraries
Requires: libpolkit-qt-core-1 = %version-%release
%description -n libpolkit-qt-gui-1
%name library

%package -n libpolkit-qt-agent-1
Summary: %name library
Group: System/Libraries
Requires: libpolkit-qt-core-1 = %version-%release
%description -n libpolkit-qt-agent-1
%name library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%prep
%setup -q -n %name-%version
#%patch1 -p1
#sed -i "s|\${LIB_INSTALL_DIR}|%_K4link \${LIB_INSTALL_DIR}|" CMakeLists.txt


%build
%Kcmake
%Kmake


%install
%Kinstall

%files devel
%_libdir/lib*.so
%_includedir/polkit-qt-1/
%_pkgconfigdir/polkit-qt*-1.pc
%_libdir/cmake/PolkitQt-1

%files -n libpolkit-qt-core-1
%_libdir/libpolkit-qt-core-1.so.*

%files -n libpolkit-qt-gui-1
%_libdir/libpolkit-qt-gui-1.so.*

%files -n libpolkit-qt-agent-1
%_libdir/libpolkit-qt-agent-1.so.*


%changelog
* Thu Dec 15 2011 Sergey V Turchin <zerg@altlinux.org> 0.103.0-alt1
- new version

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.99.0-alt3
- fix build requires

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.99.0-alt2
- fix to build

* Sun Jan 16 2011 Sergey V Turchin <zerg@altlinux.org> 0.99.0-alt1
- new version

* Sun Jan 16 2011 Sergey V Turchin <zerg@altlinux.org> 0.96.1-alt2
- rebuilt

* Fri Jul 23 2010 Sergey V Turchin <zerg@altlinux.org> 0.96.1-alt1
- new version

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.95.1-alt0.M51.1
- build for M51

* Mon Jan 18 2010 Sergey V Turchin <zerg@altlinux.org> 0.95.1-alt1
- built for ALT

