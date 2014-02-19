Name: libmm-qt
Version: 1.0.1
Release: alt1

Group: System/Libraries
Summary: Qt-only wrapper for ModemManager DBus API
Url: https://projects.kde.org/projects/extragear/libs/libmm-qt
License: LGPLv2+

Requires: ModemManager >= 1.0.0

Source: %name-%version.tar

# Automatically added by buildreq on Tue Feb 18 2014 (-bi)
# optimized out: cmake-modules elfutils libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel pkg-config python-base ruby ruby-stdlibs
#BuildRequires: ModemManager-devel cmake doxygen gcc-c++ graphviz phonon-devel qt4-designer rpm-build-ruby
BuildRequires: ModemManager-devel cmake gcc-c++ libqt4-devel kde-common-devel

%description
Qt library for ModemManager

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Qt libraries and header files for developing applications that use ModemManager

%prep
%setup -q

%build
%Kbuild

%install
%Kinstall

%files
%_libdir/libModemManagerQt.so.*

%files devel
%doc README
%_pkgconfigdir/ModemManagerQt.pc
%_includedir/ModemManagerQt/
%_libdir/libModemManagerQt.so

%changelog
* Tue Feb 18 2014 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- initial build
