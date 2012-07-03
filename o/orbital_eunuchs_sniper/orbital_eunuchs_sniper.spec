Name: orbital_eunuchs_sniper
Version: 1.30
Release: alt3.qa1
Url: http://www.icculus.org/oes/
Source0: %name-%version.tar.gz
Source11: %name-16x16.png
Source12: %name-32x32.png
Source13: %name-48x48.png
Patch: %name-gcc43.patch
License: BSD
Group: Games/Arcade
Summary: Defend VIPs killing bad guys with orbital laser
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sun Aug 03 2008
BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libSDL_mixer-devel libXt-devel

%description
Orbital Eunuchs Sniper is a simple game in which the player
must control an orbital laser to prevent harm from coming to
the VIPs (in blue squares) in the form of human threats
(in red squares). Avoid killing the neutral humans, however,
or else you may be 'retired'.

%prep
%setup -q
%patch -p1

%build
%configure	--bindir=%_gamesbindir \
		--datadir=%_datadir \
		--with-pic \
		--with-gnu-ld \
		--disable-debug
%make_build

%install
%makeinstall bindir=%buildroot%_gamesbindir datadir=%buildroot%_gamesdatadir

#(peroyvind) move ark-config to %_bindir as this belongs to the devel package
install -d %buildroot{%_bindir,%_gamesdatadir}

install -m 755 -d %buildroot%_datadir/applications/
cat > %buildroot%_datadir/applications/%name.desktop << EOF
[Desktop Entry]
Name=Orbital Eunuchs Sniper
Comment=%summary
Exec=%_gamesbindir/snipe2d
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

install -m644 %SOURCE11 -D %buildroot%_miconsdir/%name.png
install -m644 %SOURCE12 -D %buildroot%_niconsdir/%name.png
install -m644 %SOURCE13 -D %buildroot%_liconsdir/%name.png

#(peroyvind) clean out crap
rm -f %buildroot%_gamesdatadir/%name/snipe2d.*.static
mv %buildroot%_gamesdatadir/%name/snipe2d.*.dynamic %buildroot%_gamesbindir/snipe2d.bin

cat <<EOF > %buildroot%_gamesbindir/snipe2d
#! /bin/sh
cd %_gamesdatadir/orbital_eunuchs_sniper
snipe2d.bin "\$@"
EOF

%files
%doc AUTHORS ChangeLog NEWS README TODO COPYING
%_gamesdatadir/%name
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%_datadir/applications/%name.desktop
%defattr(755,root,root,755)
%_gamesbindir/*

%changelog
* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.30-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for orbital_eunuchs_sniper
  * postclean-05-filetriggers for spec file

* Tue Oct 28 2008 Fr. Br. George <george@altlinux.ru> 1.30-alt3
- GCC4.3 build fix

* Sun Sep 28 2008 Fr. Br. George <george@altlinux.ru> 1.30-alt2
- #16579 fixed

* Sun Aug 03 2008 Fr. Br. George <george@altlinux.ru> 1.30-alt1
- Version up

* Sun Aug 03 2008 Fr. Br. George <george@altlinux.ru> 1.28-alt1
Initial build from MDV


* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.28-8mdv2009.0mdv2009.0
+ Revision: 254913
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.28-6mdv2008.1mdv2008.1
+ Revision: 141036
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Sat Jan 06 2007 Pascal Terjan <pterjan@mandriva.org> 1.28-6mdv2007.0mdv2007.0
+ Revision: 104684
- add patch to handle non 32 bits pointers and re-enable x86_64

  + Götz Waschk <waschk@mandriva.org>
    - don't build on x86_64
    - Import orbital_eunuchs_sniper

* Fri Jan 05 2007 Götz Waschk <waschk@mandriva.org> 1.28-5mdv2007.1mdv2007.1
- xdg menu

* Fri Dec 23 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.28-5mdk
- %%rebuild
- %%mkrel

* Fri Aug 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.28-4mdk
- rebuild for new menu

* Wed Jun 09 2004 Götz Waschk <waschk@linux-mandrake.com> 1.28-3mdk
- rebuild for new g++

