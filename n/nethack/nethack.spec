Name:           nethack
License:        NetHack General Public License
Group:          Games/Adventure 
Version:        3.4.3
%define ver	343
Release:        alt1
Summary:        Character Based RPG
Source0:        %name-%ver-src.tar.bz2
Source1:        SuSE.tar.bz2
Patch0:         %name-config.patch
Patch1:         %name-decl.patch
Patch2:         %name-misc.patch
Patch3:         %name-syscall.patch
Patch5:         %name-gzip.patch
URL:            http://www.nethack.org/
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sun Jun 17 2007
BuildRequires: flex libncurses-devel
%add_findreq_skiplist %_libdir/nethack/recover-helper

%description
This RPG is somewhat cryptic with its character based output. But a
true fan knows and appreciates its complexity and possibilities.

This package contains the text interface.



Authors:
--------
    Stephen L. Ericksen <stevee@cc.usu.edu>

%prep
%setup
%patch0
%patch1
%patch2
%patch3
%patch5
tar xvf %SOURCE1
#sed -i "s/^CFLAGS.*/& $RPM_OPT_FLAGS/" sys/unix/Makefile*

%build
# create symlinks to makefiles
sh sys/unix/setup.sh 1
# tty
make clean
cp -f SuSE/tty/config.h include/config.h
cp -f SuSE/tty/Makefile.src src/Makefile
make nethack CFLAGS="$RPM_OPT_FLAGS -I../include -D_GNU_SOURCE"
cp dat/options dat/options.tty
# doc, data, recover...
make Guidebook data oracles options quest.dat rumors dungeon spec_levs check-dlb x11tiles pet_mark.xbm rip.xpm mapbg.xpm
cd util && make CFLAGS="$RPM_OPT_FLAGS -I../include -D_GNU_SOURCE" recover

%install
rm -rf $RPM_BUILD_ROOT
# direcotries
install -d $RPM_BUILD_ROOT%_libdir/nethack/
install -d $RPM_BUILD_ROOT%_gamesbindir
install -d $RPM_BUILD_ROOT%_datadir/games/nethack
install -d $RPM_BUILD_ROOT/%_mandir/man6/
# game directory
install -d $RPM_BUILD_ROOT/var/games/nethack/save
touch $RPM_BUILD_ROOT/var/games/nethack/perm \
        $RPM_BUILD_ROOT/var/games/nethack/record \
        $RPM_BUILD_ROOT/var/games/nethack/logfile
chmod -R 0775 $RPM_BUILD_ROOT/var/games/nethack
# binaries 
install -m 2755 src/nethack.tty $RPM_BUILD_ROOT%_libdir/nethack/
# scripts
for STYLE in tty ; do 
    install -m 755 SuSE/$STYLE/nethack.sh $RPM_BUILD_ROOT%_gamesbindir/nethack.$STYLE
    if [ -r SuSE/$STYLE/nethack-tty.sh ] ; then
        install -m 755 SuSE/$STYLE/nethack-tty.sh $RPM_BUILD_ROOT%_gamesbindir/nethack.tty.$STYLE
    fi
done
# options
install -m 644 dat/options.tty $RPM_BUILD_ROOT%_libdir/nethack/
# man pages
install -m 644 doc/{nethack,lev_comp,dlb,dgn_comp,recover}.6 $RPM_BUILD_ROOT/%_mandir/man6/
# doc
mkdir -p $RPM_BUILD_ROOT/%_defaultdocdir/nethack
install -m 644 doc/Guidebook.{tex,txt} $RPM_BUILD_ROOT/%_defaultdocdir/nethack
cd doc
tar cvfj $RPM_BUILD_ROOT/%_defaultdocdir/nethack/fixes.tar.bz2 fixes*
cd ..
chmod 644 $RPM_BUILD_ROOT/%_defaultdocdir/nethack/fixes.tar.bz2
install -m 644 dat/license $RPM_BUILD_ROOT/%_defaultdocdir/nethack
install -m 644 SuSE/README.SuSE $RPM_BUILD_ROOT/%_defaultdocdir/nethack
# common data
for file in nhdat x11tiles pet_mark.xbm rip.xpm mapbg.xpm license;
do 
  install -m 644 dat/$file  $RPM_BUILD_ROOT%_datadir/games/nethack/
done
# configs
install -m 755 -d $RPM_BUILD_ROOT%_sysconfdir/nethack
for STYLE in tty ; do 
    install -m 755 SuSE/$STYLE/nethackrc $RPM_BUILD_ROOT%_sysconfdir/nethack/nethackrc.$STYLE
done
# main launcher script
install -m 755 SuSE/nethack $RPM_BUILD_ROOT%_gamesbindir/
# recover helper
install -m 755 SuSE/recover-helper $RPM_BUILD_ROOT%_libdir/nethack/
# utils
install -m 755 util/{dgn_comp,dlb,lev_comp,makedefs,recover,tile2x11} $RPM_BUILD_ROOT%_libdir/nethack/
#install -m 755 util/tilemap $RPM_BUILD_ROOT%_libdir/nethack/
# x11 app-defaults
#mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults
#install -m 644 win/X11/NetHack.ad $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/NetHack
# x11 font
#/usr/bin/X11/bdftopcf -o nh10.pcf win/X11/nh10.bdf
#mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc/
#install -m 644 nh10.pcf $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc/
#gzip $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts/misc/nh10.pcf
# the font is added into fonts.dir by SuSEconfig.fonts

%post
#%%run_permissions
#
%verifyscript
#%%verify_permissions -e %_libdir/nethack/nethack.tty

%files
%attr(02711,games,games) %_libdir/nethack/nethack.tty
%_libdir/nethack/options.tty
%_gamesbindir/nethack*.tty
%config %_sysconfdir/nethack/nethackrc.tty
%dir %_sysconfdir/nethack
%dir %_libdir/nethack
%_datadir/games/nethack
%_libdir/nethack/recover-helper
%_libdir/nethack/dgn_comp
%_libdir/nethack/dlb
%_libdir/nethack/lev_comp
%_libdir/nethack/makedefs
%_libdir/nethack/recover
%_libdir/nethack/tile2x11
#%_libdir/nethack/tilemap
%_defaultdocdir/nethack
%_mandir/man6/*
%attr(-,games,games) /var/games/nethack
%_gamesbindir/nethack

%changelog
* Sun Jun 17 2007 Fr. Br. George <george@altlinux.ru> 3.4.3-alt1
- Initial build for ALT

* Tue Feb 14 2006 - mmarek@suse.cz
- use /usr/lib/nethack instead of /usr/%%_lib/nethack, because we
  don't install any libraries there and /etc/permissions* contains
  /usr/lib/nethack
  [#140336]
- build as user
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Fri May 06 2005 - sbrabec@suse.cz
- Fixed duplicated declarations.
- Build with correct CFLAGS.
* Thu Jan 20 2005 - ro@suse.de
- drop nethack-qt, gnomehack, xnethack
- re-unite nethack and nethack-common
* Wed Nov 10 2004 - ro@suse.de
- reduced neededforbuild
* Thu Sep 30 2004 - sbrabec@suse.cz
- Biarch path fix (#31938).
* Mon Feb 09 2004 - sbrabec@suse.cz
- Updated to version 3.4.3.
* Wed Nov 05 2003 - ro@suse.de
- package according to permissions.secure and add run_permissions
* Mon Sep 01 2003 - sbrabec@suse.cz
- Updated to version 3.4.2 (bug #29803).
* Thu Jun 12 2003 - coolo@suse.de
- fiddle with %%_docdir
* Sat Jun 07 2003 - coolo@suse.de
- compile with latest Qt
- remove buildroot before installing
- package /usr/games/nethack (as installed explicitly)
* Thu Feb 27 2003 - sbrabec@suse.cz
- Use gzip instead of compress for compression (bug #22454).
* Wed Feb 26 2003 - sbrabec@suse.cz
- Security fix (local buffer overflow).
* Mon Feb 17 2003 - sbrabec@suse.cz
- Removed -mminimal-toc from spec file for PPC, since it is now RPM
  default (bug #23266).
* Wed Oct 23 2002 - mcihar@suse.cz
- enabled data librarian
- added X11 version
- Qt version renamed to nethack-qt (from xnethack) and built against qt3
  (qt-mt)
- different styles (tty/Qt/Gnome/X11) do not conflict
- new lanching script nethack, ui can be chosen by environment variable
  HACKSTYLE=x11/qt/gnome/tty
- cleaned neededforbuild
- included some tools into nethack-common (was nethack_data)
* Fri Sep 27 2002 - ro@suse.de
- Added alsa alsa-devel to neededforbuild (esound)
* Thu Sep 12 2002 - kukuk@suse.de
- Add missing obsolete from package rename
* Wed Aug 21 2002 - mcihar@suse.cz
- added PreReqs
* Sun Jul 28 2002 - kukuk@suse.de
- change group game to games
* Tue Jul 16 2002 - mcihar@suse.cz
- nh_data renamed to nethack_data
- nh_binary renamed to nethack_binary
- updated nethack_data description to mention gnomehack also
* Mon Jul 01 2002 - olh@suse.de
- build with -mminimal-toc on ppc64
* Thu Jun 06 2002 - prehak@suse.de
- fixed for ia64
  - using of macro _syscall3 replaced with ordinary system call
  - kernel header linux/unistd.h replaced with unistd.h
* Fri May 31 2002 - prehak@suse.de
- fixed to build on x86_64 and s390x
* Thu May 16 2002 - prehak@suse.cz
- updated to new version 3.4.0
* Mon Jan 21 2002 - tcrhak@suse.cz
- fixed include dir path for gnome
* Mon Jan 14 2002 - tcrhak@suse.cz
- moved static data to /usr/share/games/nethack
- and executables to /usr/lib/nethack (FHS 2.2)
* Fri Nov 09 2001 - ro@suse.de
- use qt-devel-packages in neededforbuild
* Mon Sep 03 2001 - schwab@suse.de
- Fix conflicting declaration.
* Sun Mar 18 2001 - ro@suse.de
- fixed neededforbuild
* Thu Mar 08 2001 - uli@suse.de
- added xf86 to neededforbuild
- replaced static GTK include paths with "gtk-config --cflags"
* Thu Jan 25 2001 - vinil@suse.cz
- upgraded to 3.3.1
- difs split and cleanup
- gnome version included
* Tue Jan 23 2001 - schwab@suse.de
- Fix conflicting declarations.
* Thu Nov 30 2000 - ro@suse.de
- neededforbuild += liblcms
* Fri Nov 17 2000 - ro@suse.de
- fixed neededforbuild: += libmng-devel
* Sun Nov 05 2000 - kukuk@suse.de
- adjust neededforbuild
* Fri Oct 20 2000 - ro@suse.de
- added libmng to neededforbuild
* Tue Aug 22 2000 - vinil@suse.cz
- mesa, mesasoft added to neededforbuild
* Tue Jul 18 2000 - vinil@suse.cz
- Alt (Meta) key should work now in tty version, too
  (are there any problems with it?)
* Fri Jun 23 2000 - vinil@suse.cz
- doc files relocated
* Tue Jun 20 2000 - vinil@suse.cz
- major file relocation
- nethackrc demofile added
* Tue Jun 13 2000 - vinil@suse.cz
- nethack and xnethack are two frontends now
- nh_data is needed for both
* Sat Feb 19 2000 - kasal@suse.cz
- upgraded to 3.3.0
- added BuildRoot
- moved manpages to /usr/share/man
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Wed Jun 11 1997 - rj@suse.de
- new version 3.2.2
