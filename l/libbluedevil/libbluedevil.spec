%define bluedevil_major 1
%define libbluedevil libbluedevil%bluedevil_major

Name: libbluedevil
Version: 1.9.2
Release: alt1

Group: Graphical desktop/KDE
Summary: Qt-based library written in C++ to handle all Bluetooth functionality
License: GPL

Url: http://www.kde.org

Source: %name-%version.tar
# ALT
Patch100: libbluedevil-1.7-alt-fix-install-libdir.patch

# Automatically added by buildreq on Thu Sep 02 2010 (-bi)
#BuildRequires: cmake gcc-c++ glib2-devel glibc-devel-static libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libqt3-devel libxkbfile-devel qt4-designer
BuildRequires: cmake gcc-c++ glib2-devel glibc-devel libqt4-devel kde-common-devel

%description
Qt-based library written in C++ to handle all Bluetooth functionality

%package -n %libbluedevil
Summary: KDE 4 core library
Group: System/Libraries
%description -n %libbluedevil
Qt-based library written in C++ to handle all Bluetooth functionality

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: %libbluedevil = %version-%release
%description devel
This package contains header files needed if you wish to build applications
based on %name .


%prep
%setup -q
#%patch100 -p1

%build
%Kbuild

%install
%Kinstall

%files -n %libbluedevil
%_libdir/libbluedevil.so.%{bluedevil_major}*

%files devel
%_includedir/bluedevil
%_libdir/libbluedevil.so
%_pkgconfigdir/bluedevil.pc

%changelog
* Wed Jun 20 2012 Sergey V Turchin <zerg@altlinux.org> 1.9.2-alt1
- new version

* Wed Oct 12 2011 Sergey V Turchin <zerg at altlinux dot org> 1.9.1-alt0.M60P.1
- built for M60P

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 1.9.1-alt1
- new version

* Wed Oct 05 2011 Sergey V Turchin <zerg@altlinux.org> 1.9-alt1
- new version

* Mon Mar 28 2011 Sergey V Turchin <zerg@altlinux.org> 1.8.1-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.8-alt2
- fix to build

* Wed Sep 15 2010 Sergey V Turchin <zerg@altlinux.org> 1.8-alt0.M51.1
- built for M51

* Tue Sep 14 2010 Sergey V Turchin <zerg@altlinux.org> 1.8-alt1
- new version

* Fri Sep 10 2010 Sergey V Turchin <zerg@altlinux.org> 1.7-alt0.M51.1
- built for M51

* Thu Sep 02 2010 Sergey V Turchin <zerg@altlinux.org> 1.7-alt1
- initial specfile
