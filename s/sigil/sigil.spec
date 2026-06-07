%define _unpackaged_files_terminate_build 1

Name: sigil
Version: 2.8.0
Release: alt1

%set_verify_elf_method unresolved=relaxed

Summary: Multi-platform ebook editor
Summary(ru_RU.UTF-8): Многоплатформенный редактор для электронных книг
License: GPL-3.0-or-later
Group: Editors
Url: https://sigil-ebook.com
VCS: https://github.com/Sigil-Ebook/Sigil.git

# skip dependencies which are actually provided (but files are located at non-standard location)
%add_python3_req_skip fr_utils functionrep sdifflibparser sigil_bs4 sigil_bs4.builder._lxml
%filter_from_requires /libsigilgumbo.so/d

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(minizip)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(libpcre2-16)
BuildRequires: python3-dev
BuildRequires: qt6-base-devel
BuildRequires: qt6-webengine-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(cups)

ExcludeArch: i586 riscv64

Requires: %name-data = %EVR
Requires: mathjax

%description
Sigil is a free, open source, multi-platform ebook editor.
It is designed to edit books in ePub format.

Features:

- Full UTF-16 support;
- Full EPUB 2 spec support;
- Multiple Views: Book View, Code View and Preview View;
- WYSIWYG editing in Book View;
- Complete control over directly editing EPUB syntax in Code View;
- Table of Contents generator with multi-level heading support;
- Metadata editor with full support for all possible metadata entries
  (more than 200) with full descriptions for each;
- User interface translated into many languages;
- Spell checking with default and user configurable dictionaries;
- Full Regular Expression (PCRE) support for Find & Replace;
- Supports import of EPUB and HTML files, images, and style sheets;
- Files can be validated for EPUB compliance with the FlightCrew
  validator;
- HTML Tidy: all imported files have their formatting corrected, and
  your editing can be optionally cleaned.

%description -l ru_RU.UTF-8
Sigil это свободный, открытый, многоплатформенный редактор для
электронных книг.
Он разработан для правки книг в формате ePub.

%package data
Summary: Data files for %name
License: GPL-3.0-or-later
Group: Editors
BuildArch: noarch

%description data
Sigil is a free, open source, multi-platform ebook editor.
It is designed to edit books in ePub format.

Features:

- Full UTF-16 support;
- Full EPUB 2 spec support;
- Multiple Views: Book View, Code View and Preview View;
- WYSIWYG editing in Book View;
- Complete control over directly editing EPUB syntax in Code View;
- Table of Contents generator with multi-level heading support;
- Metadata editor with full support for all possible metadata entries
  (more than 200) with full descriptions for each;
- User interface translated into many languages;
- Spell checking with default and user configurable dictionaries;
- Full Regular Expression (PCRE) support for Find & Replace;
- Supports import of EPUB and HTML files, images, and style sheets;
- Files can be validated for EPUB compliance with the FlightCrew
  validator;
- HTML Tidy: all imported files have their formatting corrected, and
  your editing can be optionally cleaned.

This package provides the architecture-independant files.

%prep
%setup

# specify additional categories
sed -i 's|^Categories=.*|Categories=Office;Publishing;|' src/Resource_Files/freedesktop/sigil.desktop src/Resource_Files/freedesktop/*.desktop

# set correct hunspell library name
sed -i 's|libhunspell.so|libhunspell.so.2|' src/Resource_Files/plugin_launchers/python/wrapper.py
# set paths to dictionaries
sed -i '2s|^|\nexport SIGIL_DICTIONARIES=/usr/share/myspell:/usr/share/hunspell\n|' src/Resource_Files/bash/sigil-sh_install

%build
%cmake \
       -D USE_SYSTEM_LIBS=1 \
       -D USE_QT6=1 \
       -D SYSTEM_LIBS_REQUIRED=1 \
       -D INSTALL_BUNDLED_DICTS=0 \
       -D INSTALL_HICOLOR_ICONS=1 \
       -D DISABLE_UPDATE_CHECK=1 \
       -D MATHJAX3_DIR=/usr/share/javascript/mathjax \
       -D SHARE_INSTALL_PREFIX=%_prefix \
       -D CMAKE_INSTALL_PREFIX=%_prefix \
       -D CMAKE_INSTALL_LIBDIR=%_libdir \
       -D CMAKE_SKIP_RPATH=ON
%cmake_build

%install
%cmake_install

# use only python3
find %buildroot -name '*.py' -exec sed -i -e 's|#!/usr/bin/env python3|#!/usr/bin/python3|g' {} \;
find %buildroot -name '*.py' -exec sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python3|g' {} \;

# install svg-icon for desktop-file
install -m644 -D src/Resource_Files/icon/app_icons_orig/app_icon_scalable.svg %buildroot%_iconsdir/hicolor/scalable/apps/%{name}.svg

# workaround for find-requires
ln -sfv %buildroot%_libdir/%name/libsigilgumbo.so %buildroot%_libdir/libsigilgumbo.so

%files
%doc ChangeLog.txt README.md COPYING.txt
%_bindir/%name
%dir %_libdir/%name
%_libdir/%name/*
%exclude %_libdir/libsigilgumbo.so

%files data
%doc docs/*.epub
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Sun Jun 07 2026 Nikolay Strelkov <snk@altlinux.org> 2.8.0-alt1
- new version 2.8.0 (with rpmrb script)

* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 2.7.6-alt1
- new version 2.7.6 (with rpmrb script)

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 2.7.5-alt1
- new version 2.7.5 (with rpmrb script)

* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 2.7.0-alt2
- Exclude riscv64 arch as not buildable.

* Thu Dec 04 2025 Nikolay Strelkov <snk@altlinux.org> 2.7.0-alt1
- New version 2.7.0.

* Sat Sep 13 2025 Nikolay Strelkov <snk@altlinux.org> 2.6.2-alt1
- New version 2.6.2.

* Wed Jul 23 2025 Nikolay Strelkov <snk@altlinux.org> 2.6.0-alt1
- New version 2.6.0.

* Sat Jun 28 2025 Nikolay Strelkov <snk@altlinux.org> 2.5.2-alt1
- New version 2.5.2.

* Fri Sep 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.8-alt1
- Updated to upstream version 0.9.8.

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.1-alt1.qa1
- NMU: rebuilt with rebuilt libFlightCrew.so.0.7.

* Mon Dec 03 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.1-alt1
- new version

* Thu Aug 18 2011 Malo Skryleve <malo@altlinux.org> 0.4-alt1
- Imported version sigil 0.4

* Sat Feb 19 2011 Malo Skryleve <malo@altlinux.org> 0.3.4-alt1
- initial build for ALT Linux Sisyphus


