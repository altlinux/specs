%define soname 1

Name: pdf4qt
Version: 1.6.0.0
Release: alt1

Summary: Open source PDF editor

License: MIT
Group: Office

Url: https://jakubmelka.github.io
Vcs: https://github.com/JakubMelka/PDF4QT

ExcludeArch: i586

Source: %name-%version.tar

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

%package -n libpdf4qtlibcore%soname
Group: System/Libraries
Summary: %name library
Obsoletes: libpdf4qtlibcore <= 1.5.3.0-alt1
%description -n libpdf4qtlibcore%soname
%name library.

%package -n libpdf4qtlibwidgets%soname
Group: System/Libraries
Summary: %name library
Obsoletes: libpdf4qtlibwidgets <= 1.5.3.0-alt1
%description -n libpdf4qtlibwidgets%soname
%name library.

%package -n libpdf4qtlibgui%soname
Group: System/Libraries
Summary: %name library
%description -n libpdf4qtlibgui%soname
%name library.

%prep
%setup
#fix: start app from LaunchPad
subst 's|QString("./%1")|QString("/usr/bin/%1")|' Pdf4QtLaunchPad/launchapplication.cpp
#fix: load plugins
subst 's|"lib"|"lib64"|' Pdf4QtLibGui/pdfprogramcontroller.cpp
#fix: load translations
subst 's|applicationDirectory.absolutePath()|"%_datadir/pdf4qt/translations/"|' Pdf4QtLibCore/sources/pdfapplicationtranslator.cpp

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc *.md *.txt LICENSE
%_bindir/*
%_libdir/%name
%_datadir/applications/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.appdata.xml
%_datadir/%name

%files devel
%_includedir/*/*.h
%_libdir/libPdf4QtLibCore.so
%_libdir/libPdf4QtLibWidgets.so
%_libdir/libPdf4QtLibGui.so

%files -n libpdf4qtlibgui%soname
%_libdir/libPdf4QtLibGui.so.%{soname}.*

%files -n libpdf4qtlibcore%soname
%_libdir/libPdf4QtLibCore.so.%{soname}.*

%files -n libpdf4qtlibwidgets%soname
%_libdir/libPdf4QtLibWidgets.so.%{soname}.*

%changelog
* Mon Jun 15 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.6.0.0-alt1
- 1.5.3.1 -> 1.6.0.0

* Mon Jan 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.5.3.1-alt1
- 1.5.3.0 -> 1.5.3.1

* Mon Jan 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.5.3.0-alt1
- 1.5.2.0 -> 1.5.3.0

* Tue Nov 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.5.2.0-alt2
- fix: build with new blend2d 0.21.2

* Wed Oct 08 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.5.2.0-alt1
- Initial build for ALT Linux.
