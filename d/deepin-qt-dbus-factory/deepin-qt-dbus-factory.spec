%global soname dframeworkdbus
%global repo   dde-qt-dbus-factory

%def_disable clang

Name: deepin-qt-dbus-factory
Version: 5.3.0.20
Release: alt1
Summary: A repository stores auto-generated Qt5 dbus code
# The entire source code is GPLv3+ except
# libdframeworkdbus/qtdbusextended/ which is LGPLv2+
License: GPL-3.0-or-later and LGPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-qt-dbus-factory
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%endif
BuildRequires: python3-devel libglvnd-devel qt5-base-devel dtk5-core-devel

%description
A repository stores auto-generated Qt5 dbus code.

%package -n libdframeworkdbus2
Summary: Library for %name
Group: Development/KDE and QT

%description -n libdframeworkdbus2
A repository stores auto-generated Qt5 dbus code.
Library for %name.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
%__subst 's|python|python3|' libdframeworkdbus/*.{pro,py}
%__subst 's|#include <QtCore/QObject>|#include <QObject>|; s|#include <QtCore/QString>|#include <QString>|' libdframeworkdbus/types/*.h tools/qdbusxml2cpp/qdbusxml2cpp.cpp
%__subst 's|<< endl|<< Qt::endl|; s|<< endl;|<< Qt::endl;|' tools/qdbusxml2cpp/qdbusxml2cpp.cpp libdframeworkdbus/types/*.cpp
%__subst 's|com.trolltech.QtDBus.QtTypeName|org.qtproject.QtDBus.QtTypeName|' xml/org.kde.StatusNotifierItem.xml tools/qdbusxml2cpp/qdbusxml2cpp.cpp
#%%__subst 's|load(dtk_qmake)|load(%%_qt5_archdatadir/mkspecs/features/dtk_qmake)|' tools/qdbusxml2cpp/qdbusxml2cpp.pro

%build
%if_enabled clang
%qmake_qt5 \
    CONFIG+=nostrip \
    LIB_INSTALL_DIR=%_libdir \
    QMAKE_STRIP= -spec linux-clang
%else
%qmake_qt5 \
    CONFIG+=nostrip \
    LIB_INSTALL_DIR=%_libdir
%endif

%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n libdframeworkdbus2
%doc README.md
%doc LICENSE
%_libdir/lib%soname.so.2*

%files devel
%_includedir/lib%soname-2.0/
%_libdir/cmake/DFrameworkdbus/
%_pkgconfigdir/%soname.pc
%_libdir/lib%soname.so

%changelog
* Wed Oct 28 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.20-alt1
- New version (5.3.0.20) with rpmgs script.
- Fixed compatibility with qt 5.15.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.19-alt1
- New version (5.3.0.19) with rpmgs script.

* Mon Aug 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.11-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
