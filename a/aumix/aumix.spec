Name: aumix
Version: 2.9.1
Release: alt1.qa1

Summary: A GTK+/Ncurses audio mixer
License: GPL
Group: Sound

URL: http://www.jpj.net/~trevor/aumix.html
Source0: http://www.jpj.net/~trevor/aumix/%name-%version.tar.bz2

Source2: %name-16.xpm
Source3: %name-32.xpm
Source4: %name-48.xpm
Source5: %name-mute.1
Source6: %name.firsttime

Patch0: %name-2.6-mdk-datadir.patch
Patch1: %name-2.7-alt-taumix-deps.patch
Patch2: %name-2.7-mdk-devfs-compliant.patch
Patch3: aumix-2.9.1-alt-gtk_set_locale.patch
Patch6: %name-2.8-deb-autoconf25.patch
Patch7: aumix-2.9.1-alt-ru-po.patch
Patch9: %name-2.8-rh-cursor-color.patch
Patch10: aumix-2.9.1-alt-rh-crackrock.patch
Patch11: %name-2.8-deb-fgbg.patch
Patch13: aumix-2.9.1-alt-deb-failmsg.patch

Requires: %name-minimal = %version-%release

# Automatically added by buildreq on Sat Oct 09 2010
BuildRequires: libgpm-devel libgtk+2-devel libncurses-devel

%package minimal
Summary: Command-line audio mixer
Group: Sound

%description
This is a program for adjusting audio mixers from the command
line or scripts, or interactively at the console or a terminal
with a full-screen, ncurses-based interface or a GTK-based X
interface.

%description minimal
This is a program for adjusting audio mixers from the command
line or scripts.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
#patch6 -p1
%patch7 -p1
%patch9
%patch10 -p1
%patch11 -p1
%patch13 -p1
bzip2 -9fk ChangeLog

# Rename "xaumix" to "taumix".
grep -FrlZ xaumix . |
	xargs -r0 subst s/xaumix/taumix/g --
mv doc/{x,t}aumix.1
mv src/{x,t}aumix

%build
%autoreconf
%configure --prefix=/ --without-ncurses --without-gtk
%make_build
mv src/aumix{,-minimal}

%make distclean
%configure
%make_build

%install
%makeinstall
install -pDm755 {src,%buildroot/bin}/aumix-minimal

install -pDm644 %SOURCE2 %buildroot%_miconsdir/%name.xpm
install -pDm644 %SOURCE3 %buildroot%_niconsdir/%name.xpm
install -pDm644 %SOURCE4 %buildroot%_liconsdir/%name.xpm

install -pDm644 %SOURCE5 %buildroot%_man1dir/mute.1
install -pDm755 %SOURCE6 %buildroot%_sysconfdir/firsttime.d/%name

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Aumix
GenericName=Audio Mixer
Comment=Aumix Audio Mixer
Icon=%name
Exec=%name
Terminal=false
Categories=AudioVideo;Audio;Mixer;
EOF

%find_lang %name

%files -f %name.lang
%doc AUTHORS BUGS ChangeLog.bz2 NEWS README TODO
%_bindir/*
%_man1dir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%_liconsdir/*.xpm

%files minimal
/bin/%name-minimal
%config %_sysconfdir/firsttime.d/%name

%changelog
* Sun Apr 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1.qa1
- NMU: converted menu to desktop file

* Sat Oct 09 2010 Michael Shigorin <mike@altlinux.org> 2.9.1-alt1
- 2.9.1 (closes: #23600)
- dropped extra line from menufile (closes: #9350)
- bug cleanup (#7700, #8070)
- spec cleanup
  + dropped gtk1, alsa references (unsupported)
- patch cleanup:
  + updated patch3, patch7, patch10, patch13
  + patch4, patch5, patch8, patch15, patch17 merged upstream
  + patch14, patch16 seem to be reworked/merged upstream
  + dropped patch6, patch12

* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.8-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for aumix
  * update_menus for aumix
  * postclean-05-filetriggers for spec file

* Sun Apr 17 2005 Alexey Tourbin <at@altlinux.ru> 2.8-alt4
- rh-mute.patch: fix %_bindir/mute not restoring volume when unmuting
- rh-cursor-color.patch: fix cursor color on exit
- rh-crackrock.patch: fix a buffer overflow
- deb-fgbg.patch: use terminal's default foreground and background colors
- deb-xpm.patch: remove quotes in aumix.xpm, makes the icon usable in KDE
- deb-failmsg.patch: outputs an error message if aumix cannot open the mixer
- deb-redraw-balance.patch: erase "balance selected" character in ncurses mode
- deb-rec-redraw.patch: remove useless redrawing of record/play controls
- deb-DISPLAY.patch: check the DISPLAY environment is not empty
- deb-HOME.patch: check the HOME environment is not empty

* Sun Feb 29 2004 Alexey Tourbin <at@altlinux.ru> 2.8-alt3.1
- fixed build with automake-1.8

* Fri Feb 06 2004 Alexey Tourbin <at@altlinux.ru> 2.8-alt3
- mdk-close-dialogs.patch: destroy save/open dialogs on "ok" button press
- mdk-utf8-gtk2.patch: fix string convertions and make gtk2 build possible
- gtk2 build at last
- deb-autoconf25.patch: build with recent autoconf
- ru.po updated (#3300)
- mute(1) man page added (debian)

* Sun Oct 26 2003 Dmitry V. Levin <ldv@altlinux.org> 2.8-alt2
- %_sysconfdir/firsttime.d/%name:
  relocated from startup to this package.
- Additional spec&patch conventions enforcement.

* Wed Oct 08 2003 Alexey Tourbin <at@altlinux.ru> 2.8-alt1
- updated to 2.8
- gtk1 build as yet
- aumix-minimal package: /bin/aumix-minmal for command-line invocations (#3043)

* Thu Jan 09 2003 Konstantin Volckov <goldhead@altlinux.ru> 2.7-ipl14mdk
- Fixed rebuilding

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.7-ipl13mdk
- Rebuilt in new environment

* Tue Jun 18 2002 AEN <aen@logic.ru> 2.7-ipl12mdk
- uk.po fixed

* Wed Apr 17 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.7-ipl11mdk
- Fixed russian translation

* Tue Mar 05 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.7-ipl10mdk
- Added devfs-compliant patch
- Fixed translations (CP1251)
- Updated russian translation

* Tue Feb 05 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.7-ipl9mdk
- Fixed menu entry - added KDE menu

* Wed May 23 2001 Stanislav Ievlev <inger@altlinux.ru> 2.7-ipl8mdk
- Remove XFree86 requirement. We need only XFree86-libs

* Tue Jan  2 2001 Kostya Timoshenko <kt@petr.kz>
- Build for RE

* Tue Nov 21 2000 Egil Moller <redhog@mandrakesoft.com> 2.7-7mdk
- Fixed the URL

* Tue Nov 21 2000 Egil Moller <redhog@mandrakesoft.com> 2.7-6mdk
- Added large-icon to make rpmlint happy

* Sat Sep 08 2000 David BAUDENS <baudens@mandrakesoft.com> 2.7-5mdk
- Fix menu entry

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.7-4mdk
- automatically added BuildRequires

* Wed Jul 19 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.7-3mdk
- rebuild for buggy %%clean_menus

* Tue Jul 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.7-2mdk
- rebuild for BM

* Fri Jul 14 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.7-1mdk
- 2.7
- menu macros

* Tue Jun 27 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.6.1-1mdk
- 2.6.1
- chmouelization of specfile
- now "xaumix" has been renamed to "taumix"

* Fri Apr 28 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.6-3mdk
- corrected menu entry, added 32x32 icon

* Mon Apr 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.6-2mdk
- remove aumix-minimal, chmouel doesn't need it anymore
- patch to provide a correct DATADIRNAME

* Thu Apr 13 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.6-1mdk
- 2.6
- nice, this new version fixes a small bug :-)

* Mon Apr 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.5-2mdk
- added URL
- added hand-drawn (oops..) icon

* Fri Mar 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.5-1mdk
- 2.5

* Thu Mar 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.4-1mdk
- 2.4 with french translation :-)
- better without-gtk patch
- new groups
- menu entry

* Tue Mar 14 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.2-1mdk
- 2.2
- patch to new sources to continue to support aumix-minimal

* Thu Mar  9 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1-2mdk
- Remove dependences of gtk for aumix-minimal.

* Sun Feb 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1-1mdk
- Clean-up spec (thanks deb-helper).
- Reinsert aumix-minimal.
- 2.1.

* Tue Nov 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix xmix.

* Mon Nov 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.28.
- Correcting files list.

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.27.
- --with-alsa.

* Tue Sep 07 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- fixed ukrainian language code (it is 'uk' not 'ua')

* Wed Jun 23 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 1.18.2 to 1.22.1
- removed obsolete patch for 1.18.2

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Wed Feb 24 1999 Bill Nottingham <notting@redhat.com>
- update to 1.18.2

* Mon Feb 22 1999 Bill Nottingham <notting@redhat.com>
- update to 1.18.1

* Mon Feb  8 1999 Bill Nottingham <notting@redhat.com>
- update to 1.17

* Mon Feb  1 1999 Bill Nottingham <notting@redhat.com>
- update to 1.15

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- update to 1.14

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binary

* Fri Oct  2 1998 Bill Nottingham <notting@redhat.com>
- updated to 1.13

* Fri Aug 28 1998 Bill Nottingham <notting@redhat.com>
- updated to 1.12

* Mon Aug 17 1998 Bill Nottingham <notting@redhat.com>
- updated to 1.11

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.8

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed source url
- updated version

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built with glibc

* Thu Mar 20 1997 Michael Fulbright <msf@redhat.com>
- Updated to v. 1.6.1.
