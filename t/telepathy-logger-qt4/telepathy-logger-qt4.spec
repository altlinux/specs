
Name: telepathy-logger-qt4
Version: 0.4.0
Release: alt1
%define sover 1
%define libname lib%name%sover

Group: Networking/Instant messaging
Summary: Qt Wrapper around TpLogger client library
Url: https://projects.kde.org/telepathy-logger-qt
License: LGPLv2.1+

Source: %name-%version.tar
Patch1: 0.1.0-alt-shared.patch
Patch2: 0.1.0-alt-install.patch
Patch3: 0.1.0-alt-pkgconfig.patch

# Automatically added by buildreq on Wed May 30 2012 (-bi)
# optimized out: boost-devel-headers cmake-modules elfutils glib2-devel libdbus-devel libdbus-glib libdbus-glib-devel libgio-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel libtelepathy-glib libtelepathy-glib-devel libtelepathy-logger libtelepathy-qt4 libxml2-devel pkg-config python-base python-devel python-modules python-modules-encodings python-modules-xml qt-gstreamer qt4-designer xml-utils
#BuildRequires: cmake doxygen flex gcc-c++ graphviz libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 libtelepathy-logger-devel libtelepathy-qt4-devel phonon-devel python-module-distribute qt-gstreamer-devel
BuildRequires: cmake doxygen flex gcc-c++ graphviz libtelepathy-logger-devel libtelepathy-qt4-devel libqt4-devel phonon-devel qt-gstreamer-devel kde-common-devel

%description
Telepathy-logger-qt4 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%package devel
Group: Development/KDE and QT
Summary: Qt Wrapper around TpLogger client library
Requires: %libname
Requires: qt-gstreamer-devel
%description devel
Telepathy-logger-qt4 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%package -n %libname
Group: System/Libraries
Summary: Qt Wrapper around TpLogger client library

%description -n %libname
Telepathy-logger-qt4 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%Kbuild

%install
%Kinstall

%files -n %libname
%doc AUTHORS ChangeLog HACKING TODO
%_libdir/libtelepathy-logger-qt4.so.%sover
%_libdir/libtelepathy-logger-qt4.so.%sover.*

%files devel
%_includedir/telepathy-logger-*/TelepathyLoggerQt*/
%_libdir/lib*.so
%_libdir/pkgconfig/TelepathyLoggerQt4.pc

%changelog
* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
