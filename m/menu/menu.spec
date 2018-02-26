%define subversion %nil

Name: menu
Version: 2.1.41
Release: alt20

Group: System/Base
Summary: Menu system
License: GPL
URL: http://www.debian.org

PreReq: menu-messages > 0.2
Requires: sound_handler
Requires: menu-icons
Conflicts: menu-icons-crystalmdk
Conflicts: altlinux-menus <= 0.1.99

Source0: %{name}_%version%subversion.tar.bz2
#
Source4: %name.menu
#
Source6: %name.xinit
#
Source8: update-menus.sh
Source9: menu.filetrigger
#
Source11: menu-firsttime
#
Source15: menu-prepare-menus
Source16: menu-translate_menus
Source17: translate_xdg_categories
Source18: translate_menu_sections
#
Source21: xdg-menu-spec
Source22: xdg-desktop-entry-spec-dirs
Source23: xdg-desktop-entry-spec-apps
Source24: xdg-desktop-entry-spec-apps-postrun

# temporary need
Source100: menu-file2pot

# MDK
Patch1: menu-2.1.14-escaping-ALT.patch

# ALT
Patch11: menu-2.1.41-ALT.patch
Patch12: menu-2.1.14-alt-xvt.patch
Patch13: menu-2.1.14-alt-translate.patch
Patch14: menu-2.1.41-alt-substr-function.patch
Patch15: menu-2.1.41-alt-rpm.patch
#
Patch17: menu-2.1.20-alt-fix-compile.patch
Patch18: menu-2.1.23-alt-norpm.patch
Patch19: menu-2.1.27-alt-menumethod-arg-nopath-avail.patch
Patch20: menu-2.1.26-alt-create_stamp.patch
Patch21: menu-2.1.27-alt-remove_stamp.patch
Patch22: menu-2.1.35-alt-locate_icon-function.patch
Patch23: menu-2.1.41-alt-disable-menuentries.patch
Patch24: menu-2.1.41-alt-xdginput.patch

# Automatically added by buildreq on Mon Oct 29 2001
BuildRequires: gcc-c++ libpopt-devel libstdc++-devel zlib-devel

%description
The intent of this package is to streamline the menu's. For this purpose,
menu provides an "update-menus" command, that will read all installed menu
files (as provided by other packages in %_menudir), and run the frontents
for various window managers in %_sysconfdir/menu-methods to create startup files for
the window managers (or pdmenu).

The user and system admin can easily override the menu files on a by-user or
by-system bases.


%prep
%setup -q -n %name-%version
%patch1 -p1
#
%patch11 -p1 -b .ALT
%patch12 -p1
%patch13 -p1 -b .translate
%patch14 -p1 -b .substr
%patch15 -p1 -b .rpm
#
%patch17 -p1
#%patch18 -p1 -b .norpm
%patch19 -p1
%patch20 -p1 -b .stamp
%patch21 -p1 -b .stamp-rm
%patch22 -p1 -b .locate_icon
%patch23 -p1 -b .disable
%patch24 -p1 -b .xdg

for f in po/*.po
do
    sed -i "s|Dpkg|RPM|g" $f
    sed -i "s|dpkg|rpm|g" $f
done

./autogen.sh

%build
%add_optflags %optflags_shared
export CFLAGS="%optflags" CXXFLAGS="%optflags"
%configure
%make_build CFLAGS="%optflags" CXXFLAGS="%optflags"
%make_build -C po


%install
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_sbindir
mkdir -p %buildroot/%_mandir/{man1,man5}
mkdir -p %buildroot/%_sysconfdir/{menu,menu-methods,firsttime.d}
mkdir -p %buildroot/%_menudir/default
mkdir -p %buildroot/%_iconsdir/mini
mkdir -p %buildroot/%_sysconfdir/X11/xinit.d
mkdir -p %buildroot/var/lib/menu

install -p -m755 %SOURCE11 %buildroot/%_sysconfdir/firsttime.d/menu
#install -p -m755 %SOURCE15 %buildroot/%_sbindir/prepare-menus
install -p -m644 %SOURCE4 %buildroot/%_menudir/menu

%makeinstall
%makeinstall -C po

# install default menus
rm -rf %buildroot/%_menudir/default/*
rm -rf %buildroot/%_infodir/*


install -p -m0644 examples/{menu.h,menu.config} %buildroot/%_sysconfdir/menu-methods
install -p -m0644 %SOURCE16 %buildroot/%_sysconfdir/menu-methods/translate_menus
install -p -m0644 %SOURCE17 %buildroot/%_sysconfdir/menu-methods/translate_xdg_categories
install -p -m0644 %SOURCE18 %buildroot/%_sysconfdir/menu-methods/translate_menu_sections
#install -p -m0755 scripts/{su-to-root,wm-menu-config} %buildroot/%_sbindir
install -p -m0644 doc/*.1 %buildroot/%_mandir/man1
install -p -m0644 doc/*.5 %buildroot/%_mandir/man5

install -p -m0755 %SOURCE6 %buildroot/%_sysconfdir/X11/xinit.d/%name

install -pD -m755 %_sourcedir/update-menus.sh %buildroot%_sbindir/update-menus
install -pD -m755 %_sourcedir/menu.filetrigger %buildroot%_rpmlibdir/menu.filetrigger

mkdir -p %buildroot/%_sysconfdir/menu-methods
cat >%buildroot/%_sysconfdir/menu-methods/lang.h <<__EOF__
function lang()="en_US.UTF-8"
function languages()="en_US.UTF-8"
__EOF__
install -m 0755 %SOURCE21 %buildroot/%_sysconfdir/menu-methods
install -m 0755 %SOURCE22 %buildroot/%_sysconfdir/menu-methods
install -m 0755 %SOURCE23 %buildroot/%_sysconfdir/menu-methods
install -m 0755 %SOURCE24 %buildroot/%_bindir

mkdir -p \
    %buildroot/%_cachedir/applications \
    %buildroot%_cachedir/desktop-directories

%find_lang %name

# due to dependency on /etc/X11/xinit.d directory
%add_findreq_skiplist %_sysconfdir/X11/xinit.d/menu
sh -n %buildroot%_sysconfdir/X11/xinit.d/menu
# due to dependency on /etc/rc.d/init.d/function
%add_findreq_skiplist %_sysconfdir/firsttime.d/menu
sh -n %buildroot%_sysconfdir/firsttime.d/menu


%files -f %name.lang
%dir %_sysconfdir/menu-methods
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/menu-methods/lang.h
%config %_sysconfdir/menu-methods/menu*
%config %_sysconfdir/menu-methods/translate*
%config %_sysconfdir/menu-methods/xdg-desktop-entry-spec-apps
%config %_sysconfdir/menu
%config(noreplace) %_sysconfdir/X11/xinit.d/menu
%_sysconfdir/firsttime.d/*
#
%dir %_cachedir/applications
%dir %_cachedir/desktop-directories
#
%_bindir/*
%_sbindir/*
%_rpmlibdir/menu.filetrigger
%dir %_localstatedir/menu
%_menudir/*
%_man1dir/*
%_man5dir/*
%doc doc/{*html,README*,BUGS,menu.txt*} AUTHORS debian/changelog debian/copyright examples

%changelog
* Wed Jun 01 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.41-alt20
- bugfix: handle extra groups in desktop files (ALT#25702)

* Fri May 27 2011 Sergey V Turchin <zerg@altlinux.org> 2.1.41-alt19
- fix menu entry ignore message

* Wed May 25 2011 Sergey V Turchin <zerg@altlinux.org> 2.1.41-alt18
- improve menu entry ignore message (ALT#25638)

* Thu May 12 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.41-alt17
-  renamed Edutainment to Education, Amusement to Games

* Wed May 11 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.41-alt16
- bugfix: removed obsolete translations from translate_menus
  that caused pixmap loss

* Tue May 10 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.41-alt15
- bugfix: properly aligned TV submenu

* Sun May 01 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.41-alt14
- completely synchronized with nested freedesktop menu

* Mon Apr 25 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.41-alt13
- synchronized Development, Networking with freedestop menu

* Mon Apr 25 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.41-alt12
- synchronized Amusement, Science, Education with freedestop menu

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.41-alt11
- dropped obsolete %_bindir/soundwrapper
- Amusement/Simulation submenu (TORCS, ...)

* Mon Mar 28 2011 Sergey V Turchin <zerg@altlinux.org> 2.1.41-alt10
- ignore common appication menu-file entries

* Mon Jun 29 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.41-alt9
- fix to build

* Fri May 08 2009 Sergey V Turchin <zerg@altlinux.org> 2.1.41-alt8
- fill /etc/xdg/menus/applications-alt.menu

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 2.1.41-alt7
- fill default /etc/menu-methods/lang.h
- ignore update-menus exit state in filetrigger

* Thu Feb 19 2009 Sergey V Turchin <zerg at altlinux dot org> 2.1.41-alt6
- fix to use /etc/sysconfig/i18n::SUPPORTED variable for languages list

* Mon Feb 09 2009 Sergey V Turchin <zerg at altlinux dot org> 2.1.41-alt5
- /usr/share/applications/kde4 to desktop-files search paths list

* Fri Jan 30 2009 Sergey V Turchin <zerg at altlinux dot org> 2.1.41-alt4
- add /usr/share/applications/ to /usr/lib/rpm/menu.filetrigger

* Tue Nov 25 2008 Alexey Tourbin <at@altlinux.ru> 2.1.41-alt3
- /usr/sbin/update-menus: new helper script to update system menus
  (updates /etc/menu-methods/lang.h before running /usr/bin/update-menus)
- /usr/lib/rpm/menu.filetrigger: new post-transaction script for rpm
  (packages with menu files no longer need to invoke %%update_menus)
- /usr/bin/update-menus: disabled forking, enabled early exit on
  RPM_INSTALL_NAME (i.e. when running from within %%post-scripts)

* Mon Nov 10 2008 Sergey V Turchin <zerg at altlinux dot org> 2.1.41-alt2
- remove /etc/X11/xinit.d/* from requires generation list

* Mon Nov 10 2008 Sergey V Turchin <zerg at altlinux dot org> 2.1.41-alt1
- new version
- add fixes against gcc-4.3

* Wed Jun 25 2008 Anton Farygin <rider@altlinux.ru> 2.1.35-alt5.1
- create /etc/menu-methods/lang.h in firsttime script, also don't run post 
  script on system preparing stage (check DURING_INSTALL)

* Tue Oct 23 2007 Sergey V Turchin <zerg at altlinux dot org> 2.1.35-alt5
- improve desktop categories translation file

* Wed Oct 10 2007 Sergey V Turchin <zerg at altlinux dot org> 2.1.35-alt4
- extend icon search paths in locate_icon function

* Tue Oct 09 2007 Sergey V Turchin <zerg at altlinux dot org> 2.1.35-alt3
- fix locate_icon function to optimize

* Tue Oct 09 2007 Sergey V Turchin <zerg at altlinux dot org> 2.1.35-alt2
- add locate_icon function 

* Wed Aug 29 2007 Sergey V Turchin <zerg at altlinux dot org> 2.1.35-alt1
- new version
- separate menu sections translations into xdg to configuration file
- fix xdg categories translation (Amarok was in Multimedia/Video)

* Fri Sep 08 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.29-alt5
- fix .xpm icons coming from desktop-files

* Fri Sep 08 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.29-alt4
- fix some icons coming from desktop-files

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.29-alt3
- fix translate Utility;Translation; categories

* Mon Sep 04 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.29-alt2
- translate Debian menu sections to Freedestop categories

* Fri Sep 01 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.29-alt1
- new version
- fix skiping some desktop-files
- fix icons extentons coming form desktop-files

* Tue May 23 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.27-alt7
- improve cleaning desktop-file::Exec for menu-file::command

* Wed May 17 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.27-alt6
- fix xdg menu visibility in GNOME

* Wed Apr 12 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.27-alt5
- improve /etc/X11/xinit.d/menu
- fix modification time of ~/.menu-updates.stamp

* Mon Apr 03 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.27-alt4
- fix menu sections names in /etc/menu-methods/xdg-*

* Thu Mar 30 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.27-alt3
- remove --reply option from %_bindir/xdg-*

* Mon Mar 27 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.27-alt2
- remove stamp file when --remove
- add removemenu entry to /etc/menu-methods/xdg-*

* Thu Mar 23 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.27-alt1
- new version

* Wed Jan 18 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.26-alt6
- improve xdg desktop-file categories translation
- create stamp-file by update-menus instead of special menu-method

* Mon Dec 26 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.26-alt5
- fix for desktop-files without EOL at last line

* Fri Dec 23 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.26-alt4
- fix for Office freedesktop category

* Mon Dec 19 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.26-alt3
- wrap all unknown freedesktop sections to /Applications

* Fri Dec 16 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.26-alt2
- translate more freedesktop sections

* Mon Dec 12 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.26-alt1
- new version

* Tue Dec 06 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.25-alt10
- generate xdg menu to right place (/etc/xdg/menus,var/cache)
- bump %%release

* Fri Dec 02 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.25-alt5
- bump %%release

* Thu Nov 03 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.25-alt4
- fix inpit from desktop-files
- fix sections translation for desktop-files
- turn input from desktop-files on by default (remove --freedesktop option)

* Tue Sep 20 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.25-alt3
- add temporary --freedesktop option (experimental)

* Mon Jul 25 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.25-alt2
- add patch to don't require full path for --menumethod

* Thu Jun 30 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.25-alt1
- new version
- symlink soundwrapper to sound_wrapper.sh
- uncomment translations in translate_menus

* Fri Jun 17 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.23-alt4
- remove ownership of /etc/xdg

* Thu Jun 16 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.23-alt3
- fix coping .desktop files with spaces in xdg menu-method
- add menu section "Confuguration/ALT Linux" for alterator modules standalone mode.
- use rpm again because #990 was fixed in rpm >= 4.0.4-alt44

* Sat May 14 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.23-alt2
- don't apply patch for old style replacewith function
- remove unneeded .desktop-s after generating new in xdg-desktop-entry-spec-apps

* Wed Apr 13 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.23-alt1
- new version
- don't use rpm while #990 not fixed

* Thu Mar 31 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.22-alt3
- don't include menu-prepare-menus
- remove <KDELegacyDirs/> from freedesktop-menu-spec

* Tue Mar 22 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.22-alt2
- fix Type in *.directiry by freedesktop-* menumethods
- change "stop" icon to "altlinux" in freedesktop-* menumethods
- restore wm-specific filenames by freedesktop-desktop-entry-spec-apps

* Thu Mar 17 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.22-alt1
- new version
- add support for gnome and kde to freedesktop-* menumethods
- remove requires to menu-icons

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.20-alt1
- new version
- build with gcc3.4

* Tue Oct 12 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.18-alt1
- new version
- clean translation in /etc/menu-methods/translate_menus to show mistakes

* Fri Jun 18 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.14-alt1
- new version

* Thu Jun 17 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.9-alt11
- update /etc/menu-methods/translate_menus

* Thu Apr 01 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.9-alt10
- improve patch for rpm

* Tue Mar 23 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.9-alt9
- fix conflicts

* Mon Mar 22 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.9-alt8
- remove unsopported "-u" parameter from /etc/X11/xinit.d/menu 

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.9-alt7
- fix menu-method to prevent possible crash applications reading
  /etc/xdg/menus/applicatuions.menu during generation

* Wed Mar 17 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.9-alt5
- apply patch for rpm

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.9-alt4
- fix freedesktop menu-method to temporary support obsoleted
  kde_opt parameter

* Mon Mar 15 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.9-alt3
- fix file conflict with menu-icons-crystalmdk

* Tue Mar 09 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.9-alt2
- fix requires
- add freedesktop menu-method

* Thu Feb 26 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.9-alt1
- new version
- split messages and icons to other packages

* Thu Jan 22 2004 Sergey V Turchin <zerg at altlinux dot org> 2.1.5.1-alt1
- remove Serial and bump version until rpm fixed

* Wed Jan 21 2004 Sergey V Turchin <zerg at altlinux dot org> 1:2.1.5-alt1
- fix rpm locking (thanks avn@altlinux)
- bump serial to change release to alt

* Wed Sep 17 2003 Sergey V Turchin <zerg at altlinux dot org> 2.1.5-ipl85mdk
- updated Russian translation
  thanks Vitaly Lipatov <lav at altlinux>

* Fri Aug 01 2003 Sergey V Turchin <zerg at altlinux dot org> 2.1.5-ipl84mdk
- fix symlink /usr/share/icons/altlinux.png

* Mon Jul 07 2003 Sergey V Turchin <zerg at altlinux dot org> 2.1.5-ipl83mdk
- fix Russian translation
- add hack for early rpm database unlock

* Wed May 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 2.1.5-ipl82mdk
- update Russian translation
- add firsttime script

* Thu Feb 13 2003 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl81mdk
- any fix russian translation

* Mon Dec 23 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl80mdk
- fix soundwrapper script

* Fri Dec 20 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl79mdk
- update Russian translation
- fix soundwrapper script
- add new function substr(string, positon, size)
  10x 2 ldv@altlinux.org

* Thu Nov 14 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl78mdk
- update Russian translation
- update other translations from MDK

* Fri Oct 18 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl77mdk
- fix dependencies

* Mon Oct 14 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl76mdk
- fix dependencies

* Mon Oct 14 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl75mdk
- add png icons

* Mon Sep 16 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl74mdk
- update Ukrainian translation
  10x 2 mike@altlinux.ru

* Thu Sep 12 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl73mdk
- update Patch0 from cooker

* Tue Sep 10 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl72mdk
- rebuild with gcc 3.2
- split icons to external package

* Tue Jun 04 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl71mdk
- update Russian translation
- add Edutainment section

* Mon Apr 15 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl70mdk
- update Russian translation

* Fri Apr 05 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl69mdk
- fix lost applying Patch6

* Tue Apr 02 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl68mdk
- fix Patch5 . Thnx Alexey Morozov <morozov@novosoft.ru>

* Tue Mar 19 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl67mdk
- update translations from cooker

* Mon Mar 04 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl66mdk
- fix execution of x-terminal-emulator (Patch6)

* Tue Feb 12 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl65mdk
- fix Patch5
- sync with cooker
- fix some translations

* Wed Jan 09 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl64mdk
- fix Patch5

* Tue Jan 08 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl63mdk
- apply Patch6

* Sat Dec 29 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl62mdk
- add Source15 (prepare-menus)

* Wed Dec 19 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl61mdk
- fix translation

* Fri Dec 14 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl60mdk
- cleanup %%post
- fix translation
  thanx ldv, inger

* Fri Dec 14 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl59mdk
- improve %%post

* Thu Dec 13 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl58mdk
- fix %%post

* Tue Dec 11 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl57mdk
- move support list of languages from $RPM_INSTALL_LANG to $LANGUAGE
- fix languages list for KDE

* Thu Nov 08 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl56mdk
- fix translation of menu entries

* Thu Nov 08 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl55mdk
- sync sources with cooker

* Thu Nov 08 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl54mdk
- build with rpm4

* Wed Oct 31 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl53mdk
- fix %%post script

* Mon Oct 29 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl52mdk
- any fix in ru translation

* Mon Sep 10 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.1.5-ipl51mdk
- Updated translates

* Mon Sep 10 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.1.5-ipl50mdk
- Updated icons

* Sun Sep 09 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.1.5-ipl49mdk
- Updated translations
- Added menu.menu file from lates Mandrake Cooker

* Fri Jun 29 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.1.5-ipl48mdk
- fixed encode_translate function
- updated ru.po

* Mon Jun 18 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.1.5-ipl47mdk
- FIxed russian translation

* Wed Apr 04 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.5-ipl46mdk
- fixed $lang select for KDE by %post

* Thu Mar 16 2001 AEN <aen@logic.ru> 2.1.5-ipl45mdk
- ukrainian po fixed

* Wed Dec 06 2000 AEN <aen@logic.ru>
- rebuild w/o kdelibs-sound
* Thu Nov 30 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.5-ipl43mdk
- Added "Requires: rpm >= 3.0.6-ipl9mdk".
- RE adaptions.

* Wed Oct 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.5-43mdk
- Fix some gcc2.96 wheirdness.
- Fix compile for rpmv4.

* Wed Oct 18 2000 Vincent Saugey <vince@mandrakesoft.com> 2.1.5-42mdk
- Add a fonction for encoding self made menu entry into different charset

* Tue Oct 10 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.5-41mdk
- Recompile for the new libstdc++.

* Tue Oct 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.1.5-40mdk
- use "$@" instead of $@ in soundwrapper

* Tue Oct 10 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-39mdk
- use $@ instead of $* in soundwrapper.
- updated po from CVS.
- removed patch for typo in fr (it must be done in the menu-messages cvs module).

* Mon Oct  9 2000 Montel Laurent <lmontel@mandrakesoft.com> 2.1.5-38mdk
- fix typo in fr.po

* Fri Oct  6 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.1.5-37mdk
- make soundwrapper esd-aware

* Fri Oct  6 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-36mdk
- added support for RPM_INSTALL_LANG=all

* Thu Oct  5 2000 Vincent Saugey <vince@mandrakesoft.com> 2.1.5-35mdk
- Fix in encode menu fail is no po found

* Wed Oct  4 2000 Vincent Saugey <vince@mandrakesoft.com> 2.1.5-34mdk
- encode_translate get po charset to make conversion.

* Wed Oct  4 2000 Vincent Saugey <vince@mandrakesoft.com> 2.1.5-33mdk
- Add encode_tranlate() function to language.

* Tue Oct  3 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-32mdk
- corrected prefix of locales.

* Tue Oct  3 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-31mdk
- updated po from CVS.
- merged patches.
- fork in background must be better handled.

* Fri Sep 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.1.5-30mdk
- add "soundwrapper" shell script to launch apps that require sound
  through the good wrapper

* Fri Sep 29 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-29mdk
- really include mo (buggy %%find_lang call).
- updated po from CVS.
- fork to background if -n is not used.

* Tue Sep 26 2000 Daouda Lo <daouda@mandrakesoft.com> 2.1.5-28mdk
- replace ICQ section by Instant Messaging.

* Fri Sep 22 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-27mdk
- updated locales from CVS.

* Mon Sep 18 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-26mdk
- updated the translations.
- added logic to automatically run update-menus as user when a system menu has changed.

* Thu Aug 31 2000 Vincent Saugey <vince@mandrakesoft.com> 2.1.5-25mdk
- Reinsert /etc/menu directory for system menu (who's suck ????)

* Mon Aug 28 2000 David BAUDENS <baudens@mandrakesoft.com> 2.1.5-24mdk
- Fix few bugs in menu entries

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-23mdk
- automatically added BuildRequires

* Mon Aug 07 2000 David BAUDENS <baudens@mandrasoft.com> 2.1.5-22mdk
- Fix macros & BM disaster (please be carreful that ALL FILES are included
  in the new package when you use macros and make BM)
- Add missing documentation

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.1.5-21mdk
- BM

* Tue Jul 11 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>  2.1.5-20mdk
- added postun scripts
- more macros
- Stefan van der Eijk <s.vandereijk@chello.nl> :
	* makeinstall macro
	* macroszifications

* Wed May 10 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-19mdk
- po updates for fr, lt, ro and sk.

* Tue May  9 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-18mdk
- new po.

* Sat May  6 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-17mdk
- new po.

* Thu May  4 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-16mdk
- fix bad chmod on dir.

* Thu May  4 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-15mdk
- pass environment to menu methods.
- catch endofline error to try to continue.

* Thu May  4 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-14mdk
- new po.
- do a chmod 644 on new file to allow menu to work on security level 5.

* Fri Apr 28 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-13mdk
- added icons for 16, 32 and 48.

* Wed Apr 26 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-12mdk
- updated po.
- corrected typos in menu entries.

* Wed Apr 19 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-11mdk
- new po.

* Tue Apr 18 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-10mdk
- added locales.

* Tue Apr 18 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-9mdk
- exit if DURING_INSTALL is set.

* Thu Apr 13 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-8mdk
- added new icons.
- removed default menus in Apps.

* Mon Apr 10 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-7mdk
- added icons for menu sections.
- added order in sections.

* Wed Apr  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.5-6mdk
- By default rootmenu are /Mandrake not Debian.

* Mon Apr  3 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-5mdk
- 2.1.5-4 author release: added also_run feature.
- doc update.
- fix for toplevel entry.
- tanslate debian menu sections to mandrake ones.

* Fri Mar 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.5-4mdk
- Fix default structure.

* Wed Feb 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.5-3mdk
- More mandrake adpatation in default config.

* Wed Feb 23 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-2mdk
- added documentation.

* Mon Feb 21 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1.5-1mdk
- mandrake adaptation

# end of file
