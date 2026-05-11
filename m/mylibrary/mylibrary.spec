%define _unpackaged_files_terminate_build 1

%def_with check

Name: mylibrary
Version: 5.0.1
Release: alt1

Summary: Home librarian
License: GPL-3.0
Group: Office
Url: https://github.com/ProfessorNavigator/mylibrary

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: qt6-tools-devel
BuildRequires: libudb-devel
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(poppler-cpp)
BuildRequires: pkgconfig(ddjvuapi)
BuildRequires: pkgconfig(Magick++)
BuildRequires: doxygen
BuildRequires: graphviz

%if_with check
BuildRequires: ctest
%endif

%description
MyLibrary is a simple program designed to manage e-book collections.
It supports following types of books: .fb2, .epub, .pdf, .djvu, .odt,
.txt, .md and .fbd (fbd can be used for any types of files, not just
books). MyLibrary also supports same types of books, packed in archives.
Supported archive types are: zip, 7z, jar, cpio, iso, tar, tar.gz,
tar.bz2, tar.xz, rar.

Additionally MyLibrary supports inpx collections. Program creates own
databases, e-book files will not be moved or edited.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
Development files for %name.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
This package includes the documentation files for the %name
development.

%prep
%setup
%patch -p1
chmod -x ru.mail.bobilev_yury.MyLibrary.desktop
sed -i 's|^Categories=.*|Categories=Office;Database;Viewer;|' ru.mail.bobilev_yury.MyLibrary*.desktop

%build
%cmake -D CMAKE_BUILD_TYPE=None \
       -W no-dev \
       -D BUILD_MLPLUGIN_DOCS=ON \
       -D CREATE_DOCS_XMLPARSERCPP=ON \
       -D BUILD_MLBOOKPROC_DOCS=ON
%cmake_build

%if_with check
%ctest
%endif

%install
%cmake_install

%find_lang %name --all-name

%check
%ctest

%files -f %name.lang
%doc COPYING README.md README_RU.md
%_bindir/MyLibrary
%_desktopdir/ru.mail.bobilev_yury.MyLibrary.desktop
%_iconsdir/hicolor/scalable/apps/mylibrary.svg
%_libdir/libMLBookProc.so.2
%_libdir/libMLBookProc.so.2.0.1
%_libdir/libMLPlugin.so.1
%_libdir/libMLPlugin.so.1.0
%_libdir/libXMLParserCPP.so.1
%_libdir/libXMLParserCPP.so.1.1

%files devel
%dir %_includedir/MLBookProc
%_includedir/MLBookProc/*
%dir %_includedir/MLPlugin
%_includedir/MLPlugin/*
%dir %_includedir/XMLParserCPP/
%_includedir/XMLParserCPP/*
%dir %_libdir/cmake/MLBookProc
%_libdir/cmake/MLBookProc/*
%dir %_libdir/cmake/MLPlugin
%_libdir/cmake/MLPlugin/*
%dir %_libdir/cmake/XMLParserCPP/
%_libdir/cmake/XMLParserCPP/*
%_libdir/libMLBookProc.so
%_libdir/libMLPlugin.so
%_libdir/libXMLParserCPP.so

%files doc
%dir %_datadir/doc/MLBookProc
%_datadir/doc/MLBookProc/*
%dir %_datadir/doc/MLPlugin
%_datadir/doc/MLPlugin/*
%dir %_datadir/doc/XMLParserCPP
%_datadir/doc/XMLParserCPP/*
%_man3dir/*

%changelog
* Mon May 11 2026 Nikolay Strelkov <snk@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Wed May 06 2026 Nikolay Strelkov <snk@altlinux.org> 5.0-alt1
- New version 5.0.

* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 4.3-alt1
- New version 4.3.

* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 4.2.2-alt1
- New version 4.2.2.

* Sat Oct 18 2025 Nikolay Strelkov <snk@altlinux.org> 4.2.1-alt1
- New version 4.2.1.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 4.1-alt2
- Applied repocop fix for freedesktop-categories

* Wed May 28 2025 Nikolay Strelkov <snk@altlinux.org> 4.1-alt1
- New version 4.1.

* Wed May 07 2025 Nikolay Strelkov <snk@altlinux.org> 4.0.1-alt1
- New version 4.0.1.

* Thu May 01 2025 Nikolay Strelkov <snk@altlinux.org> 4.0-alt1
- New version 4.0.

* Sun Feb 23 2025 Nikolay Strelkov <snk@altlinux.org> 3.2-alt1.1
- Fixed FTBFS.

* Wed Feb 19 2025 Nikolay Strelkov <snk@altlinux.org> 3.2-alt1
- New version 3.2.

* Tue Feb 04 2025 Nikolay Strelkov <snk@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
