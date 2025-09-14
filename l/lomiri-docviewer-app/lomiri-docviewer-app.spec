%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%set_verify_elf_method none

Name: lomiri-docviewer-app
Version: 3.1.3
Release: alt1

Summary: Document Viewer App for Lomiri Operating Environment
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/apps/lomiri-docviewer-app

Source: %name-%version.tar

# sync with 3.1.1+dfsg-4 version from Debian unstable + local fixes
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(poppler-qt5)
BuildRequires: libreofficekit-still-devel

Requires: libqt5-qml
Requires: libqt5-quick
Requires: qml(Lomiri.Components)
Requires: qml(Lomiri.Content)
Requires: qml(Lomiri.Layouts)

%description
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides Lomiri's Document Viewer App.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCLICK_MODE=OFF \
       -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README-Developers.md README.md README-MergeRequest.md
%_bindir/lomiri-docviewer-app
%_man1dir/lomiri-docviewer-app.1.*
%_desktopdir/lomiri-docviewer-app.desktop
%_iconsdir/hicolor/scalable/apps/lomiri-docviewer-app.svg
%dir %_qt5_qmldir/DocumentViewer
%_qt5_qmldir/DocumentViewer/qmldir
%_qt5_qmldir/DocumentViewer/libfileqmlplugin.so
%dir %_qt5_qmldir/DocumentViewer/LibreOffice
%_qt5_qmldir/DocumentViewer/LibreOffice/Viewer.qml
%_qt5_qmldir/DocumentViewer/LibreOffice/liblibreofficetoolkitqmlplugin.so
%_qt5_qmldir/DocumentViewer/LibreOffice/qmldir
%dir %_qt5_qmldir/DocumentViewer/PDF
%_qt5_qmldir/DocumentViewer/PDF/Viewer.qml
%_qt5_qmldir/DocumentViewer/PDF/libpopplerqmlplugin.so
%_qt5_qmldir/DocumentViewer/PDF/qmldir
%dir %_datadir/lomiri-docviewer-app
%_datadir/lomiri-docviewer-app/*
%_datadir/lomiri-content-hub/peers/lomiri-docviewer-app
%_datadir/lomiri-url-dispatcher/urls/lomiri-docviewer-app.url-dispatcher
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-docviewer-app.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-docviewer-app.mo

%changelog
* Sat Sep 13 2025 Nikolay Strelkov <snk@altlinux.org> 3.1.3-alt1
- New version 3.1.3.

* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
