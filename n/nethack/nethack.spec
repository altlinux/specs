Name:           nethack
Version:        5.0.0
%define ver     500
%define Name    NetHack
Release:        alt1
Source:         %name-%ver-src.tgz
Summary:        Character Based RPG

URL:            http://www.nethack.org
License:        NGPL
Group:          Games/Adventure

%define luaver 5.4
# Automatically added by buildreq on Sat Jun 20 2026
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 libgcc15-devel libgpg-error libncurses-devel libtinfo-devel lua5.4 pkg-config python3 python3-base python3-dev sh5
BuildRequires: git-core groff-base libncursesw-devel libuuid-devel lua-devel lua-devel-static python3-module-setuptools
%filter_from_requires /^xset$/d

%description
NetHack 5.0 is an enhancement to the dungeon exploration game NetHack,
which is a distant descendent of Rogue and Hack, and a direct descendent
of NetHack 3.6.

%prep
%setup -n %Name-%version
LVR=`rpmquery --queryformat "%%{version}\n" lua5.4 | ( export IFS=.; read A B C; printf "%%d%%02d%%02d" $A $B $C )`
sed -i "s/#define NHL_VERSION_EXPECTED .*/#define NHL_VERSION_EXPECTED $LVR/" src/nhlua.c

%define luasrc lib/lua-%luaver/src
mkdir -p %luasrc
ln -s /usr/include/lua* /usr/include/laux* %luasrc
cp %_libdir/liblua.a %luasrc

%build
sys/unix/setup.sh sys/unix/hints/linux.500
%make_build LUA_VERSION=%luaver PREFIX=%prefix HACKDIR=%_localstatedir/%name

%install
%makeinstall_std LUA_VERSION=%luaver PREFIX=%buildroot%prefix HACKDIR=%buildroot%_localstatedir/%name
sed -i 's|%buildroot||' %buildroot%_gamesbindir/%name
install -D %buildroot%_localstatedir/%name/%name %buildroot%_gamesbindir/%name.bin
install -D %buildroot%_localstatedir/%name/recover %buildroot%_gamesbindir/%name.recover
ln -srf %buildroot%_gamesbindir/%name.bin %buildroot%_localstatedir/%name/%name
ln -srf %buildroot%_gamesbindir/%name.recover %buildroot%_localstatedir/%name/recover
mkdir -p %buildroot%_sysconfdir
ln -sr  %buildroot%_localstatedir/%name/sysconf %buildroot%_sysconfdir/%name

%files
%attr(02711, root, games) %_gamesbindir/%name.bin
%_gamesbindir/%name.recover
%_gamesbindir/%name
%attr(02775, root, games) %_localstatedir/%name/save
%dir %attr(0775, root, games) %_localstatedir/%name
%attr(0664, root, games) %_localstatedir/%name/?[^a]*
%_sysconfdir/%name

%changelog
* Sat Jun 20 2026 Fr. Br. George <george@altlinux.org> 5.0.0-alt1
- Total new version recreation for ALT

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.4.3-alt1.qa1
- NMU: rebuilt for debuginfo.

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
