%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mauikit-imagetools
Version: 4.0.2
Release: alt1

Summary: MauiKit Image Tools Components
License: LGPL-3.0-only
Group: Development/KDE and QT
Url: https://invent.kde.org/maui/mauikit-imagetools

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6Positioning)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kde6-libkexiv2-devel
BuildRequires: libmauikit-devel
BuildRequires: pkgconfig(opencv4)
BuildRequires: pkgconfig(tesseract)

# no libmauikit-calendar
ExcludeArch: %ix86 riscv64

Requires: kde6-kquickimageeditor
Requires: libmauikit-calendar
Requires: libmauikit
Requires: libmauikit-filebrowsing
Requires: libqt6-location
Requires: libqt6-positioning
Requires: libqt6-multimediaquick
Requires: libqt6-qml
Requires: libqt6-quick
Requires: libqt6-quickcontrols2
Requires: libqt6-quickeffects
Requires: libqt6-quickshapes
Requires: libqt6-quicklayouts

%description
%summary.

%package data
Summary: Data file for %name
Group: Other
BuildArch: noarch

%description data
%summary. Data file for %name.

%package -n lib%{name}
Summary: Library files for %name
Group: System/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-data = %{version}-%{release}

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

%find_lang mauikitimagetools

%files -f mauikitimagetools.lang
%doc README.md
%_libdir/libMauiKitImageToolsEditor4.so
%dir %_libdir/qt6/qml/org/mauikit/imagetools
%_libdir/qt6/qml/org/mauikit/imagetools/*.*
%dir %_libdir/qt6/qml/org/mauikit/imagetools/editor
%_libdir/qt6/qml/org/mauikit/imagetools/editor/*.*
%dir %_libdir/qt6/qml/org/mauikit/imagetools/editor/private
%_libdir/qt6/qml/org/mauikit/imagetools/editor/private/*.*
%_libdir/qt6/qml/org/mauikit/imagetools/editor/qmldir
%dir %_libdir/qt6/qml/org/mauikit/imagetools/image2text
%_libdir/qt6/qml/org/mauikit/imagetools/image2text/OCRPage.qml
%_libdir/qt6/qml/org/mauikit/imagetools/kde-qmlmodule.version
%_libdir/qt6/qml/org/mauikit/imagetools/libMauiKitImageTools4plugin.so
%_libdir/qt6/qml/org/mauikit/imagetools/qmldir
%dir %_datadir/org/mauikit/imagetools

%files data
%_datadir/org/mauikit/imagetools/cities.db

%files -n lib%{name}
%_libdir/libMauiKitImageTools4.so.4
%_libdir/libMauiKitImageTools4.so.4.0.2

%files -n lib%{name}-devel
%_includedir/MauiKit4/FileBrowsing/imagetools_version.h
%_includedir/MauiKit4/ImageTools/cities.h
%_includedir/MauiKit4/ImageTools/city.h
%_includedir/MauiKit4/ImageTools/exiv2extractor.h
%_includedir/MauiKit4/ImageTools/imagetools_export.h
%_includedir/MauiKit4/ImageTools/moduleinfo.h
%_includedir/MauiKit4/ImageTools/textscanner.h
%_libdir/cmake/MauiKitImageTools4/MauiKitImageTools4Config.cmake
%_libdir/cmake/MauiKitImageTools4/MauiKitImageTools4ConfigVersion.cmake
%_libdir/cmake/MauiKitImageTools4/MauiKitImageTools4Targets-noconfig.cmake
%_libdir/cmake/MauiKitImageTools4/MauiKitImageTools4Targets.cmake
%_libdir/libMauiKitImageTools4.so

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
