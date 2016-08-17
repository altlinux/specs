
%define rname appmenu-qt
Name: appmenu-qt4
Version: 0.2.7
Release: alt0.1

Group: Graphical desktop/Other
Summary: Global application menu to Qt
Url: http://launchpad.net/appmenu-qt
License: LGPLv2 with exceptions and GPLv3

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Feb 11 2013 (-bi)
# optimized out: cmake-modules elfutils fontconfig libdbusmenu-qt2 libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel pkg-config python-base ruby ruby-stdlibs
#BuildRequires: cmake gcc-c++ libdbusmenu-qt-devel libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 phonon-devel python-module-distribute rpm-build-ruby
BuildRequires: cmake gcc-c++ libdbusmenu-qt-devel libqt4-devel
BuildRequires: kde-common-devel

%description
This package allows Qt to export its menus over DBus.

%prep
%setup -qn %rname-%version

%build
%Kbuild \
    -DUSE_QT4=ON \
    #

%install
%Kinstall

%files
%doc LGPL_EXCEPTION.txt NEWS README
%_qt4dir/plugins/menubar/libappmenu-qt.so

%changelog
* Wed Aug 17 2016 Sergey V Turchin <zerg@altlinux.org> 0.2.7-alt0.1
- use 0.2.7 20140305 snapshot

* Mon Feb 11 2013 Sergey V Turchin <zerg@altlinux.org> 0.2.6-alt1
- initial build

