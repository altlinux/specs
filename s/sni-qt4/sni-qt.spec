
%define rname sni-qt

Name: sni-qt4
Version: 0.2.7
Release: alt0.1

Group: System/Libraries
Summary: Plugin for Qt4 that turns QSystemTrayIcons into status notifiers
Url: https://launchpad.net/sni-qt
License: LGPLv3

Provides: %rname = %EVR
Obsoletes: %rname < %EVR

Source: %rname-%version.tar
Source1: sni-qt.conf

# Automatically added by buildreq on Mon Oct 05 2015 (-bi)
# optimized out: cmake-modules elfutils fontconfig libdbusmenu-qt2 libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-webkit-devel libqt4-xml libstdc++-devel pkg-config python-base python3 python3-base ruby ruby-stdlibs
#BuildRequires: cmake gcc-c++ libdbusmenu-qt-devel libicu50 libqt3-devel phonon-devel python-module-google qt4-designer rpm-build-python3 rpm-build-ruby
BuildRequires(pre): kde-common-devel
BuildRequires: cmake gcc-c++ libqt4-devel libdbusmenu-qt-devel phonon-devel

%description
This package contains a Qt4 plugin which turns all QSystemTrayIcon into
StatusNotifierItems (appindicators).

%prep
%setup -qn %rname-%version

%build
%Kbuild

%install
%Kinstall

install -m644 -D -p %SOURCE1 %buildroot/%_xdgconfigdir/sni-qt.conf

%files
%doc COPYING NEWS README
%config(noreplace) %_xdgconfigdir/sni-qt.conf
%_qt4dir/plugins/systemtrayicon/

%changelog
* Mon Oct 05 2015 Sergey V Turchin <zerg@altlinux.org> 0.2.7-alt0.1
- initial build
- use snapshot 20151015
