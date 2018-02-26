Name: supertux2
Version: 0.3.3
Release: alt3

Summary: SuperTux is a classic 2D jump'n run sidescroller game in a Super Mario style

License: GPLv3
Group: Games/Arcade
URL: http://supertux.lethargik.org/

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: supertux-%version.tar.bz2

Source1: supertux-16x16.png
Source2: supertux-32x32.png
Source3: supertux-48x48.png

Patch0: supertux-alt-desktop-file.patch
Patch1: supertux-0.3.3-alt-curl.patch

Conflicts: supertux

Requires: %name-data = %version

# Automatically added by buildreq on Thu Apr 12 2012 (-bi)
# optimized out: cmake-modules elfutils libGL-devel libGLU-devel libSDL-devel libX11-devel libogg-devel libstdc++-devel python-base xorg-kbproto-devel xorg-xproto-devel
# WTF? subversion?
BuildRequires: boost-devel-headers cmake gcc-c++ libSDL_image-devel libXau-devel libXdmcp-devel libcurl-devel libglew-devel libopenal-devel libphysfs-devel libvorbis-devel

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
Requires: %name = %version
Conflicts: %name < %version
BuildArch: noarch

%description data
SuperTux is a jump'n run like game, with strong inspiration from the
Super Mario Bros games for Nintendo.

Run and jump through multiple worlds, fighting off enemies by jumping
on them or bumping them from below.  Grabbing power-ups and other stuff
on the way.

This is package contains data files for supertux2.

%prep
%setup -q -n supertux-%version
%patch0
%patch1 -p1

%build
cmake \
        -D CMAKE_INSTALL_PREFIX=%_prefix \
%if %_lib == lib64
        -D LIB_SUFFIX=64 \
%endif
        -D CMAKE_CXX_FLAGS:STRING="%optflags" \
        -D INSTALL_SUBDIR_BIN=bin \
        -D CMAKE_BUILD_TYPE="Release" \
        -D CMAKE_SKIP_RPATH=YES .

%make_build

%install
%makeinstall_std
%find_lang %name

install -m644 %SOURCE1 -D %buildroot/%_miconsdir/supertux.png
install -m644 %SOURCE2 -D %buildroot/%_niconsdir/supertux.png
install -m644 %SOURCE3 -D %buildroot/%_liconsdir/supertux.png

# install game man file
install -D -m 644 man/man6/%name.6 %buildroot/%_man6dir/%name.6

%files -f %name.lang
%doc README WHATSNEW.txt docs
%_bindir/supertux2
%_desktopdir/supertux2.desktop
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png
%_pixmapsdir/supertux.*
%_man6dir/*

%files data
%_gamesdatadir/supertux2/*

%changelog
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
