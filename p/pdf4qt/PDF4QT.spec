Name: pdf4qt
Version: 1.5.2.0
Release: alt2

Summary: Open source PDF editor

License: MIT
Group: Office

Url: https://jakubmelka.github.io
Vcs: https://github.com/JakubMelka/PDF4QT

ExcludeArch: i586

Source: %name-%version.tar

#migrated to blend2d 0.21.0
Patch: pdfblpainter-1.5.2.0-alt-build.patch
#move translations
Patch1: CMakeLists-1.5.2.0-alt-fixes.patch

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake clang qt6-base-devel qt6-tools-devel
BuildRequires: qt6-svg-devel qt6-speech-devel libcups-devel
BuildRequires: zlib-devel libfreetype-devel libopenjpeg2.0-devel
BuildRequires: openjpeg-tools2.0 libjpeg-devel blend2d-devel
BuildRequires: liblcms2-devel tbb-devel

%description
%summary.

%package devel
Group:Development/C++
Summary: Development files for %name
%description devel
This package contains libraries and header files for
developing applications that use %name.

%package -n libpdf4qtlibcore
Group: System/Libraries
Summary: %name library
%description -n libpdf4qtlibcore
%name library.

%package -n libpdf4qtlibwidgets
Group: System/Libraries
Summary: %name library
%description -n libpdf4qtlibwidgets
%name library.

%prep
%setup
%autopatch -p0
#fix start app from LaunchPad
subst 's|QString("./%1")|QString("/usr/bin/%1")|' Pdf4QtLaunchPad/launchdialog.cpp
#fix load plugins
subst 's|"lib"|"lib64"|' Pdf4QtLibGui/pdfprogramcontroller.cpp
#fix load translations
subst 's|applicationDirectory.absolutePath()|"%_datadir/Pdf4qt/translations/"|' Pdf4QtLibCore/sources/pdfapplicationtranslator.cpp
#fix: build with new blend2d 0.21.2
subst 's|<blend2d.h>|<blend2d/blend2d.h>|' Pdf4QtLibCore/sources/pdfblpainter.cpp

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc *.md *.txt LICENSE
%_bindir/*
%_libdir/%name
%_libdir/libPdf4QtLibGui.so.%version
%_libdir/libPdf4QtLibGui.so
%_datadir/applications/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.appdata.xml
%_datadir/Pdf4qt/*

%files devel
%_includedir/*/*.h
%_libdir/libPdf4QtLibCore.so
%_libdir/libPdf4QtLibWidgets.so

%files -n libpdf4qtlibcore
%_libdir/libPdf4QtLibCore.so.%version

%files -n libpdf4qtlibwidgets
%_libdir/libPdf4QtLibWidgets.so.%version

%changelog
* Tue Nov 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.5.2.0-alt2
- fix: build with new blend2d 0.21.2

* Wed Oct 08 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.5.2.0-alt1
- Initial build for ALT Linux.
