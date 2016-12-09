Name: supertux2
Version: 0.5.1
Release: alt1

Summary: Classic 2D jump'n run sidescroller game in a Super Mario style
License: GPLv3
Group: Games/Arcade
Url: http://supertux.lethargik.org/

Packager: Anton Midyukov <antohami@altlinux.org>

Source: SuperTux-v%version-Source.tar.gz

Source1: supertux-16x16.png
Source2: supertux-32x32.png
Source3: supertux-48x48.png

Patch: supertux-alt-desktop-file.patch

Requires: %name-data = %version-%release

# Automatically added by buildreq on Mon Oct 01 2012 (-bi)
# WTF? vorbis-tools? really?
BuildPreReq: cmake rpm-macros-cmake
BuildRequires: boost-devel boost-filesystem-devel gcc-c++ libSDL2_image-devel libSM-devel libXau-devel libXdmcp-devel libXft-devel libcurl-devel libglew-devel libopenal-devel libphysfs-devel libvorbis-devel

%description
SuperTux is a jump'n run like game, with strong inspiration from the
Super Mario Bros games for Nintendo.

Run and jump through multiple worlds, fighting off enemies by jumping
on them or bumping them from below.  Grabbing power-ups and other stuff
on the way.

Note! This is a still development version.

%package data
Summary: Data files for supertux2
Group: Games/Arcade
BuildArch: noarch

%description data
SuperTux is a jump'n run like game, with strong inspiration from the
Super Mario Bros games for Nintendo.

Run and jump through multiple worlds, fighting off enemies by jumping
on them or bumping them from below. Grabbing power-ups and other stuff
on the way.

This is package contains data files for supertux2.

%prep
%setup -qn SuperTux-v%version-Source
%patch

%build
%cmake_insource \
        -DINSTALL_SUBDIR_BIN=bin \
        -DINSTALL_SUBDIR_SHARE=share/supertux2 \
        -DCMAKE_BUILD_TYPE="Release" \
        -DENABLE_BOOST_STATIC_LIBS=OFF
%make_build

%install
%makeinstall_std
%find_lang %name

install -m644 %SOURCE1 -D %buildroot/%_miconsdir/%name.png
install -m644 %SOURCE2 -D %buildroot/%_niconsdir/%name.png
install -m644 %SOURCE3 -D %buildroot/%_liconsdir/%name.png

# install game man file
install -D -m 644 man/man6/%name.6 %buildroot/%_man6dir/%name.6

rm -rf %buildroot/%_docdir/supertux2/

%files -f %name.lang
%_bindir/supertux2
%_desktopdir/supertux2.desktop
%doc docs/* LICENSE.txt NEWS.md README.md

%files data
%_datadir/supertux2
%_datadir/appdata/*
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png
%exclude %_pixmapsdir/supertux.*
%_man6dir/*
%exclude %_datadir/supertux2/sounds/normalize.sh

%changelog
* Sat Dec 10 2016 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt1
- 0.5.1 release

* Wed Oct 19 2016 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt2
- remove conflict with supertux

* Mon Sep 26 2016 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt1
- 0.5.0 release

* Thu Jul 07 2016 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- 0.4.0 release

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm at altlinux.org> 0.3.4-alt6.qa1
- Rebuilt for gcc5 C++11 ABI.

* Mon Jul 29 2013 Igor Zubkov <icesik@altlinux.org> 0.3.4-alt6
- 0.3.4 release

* Sun Jul 21 2013 Igor Zubkov <icesik@altlinux.org> 0.3.4-alt5
- git snapshot from f9e48410db28cb4bd1b91fa46414be660d3f5f8b

* Sat Jul 06 2013 Igor Zubkov <icesik@altlinux.org> 0.3.4-alt4
- git snapshot from cabf498f3931ad06fc696ddee840778240fbf130

* Sat Jun 22 2013 Igor Zubkov <icesik@altlinux.org> 0.3.4-alt3
- fix Summary
- git snapshot from 0fdd44fa8c98960abcd6a956c85ba362e45df39e

* Wed Jan 30 2013 Igor Zubkov <icesik@altlinux.org> 0.3.4-alt2
- git snapshot from 60478aa53db0d2874acc495037ff4f94b2efc3ae
- %%exclude %%_datadir/supertux2/sounds/normalize.sh

* Mon Oct 01 2012 Igor Zubkov <icesik@altlinux.org> 0.3.4-alt1
- git snapshot from c7cab5080d6aef977159766cbd8cbdc6b68b38eb
- relocate data from /usr/share/games/ to /usr/share/
- buildreq

* Sun Jul 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt3.1
- Fixed build

* Thu Apr 12 2012 Igor Zubkov <icesik@altlinux.org> 0.3.3-alt3
- Build with libcurl for addons manager

* Wed Apr 11 2012 Igor Zubkov <icesik@altlinux.org> 0.3.3-alt2
- Rebuilt for debuginfo
- buildreq

* Sat Nov 27 2010 Anton Chernyshov <ach@altlinux.org> 0.3.3-alt1
- upstream 0.3.3 release
- completely new list build deps because change upstream build process
- fix macros in spec

* Sun Oct 25 2009 Igor Vlasenko <viy@altlinux.ru> 0.3.1d-alt4.1
- a friendly repocop NMU: fixed _niconsdir.

* Tue Aug 04 2009 Igor Zubkov <icesik@altlinux.org> 0.3.1d-alt4
- fix FTBFS

* Wed Dec 03 2008 Igor Zubkov <icesik@altlinux.org> 0.3.1d-alt3
- fix requires

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 0.3.1d-alt2
- apply patch from repocop
- fix desktop file
- move data files to noarch subpackage
- buildreq

* Tue Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 0.3.1d-alt1.1
- rebuild

* Mon Mar 10 2008 Igor Zubkov <icesik@altlinux.org> 0.3.1d-alt1
- 0.3.0 -> 0.3.1d

* Sat Feb 17 2007 Igor Zubkov <icesik@altlinux.org> 0.3.0-alt1
- 0.1.3 -> 0.3.0 (closes #10563)
- warning: this is Tech Demo release
- buildreq
- rename supertux to supertux2
- add Conflict to supertux

* Fri May 19 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.1.3-alt2
- gcc4.1 compatible
- menu-file removed (using desktop-file instead)

* Sun Jul 24 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Tue Oct 26 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.1.2-alt2
- menu file group fix

* Thu Aug 26 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.1.2-alt1
- new version

* Tue Jul 06 2004 Anton Farygin <rider@altlinux.ru> 0.1.1-alt1
- new version
- menu permissions fixed (#4169)

* Sun May 16 2004 Albert R. Valiev <darkstar@altlinux.ru> 0.1.0-alt2
- Fixed menu file

* Wed May 05 2004 Albert R. Valiev <darkstar@altlinux.ru> 0.1.0-alt1
- Initial release
