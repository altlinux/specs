%define _unpackaged_files_terminate_build 1

%def_with check

Name:    mylibrary
Version: 4.2.1
Release: alt1

Summary: Home librarian
License: GPL-3.0
Group:   Office
Url:     https://github.com/ProfessorNavigator/mylibrary

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtkmm-4.0)
BuildRequires: pkgconfig(poppler-cpp)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(ddjvuapi)
BuildRequires: pkgconfig(Magick++)
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: /usr/bin/pdflatex
BuildRequires: texlive-dist

%if_with check
BuildRequires: ctest
%endif

%description
MyLibrary is a simple program for managing .fb2, .epub, .pdf and .djvu
e-book file collections. It can also work with same formats packed in
zip, 7z, jar, cpio, iso, tar, tar.gz, tar.bz2, tar.xz, rar (see notes)
archives itself or  packed in same types of archives with .fbd files
(epub, djvu and pdf books).
MyLibrary creates own database and does not change files content, names
or location.

%prep
%setup
%patch -p1
chmod -x ru.mail.bobilev_yury.MyLibrary.desktop
sed -i 's|^Categories=.*|Categories=Office;Database;Viewer;|' ru.mail.bobilev_yury.MyLibrary*.desktop

%build
%cmake -D CMAKE_BUILD_TYPE=None \
       -W no-dev \
       -D USE_OPENMP=OFF \
       -D USE_PLUGINS=ON \
       -D CREATE_HTML_DOCS_MLBOOKPROC=ON \
       -D CREATE_PDF_DOCS_MLBOOKPROC=ON \
       -D CREATE_HTML_DOCS_PLUGINIFC=ON \
       -D CREATE_PDF_DOCS_PLUGINIFC=ON
%cmake_build

%if_with check
%cmake_build --target test
%endif

%install
%cmake_install
rm -v %{buildroot}%{_datadir}/MyLibrary/COPYING

%find_lang %name --all-name

%check
%ctest

%files -f %name.lang
%doc COPYING *.md
%_bindir/%name
%dir %{_datadir}/MyLibrary/
%{_datadir}/MyLibrary/*
%{_datadir}/applications/ru.mail.bobilev_yury.MyLibrary.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_includedir}/MLBookProc
%{_includedir}/MLBookProc/*
%dir %{_includedir}/MLPluginIfc
%{_includedir}/MLPluginIfc/*
%dir %{_libdir}/cmake/MLBookProc
%{_libdir}/cmake/MLBookProc/*
%dir %{_libdir}/cmake/MLPluginIfc
%{_libdir}/cmake/MLPluginIfc/*
%{_libdir}/libml*.so*
%dir %{_datadir}/MLBookProc
%{_datadir}/MLBookProc/*
%dir %{_datadir}/doc/MLBookProc
%{_datadir}/doc/MLBookProc/*
%dir %{_datadir}/doc/MLPluginIfc
%{_datadir}/doc/MLPluginIfc/*

%changelog
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
