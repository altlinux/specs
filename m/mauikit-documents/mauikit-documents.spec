%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mauikit-documents
Version: 4.0.2
Release: alt2

Summary: MauiKit QtQuick plugins for text editing
License: LGPL-3.0-only
Group: Development/KDE and QT
Url: https://invent.kde.org/maui/mauikit-documents

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: libmauikit-devel
BuildRequires: pkgconfig(poppler-qt6)
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kfilemetadata-devel
BuildRequires: pkgconfig(zlib)

Requires: libmauikit
Requires: libqt6-qml
Requires: libqt6-quick
Requires: libqt6-quickcontrols2
Requires: libqt6-quicklayouts

%description
%summary.

%package -n lib%{name}
Summary: Library files for %name
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}
%summary. Library files for %name.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}-devel
%summary. Development files for %name.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang mauikitdocuments

%files -f mauikitdocuments.lang
%doc README.md
%dir %_libdir/qt6/qml/org/mauikit/documents
%_libdir/qt6/qml/org/mauikit/documents/MauiKitDocuments4.qmltypes
%_libdir/qt6/qml/org/mauikit/documents/kde-qmlmodule.version
%_libdir/qt6/qml/org/mauikit/documents/libMauiKitDocuments4plugin.so
%dir %_libdir/qt6/qml/org/mauikit/documents/poppler
%_libdir/qt6/qml/org/mauikit/documents/poppler/PDFViewer.qml
%_libdir/qt6/qml/org/mauikit/documents/qmldir

%files -n lib%{name}
%_libdir/libMauiKitDocuments4.so.4
%_libdir/libMauiKitDocuments4.so.4.0.2

%files -n lib%{name}-devel
%dir %_includedir/MauiKit4/Documents
%_includedir/MauiKit4/Documents/documents_export.h
%_includedir/MauiKit4/Documents/documents_version.h
%_includedir/MauiKit4/Documents/moduleinfo.h
%dir %_libdir/cmake/MauiKitDocuments4
%_libdir/cmake/MauiKitDocuments4/MauiKitDocuments4Config.cmake
%_libdir/cmake/MauiKitDocuments4/MauiKitDocuments4ConfigVersion.cmake
%_libdir/cmake/MauiKitDocuments4/MauiKitDocuments4Targets-noconfig.cmake
%_libdir/cmake/MauiKitDocuments4/MauiKitDocuments4Targets.cmake
%_libdir/libMauiKitDocuments4.so

%changelog
* Fri Feb 06 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt2
- Fixed FTBFS with Qt 6.10.

* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
