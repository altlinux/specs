# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define majver 6.0

Name: kicad
Version: 6.0.11
Release: alt1
Epoch: 1

Summary: An open source software for the creation of electronic schematic diagrams
Summary(ru_RU.UTF-8): Программа с открытым исходным кодом для проектирования электронных схем
License: AGPL-3-or-later
Group: Engineering

Url: https://gitlab.com/kicad/code/kicad.git
Source: %name-%version.tar
Patch: require-libngspice.so.0.patch
Patch2000: kicad-e2k.patch
Packager: Anton Midyukov <antohami@altlinux.org>

ExcludeArch: %arm

BuildRequires(pre): cmake rpm-macros-cmake
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-dev
BuildRequires: python3-module-wx
BuildRequires: boost-devel boost-asio-devel boost-asio-devel boost-context-devel boost-filesystem-devel boost-geometry-devel boost-interprocess-devel boost-locale-devel boost-program_options-devel
BuildRequires: ccmake gcc-c++
BuildRequires: libwxGTK3.2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libGLEW-devel libcairo-devel libssl-devel swig pkgconfig(gobject-2.0) libpcre-devel libpixman-devel pkgconfig(harfbuzz) pkgconfig(expat) pkgconfig(libdrm) pkgconfig(xdmcp) pkgconfig(xdamage) pkgconfig(xxf86vm) libcurl-devel
BuildRequires: doxygen
BuildRequires: dos2unix
BuildRequires: python-devel
BuildRequires: libglm-devel
BuildRequires: libuuid-devel
BuildRequires: ngspice-devel
BuildRequires: opencascade-devel
BuildRequires: openmpi-devel
BuildRequires: ImageMagick-tools
BuildRequires: desktop-file-utils

#Requires: kicad-packages3D >= %majver
Requires: kicad-symbols >= %majver
Requires: kicad-footprints >= %majver
Requires: kicad-templates >= %majver
Requires: %name-doc >= %epoch:%majver
Requires: %name-common >= %EVR
Requires: libngspice

%add_python3_path %_datadir/%name

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

Включает в себя редактор схем, средство трассировки печатных плат,
средства трёхмерного просмотра печатных плат в конечном виде.

Kicad состоит из 5 основных компонентов:

 * kicad — менеджер проектов
 * eeschema — редактор схем
 * pcbnew — редактор печатных плат
 * gerbview — просмотр GERBER
 * cvpcb — выбор мест для компонентов

На заметку:
Для использования рамки ГОСТ необходимо выбрать шаблон
gost_landscape.kicad_wks или gost_portrait.kicad_wks в диалоговом окне
"Настройки страницы" в поле "Файл описания разметки листа".
Стандартные файлы рамки (*.kicad_wks) находятся в %_datadir/kicad/template/.

%package common
Summary: Common package for kicad
Group: Engineering

BuildArch: noarch

Obsoletes: kicad-data <= %EVR
Obsoletes: kicad-i18n <= %EVR

%description common
Common package for kicad.

%prep
%setup
%ifarch %e2k
%patch2000 -p1
sed -i "s/-Wreturn-type/-Wbuggy-edg/" CMakeModules/Warnings.cmake
%endif
%patch -p1

%build
%ifarch %e2k
# LCC produces an insane amount of debug info (14Gb)
# -g1 is the same as default
%define optflags_debug -g0
%endif
%cmake \
    %_cmake_skip_rpath \
    -DKICAD_USE_OCC:=ON \
    -DKICAD_SCRIPTING=ON \
    -DKICAD_SCRIPTING_MODULES=ON \
    -DKICAD_SCRIPTING_PYTHON3=ON \
    -DPYTHON_SITE_PACKAGE_PATH=%python3_sitelibdir \
    -DKICAD_SCRIPTING_WXPYTHON=ON \
    -DKICAD_SCRIPTING_WXPYTHON_PHOENIX=ON \
    -DKICAD_SCRIPTING_ACTION_MENU=ON \
    -DKICAD_SPICE=ON \
    -DKICAD_USE_EGL=ON \
    -DKICAD_BUILD_I18N=ON \
    -DKICAD_I18N_UNIX_STRICT_PATH=ON \
    -DKICAD_VERSION_EXTRA=%release \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="-DNDEBUG" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo

%cmake_build

%install
%cmake_install

#fix line ending
dos2unix %buildroot%_desktopdir/*.desktop

#validate desktop files
desktop-file-validate %buildroot%_desktopdir/*.desktop
for i in %buildroot%_desktopdir/*.desktop; do
	desktop-file-install --dir %buildroot%_desktopdir \
		--add-category=Engineering \
		"$i"
done

# remove not supported locale
rm -r %buildroot/%_datadir/locale/pt_br

%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*.desktop
%_libdir/*.so*
%_libdir/%name/
%python3_sitelibdir/_pcbnew.so
%python3_sitelibdir/pcbnew.py
%python3_sitelibdir/__pycache__/pcbnew*
%doc %_docdir/%name
%_datadir/metainfo/*.metainfo.xml
%_iconsdir/hicolor/*/mimetypes/application-x-*.*
%_iconsdir/hicolor/*/apps/*.*
%_datadir/%name/
%_datadir/mime/packages/*

%files common
%dir %_datadir/kicad
%dir %_datadir/kicad/template

%changelog
* Mon Jan 30 2023 Anton Midyukov <antohami@altlinux.org> 1:6.0.11-alt1
- new version 6.0.11

* Sun Jan 15 2023 Anton Midyukov <antohami@altlinux.org> 1:6.0.10-alt1
- new version 6.0.10

* Sun Jan 15 2023 Anton Midyukov <antohami@altlinux.org> 1:6.0.7-alt2
- Build with wxGTK3.2
- Fix required soname by libngspice
- Requires libngspice (Closes: 44791)

* Sat Sep 10 2022 Anton Midyukov <antohami@altlinux.org> 1:6.0.7-alt1
- new version 6.0.7

* Wed Jun 22 2022 Anton Midyukov <antohami@altlinux.org> 1:6.0.6-alt1
- new version 6.0.6

* Sun May 08 2022 Anton Midyukov <antohami@altlinux.org> 1:6.0.5-alt1
- new version 6.0.5

* Wed Feb 23 2022 Anton Midyukov <antohami@altlinux.org> 1:6.0.2-alt1
- new version 6.0.2

* Sat Jan 08 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:6.0.0-alt2.1
- Fixed build for Elbrus.

* Thu Jan 06 2022 Anton Midyukov <antohami@altlinux.org> 1:6.0.0-alt2
- build with swig 4.0, without external pcbnew.py

* Tue Jan 04 2022 Anton Midyukov <antohami@altlinux.org> 1:6.0.0-alt1
- new version 6.0.0
- obsolete kicad-18n
- ExcludeArch %arm

* Tue Oct 12 2021 Anton Midyukov <antohami@altlinux.org> 1:5.1.9-alt4
- build on armh without python scripting
- remove data subpackage

* Wed Sep 01 2021 Michael Shigorin <mike@altlinux.org> 1:5.1.9-alt3
- E2K: add architecture support (patch by ilyakurdyukov@)
- minor spec cleanup

* Tue Jun 01 2021 Arseny Maslennikov <arseny@altlinux.org> 1:5.1.9-alt2.1
- NMU: fixed FTBFS: explicitly skip rpaths.

* Tue May 04 2021 Anton Midyukov <antohami@altlinux.org> 1:5.1.9-alt2
- Rebuild with opencascade

* Sat Feb 13 2021 Anton Midyukov <antohami@altlinux.org> 1:5.1.9-alt1
- new version 5.1.9

* Mon Oct 12 2020 Anton Midyukov <antohami@altlinux.org> 1:5.1.7-alt1
- new version 5.1.7

* Mon Apr 20 2020 Anton Midyukov <antohami@altlinux.org> 1:5.1.6-alt1.rc1
- new version 5.1.6-rc1
- enable wxpython scripts support
- build with wxGTK3.0
- fixed License tag

* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 1:5.1.4-alt1
- new version 5.1.4

* Mon May 20 2019 Anton Midyukov <antohami@altlinux.org> 1:5.1.2-alt2
- Not requires to kicad-packages3D (large package)

* Thu Apr 25 2019 Anton Midyukov <antohami@altlinux.org> 1:5.1.2-alt1
- new version 5.1.2

* Fri Mar 15 2019 Anton Midyukov <antohami@altlinux.org> 1:5.1.0-alt1
- new version 5.1.0
- disable srcipting support
- build with wxGTK3.1

* Thu Jan 03 2019 Anton Midyukov <antohami@altlinux.org> 1:5.0.2-alt1
- new version 5.0.2

* Fri Nov 23 2018 Anton Midyukov <antohami@altlinux.org> 1:5.0.1-alt1
- new version 5.0.1

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.0.0-alt1.1.qa1
- NMU: applied repocop patch

* Wed Sep 12 2018 Anton Midyukov <antohami@altlinux.org> 1:5.0.0-alt1.1
- Rebuilt with libssl-1.1

* Thu Jul 19 2018 Anton Midyukov <antohami@altlinux.org> 1:5.0.0-alt1
- New version 5.0.0
- Change group Engineering

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.0.7-alt2.1
- NMU: rebuilt with boost-1.67.0

* Thu Oct 26 2017 Anton Midyukov <antohami@altlinux.org> 1:4.0.7-alt2
- Skip requires pcbnew.

* Wed Aug 30 2017 Anton Midyukov <antohami@altlinux.org> 1:4.0.7-alt1
- New version 4.0.7
- exclude cvpcb.desktop

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
