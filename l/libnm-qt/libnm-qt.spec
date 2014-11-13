
Name: libnm-qt
Version: 0.9.8.3
Release: alt1
Epoch: 1

Group: System/Libraries
Summary: Qt-only wrapper for NetworkManager DBus API
Url: https://projects.kde.org/projects/extragear/libs/libnm-qt
License: LGPLv2+

Requires: NetworkManager-daemon

Source: %name-%version.tar

# Automatically added by buildreq on Tue Feb 18 2014 (-bi)
# optimized out: ModemManager-devel NetworkManager-devel cmake-modules elfutils glib2-devel libdbus-devel libdbus-glib-devel libmm-qt libnm-glib-devel libnm-util-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-xml libstdc++-devel pkg-config python-base ruby ruby-stdlibs
#BuildRequires: cmake doxygen gcc-c++ graphviz libmm-qt-devel phonon-devel qt4-designer rpm-build-ruby
BuildRequires: cmake gcc-c++ libmm-qt-devel libqt4-devel kde-common-devel NetworkManager-glib-devel

%description
Qt library for NetworkManager

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Qt libraries and header files for developing applications
that use NetworkManager

%prep
%setup -q

%build
%Kbuild

%install
%Kinstall

%files
%_libdir/libNetworkManagerQt.so.*

%files devel
%_pkgconfigdir/NetworkManagerQt.pc
%_libdir/libNetworkManagerQt.so
%_includedir/NetworkManagerQt/

%changelog
* Thu Nov 13 2014 Sergey V Turchin <zerg@altlinux.org> 1:0.9.8.3-alt1
- new version

* Tue Aug 26 2014 Sergey V Turchin <zerg@altlinux.org> 1:0.9.8.2-alt10
- fallback to stable release

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.9.1-alt2
- rebuild with new NM

* Mon May 12 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.9.1-alt1
- new version

* Tue Feb 18 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.8.1-alt1
- initial build
