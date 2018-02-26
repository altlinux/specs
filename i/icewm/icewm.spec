# -*- mode: rpm-spec; coding: utf-8 -*-
%def_with menu

Name: icewm
Version: 1.3.7
Release: alt7
Epoch: 2

Summary: X11 Window Manager
Group: Graphical desktop/Icewm
License: LGPLv2
Url: http://www.icewm.org/
Packager: Dmitriy Khanzhin <jinn@altlinux.ru>

Source: %name-%version.tar
Source1: %name.menu
Source2: %name.menu-method
Source3: %name-16.png
Source4: %name-32.png
Source5: %name-48.png
Source6: start%name
Source7: IceWM.xpm
Source8: %name.wmsession
Source9: %name.alternatives
Source11: README.ALT
Source12: %name.desktop
Source13: restart

Patch0: %name-multibyte.patch
Patch1: %name-alt-altconf.patch
Patch2: %name-alt-fonts.patch
Patch3: %name-alt-icons.patch
Patch4: %name-alt-findicon.patch
Patch5: %name-deb-alt-i18n_update.patch
Patch6: %name-alt-cpustatus.patch
Patch7: %name-deb-tray_hotfixes.patch
Patch8: %name-alt-taskbar.patch
Patch9: %name-alt-ubuntu-fix-deprecated.patch

PreReq: %name-light = %epoch:%version-%release

# Automatically added by buildreq on Sun May 20 2012
BuildRequires: gcc-c++ imake libSM-devel libXext-devel libXft-devel libXinerama-devel libXrandr-devel libgdk-pixbuf-devel mkfontdir xorg-cf-files

%if_without menu
BuildPreReq: desktop-file-utils
%endif

%description
Window Manager for X Window System. Can emulate the look of Windows'95, OS/2
Warp 3,4, Motif or the Java Metal GUI. Tries to take the best features of the
above systems. Features multiple workspaces, opaque move/resize, task bar,
window list, mailbox status, digital clock. Fast and small.

Recommends: iftop, mutt

%package light
Summary: A light version of Icewm
Group: Graphical desktop/Icewm
Requires: design-%name >= 1.0-alt6

%description light
Window Manager for X Window System. Can emulate the look of Windows'95, OS/2
Warp 3,4, Motif or the Java Metal GUI. Tries to take the best features of the
above systems. Features multiple workspaces, opaque move/resize, task bar,
window list, mailbox status, digital clock. Fast and small.

Recommends: iftop, mutt

%prep
%setup

%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2
%patch6 -p2
%patch7 -p2
%patch8 -p2
%patch9 -p2

%add_optflags %optflags_nocpp

%build

./autogen.sh
%configure \
	--sysconfdir=%_sysconfdir/X11 \
	--with-cfgdir=%_sysconfdir/X11/%name \
	--with-libdir=%_x11x11dir/%name \
	--enable-nls \
	--enable-i18n \
	--disable-shaped-decorations \
	--disable-gradients \
	--disable-taskbar \
	--enable-lite
%make_build
cp src/%name src/%name-light

make distclean

%configure \
	--sysconfdir=%_sysconfdir/X11 \
	--with-cfgdir=%_sysconfdir/X11/%name \
	--with-libdir=%_x11x11dir/%name \
	--enable-nls \
	--enable-i18n \
	--enable-antialiasing \
	--enable-shaped-decorations \
	--enable-gradients \
	--enable-guievents

touch src/Makefile
%make_build
cp -p src/%name src/%name-full

%install
%make_install \
	BINDIR=%buildroot%_bindir \
	LIBDIR=%buildroot%_x11x11dir/%name \
	ETCDIR=%buildroot%_sysconfdir/X11/%name \
	DOCDIR=%buildroot%_docdir \
	LOCDIR=%buildroot%_datadir/locale \
	install

rm -f %buildroot%_bindir/%name
install src/%name-light %buildroot%_bindir/
install src/%name-full %buildroot%_bindir/

%if_with menu
mkdir -p %buildroot%_menudir
install -m 644 %SOURCE1 %buildroot%_menudir/%name
%endif
mkdir -p %buildroot%_sysconfdir/menu-methods
install -m 755 %SOURCE2 %buildroot%_sysconfdir/menu-methods/%name

install -pD -m644 %SOURCE3 %buildroot%_miconsdir/%name.png
install -pD -m644 %SOURCE4 %buildroot%_niconsdir/%name.png
install -pD -m644 %SOURCE5 %buildroot%_liconsdir/%name.png
install -pD -m644 %SOURCE7 %buildroot%_pixmapsdir/IceWM.xpm
install -pD -m644 %SOURCE8 %buildroot%_sysconfdir/X11/wmsession.d/04IceWM
install -pD -m644 %SOURCE9 %buildroot%_altdir/%name
install -m 644 %SOURCE11 doc/README.ALT

mkdir -p %buildroot%_sysconfdir/X11/%name

mv %buildroot%_x11x11dir/%name/{menu,preferences,keys,toolbar,winoptions} %buildroot%_sysconfdir/X11/%name/

install -m 755 %SOURCE6 %buildroot%_bindir/start%name
install -m 755 %SOURCE13 %buildroot%_sysconfdir/X11/%name/restart

%if_without menu
desktop-file-install --vendor alt --dir %buildroot%_desktopdir %SOURCE12
%endif

%find_lang  %name

# remove unpackaged files
rm -f %buildroot/%_bindir/%name-set-gnomewm
rm -rf %buildroot/%_x11x11dir/%name/themes/*

%files
%_bindir/%name-full
#_bindir/icesound
%_bindir/icesh
%_bindir/icehelp
%_bindir/%{name}hint
%_x11x11dir/%name/icons/*
%exclude %_x11x11dir/%name/icons/app*
%exclude %_x11x11dir/%name/icons/xterm*

%doc README CHANGES TODO BUGS AUTHORS %name.lsm  doc/*.html doc/%name.sgml doc/README*

%files light -f %name.lang
%config(noreplace) %_sysconfdir/menu-methods/*
%_sysconfdir/X11/wmsession.d/*
%_altdir/%name
%_bindir/%name-light
%_bindir/%name-session
%_bindir/start%name
%_bindir/%{name}tray
%_bindir/%{name}bg
%dir %_x11x11dir/%name
%_x11x11dir/%name/mailbox
%dir %_sysconfdir/X11/%name
%ghost %config(noreplace) %_sysconfdir/X11/%name/menu
%config(noreplace) %_sysconfdir/X11/%name/preferences
%config(noreplace) %_sysconfdir/X11/%name/restart
%config(noreplace) %_sysconfdir/X11/%name/toolbar
%config(noreplace) %_sysconfdir/X11/%name/keys
%config(noreplace) %_sysconfdir/X11/%name/winoptions
%_x11x11dir/%name/taskbar
%_x11x11dir/%name/ledclock
%dir %_x11x11dir/%name/icons
%dir %_x11x11dir/%name/themes
%_x11x11dir/%name/icons/app*
%_x11x11dir/%name/icons/xterm*
%if_with menu
%_menudir/*
%else
%_desktopdir/*
%endif
%_niconsdir/*
%_miconsdir/*
%_liconsdir/*
%_pixmapsdir/*

%changelog
* Mon Jun 18 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 2:1.3.7-alt7
- fixed warnings of using deprecated functions
- updated defaults of 'keys' and 'winoptions' files

* Sun May 20 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 2:1.3.7-alt6
- fixed DSO link error
- buildreq

* Wed Apr 04 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 2:1.3.7-alt5
- don't define "deprecated", use "_ICEWM_deprecated" instead
- added TaskBarCentered feature
- WorkspaceNames set as themable

* Tue May 10 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 2:1.3.7-alt4
- fixed /etc/menu-methods/icewm

* Sat May 07 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 2:1.3.7-alt3
- adapted themable_taskWidth_taskButtons_atrayPix_1.2.27.diff
- adapted task_bar_length.patch

* Sun Apr 10 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 2:1.3.7-alt2
- added request of the CPU temperature from /sys/class/thermal/
- added tray_hotfixes patch from debian
- removed call of apt-indicator from starticewm
- icewm-light now reqiures design-icewm >= 1.0-alt6

* Mon Nov 01 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 2:1.3.7-alt1
- 1.3.7
- removed unpackaged files

* Tue Sep 21 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 1:1.3.7pre2-alt2
- updated i18n from debian
- build with menu again
- disabled taskbar, gradients, shaped-decorations for icewm-light
- updated README.ALT

* Mon Sep 06 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 1:1.3.7pre2-alt1
- 1.3.7pre2

* Sun Sep 05 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 1:1.3.6-alt0.99.1
- 1.3.6
- build without icesound, alsa, menu
- buildreq

* Sat Sep 04 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 1:1.2.38pre2-alt1
- 1.2.38pre2
- changed packager

* Mon Aug 30 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 1:1.2.38pre1-alt3
- fixed bad wmsession config

* Thu Nov 26 2009 Terechkov Evgenii <evg@altlinux.ru> 1:1.2.38pre1-alt2
- Repocop patch applied

* Fri Jun 12 2009 Terechkov Evgenii <evg@altlinux.ru> 1:1.2.38pre1-alt1
- 1.2.38pre1

* Mon Jan 26 2009 Terechkov Evgenii <evg@altlinux.ru> 1:1.2.37-alt1
- 1.2.37

* Fri Dec 26 2008 Terechkov Evgenii <evg@altlinux.ru> 1:1.2.36-alt2.1
- Alternatives files resurrected (shame on me and thanks to ldv@)

* Thu Dec 25 2008 Terechkov Evgenii <evg@altlinux.ru> 1:1.2.36-alt2
- Allternatives now unneeded
- Migrate to new filetriggers system

* Mon Nov  3 2008 Terechkov Evgenii <evg@altlinux.ru> 1:1.2.36-alt1
- 1.2.36
- Set epoch (shame on me!)
- s/gear-update/gear-merge/ in prev changelog entry

* Tue Aug 12 2008 Terechkov Evgenii <evg@altlinux.ru> 1.2.36pre1-alt1
- 1.2.36pre1
- Migrate to gear-update (thanks, legion@)

* Sun Aug 10 2008 Terechkov Evgenii <evg@altlinux.ru> 1.2.35-alt4
- Migrate to new gear scheme (thanks, raorn@)

* Wed May 14 2008 Terechkov Evgenii <evg@altlinux.ru> 1.2.35-alt3
- Patch53 added to fix build with new libalsa (Brain-dead code in Icewm, fixes #15640)
- desktop-file-utils needed only when we build with .desktop
- Redundant PreReq removed (thanks, at@)
- Last change in Patch10 reverted back (#15645)

* Sat Feb 16 2008 Terechkov Evgenii <evg@altlinux.ru> 1.2.35-alt2.1
- Patch10 updated to fix non-working reboot and shutdown in CTRL-ALT-DEL dialog (paths set to absolute)

* Sat Jan 19 2008 Terechkov Evgenii <evg@altlinux.ru> 1.2.35-alt2
- Patch21 updated from upstream (fix for #14082)

* Sat Jan 12 2008 Terechkov Evgenii <evg@altlinux.ru> 1.2.35-alt1
- 1.2.35
- Patch23 updated
- Patch46 removed (merged in upstream)

* Tue Jan  1 2008 Terechkov Evgenii <evg@altlinux.ru> 1.2.34-alt1
- 1.2.34

* Thu Nov 22 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.33-alt1
- 1.2.33
- Patch52 added (README.ALT updated)
- Patch48 removed (fixed in upstream)
- Patch19 updated

* Sat Nov  3 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.32-alt3.2
- Package separation fixes
- Patch49 default setting changed to true
- README.ALT updated

* Sun Sep  2 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.32-alt3.1
- Patch50 updated to generate valid config
- Patch0 updated (IconPath) to reflect Patch51 changes
- Patch51 added to support Fd.o icon paths

* Mon Aug 27 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.32-alt3
- s/LGPL/LGPLv2/ in license tag
- Patch49,50 added (later require former)
- Patch47 replaced with Patch48

* Fri Aug 24 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.32-alt2.1
- README.ALT spelled and updated (thanks to php-coder@)

* Thu Aug 23 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.32-alt2
- README.ALT updated to reflect recently added patches
- Packager tag added to spec
- Patch45 removed (Was not applied and broken, anyway)
- Patch21 updated (Thanks to Vladimir Gusev!)

* Sat Aug 18 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.32-alt1
- Patch47 added to fix 1.2.32 tray behavior

* Thu Aug 16 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.32-alt0
- Patch43 removed (merged in upstream)
- Patch46 added - fix for noFocusOnMap
- Patch35 removed (merged in upstream)
- Patch34 removed (merged in upstream)

* Mon Jul  2 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.30-alt8
- Patch44,45 added (experimental)
- Russian summary and description removed (Specspo)
- Spec cleanups (un__.sh)

* Thu May 24 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.30-alt7
- Patch0 updated (%%_niconsdir added to IconPath)
- Patch11 removed (no needed for a long time)
- Many patches updated to work with -p0 && diffstats

* Sat Apr 28 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.30-alt6
- Patch42 (from Suse) added
- .desktop file replaced by FC6's. It was broken anyway.
- Patch43 (from FC6) added

* Tue Apr 17 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.30-alt5
- Patch10 updated (number of workspaces set to 4)
- Patch37-41 added (README.ALT updated)
- Patch21 updated (README.pager updated)

* Sat Feb 24 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.30-alt4
- Patch36 to allow environment variables in configs

* Sun Feb 11 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.30-alt3
- Patch35 to show ShowFocusModeMenu and ShowSettingsMenu entrys

* Thu Jan 25 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2.30-alt2
- Spec converted to utf-8
- 32 pixel icon moved to right place
- missed %_iconsdir/IceWM.xpm added (#10690).

* Tue Dec 26 2006 Terechkov Evgenii <evg@altlinux.ru> 1.2.30-alt1
- 1.2.30
- Patch23 updated
- Patch33 removed (fixed in upstream)
- ru.po patch (#34) added

* Wed Dec 13 2006 Terechkov Evgenii <evg@altlinux.ru> 1.2.29-alt2
- %%config issues fixed (including #10412)
- Patch33 added to fix transient windows behavior
- icewmtray patch (Patch32) added to fix crash on sighup
- spec cleanups (s/%name/%%name/)
- winoptions additionals
- #1040 fixed in menu-methods and toolbar
- icewmbg moved to icewm-light (partial fix for #8072)

* Tue Dec  5 2006 Terechkov Evgenii <evg@altlinux.ru> 1.2.29-alt1
- 1.2.29
- New menu method
- Wrong entries in %%files fixed
- Patch0 updated (IconPath)
- qt4 segfault patch (#32) removed (fixed in upstream)

* Sat Dec  2 2006 Terechkov Evgenii <evg@altlinux.ru> 1.2.28-alt4
- Bugs #10355,#10353 fixed (patch0,10 updated)
- icewm.menu-methods changed according menu packaging policy

* Mon Nov 13 2006 Terechkov Evgenii <evg@altlinux.ru> 1.2.28-alt3
- qt4 segfault patch (#32) added to fix bug #10108

* Sat Nov 11 2006 Terechkov Evgenii <evg@altlinux.ru> 1.2.28-alt2
- themable_taskWidth_taskButtons_atrayPix_1.2.27.diff (#31) from lxp project added
- themes.patch (#30) added (thanks to Vladimir Gusev)
- restart script added (thanks to Vladimir Gusev)
- Patches 27-28 from OpenSuSE added
- BuildRequires updated
- .desktop file added (disabled for now - file need to be fixed)

* Sun Nov  5 2006 Terechkov Evgenii <evg@altlinux.ru> 1.2.28-alt1
- Major spec cleanups
- icewm.menu updated (s/xpm/png/)
- patch10 renewed
- added icewmhelp
- Recommends: added
- patches 22-26 added
- patch1 removed (fixed in upstream)
- source 14-15 added (README.pager, README.ALT)
- 1.2.28

* Fri Mar 24 2006 Anton Farygin <rider@altlinux.ru> 1.2.25-alt3
- added %_iconsdir/IceWM.xpm (#9303)

* Wed Mar 22 2006 Anton Farygin <rider@altlinux.ru> 1.2.25-alt2
- rebuild fixed (icons)

* Tue Feb 07 2006 Anton Farygin <rider@altlinux.ru> 1.2.25-alt1
- new version

* Mon Jan 30 2006 Anton Farygin <rider@altlinux.ru> 1.2.23-alt2
- xorg-7.0 support
- use /etc/X11/icewm for preferences and menus
- use /usr/share/X11/icewm for themes

* Thu Sep 08 2005 Anton Farygin <rider@altlinux.ru> 1.2.23-alt1
- new version

* Thu Jul 14 2005 Anton Farygin <rider@altlinux.ru> 1.2.21-alt1
- new version
- fixed #4282
- fixed #6004

* Tue Sep 07 2004 Anton Farygin <rider@altlinux.ru> 1.2.16-alt1
- 1.2.16
- fixed #4282

* Mon Jul 12 2004 Anton Farygin <rider@altlinux.ru> 1.2.14-alt1
- new version
- builded light version without anialiasing
- icewmtray moved to %name-light package
- fixed bugs #1065, #4282, #4193

* Tue Dec 23 2003 Rider <rider@altlinux.ru> 1.2.13-alt4
- fix for build with readline support

* Mon Oct 20 2003 Rider <rider@altlinux.ru> 1.2.13-alt3
- disabled antialiasing and readline for icewm-light
- fixed bug in icewm-session: if user exit from XFree by CTRL+ALT+BackSpace, 
    then icewm-session using 100%% CPU. (patch18)
- fixed bug in icons.cc: speed up first time menu show (patch18)

* Sun Sep 28 2003 Rider <rider@altlinux.ru> 1.2.13-alt2
- new version (with fix for bug #1573)
- added alt-update applet to starticewm
- icewm changed to icewm-session in starticewm script (fix for bug #2881)

* Wed Sep 03 2003 Rider <rider@altlinux.ru> 1.2.12-alt1
- new version

* Fri Aug 22 2003 Rider <rider@altlinux.ru> 1.2.11-alt1
- new version
- fixed bug with keyboard hotkeys
- set default WorkspaceNames to 8 workspaces 
- disable apm status by default
- enabled TaskBarClockLeds option
- added new keyboard shorcuts to programs:
    Alt+Ctrl+t - xterm
    Alt+Ctrl+n - mozilla
    Alt+Ctrl+m - mozilla-mail
    Alt+Ctrl+p - psi
    Alt+Ctrl+x - xchat

* Fri Jul 11 2003 Rider <rider@altlinux.ru> 1.2.9-alt1
- new version
- added icesound and icewmtray to icewm package
- removed obsoletted by icewmtray winoptions (licq, psi and otcher)
- fixed toolbar for xine icon
- fixed bug in icewm-1.2.9, double sized taskbar and docking tray
- patch for readline support in addressbar from Kachalov Anton (mouse)


* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 1.2.0-alt4.2
- new alternatives config format

* Thu Mar 20 2003 Stanislav Ievlev <inger@altlinux.ru> 1.2.0-alt4.1
- move to new alternatives scheme
- added packager file

* Wed Jan 29 2003 Rider <rider@altlinux.ru> 1.2.0-alt4
- use /usr/X11R6/bin/xscreenlock in toolbar and icewm lock command
  (bug #0002099)
- fix for search icons with size in name (like icewm_16x16.xpm)
- include lock icons to package
- temporary fix menu-methods for search icons from KDE

* Mon Dec 30 2002 Rider <rider@altlinux.ru> 1.2.0-alt3
- added patch for search png icons

* Mon Dec 23 2002 Rider <rider@altlinux.ru> 1.2.0-alt2
- updated toolbar (remove LICQ icon and add PSI icon)

* Fri Oct 18 2002 Rider <rider@altlinux.ru> 1.2.0-alt1
- 1.2.0
- icewm-full version build with libXft2 ( --enable-antialiasing, icewm-1.2.0-alt-xft2.patch)
- icesh included to icewm package
- removed update_menus and clean_menus from icewm package (now only in icewm-light)
- default theme moved to design-icewm package
- more themes moved to design-icewm-themes package
- png icons from MDK
- menu and titlebar fonts set to MEDIUM

* Mon Oct 14 2002 Rider <rider@altlinux.ru> 1.0.9-alt15
- build without freetype
- rename icewm-gnome to icewm-full
- build icewm-light without --enable-light
- default background from design-graphics package
- icewm-light build with imlib (for PNG icons)
- preun scripts bugfix

* Mon Oct 13 2002 Rider <rider@altlinux.ru> 1.0.9-alt14
- rebuild

* Thu Oct 03 2002 Rider <rider@altlinux.ru> 1.0.9-alt13
- removed Almost_Mac theme (specially for moslem users)

* Wed Sep 25 2002 Rider <rider@altlinux.ru> 1.0.9-alt12
- patches from MDK for gcc3 build
- gcc 3.2 rebuild 

* Wed Apr 17 2002 Rider <rider@altlinux.ru> 1.0.9-alt11
- cool winoptions for psi, movatk and gkrellm (thanks for Migor)

* Fri Apr 12 2002 Rider <rider@altlinux.ru> 1.0.9-alt10
- fixed default fonts in Infadel2 theme
- bug #0000774 closed
- default background now /usr/share/wallpapers/altlinux-bg.png

* Fri Feb 01 2002 Rider <rider@altlinux.ru> 1.0.9-alt9
- more winoptions for licq
- not show apm status if battery is not detected (patch1)
- fix xterm options

* Fri Jan 18 2002 Rider <rider@altlinux.ru> 1.0.9-alt8
- disable default xfreetype config option
- default mail client now mutt
- fix poweroff and reboot (on CTRL+ALT+DEL menu)

* Mon Jan 14 2002 Rider <rider@altlinux.ru> 1.0.9-alt7
- fix ALT+F12 desktop switch

* Fri Jan 11 2002 Rider <rider@altlinux.ru> 1.0.9-alt6
- themes update

* Tue Jan 08 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.9-alt5
- Updated wmsession.d and startup scripts.
- Minor specfile cleanup.

* Wed Jan 02 2002 Rider <rider@altlinux.ru> 1.0.9-alt4
- default theme fix
- russian summary and description
- added special winoptions for licq.

* Fri Oct 12 2001 AEN <aen@logic.ru> 1.0.9-alt3
- rebuilt with libpng.so.3

* Wed Oct 10 2001 Rider <rider@altlinux.ru> 1.0.9-alt2
- 1.0.9-2

* Tue Sep 11 2001 Rider <rider@altlinux.ru> 1.0.8-alt3
- default theme bugfix
- new toolbar setup and icons

* Tue Sep 11 2001 Rider <rider@altlinux.ru> 1.0.8-alt3
- new themes

* Fri May 05 2001 Rider <rider@altlinux.ru> 1.0.8-alt2
- 1.0.8-5

* Wed Apr 24 2001 Rider <rider@altlinux.ru>
- 1.0.8
- build icewm-light version with icewm-lite option

* Sun Mar 18 2001 Rider <rider@altlinux.ru>
- 1.0.7

* Fri Mar 16 2001 Rider <rider@altlinux.ru>
- fdleak patch from Sergey Vlasov <vsu@mivlgu.murom.ru>
- add MicroGUI theme

* Thu Feb 22 2001 Rider <rider@linux.ru.net>
- time.h patch

* Sat Jan 20 2001 Rider <rider@linux.ru.net>
- new version: 1.0.6
- removed patch for ru.po
- changed default IceWM config (icewm-defconf.patch)
- changed default IceWM theme

* Tue Dec 19 2000 AEN <aen@logic.ru>
- 1.0.5
- ru.po fixed

* Tue Dec 05 2000 AEN <aen@logic.ru>
- fonts patch

* Fri Oct 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-14mdk
- Fix compilation for gcc-2.96.

* Tue Oct 03 2000 Florin Grad <florin@mandrakesoft.com> 1.0.4-13mdk
- the isdn patch gives coredumps again

* Mon Oct 02 2000 Florin Grad <florin@mandrakesoft.com> 1.0.4-12mdk
- added the isdn patch (thanks to Mathias Hasselmann)
- added the logout patch (thanks again)

* Wed Sep 27 2000 Florin Grad <florin@mandrakesoft.com> 1.0.4-11mdk
- fix the theme

* Tue Sep 26 2000 Florin Grad <florin@mandrakesoft.com> 1.0.4-10mdk
- the isdn creates some conflicts so I take it away for the moment

* Tue Sep 26 2000 Florin Grad <florin@mandrakesoft.com> 1.0.4-9mdk
- added the isdn status patch
- modify the menu method for the default icon
- "new" lighter default theme

* Thu Sep 21 2000 Florin Grad <florin@mandrakesoft.com> 1.0.4-8mdk
- transparent icons
- added large icon
- fixed some dangling symlinks

* Tue Sep 19 2000 Florin Grad <florin@mandrakesoft.com> 1.0.4-7mdk
- modified the icewm-menu-method for the kde icons (locolor and hicolor ones) and added to iconPath
- added the window-transient patch
- added the tooltips-show-forever patch
- added the non-latin(1)-(lang)fonts patch
- added the better-ppp-status patch
- eth0 is now as default in src/default.h

* Wed Sep 6 2000 Florin Grad <florin@mandrakesoft.com> 1.0.4-6mdk
- replace rxvt with xterm in menus and shortcuts (priority package is higher)

* Tue Sep 5 2000 Florin Grad <florin@mandrakesoft.com> 1.0.4-5mdk
- adding some new themes and fix the terminal command in the task bar
- adding the alternatives method
- adding a shortcut to rxvt Alt+Ctrl+t

* Mon Sep 4 2000 Florin Grad <florin@mandrakesoft.com> 1.0.4-4mdk
- replaced /usr/X11/bin/xsetroot with /usr/X11R6/bin/xsetroot

* Thu Aug 31 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.4-3mdk
- New wmsession support

* Tue Aug 22 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.4-2mdk
- BM
- more macros
- config(noreplace) the menu-method
- fixed %install section which was not working anymore

* Tue Jun 13 2000 Florin Grad <florin@mandrakesoft.com> 1.0.4-1mdk
- 1.0.4
- comment the gnome-patch

* Tue May  9 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.3-11mdk
- added an xterm entry in toplevel menu.

* Sun May  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.3-10mdk
- default panel: rxvt -> xterm because xterm is always installed, not
  rxvt

* Sat Apr 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.3-9mdk
- added specific menu entries /IceWM/.. with help of Frederic Lepied

* Fri Apr 28 2000 dam's <damien@mandrakesoft.com> 1.0.3-8mdk
- added fndSession call

* Fri Apr 28 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.3-7mdk
- re-fixed menu-method: now prints out the submenu icons
- added icons for the menu entry

* Thu Apr 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.3-6mdk
- fixed icons in menu-method: now takes the mini icon if present
  before trying to take the main icon

* Wed Apr 19 2000 dam's <damien@mandrakesoft.com> 1.0.3-5mdk
- Changed iceons.

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 1.0.3-4mdk
- Change taskbar icon.

* Fri Apr  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.3-3mdk
- Apply mdkconf patch.

* Fri Apr 07 2000 Daouda Lo <daouda@mandrakesoft.com> 1.0.3-2mdk
- remove the hardcoded gnome menu entry
- some minor fixes to spec (clean up , add -q to setup ...)

* Wed Apr  5 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.3-1mdk
- 1.0.3

* Sun Apr  2 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.2-4mdk
- added support for menu i18n

* Wed Feb 23 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.2-3mdk
- added a prereq on menu.

* Mon Feb 21 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.2-2mdk
- added menu support.

* Sun Feb 20 2000 Pixel <pixel@mandrakesoft.com> 1.0.2-1mdk
- new version
- clean up (nice spec-helper :)

* Tue Jan 18 2000 Florin Grad <florin@mandrakesoft.com>
- 1.0.1
- obviously icewm is Y2K compliant ;)

* Thu Dec 30 1999 Frederic Lepied <flepied@mandrakesoft.com> 1.0.0-2mdk
- fix perms for /usr/X11R6/lib/X11/icewm/themes/IceGTK.

* Tue Dec 28 1999 Pixel <pixel@mandrakesoft.com>
- 1.0.0

* Tue Dec 21 1999 Florin Grad <florin@mandrakesoft.com>
- add the kde2ice python script
- with-gnome-menu
- remove the background picture
- update of the Mandrake icons
- modify the IconPath in default.c

* Mon Dec 13 1999 Florin Grad <florin@mandrakesoft.com>
- add FAQ-french
- add rpmdrake in the Mandrake menu
- use a 1024x768 background image instead of a 800x600 one
- 0.9.54

* Sun Nov 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Split icewm in multiple package icewm-light and icewm-gnome(default).

* Fri Nov 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- DesktopBackgoundColor=1 by default.

* Wed Nov 17 1999 Florin Grad <florin@mandrakesoft.com>
- Add a new default background.
- A nice theme collection.
- New default theme.
- New associative icons.
- C-x C-t between xterm and rxvt in menu.

* Wed Nov 17 1999 Damien Krotkine <damien@mandrakesoft.com>
- 0.9.50

* Wed Aug 25 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 0.9.48

* Mon Aug 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 0.9.47
- Remove ShowNetStatus by default.

* Fri Aug 13 1999 Bernhard RosenkrДnzer <bero@mandrakesoft.com>
- 0.9.46
- hope the date (Friday 13th) doesn't affect the stability ;)

* Wed Aug 11 1999 Bernhard RosenkrДnzer <bero@mandrakesoft.com>
- 0.9.44
- fix compilation with gcc 2.95

* Tue Jul 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Add patch to have a mandrake menus.

* Tue Jul 20 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- add french description from Gregus <gregus@etudiant.net>

* Fri Jul 16 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Reinserting the mandrake pixmaps.

* Tue Jul 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Patch to have by default a mandrake background.

* Wed Jul 07 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 0.9.43 :
        - fixes to configure
	- fixed some focusing problems
        - some new netscape icons added
        - fixes to shell command execution (no longer crashes on restart wm)
        - improvement in shaped windows handling
        - allow relative pathname in background image specification
        - made window stacking not interfere with DND icons
        - fix: minimize action in window list is no longer a toggle
        - detect both Alt_L and Alt_R keysf for Alt modifier.
        - configure event coalescing is now done to improve performance

* Tue May 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Reinsertion of mandrake xpm.

* Sun May 23 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 0.9.41
- Recreated Chmouel's patches for 0.9.41

* Sat May 22 1999 Bernhard RosenkrДnzer <bero@mandrakesoft.com>
- 0.9.39, hoping to fix segfaults.
- disable debug

* Mon Apr 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.
- Build with Gnome Support
- Handle RPM_OPT_FLAGS.
- Add Mandrake Icons.
- Add patch to make Mandrake Icons by default.
- Add patch to have GTK theme by default instead of Win95 look (BEURK).

