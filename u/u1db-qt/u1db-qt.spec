%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: u1db-qt
Version: 0.1.8
Release: alt1

Summary: Simple Qt5 binding and QtQuick2 plugin for U1DB
License: GPL-3.0-only
Group: System/Libraries
Url: https://gitlab.com/ubports/development/core/u1db-qt

Source: %name-%version.tar

# sync with version 0.1.8 from Debian unstable
Patch: %name-%version-%release.patch
Source1: service-u1.svg

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: qt5-tools

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /usr/bin/dbus-test-runner
BuildRequires: /usr/bin/xvfb-run
%endif

%description
%summary

%package -n lib%{name}5
Group: System/Libraries
Summary: Qt5 binding for U1DB - shared library

%description -n lib%{name}5
Simple Qt5 binding and QtQuick2 plugin for U1DB.

This package contains the shared library.

%package -n lib%{name}5-devel
Group: Development/KDE and QT
Summary: Qt5 binding and QtQuick2 plugin for U1DB - development files
Requires: lib%{name}5 = %{version}-%{release}

%description -n lib%{name}5-devel
Simple Qt5 binding and QtQuick2 plugin for U1DB.

This package contains the developer headers for the Qt binding for U1DB

%package -n lib%{name}5-examples
Group: Development/KDE and QT
Summary: Qt5 binding and QtQuick2 plugin for U1DB - examples
Requires: lib%{name}5 = %{version}-%{release}

%description -n lib%{name}5-examples
Simple Qt5 binding and QtQuick2 plugin for U1DB.

This package contains examples showcasing the use of the Qt binding for
U1DB.

%package -n lib%{name}5-doc
Group: Documentation
Summary: Qt5 binding and QtQuick2 plugin for U1DB - offline documentation

%description -n lib%{name}5-doc
Simple Qt5 binding and QtQuick2 plugin for U1DB.

This package contains the offline documentation for the Qt binding for
U1DB.

%prep
%setup
%patch -p1

%build
export PATH=$PATH:/usr/share/qt5/bin
%cmake \
       -DBUILD_DOCS=ON
%cmake_build

%install
%cmake_install

install -m644 -D %SOURCE1 %buildroot%_iconsdir/hicolor/scalable/apps/service-u1.svg

%check
export PATH=$PATH:/usr/share/qt5/bin
xvfb-run %ctest -j1 -VV

%files -n lib%{name}5
%doc AUTHORS ChangeLog COPYING HACKING
%_libdir/libu1db-qt5.so.3
%_libdir/libu1db-qt5.so.3.0.0
%dir %_qt5_qmldir/U1db
%_qt5_qmldir/U1db/libU1DBPlugin.so
%_qt5_qmldir/U1db/plugins.qmltypes
%_qt5_qmldir/U1db/qmldir

%files -n lib%{name}5-devel
%dir %_includedir/libu1db-qt5
%_includedir/libu1db-qt5/database.h
%_includedir/libu1db-qt5/document.h
%_includedir/libu1db-qt5/global.h
%_includedir/libu1db-qt5/index.h
%_includedir/libu1db-qt5/query.h
%_includedir/libu1db-qt5/synchronizer.h
%_libdir/libu1db-qt5.so
%_pkgconfigdir/libu1db-qt5.pc
%_datadir/qt5/doc/qch/u1dbqt.qch
%_datadir/qtcreator/templates/qml/contacts/main.qml
%_datadir/qtcreator/templates/qml/contacts/template.xml
%_datadir/qtcreator/templates/qml/settings/main.qml
%_datadir/qtcreator/templates/qml/settings/template.xml

%files -n lib%{name}5-examples
%_desktopdir/u1db-qt-gallery.desktop
%_iconsdir/hicolor/scalable/apps/service-u1.svg
%dir %_datadir/u1db-qt
%dir %_datadir/u1db-qt/examples
%_datadir/u1db-qt/examples/AdvancedGame.qml
%_datadir/u1db-qt/examples/CreatePlayerPage.qml
%_datadir/u1db-qt/examples/FilterPlayers.qml
%_datadir/u1db-qt/examples/ListPlayers.qml
%_datadir/u1db-qt/examples/bookmarks.qml
%_datadir/u1db-qt/examples/u1db-qt-example-1.qml
%_datadir/u1db-qt/examples/u1db-qt-example-2.qml
%_datadir/u1db-qt/examples/u1db-qt-example-2b.qml
%_datadir/u1db-qt/examples/u1db-qt-example-3.qml
%_datadir/u1db-qt/examples/u1db-qt-example-5.qml
%_datadir/u1db-qt/examples/u1db-qt-example-6.qml
%_datadir/u1db-qt/examples/u1db-qt-example-7.qml
%dir %_datadir/u1db-qt/gallery
%_datadir/u1db-qt/gallery/SplitView.qml
%_datadir/u1db-qt/gallery/gallery.qml

%files -n lib%{name}5-doc
%dir %_datadir/doc/u1db-qt
%dir %_datadir/doc/u1db-qt/html
%_datadir/doc/u1db-qt/html/concepts.html
%_datadir/doc/u1db-qt/html/overview.html
%_datadir/doc/u1db-qt/html/qml-u1db-database-members.html
%_datadir/doc/u1db-qt/html/qml-u1db-database.html
%_datadir/doc/u1db-qt/html/qml-u1db-document-members.html
%_datadir/doc/u1db-qt/html/qml-u1db-document.html
%_datadir/doc/u1db-qt/html/qml-u1db-index-members.html
%_datadir/doc/u1db-qt/html/qml-u1db-index.html
%_datadir/doc/u1db-qt/html/qml-u1db-query-members.html
%_datadir/doc/u1db-qt/html/qml-u1db-query.html
%_datadir/doc/u1db-qt/html/qml-u1db-synchronizer-members.html
%_datadir/doc/u1db-qt/html/qml-u1db-synchronizer.html
%dir %_datadir/doc/u1db-qt/html/style
%_datadir/doc/u1db-qt/html/style/base.css
%_datadir/doc/u1db-qt/html/style/css_002.css
%_datadir/doc/u1db-qt/html/style/qtquick.css
%_datadir/doc/u1db-qt/html/style/reset.css
%_datadir/doc/u1db-qt/html/style/scratch.css
%_datadir/doc/u1db-qt/html/tutorial.html
%_datadir/doc/u1db-qt/html/u1db-qmlmodule.html
%_datadir/doc/u1db-qt/html/u1db-qt-tutorial-1.html
%_datadir/doc/u1db-qt/html/u1db-qt-tutorial-2.html
%_datadir/doc/u1db-qt/html/u1db-qt-tutorial-2b.html
%_datadir/doc/u1db-qt/html/u1db-qt-tutorial-3.html
%_datadir/doc/u1db-qt/html/u1db-qt-tutorial-5.html
%_datadir/doc/u1db-qt/html/u1db-qt-tutorial-6.html
%_datadir/doc/u1db-qt/html/u1db-qt.index
%_datadir/qt5/phrasebooks/u1dbqt.qch

%changelog
* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.8-alt1
- Initial build for Sisyphus
