Name: dosemu
Version: 1.4.0.1
Release: alt1.qa1
Serial: 1
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: The Linux DOS emulator
Summary(ru_RU.UTF-8): Эмулятор DOS под Linux
License: GPL
Group: Emulators
Url: http://dosemu.sourceforge.net/

Source0: http://telia.dl.sourceforge.net/sourceforge/dosemu/%name-%version.tar

# icons from Mandrake
Source2: xdosemu.xpm
Source3: xdosemu-mini.xpm
Source4: xdosemu-large.xpm

# sources and precompiled fonts
Source9: dosemu-1.4.0-alt-fonts.tar

# default /etc/dosemu.users
Source13: dosemu.users

Patch: %name-%version-alt.patch

Obsoletes: dosemu-bin-nox
Conflicts: dosemu-freedos < 050405-alt3
Conflicts: dosemu-bin-x

# Automatically added by buildreq on Wed Mar 11 2009
BuildRequires: flex imake libICE-devel libSDL-devel libX11-devel libXext-devel libXxf86vm-devel libalsa-devel libgpm-devel libslang-devel libsndfile-devel

%description
This package allows MS-DOS programs to be started in Linux. A virtual
machine (the DOS box) provides the necessary BIOS functions and emulates
most of the chip devices (e.g. timer, interrupt- and keyboard controler)
Documentation can be found in %_defaultdocdir/%name-%version and in the man
page, as well as in the sources.
You probably need dosemu-freedos package too.

%description -l ru_RU.UTF-8
DOSEmu позволяет запускать программы MS-DOS под Linux. Виртуальная
машина (DOS) предоставляет необходимые функции BIOS и эмулирует
большинство устройств, таких как таймер, контроллеры прерываний
и клавиатуры. Документацию можно найти в %_defaultdocdir/%name-%version
и на страницах руководства (man). Как, впрочем, и в исходниках.
Вероятно, вам также понадобится пакет dosemu-freedos.

%package plugins-x-sdl
Summary: Dosemu X11 and SDL plugins
License: GPL
Group: Emulators
Requires: dosemu = %version-%release
Obsoletes: xdosemu
Obsoletes: dosemu-bin-x

%description plugins-x-sdl
The Linux DOS Emulator XFree86/Xorg and SDL plugins.

%package plugins-sound
Summary: Dosemu ALSA and Sndfile plugins
License: GPL
Group: Emulators
Requires: dosemu = %version-%release

%description plugins-sound
The Linux DOS Emulator ALSA and Sndfile plugins.

%prep
%setup -q

cp -f compiletime-settings.devel compiletime-settings
%patch -p1

sed -i -e "s!#[[:space:]]*\(\$_cli_timeout[[:space:]]*=[[:space:]]*\)(.*!\1(10)!g" etc/dosemu.conf
sed -i -e "s!#[[:space:]]*\(\$_ttylocks[[:space:]]*=[[:space:]]*\)\".*!\1\"/var/lock/serial\"!g" etc/dosemu.conf

# copy sources and precompiled VGA fonts
tar xf %SOURCE9 -C etc
gzip etc/*.pcf

# to avoid automatic autoreconf call
#touch configure.ac configure

%build
# TODO: why not try to disable these plugins?
sed -i -e "s! x off! x on!g" compiletime-settings
sed -i -e "s! plugin_sdl off! plugin_sdl on!g" compiletime-settings
%configure --with-pthreads
%make_build WAIT=no prefix=%_prefix

%install
# install itself
%make_install install DESTDIR=%buildroot prefix=%prefix \
	      mandir=%_mandir docdir=%_defaultdocdir/%name-%version
# /var/lib/dosemu for custom DOS
mkdir -p %buildroot%_localstatedir/dosemu

# default /etc/dosemu.users
install -m644 %SOURCE13 %buildroot%_sysconfdir/dosemu.users
# copy icons
mkdir -p %buildroot{%_niconsdir,%_liconsdir,%_miconsdir}
install -m644 %SOURCE2 %buildroot%_niconsdir/xdosemu.xpm
install -m644 %SOURCE3 %buildroot%_miconsdir/xdosemu.xpm
install -m644 %SOURCE4 %buildroot%_liconsdir/xdosemu.xpm
# adjusting docs
#mv %buildroot%_sysconfdir/%name/global.conf %buildroot%_defaultdocdir/%name-%version
install -m644 doc/HP1100-cp866-fonts-HOWTO.txt %buildroot%_defaultdocdir/%name-%version/

# Menu entry for xdosemu
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/x%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=X DOS emulator
Comment=DOS emulator running under X
Icon=xdosemu
Exec=xdosemu
Terminal=false
Categories=System;Emulator;
EOF

# Be compatible with package upgrade
mv %buildroot%_datadir/%name/drive_z %buildroot%_datadir/%name/freedos
ln -s freedos %buildroot%_datadir/%name/drive_z
# Provide default autoexec.bat and config.sys
install -m644 dist/{autoexec.bat,config.sys} %buildroot%_datadir/%name/freedos/

%pre
# Prevent alternative update during older package removal
[ -f %_altdir/dosemu-bin-nox.xml ] && rm -f %_altdir/dosemu-bin-nox.xml ||:
[ -f %_altdir/dosemu-bin-x.xml ] && rm -f %_altdir/dosemu-bin-x.xml ||:

%post plugins-x-sdl
# (making fontlist)
if [ -x %_x11bindir/mkfontdir ]; then
   (cd %_datadir/dosemu/Xfonts; %_x11bindir/mkfontdir)
fi

%preun plugins-x-sdl
# (removing fontlist)
if [ $1 = "0" -a -f %_datadir/dosemu/Xfonts/fonts.dir ]; then
   rm -f %_datadir/dosemu/Xfonts/fonts.dir
fi

%files
%config(noreplace) %_sysconfdir/dosemu.conf
%config(noreplace) %_sysconfdir/dosemu.users
%config(noreplace) %_sysconfdir/global.conf
%exclude %_bindir/xdosemu*
%_bindir/*
%dir %_localstatedir/dosemu
%dir %_datadir/dosemu
%exclude %_datadir/dosemu/Xfonts
%_datadir/dosemu/*
%doc %_defaultdocdir/%name-%version
%exclude %_man1dir/xdosemu.*
%doc %_man1dir/*
%dir %_libdir/%name/
%_libdir/%name/libplugin_gpm.so
%_libdir/%name/libplugin_term.so

%files plugins-x-sdl
%_bindir/xdosemu*
%_desktopdir/xdosemu.desktop
%_libdir/%name/libplugin_sdl.so
%_libdir/%name/libplugin_X.so
%_datadir/dosemu/Xfonts
%_niconsdir/xdosemu.xpm
%_miconsdir/xdosemu.xpm
%_liconsdir/xdosemu.xpm
%doc %_man1dir/xdosemu.*

%files plugins-sound
%_libdir/%name/libplugin_alsa.so
%_libdir/%name/libplugin_sndfile.so

%changelog
* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0.1-alt1.qa1
- NMU: converted menu to desktop file

* Thu Nov 05 2009 Grigory Batalov <bga@altlinux.ru> 1:1.4.0.1-alt1
- Update sources for last tagged version.
- Give error on low DOS memory map failure (vm.mmap_min_addr != 0).
- Specfile cleanup.

* Mon Aug 17 2009 Grigory Batalov <bga@altlinux.ru> 1:1.4.0-alt5
- Fix building with gcc4.4.

* Wed Mar 11 2009 Grigory Batalov <bga@altlinux.ru> 1:1.4.0-alt4
- Updated build requirements (libalsa-devel).

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt3.1.1
- NMU:
  * updated build dependencies

* Wed Oct 22 2008 Grigory Batalov <bga@altlinux.ru> 1:1.4.0-alt3.1
- Fix incorrect file creation in dexeconfig.c (Bart Oldeman).

* Tue Oct 21 2008 Grigory Batalov <bga@altlinux.ru> 1:1.4.0-alt3
- MFS: filename in upper case is checking as well.

* Fri Sep 05 2008 Grigory Batalov <bga@altlinux.ru> 1:1.4.0-alt2
- Build requirements update.
- Master 2.4 macro removed.
- Persent sign '%%' in changelog quoted.

* Tue May 15 2007 Grigory Batalov <bga@altlinux.ru> 1:1.4.0-alt1
- 1.4.0.
- Sound plugin added.
- Some new fonts.

* Mon Dec 04 2006 Grigory Batalov <bga@altlinux.ru> 1:1.3.4-alt1
- 1.3.4.
- Distribute X and SDL plugins (new feature) in separate packages.
- Check if plugin is necessary before load.
- No need for xdosemu.wrapper.
- Provide autoexec.bat and config.sys for FreeDOS.
- Various code updates from SVN.

* Wed Aug 10 2005 Grigory Batalov <bga@altlinux.ru> 1:1.3.2-alt4
- Fix upgrade to bin-x/bin-nox with triggers

* Thu Aug 04 2005 Grigory Batalov <bga@altlinux.ru> 1:1.3.2-alt3
- Split to dosemu, dosemu-bin-x and dosemu-bin-nox

* Thu Jun 09 2005 Grigory Batalov <bga@altlinux.ru> 1:1.3.2-alt2
- Patch against blinking character attribute (for Norton Diags
  and DOS Navigator)

* Mon May 23 2005 Grigory Batalov <bga@altlinux.ru> 1:1.3.2-alt1
- 1.3.2
- Build requirements were updated

* Wed Apr 06 2005 Grigory Batalov <bga@altlinux.ru> 1:1.2.2-alt4
- Another try to specify target CPU

* Tue Mar 01 2005 Grigory Batalov <bga@altlinux.ru> 1:1.2.2-alt3
- External/internal charset detection was fixed
- Menu group was changed to 'Applications/Emulators'
- Correct build arch was specified

* Thu Aug 26 2004 Grigory Batalov <bga@altlinux.ru> 1:1.2.2-alt2
- Tr arguments escaped in locale detection ( by voins@ )

* Tue Jul 13 2004 Grigory Batalov <bga@altlinux.ru> 1:1.2.2-alt1
- 1.2.2 release

* Sun Jul 04 2004 Grigory Batalov <bga@altlinux.ru> 1:1.2.1-alt2
- Patched to 1.2.1.2
- Contains filename unicode translation

* Thu Mar 11 2004 Grigory Batalov <bga@altlinux.ru> 1:1.2.1-alt1
- 1.2.1

* Thu Feb 19 2004 Grigory Batalov <bga@altlinux.ru> 1:1.2.0-alt1
- 1.2.0 release
- Patched to 1.2.0.1
- Xdosemu.wrapper updated

* Tue Oct 21 2003 Grigory Batalov <bga@altlinux.ru> 1:1.1.99-alt1
- 1.2.0rc1 aka 1.1.99.1

* Mon Jun 09 2003 Grigory Batalov <bga@altlinux.ru> 1:1.1.5-alt1
- 1.1.5

* Thu Apr 10 2003 Grigory Batalov <bga@altlinux.ru> 1:1.1.4-alt4
- Dosemu updated to 1.1.4.15 (so includes most previous patches)
- $_ttylocks set to /var/lock/serial

* Sun Jan 12 2003 Grigory Batalov <bga@altlinux.ru> 1:1.1.4-alt3
- Wrong links in dosemu-bin.tgz fixed
- Dosemu updated to 1.1.4.3
- Patches from SourceForge bugtracker included:
  + loop in coopthreads (ID #605551)
  + newlines in X selection (ID #666068)
  + MFS bug (ID #666518)
- PrtScr patch by Stas Sergeev
- Comcom patches by Clarence Dang and Stas Sergeev

* Wed Jan 08 2003 Grigory Batalov <bga@altlinux.ru> 1:1.1.4-alt2
- Another parsing method choosen
- System-wide cyrillic defaults removed

* Fri Dec 27 2002 Grigory Batalov <bga@altlinux.ru> 1:1.1.4-alt1.1
- Preun section fixed

* Sun Dec 22 2002 Grigory Batalov <bga@altlinux.ru> 1:1.1.4-alt1
- DOSEmu upgraded to 1.1.4
- Dosemu-freedos-bin.tgz moved to external package

* Fri Nov 01 2002 Grigory Batalov <bga@altlinux.ru> 1:1.1.3-alt5
- DOSEmu upgraded to 1.1.3.5
- Remaining patches from Stas Sergeev updated
- CP1251 support fixed

* Sun Aug 11 2002 Grigory Batalov <bga@altlinux.ru> 1:1.1.3-alt4
- DOSEmu updated to 1.1.3.2
- Patches from Stas Sergeev updated
- Kernel upgraded to 1.1.26b (build 2026b)
- FreeCOM (command.com) upgraded to 0.83 beta 44

* Thu Apr 11 2002 Grigory Batalov <bga@altlinux.ru> 1.1.3-alt3
- Fixed execution by root
- Removed systemwide fonts

* Mon Apr 08 2002 Grigory Batalov <bga@altlinux.ru> 1.1.3-alt2
- Specfile ceanup

* Thu Apr 04 2002 Grigory Batalov <bga@altlinux.ru> 1.1.3-alt1
- 1.1.3
- Added cp1251 layout and cp866 fonts

* Sat Jan 13 2001 AEN <aen@logic.ru> 1.0.1-ipl8mdk
- RE  adaptation

* Thu Oct 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-7mdk
- Fix gcc2.96  and various compilation problems.

* Wed Sep 20 2000 Francis Galiegue <fg@mandrakesoft.com> 1.0.1-6mdk
- Large icon is now transparent
- Let users at least do some things

* Fri Sep 15 2000 Francis Galiegue <fg@mandrakesoft.com> 1.0.1-4mdk
- More macros
- Added large icon
- fix %%post for menus

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.1-3mdk
- automatically added BuildRequires

* Thu Jul 20 2000 Francis Galiegue <fg@mandrakesoft.com> 1.0.1-2mdk
- BMacros
- hdimage.freedos is %%config(noreplace)

* Wed Jul 05 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.1-1mdk
- new release

* Mon Apr 10 2000 Francis Galiegue <fg@mandrakesoft.com> 1.0.0-5mdk

- Use new icons from LN
- Menu entry changed accordingly
- no icon for dosemu package, only for xdosemu

* Fri Apr 07 2000 Francis Galiegue <fg@mandrakesoft.com> 1.0.0-4mdk

- freedos doesn't depend on dosemu
- freedos provides dosimage
- Both xdosemu and dosemu require dosimage
- Doubt: is mtools a Requires or a BuildRequires ?

* Mon Apr 03 2000 Francis Galiegue <fg@mandrakesoft.com> 1.0.0-3mdk

- Added %%defattr for freedos

* Wed Mar 22 2000 Francis Galiegue <fg@mandrakesoft.com> 1.0.0-2mdk

- Rebuilt on kenobi

* Mon Mar 13 2000 Francis Galiegue <francis@mandrakesoft.com> 1.0.0-1mdk

- Version 1.0.0
- Changed group to match those of 7.1
- Build as non root
- Added menu entry for xdos
- spec file rework
- let spec-helper do its job
* Tue Dec 07 1999 Jerome Dumonteil <jd@mandrakesoft.com>
- added _tmppath in buildroot
- build release

* Wed Jul 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 0.99.13 version.

* Mon Jul 05 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Reinserting Mandrake adaptations for maintenance release.

* Mon Jun 07 1999 Dale Lovelace <dale@redhat.com>
- remove ^H's from documentation
- freedos version beta 2
- add autoexec.bat and config.sys for path
- add freedos utils
- add vim

* Wed Mar 31 1999 Preston Brown <pbrown@redhat.com>
- add dexe stuff back into package

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- remove hdimage.first link on deinstallation of freedos.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Wed Mar 17 1999 Matt Wilson <msw@redhat.com>
- fixed %%post and %%postun scripts
- version 0.99.10

* Tue Jan 12 1999 Matt Wilson <msw@redhat.com>
- version 0.99.6

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- version 0.98.1
- freedos has its own subpackage

* Wed Jun 24 1998 Alan Cox <alan@redhat.com>
- Wrote additional fixes for dexe overflow problem in parser.y

* Tue Jun 23 1998 Alan Cox <alan@redhat.com>
- Applied the security fixes from Hans Lerman

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- added DOS-C kernel and FreeDos utilities

* Thu Jan 29 1998 Cristian Gafton <gafton@redhat.com>
- updated spec file to include all the available commands
- uses a buildroot
- ship mkfatimage16, which is the only binary that can create a real hdimage
  file

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- Updated to 0.66.7
- Ported to glibc

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- Updated to 0.66.2.
- Removed /usr/bin/load-dosmods as we don't need emumod.o anymore

* Tue Mar 11 1997 Michael K. Johnson <johnsonm@redhat.com>
- Modify the default configuration file to use /var/lock in
  ascii format for lock files, as specified in the FSSTD/FHS.

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Assume vm86plus system call does not exist.
- N.B. This should be changed in a future version with a later kernel
  that supports that system call by default.
- Install the mkhdimage program.
