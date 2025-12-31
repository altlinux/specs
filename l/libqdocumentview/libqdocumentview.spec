%define _unpackaged_files_terminate_build 1

Name: libqdocumentview
Version: 0.3.0.1
Release: alt1

Summary: QDocumentView is a widget to render multi-page documents
License: GPL-3.0-only
Group: System/Libraries
Url: https://gitlab.com/extraqt/qdocumentview

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(poppler-qt6)

%description
%summary. Also provides the abstract QDocument class, which can be
used to build backends for various single/multi-page document formats,
like PDF, DjVu, etc.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
%summary. Also provides the abstract QDocument class, which can be
used to build backends for various single/multi-page document formats,
like PDF, DjVu, etc.

This package provides the files necessary for development with
%name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc Changelog README.md ReleaseNotes
%_libdir/libQt6DocumentView.so.0
%_libdir/libQt6DocumentView.so.0.3.0

%files devel
%dir %_includedir/qdocumentview
%dir %_includedir/qdocumentview/qt6
%_includedir/qdocumentview/qt6/PopplerDocument.hpp
%_includedir/qdocumentview/qt6/QDocument.hpp
%_includedir/qdocumentview/qt6/QDocumentNavigation.hpp
%_includedir/qdocumentview/qt6/QDocumentPluginInterface.hpp
%_includedir/qdocumentview/qt6/QDocumentPrintOptions.hpp
%_includedir/qdocumentview/qt6/QDocumentRenderOptions.hpp
%_includedir/qdocumentview/qt6/QDocumentRenderer.hpp
%_includedir/qdocumentview/qt6/QDocumentSearch.hpp
%_includedir/qdocumentview/qt6/QDocumentView.hpp
%_libdir/libQt6DocumentView.so
%_pkgconfigdir/Qt6DocumentView.pc

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0.1-alt1
- Initial build for Sisyphus
