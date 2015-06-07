Name: texworks
Version: 0.4.6
Release: alt1

Summary: A simple IDE for authoring TeX documents
Summary(ru_RU.UTF-8): Простой редактор для документов TeX

License: GPL
Group: Publishing
URL: http://tug.org/texworks/
Packager: Denis Kirienko <dk@altlinux.ru>

BuildPreReq: gcc-c++ libqt4-devel libhunspell-devel libdbus-devel libpoppler-qt4-devel unzip cmake
Requires: libqt4-core

Source0: texworks-0.4.6-20150403-git_c29723a.tar.gz
Source2: TeXworks-manual-r1029.pdf
Source4: %{name}-alt-icons.tar.bz2

Patch1: %{name}-0.4.3-desktop.patch

%description
TeXworks is an environment for authoring TeX (LaTeX, ConTeXt, etc)
documents, with a Unicode-based, TeX-aware editor, integrated PDF
viewer, and a clean, simple interface accessible to casual
and non-technical users.

You may install the texlive-* packages to make this program useful.

%description -l ru_RU.UTF-8
TeXworks - это простой редактор для работы с TeX документами (LaTeX,
ConTeXt и другие) с возможностью просмотра скомпилированных
PDF-документов и простым интерфейсом, понятным даже для
начинающих осваивать TeX.

Для того, чтобы использовать TeXworks вам также понадобится установить
пакеты texlive-*.

%package doc
Summary: Documentation for TeXworks
Summary(ru_RU.UTF-8): Документация для редактора TeXworks
Group: Publishing
Requires: %name = %version-%release
BuildArch: noarch

%description doc
User manual for TeXworks editor.

%description doc -l ru_RU.UTF-8
Документация к редактору TeXworks.

%prep
%setup -q -n texworks-0.4.6-20150403-git_c29723a -a 4
%patch1 -p1
cp %SOURCE2 .

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make

%install
cd build
%make_install DESTDIR=%buildroot install
cd ..
install -m 644 TeXworks-manual-*.pdf %buildroot/%{_docdir}/%{name}
install -m 644 -D TeXworks-16x16.png %buildroot%_miconsdir/TeXworks.png
install -m 644 -D TeXworks-32x32.png %buildroot%_niconsdir/TeXworks.png
install -m 644 -D TeXworks-48x48.png %buildroot%_liconsdir/TeXworks.png

%files
%{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/*/*/*/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*
%{_mandir}/man1/*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/README.md
%{_docdir}/%{name}/NEWS

%files doc
%{_docdir}/%{name}/TeXworks-manual-*.pdf

%changelog
* Sun Jun 07 2015 Denis Kirienko <dk@altlinux.org> 0.4.6-alt1
- Version 0.4.6

* Fri Jun 21 2013 Denis Kirienko <dk@altlinux.org> 0.4.5-alt1
- Version 0.4.5 (SVN 1281)

* Sun Apr 07 2013 Denis Kirienko <dk@altlinux.org> 0.4.4-alt2
- Rebuild with new libpoppler

* Sat Jun 02 2012 Denis Kirienko <dk@altlinux.org> 0.4.4-alt1
- Version 0.4.4 (SVN 1004)

* Fri Aug 05 2011 Denis Kirienko <dk@altlinux.ru> 0.4.3-alt1
- Version 0.4.3 (SVN 858)

* Fri Apr 22 2011 Denis Kirienko <dk@altlinux.ru> 0.4.0-alt1
- Version 0.4.0 (SVN 759)

* Fri Feb 18 2011 Denis Kirienko <dk@altlinux.ru> 0.3-alt2
- SVN 731

* Wed May 05 2010 Denis Kirienko <dk@altlinux.ru> 0.3-alt1
- SVN 641
- Added user manual
- Fixed spellchecking support

* Sat May 01 2010 Denis Kirienko <dk@altlinux.ru> 0.2.3-alt1
- First build for Sisyphus, based on Fedora specfile
