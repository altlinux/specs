Summary: An open source software for the creation of electronic schematic diagrams
Summary(ru_RU.UTF-8): Программа с открытым исходным кодом для проектирования электронных схем
Name: kicad
Version: 4.0.6
Release: alt1
Epoch: 1
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
# Source-url: https://github.com/KiCad/kicad-source-mirror/archive/%version.tar.gz
Patch: kicad-boost-1_61-boost-context-changes.patch
License: GPLv2+
Group: Sciences/Computer science
Url: https://code.launchpad.net/kicad
#Url: https://github.com/KiCad/kicad-source-mirror.git

BuildRequires(pre): cmake rpm-macros-cmake
# Automatically added by buildreq on Mon Sep 28 2015
# optimized out: at-spi2-atk boost-devel boost-devel-headers boost-polygon-devel cmake cmake-modules fontconfig libGL-devel libGLU-devel libX11-devel libat-spi2-core libcairo-gobject libcom_err-devel libgdk-pixbuf libkrb5-devel libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server pkg-config python-base python-devel python-modules swig-data xorg-xproto-devel xz
BuildRequires: boost-devel boost-asio-devel boost-asio-devel boost-context-devel boost-filesystem-devel boost-geometry-devel boost-interprocess-devel boost-locale-devel boost-program_options-devel ccmake doxygen gcc-c++ libGLEW-devel libcairo-devel libssl-devel swig libwxGTK3.1-gtk2-devel pkgconfig(gobject-2.0) libpcre-devel libpixman-devel pkgconfig(harfbuzz) pkgconfig(expat) pkgconfig(libdrm) pkgconfig(xdmcp) pkgconfig(xdamage) pkgconfig(xxf86vm) dos2unix libcurl-devel
BuildRequires: openmpi-devel 
BuildRequires: ImageMagick-tools
BuildRequires: desktop-file-utils
Requires: %name-data = %version
Requires: %name-library
Requires: %name-doc
Requires: %name-i18n
%add_python_req_skip kicad

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad is a set of four softwares and a project manager:

Kicad: Project manager.
Eeschema: Schematic entry.
Pcbnew: Board editor.
Cvpcb: Footprint selector for components used in the circuit design.
Gerbview: GERBER viewer (photoplotter documents).

%description -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

Для использования рамки ГОСТ необходимо выбрать шаблон
gost_landscape.kicad_wks или gost_portrait.kicad_wks в диалоговом окне
"Настройки страницы" в поле "Файл описания разметки листа".
Стандартные файлы рамки (*.kicad_wks) находятся в %_datadir/kicad/template/.

%package data
Summary: An open source software for the creation of electronic schematic diagrams
Summary(ru_RU.UTF-8): Программа с открытым исходным кодом для проектирования электронных схем
Group: Sciences/Computer science
BuildArch: noarch
Requires: icon-theme-hicolor
%add_python_req_skip kicad

%description data
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad is a set of four softwares and a project manager:

Kicad: Project manager.
Eeschema: Schematic entry.
Pcbnew: Board editor.
Cvpcb: Footprint selector for components used in the circuit design.
Gerbview: GERBER viewer (photoplotter documents).

Package contains data files.

%description data -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

Для использования рамки ГОСТ необходимо выбрать шаблон
gost_landscape.kicad_wks или gost_portrait.kicad_wks в диалоговом окне
"Настройки страницы" в поле "Файл описания разметки листа".
Стандартные файлы рамки (*.kicad_wks) находятся в %_datadir/kicad/template/.

Пакет содержит архитектурно-независимые файлы.

%prep
%setup -n %name-%version
%patch -p1

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DDEFAULT_INSTALL_PATH=/usr \
	-DBUILD_GITHUB_PLUGIN=ON \
	-DKICAD_SCRIPTING=ON \
	-DKICAD_SCRIPTING_MODULES=ON \
	-DKICAD_SCRIPTING_WXPYTHON=OFF \
	-DKICAD_SKIP_BOOST=ON

%make_build -C BUILD

%install
%makeinstall_std -C BUILD

#fix line ending
dos2unix %buildroot%_desktopdir/*.desktop
dos2unix %buildroot%_datadir/mimelnk/application/*.desktop

#validate desktop files
desktop-file-validate %buildroot%_desktopdir/*.desktop
#desktop-file-validate %buildroot%_datadir/mimelnk/application/*.desktop

%files
%_bindir/*
%_desktopdir/*.desktop
%_libexecdir/%name
%_datadir/mimelnk/application/*.desktop

%files data
%doc %_docdir/%name
%_datadir/mime/packages/kicad.xml
%_iconsdir/hicolor/*/mimetypes/application-x-*.*
%_iconsdir/hicolor/*/apps/*.*
%_datadir/%name/

%changelog
* Wed Feb 22 2017 Anton Midyukov <antohami@altlinux.org> 1:4.0.6-alt1
- New version 4.0.6

* Mon Jan 30 2017 Anton Midyukov <antohami@altlinux.org> 1:4.0.5-alt2
- Fix build with gcc6 and boost-1.61

* Sat Dec 10 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.5-alt1
- New version 4.0.5

* Wed Aug 31 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.4-alt1
- New version 4.0.4

* Thu Jul 21 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.2-alt2
- Enable build github plugin
- New packages kicad-data (fix arch-dep-package-has-big-usr-share)
- Fix line ending in desktop files
- Fix missing buildrequires.

* Sat Jun 04 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.2-alt1
- New version.

* Sat Feb 27 2016 barssc <barssc at altlinux.ru> r4029-alt2
- fix build for Sisyphus

* Sat Nov 29 2014 barssc <barssc at altlinux.ru> r4029-alt1
- new version

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110522-alt2.1
- Fixed build with gcc 4.7

* Tue Jun 07 2011 Denis Klimov <zver at altlinux.org> 20110522-alt2
- fix inherit

* Mon Jun 06 2011 Denis Klimov <zver at altlinux.org> 20110522-alt1
- new version

* Tue May 24 2011 Repocop Q. A. Robot <repocop at altlinux.org> 20110421-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for kicad

* Fri Apr 22 2011 Denis Klimov <zver at altlinux.org> 20110421-alt1
- new version

* Tue Apr 12 2011 Denis Klimov <zver at altlinux.org> 20110409-alt2
- fix install netlist_form_pads-pcb.xsl for x86_64

* Mon Apr 11 2011 Denis Klimov <zver at altlinux.org> 20110409-alt1
- new version

* Fri Apr 08 2011 Denis Klimov <zver at altlinux.org> 20110401-alt1
- new version

* Mon Mar 28 2011 Denis Klimov <zver at altlinux.org> 20110325-alt1
- new version
- remove patches
- cleanup spec

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop at altlinux.org> 20080825-alt0.2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for kicad
  * postclean-05-filetriggers for spec file

* Fri Feb 13 2009 Alexey Shentzev <ashen at altlinux.ru> 20080825-alt0.2
- fix desktop files

* Fri Feb 13 2009 Alexey Shentzev <ashen at altlinux.ru> 20080825-alt0.1
- first build for ALT Linux
