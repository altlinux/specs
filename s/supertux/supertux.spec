Name: supertux
Summary: SuperMario like game
Version: 0.1.3
Release: alt3
License: GPL
Group: Games/Arcade
Url: http://super-tux.sf.net/

Source: %name-%version.tar.bz2
Source11: %name-16x16.png
Source12: %name-32x32.png
Source13: %name-48x48.png
Patch: %name-%version-gcc4.patch
Patch1: %name-%version-desktop.patch

# Automatically added by buildreq on Fri May 19 2006
BuildRequires: esound gcc-c++ imake libSDL-devel libSDL_image-devel libSDL_mixer-devel libXt-devel libGL-devel xorg-cf-files zlib-devel

%description
SuperTux is a jump'n run like game, with strong inspiration from the
Super Mario Bros games for Nintendo.

Run and jump through multiple worlds, fighting off enemies by jumping
on them or bumping them from below.  Grabbing power-ups and other stuff
on the way.

%prep
%setup
%patch0 -p0
%patch1 -p0

%build
%configure --disable-debug
%make_build

%install
%make_build install DESTDIR=%buildroot

install -m644 %SOURCE11 -D %buildroot%_miconsdir/%name.png
install -m644 %SOURCE12 -D %buildroot%_niconsdir/%name.png
install -m644 %SOURCE13 -D %buildroot%_liconsdir/%name.png

%files
%_bindir/%name
%_datadir/%name
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Sun Apr 10 2011 Lenar Shakirov <snejok@altlinux.ru> 0.1.3-alt3
- Fixed build: BuildReqs: libmesa-devel -> libGL-devel
- Spec cleaned: thanks to rpmcs script!
- Desktop file cleaned and fixed: thanks to repocop!

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.3-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for supertux
  * pixmap-in-deprecated-location for supertux
  * postclean-05-filetriggers for spec file

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
