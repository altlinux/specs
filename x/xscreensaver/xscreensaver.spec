# vim: set ft=spec: -*- spec -*-
# gnome3 in sisyphus
%def_without gnome2

%define _libexecdir /usr/libexec

# xscreensaver RPM macros
%define xss_hack_dir	%_libexecdir/%name
%define xss_conf_dir	%_datadir/%name/config
%define xss_ad_dir	%_sysconfdir/X11/%name/hack.d
#

Name: xscreensaver
Version: 5.14
Release: alt3
Summary: A screen saver and locker for the X window system
License: BSD
Group: Graphical desktop/Other
Url: http://www.jwz.org/%name

# gear repos: http://packages.altlinux.org/en/Sisyphus/srpms/xscreensaver/gear
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Source1: %name-%version-ad.tar

Source2: %name.pamd
Source3: %name-update.sh

Source4: xscreensaver-hacks
Source5: xscreensaver-hacks-gl

Source6: ru.po

Requires: xli urlview appres
Requires: %name-hack
Provides: %name-contrib = %version-%release
Obsoletes: %name-contrib

Provides: screen-saver-engine

%if_with gnome2
# NB: gnome-screensaver-3.0.0 doesn't contain migration script
BuildPrereq: gnome-screensaver-utils
%endif
# Automatically added by buildreq on Mon Apr 18 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libGL-devel libICE-devel libSM-devel libX11-devel libXext-devel libXrender-devel libXt-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgdk-pixbuf-xlib libgio-devel libgtk+2-devel libpango-devel perl-XML-Parser pkg-config xorg-inputproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel
BuildRequires: bc imake intltool libGLU-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXxf86misc-devel libXxf86vm-devel libglade-devel libgle-devel libjpeg-devel libpam-devel libxml2-devel xorg-cf-files gdk-pixbuf-devel

%description
A modular screen saver and locker for the X Window System.
Highly customizable: allows the use of any program that
can draw on the root window as a display mode.

%package -n rpm-build-%name
Summary: A screen saver and locker for the X window system - RPM macros
Group: Development/Other
Conflicts: %name > %version-%release
Conflicts: %name < %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel <= 5.05-alt1

%description -n rpm-build-%name
A modular screen saver and locker for the X Window System.
Highly customizable: allows the use of any program that
can draw on the root window as a display mode.

This package contains RPM macros needed to build packages
for additional xscreensaver hacks.

%package hacks
Summary: A screen saver and locker for the X window system - standard hacks
Group: Graphical desktop/Other
Requires: %name = %version-%release
Requires: %name-modules = %version-%release
Provides: %name-hack = %version-%release
# By webcollage...
Requires: netpbm libjpeg-utils
# By noseguy and phosphor
Requires: fortune-mod

%description hacks
A modular screen saver and locker for the X Window System.
Highly customizable: allows the use of any program that
can draw on the root window as a display mode.

This package contains standard xscreensaver hacks.

%package hacks-gl
Summary: A screen saver and locker for the X window system - GL hacks
Group: Graphical desktop/Other
Requires: %name = %version-%release
Requires: %name-modules-gl = %version-%release
Provides: %name-hack = %version-%release
Provides: %name-gl = %version-%release
Obsoletes: %name-gl

%description hacks-gl
A modular screen saver and locker for the X Window System.
Highly customizable: allows the use of any program that
can draw on the root window as a display mode.

This package contains OpenGL xscreensaver hacks.

%if_with gnome2
%package -n gnome-screensaver-modules-xscreensaver
Summary: A screen saver and locker for the X window system - GNOME Screensaver modules
Group: Graphical desktop/Other
Requires: %name-modules = %version-%release
Requires: gnome-screensaver
Provides: gnome-screensaver-module

%description -n gnome-screensaver-modules-xscreensaver
A modular screen saver and locker for the X Window System.
Highly customizable: allows the use of any program that
can draw on the root window as a display mode.

This package contains modules for GNOME Screensaver.

%package -n gnome-screensaver-modules-xscreensaver-gl
Summary: A screen saver and locker for the X window system - GNOME Screensaver modules
Group: Graphical desktop/Other
Requires: %name-modules-gl = %version-%release
Requires: gnome-screensaver
Provides: gnome-screensaver-module

%description -n gnome-screensaver-modules-xscreensaver-gl
A modular screen saver and locker for the X Window System.
Highly customizable: allows the use of any program that
can draw on the root window as a display mode.

This package contains OpenGL modules for GNOME Screensaver.
%endif

%package modules
Summary: A screen saver and locker for the X window system - standard modules
Group: Graphical desktop/Other
Conflicts: %name < %version-%release
Conflicts: %name > %version-%release
# By webcollage...
Requires: netpbm libjpeg-utils
# By noseguy and phosphor
Requires: fortune-mod

%description modules
A modular screen saver and locker for the X Window System.
Highly customizable: allows the use of any program that
can draw on the root window as a display mode.

This package contains standard standalone modules.

%package modules-gl
Summary: A screen saver and locker for the X window system - GL modules
Group: Graphical desktop/Other
Conflicts: %name < %version-%release
Conflicts: %name > %version-%release
# By starwars
Requires: fortune-mod

%description modules-gl
A modular screen saver and locker for the X Window System.
Highly customizable: allows the use of any program that
can draw on the root window as a display mode.

This package contains OpenGL standalone modules.

%package frontend
Summary: A screen saver and locker for the X window system - configuration frontend
Group: Graphical desktop/Other
Requires: %name = %version-%release
Provides: %name-gnome = %version-%release
Provides: screen-saver-frontend
Obsoletes: %name-gnome

%description frontend
A modular screen saver and locker for the X Window System.
Highly customizable: allows the use of any program that
can draw on the root window as a display mode.

This package contains xscreensaver configuration frontend.

%prep
%setup
%patch -p1
cp %SOURCE6 po/ru.po

%build
%autoreconf
%configure \
  --without-motif \
  --with-pam \
  --without-shadow \
  --with-gl \
  --with-pixbuf \
  --with-proc-interrupts
# Hack to install locale files
subst 's,@install_sh@,install,' po/Makefile

%make_build all

%install
mkdir -p %buildroot{%_bindir,%_sysconfdir/{X11/{app-defaults,%name},pam.d},%_datadir/pixmaps,%_rpmlibdir,%_rpmmacrosdir}
%makeinstall_std install_prefix=%buildroot \
  KDEDIR=%_prefix \
  GNOME_BINDIR=%_bindir \
  AD_DIR=%_sysconfdir/X11/app-defaults

install -m640 %_sourcedir/%name.pamd %buildroot%_sysconfdir/pam.d/%name
install -m755 %_sourcedir/%name-update.sh %buildroot%_bindir/update-%name

cat <<EOF >%buildroot%_rpmmacrosdir/%name
%%xss_hack_dir	%xss_hack_dir	
%%xss_conf_dir	%xss_conf_dir	
%%xss_ad_dir	%xss_ad_dir	

# post-install commands (obsoleted by filetrigger)
%%update_xscreensaver	%%{warning %%%%update_xscreensaver is obsolete}
%%clean_xscreensaver	%%{warning %%%%clean_xscreensaver is obsolete}
EOF

cat <<EOF >%buildroot%_rpmlibdir/%name.filetrigger
#!/bin/sh -e

grep -qs '^%xss_ad_dir/' && update-%name ||:
EOF
chmod 755 %buildroot%_rpmlibdir/%name.filetrigger

tar xf %_sourcedir/%name-%version-ad.tar -C %buildroot%_sysconfdir/X11/%name

%find_lang %name

MkModuleFilelists() {
  list="$1" && shift
  name="$1" && shift

  :> "%name-hacks-$name"
  :> "%name-modules-$name"
  :> "%name-gnome-$name"

  while read module; do
    [ "$module" = "providence" ] && continue
    echo "%%config %xss_ad_dir/$module.xss" >> "%name-hacks-$name"
    echo "%xss_conf_dir/$module.xml" >> "%name-hacks-$name"
    echo "%xss_hack_dir/$module" >> "%name-modules-$name"
    [ -f "%buildroot%_man6dir/$module.6" ] && echo "%_man6dir/$module.6*" >> "%name-modules-$name" ||:
%if_with gnome2
    pushd %buildroot%_datadir/applications/screensavers
    %_libexecdir/gnome-screensaver/gnome-screensaver-migrate-xscreensaver-config.sh %buildroot%xss_conf_dir/$module.xml
    popd
    echo "%_datadir/applications/screensavers/xscreensaver-$module.desktop" >> "%name-gnome-$name"
%endif
  done < "$list"
}

mkdir -p %buildroot%_datadir/applications/screensavers
MkModuleFilelists %_sourcedir/xscreensaver-hacks std
MkModuleFilelists %_sourcedir/xscreensaver-hacks-gl gl

%files
%doc README README.hacking
%verify(not md5 size mtime) %ghost %config(missingok) %_sysconfdir/X11/app-defaults/XScreenSaver
%dir %_sysconfdir/X11/%name
%dir %xss_ad_dir
%config %_sysconfdir/X11/%name/%name.top
%config %_sysconfdir/X11/%name/%name.bottom
%attr(640,root,chkpwd) %config(noreplace) %_sysconfdir/pam.d/*
%attr(2711,root,chkpwd) %_bindir/%name
%_bindir/%name-command
%_bindir/%name-getimage
%_bindir/%name-getimage-file
%_bindir/%name-getimage-video
%_bindir/%name-text
%_bindir/update-%name
%_man1dir/%name.1*
%_man1dir/%name-command.1*
%_man1dir/%name-getimage.1*
%_man1dir/%name-getimage-file.1*
%_man1dir/%name-getimage-video.1*
%_man1dir/%name-text.1*

%dir %_datadir/%name
%_datadir/%name/glade
%dir %xss_conf_dir
%doc %xss_conf_dir/README
%dir %xss_hack_dir

%xss_hack_dir/ljlatest
%_man6dir/ljlatest.6*

%_rpmlibdir/%name.filetrigger

%files frontend -f %name.lang
%_bindir/%name-demo
%_man1dir/%name-demo.1*
%_desktopdir/xscreensaver-properties.desktop
%_datadir/pixmaps/%name.xpm

%files -n rpm-build-%name
%_rpmmacrosdir/%name

%files hacks -f xscreensaver-hacks-std

%files hacks-gl -f xscreensaver-hacks-gl
%_bindir/xscreensaver-gl-helper
%_man6dir/xscreensaver-gl-helper.6*

%files modules -f xscreensaver-modules-std
%dir %xss_hack_dir

%files modules-gl -f xscreensaver-modules-gl
%dir %xss_hack_dir

%if_with gnome2
%files -n gnome-screensaver-modules-xscreensaver -f xscreensaver-gnome-std

%files -n gnome-screensaver-modules-xscreensaver-gl -f xscreensaver-gnome-gl
%endif

%changelog
* Fri Feb 03 2012 Andrey Cherepanov <cas@altlinux.org> 5.14-alt3
- Fix xscreensaver-demo Russian localization (closes: #26110)

* Wed Jul 06 2011 Michael Shigorin <mike@altlinux.org> 5.14-alt2
- drop providence module (masonry sucks)

* Sat Jun 11 2011 Michael Shigorin <mike@altlinux.org> 5.14-alt1
- [5.14]
  + Stability fixes (incl. crash in Blank Only Mode when DPMS disabled)
  + Passwords that contain UTF-8 non-Latin1 chars are now typeable
- Reused source import and resource tweaks by raorn@
- Left conditional gnome2 support in for the time being

* Sat Jun 11 2011 Michael Shigorin <mike@altlinux.org> 5.12-alt3
- Fix build: conditional gnome2 related part (gnome-screensaver
  from gnome3 doesn't contain the script in question), off by default

* Mon Apr 18 2011 Mikhail Efremov <sem@altlinux.org> 5.12-alt2
- Fix build: updated BR.

* Fri Oct 01 2010 Alexey I. Froloff <raorn@altlinux.org> 5.12-alt1
- [5.12]

* Sat Mar 13 2010 Alexey I. Froloff <raorn@altlinux.org> 5.10-alt1
- [5.10]
- Added deps on appres (due to xscreensaver-text, closes: #23022)
- New hacks:
  + rubikblocks (GL)
  + surfaces (GL)
- Removed hacks:
  + hyperball
  + hypercube
  + juggle

* Mon Apr 13 2009 Alexey I. Froloff <raorn@altlinux.org> 5.08-alt2
- Fix filetrigger interpreter

* Tue Jan 06 2009 Sir Raorn <raorn@altlinux.ru> 5.08-alt1.1
- Fix filetrigger permittions

* Mon Dec 29 2008 Sir Raorn <raorn@altlinux.ru> 5.08-alt1
- [5.08]
- New hacks:
  + photopile (GL)
- Hacks rewritten as GL:
  + sonar
  + jigsaw
- Removed hacks:
  + bubbles
  + critical
  + flag
  + forest
  + glforestfire (GL)
  + lmorph
  + laser
  + lightning
  + lisa
  + lissie
  + rotor
  + sphere
  + spiral
  + t3d
  + vines
  + whirlygig
  + worm
- Removed obsolete update_menus calls
- Packaged filetrigger for updating screensaver AD
- %%update_xscreensaver/%%clean_xscreensaver macros made obsolete

* Tue Aug 12 2008 Sir Raorn <raorn@altlinux.ru> 5.07-alt1
- [5.07]
- New hacks:
  + skytentacles (GL)
- Added generic screen-saver-engine/frontend provides
- gnome-screensaver compatibility
- xscreensaver-devel renamed to rpm-build-xscreensaver

* Tue Apr 15 2008 Sir Raorn <raorn@altlinux.ru> 5.05-alt2
- Suggest xscreensaver-frontend installation if
  xscreensaver-demo missing (closes: #15278)

* Sat Mar 08 2008 Sir Raorn <raorn@altlinux.ru> 5.05-alt1
- [5.05]
- New hacks:
  + cubicgrid (GL)
  + hypnowheel (GL)
  + lcdscrub

* Wed Nov 14 2007 Sir Raorn <raorn@altlinux.ru> 5.04-alt1
- [5.04]
- New hacks:
  + abstractile
  + lockward (GL)
  + moebiusgears (GL)

* Sun Oct 28 2007 Sir Raorn <raorn@altlinux.ru> 5.03-alt1
- [5.03]
- New hacks:
  + cwaves
  + glcells (GL)
  + m6502
  + voronoi (GL)

* Wed Oct 17 2007 Sir Raorn <raorn@altlinux.ru> 5.02-alt1
- [5.02]
- Don't use pam_userpass, this allows use of non-password
  auth modules (like fingerprint check)

* Sun Sep 24 2006 Sir Raorn <raorn@altlinux.ru> 5.01-alt1
- [5.01]
- All patches merged in git repository

* Wed May 24 2006 Sir Raorn <raorn@altlinux.ru> 5.00-alt1
- [5.00]
- Removed patches:
  + cyrilm-alt-maze_walk.patch (unsupported)
- New hacks:
  + glschool (GL)
  + topblock (GL)
- Removed hacks:
  + xteevee (superceded by xanalogtv)

* Sun Feb 12 2006 Sir Raorn <raorn@altlinux.ru> 4.24-alt1
- [4.24]

* Sat Jan 28 2006 Sir Raorn <raorn@altlinux.ru> 4.23-alt2
- Rebuilt with new Xorg, buildreqs updated
- Do not generate menu file
- Removed compatibility symlinks to %%_x11bindir

* Sat Oct 22 2005 Sir Raorn <raorn@altlinux.ru> 4.23-alt1
- [4.23]
- Removed patches:
  + alt-double-free (merged upstream)
- %%_x11bindir links made relative
- New hacks:
  + celtic
  + cube21 (GL)
  + glhanoi (GL)
  + juggler3d (GL)
  + timetunnel (GL)
- Removed hacks:
  + ant

* Fri Aug 12 2005 Sir Raorn <raorn@altlinux.ru> 4.22-alt2
- Eliminated double-free in xscreensaver-demo
- Added compatibility symlinks to xscreensaver, xscreensaver-command
  and xscreensaver-demo (closes: #7617)
- Reviewed %%update_xscreensaver and %%clean_xscreensaver macros to
  run only after uninstall of old package

* Tue Aug 02 2005 Sir Raorn <raorn@altlinux.ru> 4.22-alt1
- [4.22]
- Updated patches:
  + alt-mdk-oneshot
  + alt-perl-disable-diagnostics
- New filesystem layout:
  + /usr/X11R6/bin -> /usr/bin
  + /usr/X11R6/lib/xscreensaver -> /usr/libexec/xscreensaver
  + /usr/X11R6/lib/xscreensaver/config -> /usr/share/xscreensaver/config
- gnome subpackage removed (ancient GNOME versions support dropped in upstream)
- contrib subpackage removed (xml files for foreign hacks was dropped
  in upstream, *.xss files comes into main package)
- New hacks:
  + antmaze (GL)
  + crackberg (GL)
  + fliptext (GL)
  + interaggregate
  + tangram (GL)

* Sun Feb 27 2005 Sir Raorn <raorn@altlinux.ru> 4.20-alt1
- [4.20]
- Removed obsolete GNOME stuff
- Removed KDE support (it doesn't work with KDE3 anyway)
- Use freedesktop2menu.pl for menu generation
- New hacks:
  boing (GL)
  boxfit
  carousel (GL)
  fiberlamp

* Thu Dec 16 2004 Sir Raorn <raorn@altlinux.ru> 4.19-alt1
- [4.19]
- Disabled buggy MIT-SCREEN-SAVER extension
- New hacks:
  fireworkx
  intermomentary
  pinion (GL)
  substrate

* Mon Oct 04 2004 Sir Raorn <raorn@altlinux.ru> 4.18-alt2
- Fixed typo in providence.xss (closes: #5280)

* Mon Aug 16 2004 Sir Raorn <raorn@altlinux.ru> 4.18-alt1
- [4.18]
- New hacks:
  anemotaxis
  memscroller

* Thu May 13 2004 Sir Raorn <raorn@altlinux.ru> 4.16-alt1
- [4.16]
- Fix deps in -kde (kdebase -> kdebase-common)
- Spec cleanup
- New hacks:
  antinspect (GL)
  fuzzyflakes
  polyhedra (GL)
  providence (GL)

* Tue Mar 02 2004 Sir Raorn <raorn@altlinux.ru> 4.15-alt1
- [4.15]
- New hacks:
  mismunch
  noof (GL)
  pacman
  wormhole

* Sun Nov 09 2003 Sir Raorn <raorn@altlinux.ru> 4.14-alt2
- Fixed insecure tempfile handling

* Tue Oct 28 2003 Sir Raorn <raorn@altlinux.ru> 4.14-alt1
- [4.14]
- New hacks:
  apple2
  blinkbox (GL)
  fontglide
  gleidescope (GL)
  mirrorblob (GL)
  pong
  xanalogtv

* Mon Sep 22 2003 Sir Raorn <raorn@altlinux.ru> 4.13-alt1
- [4.13]
- ljlatest helper (fortune(6) replacement - see man ljlatest)

* Sat Sep 06 2003 Sir Raorn <raorn@altlinux.ru> 4.12-alt1
- [4.12]
- New hacks:
  antspotlight (GL)
  fireflies (contrib)
  flipflop (GL)
  polytopes (GL)

* Wed Jul 02 2003 Sir Raorn <raorn@altlinux.ru> 4.11-alt1
- [4.11]
- Updated patches:
  alt-pam_userpass
  alt-encoding
  alt-glplanet-args
  alt-perl-disable-diagnostics
- New hacks:
  blocktube (GL)
  cloudlife
  cubestorm (GL)
  glknots (GL)
  glmatrix (GL)
  hypertorus (GL)
  klein (GL)

* Sat May 17 2003 Sir Raorn <raorn@altlinux.ru> 4.09-alt3
- Dropped pixbuf support (this removes daemon's dependency to
  libgtk+2)
- netpbm and libjpeg-utils are *required* by webcollage (-hacks)
- fortune-mod is really required by noseguy, phosphor and
  starwars (-hacks and -hacks-gl)

* Sat May 10 2003 Sir Raorn <raorn@altlinux.ru> 4.09-alt2
- xscreensaver-demo moved to -frontend subpackage
- Added xscreensaver-demo menu entry

* Mon Apr 14 2003 Sir Raorn <raorn@altlinux.ru> 4.09-alt1
- [4.09]
- Updated BuildRequires
- Split to xscreensaver, xscreensaver-hacks and xscreensaver-hacks-gl
- Replace chbg with xli in Requires
- Ignore missing hacks by default (suggested by rider)
- Use MIT-SCREEN-SAVER by default if available
- Set .loadURL program to url_handler.sh from urlview package
- Set .manualCommand to xvt ... -e sh -c man (get rid of fscking yelp)
- Fix glplanet's config and manpage (closes #0002399)
- Do not 'use diagnostics' in perl scripts since it (indirectly)
  requires perl-pod (reported by dfo)
- Split XScreenSaver AD to pieces 
  update-xscreensaver script
- RPM macros (in -devel)
- New hacks:
  bouncingcow (GL)
  extrusion (GLE)
  flyingtoasters (GL)
  glslideshow (GL)
  jigglypuff (GL)

* Mon Mar 10 2003 Sir Raorn <raorn@altlinux.ru> 4.08-alt1
- [4.08]
- mesa_version patch is no longer needed
- New hacks:
  atunnel (GL)
  barcode
  eruprion
  flurry (GL)
  metaballs
  piecewise
  popsquares
- Fix icon in -gnome
- XScreenSaver AD is no longer "noreplace"

* Tue Nov 19 2002 Sir Raorn <raorn@altlinux.ru> 4.06-alt2
- Added -contrib package
- Fixed filelist (all work and no sleep makes raorn a dull boy)
- Patch by Cyril "Sir Kot" Margorin <cyrilm@immo.ru>:
  Walk through Maze after solving it

* Sun Nov 17 2002 Sir Raorn <raorn@altlinux.ru> 4.06-alt1
- [4.06]
- Specfile rewritten from scratch
- Patches from 4.00-alt3:
  oneshot
  pam_userpass
  progname
- KDE and GNOME control panel applets
