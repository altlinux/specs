%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: lomiri-content-hub
Version: 2.2.3
Release: alt1

Summary: content sharing/picking service for Lomiri
License: GPL-3.0-only and LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-content-hub

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: ayatana-cmake-modules
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(lomiri-download-manager-client)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libapparmor)
BuildRequires: doxygen
BuildRequires: /usr/bin/dot
BuildRequires: qt5-declarative-devel

%if_with check
BuildRequires: ctest
BuildRequires: pkgconfig(gtest)
BuildRequires: dbus
BuildRequires: /usr/bin/dbus-test-runner
BuildRequires: /usr/bin/xvfb-run
%endif

# qt5/qml/QtQuick.2/qmldir
Requires: libqt5-quick

%description
Content sharing/picking infrastructure and service, designed to allow
apps to securely and efficiently exchange content.

This package includes the content sharing service.

%package -n lib%{name}
Summary: content sharing/picking library for Lomiri - shared libraries
Group: System/Libraries

%description -n lib%{name}
Content sharing/picking infrastructure and service, designed to allow
apps to securely and efficiently exchange content.

This package contains the Qt5 shared librares.

%package -n lib%{name}-devel
Summary: content sharing development files (Qt5)
Group: Development/KDE and QT
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
Content sharing/picking infrastructure and service, designed to allow
apps to securely and efficiently exchange content.

This package contains the Qt5 development headers of the library.

%package doc
Summary: Documentation files for Lomiri's liblomiri-content-hub-dev
Group: Documentation
BuildArch: noarch

%description doc
Content sharing/picking infrastructure and service, designed to allow
apps to securely and efficiently exchange content.

Documentation files for the liblomiri-content-hub development

%if_with check
%package -n %{name}-testability
Summary: content sharing testability for Lomiri
Group: Development/KDE and QT

%description -n %{name}-testability
Content sharing/picking infrastructure and service, designed to allow
apps to securely and efficiently exchange content.

Files and utilities needed for automated testing of content-hub
%endif

%prep
%setup
%patch -p1

sed -i '/^Comment/d' tools/send/lomiri-content-hub-send.desktop

%if_with check
echo "Categories=Development;Debugger;" >> tests/peers/importer/lomiri-content-hub-test-importer.desktop
echo "Categories=Development;Debugger;" >> tests/peers/exporter/lomiri-content-hub-test-exporter.desktop
echo "Categories=Development;Debugger;" >> tests/peers/sharer/lomiri-content-hub-test-sharer.desktop
%endif

%build
%cmake \
       -W no-dev \
       -DQML_PLUGIN_DUMP=%_qt5_bindir/qmlplugindump \
       -DQDOC_EXECUTABLE=%_qt5_bindir/qdoc \
       -DENABLE_COVERAGE=OFF \
%if_with check
       -DENABLE_TESTS=ON
%else
       -DENABLE_TESTS=OFF
%endif
%cmake_build

%install
%cmake_install

%find_lang %name

%check
%ctest -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING.GPL COPYING.LGPL README.md
%_bindir/lomiri-content-hub-send
%_bindir/lomiri-content-hub-service
%_desktopdir/lomiri-content-hub-send.desktop
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-content-hub.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-content-hub.mo
%_datadir/dbus-1/services/com.lomiri.content.dbus.Service.service
%_datadir/lomiri-url-dispatcher/urls/lomiri-content-hub-send.url-dispatcher
%_qt5_qmldir/Lomiri/Content/ContentPageHeader.qml
%_qt5_qmldir/Lomiri/Content/ContentPeerPicker10.qml
%_qt5_qmldir/Lomiri/Content/ContentPeerPicker11.qml
%_qt5_qmldir/Lomiri/Content/ContentPeerPicker13.qml
%_qt5_qmldir/Lomiri/Content/ContentTransferHint.qml
%_qt5_qmldir/Lomiri/Content/ResponsiveGridView.qml
%_qt5_qmldir/Lomiri/Content/liblomiri-content-hub-plugin.so
%_qt5_qmldir/Lomiri/Content/plugins.qmltypes
%_qt5_qmldir/Lomiri/Content/qmldir
%dir %_datadir/lomiri-content-hub
%dir %_datadir/lomiri-content-hub/icons
%_datadir/lomiri-content-hub/icons/xorg.png
%_datadir/glib-2.0/schemas/com.lomiri.content.hub.gschema.xml

%files -n lib%{name}
%_libdir/liblomiri-content-hub.so.1*
%_libdir/liblomiri-content-hub-glib.so.1*

%files -n lib%{name}-devel
%_includedir/com/lomiri/content/glib/content-hub-glib-compat.h
%_includedir/com/lomiri/content/glib/content-hub-glib.h
%_includedir/qt5/com/lomiri/content/hub.h
%_includedir/qt5/com/lomiri/content/import_export_handler.h
%_includedir/qt5/com/lomiri/content/item.h
%_includedir/qt5/com/lomiri/content/paste.h
%_includedir/qt5/com/lomiri/content/peer.h
%_includedir/qt5/com/lomiri/content/scope.h
%_includedir/qt5/com/lomiri/content/store.h
%_includedir/qt5/com/lomiri/content/transfer.h
%_includedir/qt5/com/lomiri/content/type.h
%_libdir/liblomiri-content-hub.so
%_libdir/liblomiri-content-hub-glib.so
%_pkgconfigdir/liblomiri-content-hub.pc
%_pkgconfigdir/liblomiri-content-hub-glib.pc

%files doc
%dir %_docdir/%name
%_docdir/%name/*

%if_with check
%files -n %{name}-testability
%_bindir/lomiri-content-hub-test-exporter
%_bindir/lomiri-content-hub-test-importer
%_bindir/lomiri-content-hub-test-sharer
%_desktopdir/lomiri-content-hub-test-exporter.desktop
%_desktopdir/lomiri-content-hub-test-importer.desktop
%_desktopdir/lomiri-content-hub-test-sharer.desktop
%_iconsdir/hicolor/512x512/apps/lomiri-content-hub-test-exporter.png
%_iconsdir/hicolor/512x512/apps/lomiri-content-hub-test-importer.png
%_iconsdir/hicolor/512x512/apps/lomiri-content-hub-test-sharer.png
%dir %_datadir/lomiri-content-hub/peers
%_datadir/lomiri-content-hub/peers/lomiri-content-hub-test-exporter
%_datadir/lomiri-content-hub/peers/lomiri-content-hub-test-importer
%_datadir/lomiri-content-hub/peers/lomiri-content-hub-test-sharer
%dir %_datadir/lomiri-content-hub/testability
%dir %_datadir/lomiri-content-hub/testability/data
%_datadir/lomiri-content-hub/testability/data/*
%endif

%changelog
* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 2.2.3-alt1
- New version 2.2.3.

* Sun Feb 15 2026 Nikolay Strelkov <snk@altlinux.org> 2.2.2-alt2
- Fixed FTBFS.

* Fri Dec 26 2025 Nikolay Strelkov <snk@altlinux.org> 2.2.2-alt1
- New version 2.2.2.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 2.2.1-alt1
- New version 2.2.1.

* Thu Dec 04 2025 Nikolay Strelkov <snk@altlinux.org> 2.2.0-alt1
- New version 2.2.0.

* Wed Jul 16 2025 Nikolay Strelkov <snk@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
