Name: celestia
Version: 1.7.0
Release: alt1
Epoch: 1

Summary: A real-time visual space simulation

License: GPL-2.0
Group: Education
Url: https://celestiaproject.space/

# Code: git snapshot of master a221a47d (2025-10-06)
#   https://github.com/CelestiaProject/Celestia
# The astronomical data files are shipped by the separate celestia-data package
#   (built from https://github.com/CelestiaProject/CelestiaContent)
Vcs: https://github.com/CelestiaProject/Celestia.git
# Source-url: https://github.com/CelestiaProject/Celestia/commit/a221a47d
Source: %name-%version.tar

# https://github.com/CelestiaProject/Celestia/pull/2407
Patch1: celestia-eigen3-5.0.patch

# base runtime data (config, fonts, shaders) is in celestia-common
Requires: celestia-common = %EVR
# astronomical content (stars, textures, models) lives in celestia-data
Requires: celestia-data >= 1:%version
Conflicts: celestia-data >= 1:1.8.0
# compatibility with previous 1.6 layout
Provides: celestia-ui = %EVR
Provides: celestia-qt = %EVR
Obsoletes: celestia-qt < %EVR
Obsoletes: celestia-gtk < %EVR
Obsoletes: celestia-glut < %EVR

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: eigen3-devel libfmt-devel libepoxy-devel
BuildRequires: libpng-devel libjpeg-devel
BuildRequires: liblua5-devel
BuildRequires: libfreetype-devel
BuildRequires: gperf boost-devel
BuildRequires: libGL-devel
BuildRequires: gettext-tools

%description
Celestia is a free real-time space simulation that
lets you experience our universe in three dimensions.
Unlike most planetarium software, Celestia does not
confine you to the surface of the Earth. You can
travel throughout the solar system, to any of over
100,000 stars, or even beyond the galaxy.

This package contains the Qt6 frontend. The base runtime data
is in celestia-common, the astronomical content in celestia-data.

%package common
Summary: Base runtime data for Celestia (config, fonts, shaders)
Group: Education
BuildArch: noarch

%description common
Celestia is a free real-time space simulation.

This package contains the architecture-independent base runtime
data (configuration, fonts, shaders, demo scripts) needed by
Celestia. The astronomical content is in the celestia-data package.

%prep
%setup
%patch1 -p1

%build
%cmake \
    -DENABLE_QT5:BOOL=OFF \
    -DENABLE_QT6:BOOL=ON \
    -DENABLE_NLS:BOOL=ON \
    -DENABLE_MINIAUDIO:BOOL=ON \
    -DENABLE_TOOLS:BOOL=OFF \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

# provide plain "celestia" command (the Qt6 frontend)
ln -s celestia-qt6 %buildroot%_bindir/celestia

%find_lang %name

%files
%doc README.md AUTHORS TRANSLATORS
%_bindir/celestia
%_bindir/celestia-qt6
%_libdir/libcelestia.so.*
%_datadir/applications/*.desktop
%_datadir/metainfo/*.metainfo.xml
%_datadir/pixmaps/%name.png
%_man1dir/celestia-qt6.1*

%files common -f %name.lang
%_datadir/%name/

%changelog
* Tue Jun 30 2026 Vitaly Lipatov <lav@altlinux.ru> 1:1.7.0-alt1
- new version 1.7.0 (git snapshot a221a47, 2025-10-06)
- switch build system from autotools to cmake
- switch to Qt6 frontend (GTK and GLUT frontends dropped upstream)
- provide plain celestia command (symlink to celestia-qt6)
- split data out: base data to celestia-common, content to celestia-data
- apply upstream PR #2407 to build with Eigen3 5.0

* Thu May 22 2025 L.A. Kostis <lakostis@altlinux.ru> 1:1.6.4-alt1.1
- fix .desktop category (closes #42030).

* Thu May 22 2025 L.A. Kostis <lakostis@altlinux.ru> 1:1.6.4-alt1
- Update to 1.6.4.

* Thu May 22 2025 L.A. Kostis <lakostis@altlinux.ru> 1:1.6.2.2-alt4
- Fix build with autoconf-2.72 (tnx to glebfm@).
- Update URL and add Vcs link.

* Thu Sep 22 2022 L.A. Kostis <lakostis@altlinux.ru> 1:1.6.2.2-alt3
- Fix FTBFS (build w/ lua5.4).
- Remove obsoleted patches.

* Fri Jul 09 2021 Sergey V Turchin <zerg@altlinux.org> 1:1.6.2.2-alt2
- fix requires (closes: 40394)

* Thu Feb 25 2021 Sergey V Turchin <zerg@altlinux.org> 1:1.6.2.2-alt1
- new version

* Sat Feb 02 2019 Michael Shigorin <mike@altlinux.org> 1.6.9.git-alt2
- build with system libfmt

* Sat Dec 08 2018 Vitaly Lipatov <lav@altlinux.ru> 1.6.9.git-alt1
- new version (1.6.9.git) with rpmgs script
- cleanup spec, build gtk, glut, qt builds

* Wed Aug 29 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.6.1-alt6
- build without ancient libgnome-ui

* Fri Nov 17 2017 Oleg Solovyov <mcpain@altlinux.org> 1.6.1-alt5
- fix build

* Mon Jan 09 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6.1-alt4.qa1
- Fixed build with lua5.3.

* Thu Nov 05 2015 Michael Shigorin <mike@altlinux.org> 1.6.1-alt4
- Rebuilt against gcc5-built qt3.

* Fri Dec 26 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6.1-alt3
- Recovered celestia package for Sisyphus.
- Fixed build.

* Thu Mar 28 2013 Andrey Cherepanov <cas@altlinux.org> 1.6.1-alt2.4
- Fix build with new xorg version

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.3
- Fixed build with glibc 2.16

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.2
- Rebuilt with libpng15

* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.1
- Fixed build

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 1.6.1-alt2
- Build for TDE 3.5.13 release

* Wed Jun 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Fri Apr 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt6.1
- build fixd

* Mon Mar 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt6
- build fixed

* Fri Nov 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt5
- build fixed

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.6.0-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for celestia
  * postclean-05-filetriggers for spec file

* Tue Aug 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt4
- encoding bug fixed

* Wed Aug 12 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt3
- Theora support added
- two subpackages for gnome and kde interfaces

* Mon Aug 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt2
- russian in bookmarks fixed

* Mon Jul 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt1
- release 1.6.0

* Tue Jun 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.1-alt1.1
- rebuild with libpng.git=1.2.37-alt2

* Mon Jun 08 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.1-alt1
- release 1.5.1

* Fri Feb 22 2008 Eugine V. Kosenko <maverik@altlinux.ru> 1.5.0-alt2
- add i18n to new release

* Wed Feb 20 2008 Eugine V. Kosenko <maverik@altlinux.ru> 1.5.0-alt1
- release 1.5.0

* Fri Oct 19 2007 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt5
- fix requirement

* Thu Oct 18 2007 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt4
- added requirement to GConf2

* Mon Apr 09 2007 Eugine V. Kosenko <maverik@altlinux.ru> 1.4.1-alt3.i18n
- add trial i18n (fonts and fixes)

* Mon May 15 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt2
- fix compile woth gcc4.1 (patch from fedoraproject.org)

* Sat Mar 25 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Sun Mar 12 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.0-alt2
- fixed build with LDFLAGS="-Wl,--as-needed"
- removed .la->.so replacement
- fixed update from previous versions (thanks to shrek@)

* Sat Feb 18 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.0-alt1
- new version (1.4.0)
- rebuild with new xorg (#8813)
- menu-file replaced with celestia.desktop
- installation fix (/usr/share/apps/celestia -> /usr/share/celestia)

* Tue Jan 18 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.3.2-alt2
- this build make more gcc3.4 compatible

* Wed Sep 22 2004 Eugene V. Horohorin <genix@altlinux.org> 1.3.2-alt1
- new version

* Wed Jun 23 2004 Eugene V. Horohorin <genix@altlinux.ru> 1.3.1-alt2
- spec clean up

* Sat May 08 2004 Eugene V. Horohorin <genix@altlinux.ru> 1.3.1-alt1
- First build.

