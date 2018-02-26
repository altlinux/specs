%define qtdir %_qt3dir
%define kdedir %_K3prefix

Name: kpowersave
Version: 0.7.3
Release: alt6

Group: Graphical desktop/KDE
Summary: KDE Frontend to powersave Package, Battery Monitor and General Power Management Support
License: LGPL
URL: http://www.kde-apps.org/content/show.php?content=29295

Packager: Damir Shayhutdinov <damir@altlinux.ru>

ExclusiveArch: %ix86 x86_64 ia64

Requires: powersave >= 0.9.23
Requires: %{get_dep kdelibs}

Source: %name-%version.tar.bz2

Patch0: kpowersave-0.7.2-alt-screenlock.patch
Patch1: tde-3.5.13-build-defdir-autotool.patch
Patch2: kpowersave-shutdown.patch
Patch3: cvs-auto_version_check.patch

# Automatically added by buildreq on Tue May 13 2008
BuildRequires: gcc-c++ imake kdelibs-devel libXScrnSaver-devel libXt-devel libXtst-devel libdbus-tqt-devel libhal-devel libjpeg-devel xml-utils

%description
The package provides battery monitoring and suspend/standby triggers.
It is based on the powersave package and therefore supports APM and
ACPI. Together with the powersave package and the YaST Powermanagement
module it is the preferred package that should be used for battery
monitoring and control of power management related tasks. See powersave
package for additional features such as CPU frequency scaling(SpeedStep
and PowerNow) and more.

Authors:
--------
    Thomas Renninger (trenn@suse.de, mail@renninger.de)
    Danny Kukawka (dkukawka@suse.de, danny.kukawka@web.de)

#debug_package
%prep
%setup -qn %name-%version
#patch0 -p1
%patch1
%patch2
%patch3

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%kdedir

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

%K3configure --disable-rpath

%make_build

%install
%K3install
%find_lang %name

%files -f %name.lang
%doc README AUTHORS ChangeLog COPYING INSTALL
%doc %_K3doc/*/kpowersave/
%_K3bindir/%name
%_K3lib/*
%_libdir/libkdeinit_%name.so*
%_K3apps/%name
%_K3start/%name-autostart.desktop
%_K3conf/%{name}rc
%_kde3_iconsdir/*/*/apps/%name.png
%_K3xdg_apps/%name.desktop
%_K3i18n/*

%changelog
* Thu Apr 26 2012 Roman Savochenko <rom_as@altlinux.ru> 0.7.3-alt6
- Automake version is fixed to 1.11.5 detect.
- Shutdown is fixed by replace DCOP ksmserver command "logout 0 2 2" by "logout 0 2 -1".

* Sun Mar 11 2012 Roman Savochenko <rom_as@altlinux.ru> 0.7.3-alt5
- Shutdown is fixed by replace DCOP ksmserver command "logout 0 2 2" by "logout 0 2 1".

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.7.3-alt4
- Build for TDE 3.5.13 release

* Thu Aug 27 2009 Damir Shayhutdinov <damir@altlinux.ru> 0.7.3-alt3
- Fixed build with new autotools

* Tue May 13 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.7.3-alt2
- Updated BuildRequires

* Sat Mar 29 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.7.3-alt1
- Updated to 0.7.3

* Tue Jan 15 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.7.2-alt2
- Fix build with new autotools

* Fri Apr 27 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Thu Feb 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.7.2-alt0.pre
- Updated kpowersave to 0.7.2pre version from https://bugzilla.novell.com/show_bug.cgi?id=225212 (#10803).
- Removed ru.po from package - use upstream's one instead.

* Thu Jan 18 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.7.1-alt3
- Added a patch for correct screen lock (#10640).

* Thu Dec 28 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.7.1-alt2
- Rebuilt with new dbus.

* Mon Dec 11 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.7.1-alt1
- New version

* Fri Jul 15 2005 Sergey V Turchin <zerg at altlinux dot org> 0.4.5-alt1
- built for ALT

* Fri Jun 24 2005 - dkukawka@suse.de
- implemented new feature:
- configurable sound for battery warning states, ac events and
  autosuspend
- fixed bug within parsing messages for progress dialog.
- updated (code-)documentation
- updated README for compile kpowersave on other distributions
* Thu May 26 2005 - dkukawka@suse.de
- added new menu entry to disable autosuspend trough applet-menu if
  autosuspend activated on the current scheme, if not the menu-item
  is not visible
- fixed bug with initalise import of global blacklist to scheme
  blacklist. Now the imported blacklist is maked as changed.
- cleaned up and changed size policy related values in the
  configure dialog
* Wed May 25 2005 - dkukawka@suse.de
- added suse-release to neededforbuild to detect the correct
  distribution in autobuild system
* Tue May 24 2005 - dkukawka@suse.de
- added scheme specific autosuspend blacklist
- changed and improved config dialog:
- added autosuspend blacklist edit dialog and button to general
  settings
- added enable scheme specific autosuspend blacklist and edit
  dialog
- redesigned scheme settings page
- added icons to schemes in scheme settings page
- added fix/workaround for bug #85611
- changed params of autosuspend->start() to QStringList
* Fri May 13 2005 - dkukawka@suse.de
- implemented blacklist for autosuspend (if a program in the
  blacklist is detected as running autosuspend is stopped)
- added dcop interface function to stop/start autosuspend
- updated documentation
* Tue May 10 2005 - dkukawka@suse.de
- implemented autosuspend (detect userinactivity from X-Server)
* Tue May 10 2005 - dkukawka@suse.de
- fixed bug #82880
* Sun May 08 2005 - dkukawka@suse.de
- additional fix for bug #81681
* Fri May 06 2005 - dkukawka@suse.de
- fixed bug #81681:
- added a new suspend dialog which is now toplevel
- added icons to dialog for the related suspend/standby
- updated documentation
* Wed Apr 13 2005 - dkukawka@suse.de
- fixed for gcc 4.0
* Mon Mar 21 2005 - dkukawka@suse.de
- added updated translation file
- fixed string in en_US
* Fri Mar 18 2005 - dkukawka@suse.de
- fixed bug #73810, now we restart XScreensaver to be shure that
  the user default settings are set
- fixed bug #73805 (closed file descriptor leak)
- updated Changelog and code doc
- updated version to final 0.4.0
* Thu Mar 17 2005 - dkukawka@suse.de
- implemented progressbar for powersave suspend
- removed 'Disable Screensaver' from menu (and also all related
  functions and variables) because this is not needed anymore since
  the user can change scheme related screensaver settings
- updated documentation
* Wed Mar 16 2005 - dkukawka@suse.de
- fixed bug #72939, now on quit reset KDE settings
- fixed setSchemesettings(), now we check for KDE befor reset to KDE
  settings
- updated documentation, Changelogs and version strings
* Tue Mar 15 2005 - dkukawka@suse.de
- added new [zh_CN, zh_TW] and updated translation files
- fixed blocker bug #72846
- fixed bug within the activation of widgets in the configure dialog
- fixed text on labels in configure dialog
- fixed bug in load KDE settings from configfile, to prevent wrong
  settings if user changed KDE settings in KDE Control Center while
  KPowersave is running
- updated version to 0.3.99 for the final release in SuSE 9.3final
  (should be 0.4)
* Mon Mar 14 2005 - dkukawka@suse.de
- updated icon for kmenu (now 16x16 and 32x32 the same)
- added new [en_US, pa, uk] and updated translation files
- fixed lable width in configure dialog
- fixed bug, now kcmdisplayrc is loaded for KDE DPMS settings
* Fri Mar 11 2005 - dkukawka@suse.de
- undo change in QPowersaveClientSocket::connect() depends on
  undo in last powersave fixes
* Thu Mar 10 2005 - dkukawka@suse.de
- fixed bugs #71955 and #71875 (kpowersave related part and needed
  adaptations to changed powersave)
- removed unneeded functions and declarations
- added errormessages to do_setSpeedPolicy() and
  lockscreen_on_lidcloseEvent()
* Wed Mar 09 2005 - dkukawka@suse.de
- Fixed bug #71192, changed sequence of enable/disable the
  widget/items for DPMS settings.
- added new functions to dcop interface: allowed_sleepingStates()
  and list_schemes()
* Mon Mar 07 2005 - dkukawka@suse.de
- fixed bug #71016
- added dcop interfaces for lock screen, suspend/standby and
  to get information about current scheme and CPUFreqPolicy
- fixed bug: now the configure entry in kpowersave isn't displayed
  if the powersavedaemon is not running
- fixed message strings
- updated documentation
* Fri Mar 04 2005 - dkukawka@suse.de
- Added enterEvent( QEvent * ) eventhandler to reduce polling. Now
  the tooltip updated only if this event is triggered for the
  kpowersace systray/kicker icon.
* Fri Mar 04 2005 - dkukawka@suse.de
- implemented 'AutostartNeverAsk' to quell the dialog on exit
- added and implemented configure entry for 'lock screen method'
  Now the user can configure which method (KScreensaver,
  XScreensaver, Xlock, or autoselected) used for lock on suspend/
  standby and lid closed
- full implementation of powersave client notification, we now
  need only poll active for information if powersave died
- different cleanups
- updated code documentation and additional doc files
* Sun Feb 27 2005 - dkukawka@suse.de
- removed unneeded config values from kpowersaverc
- implemented all functions to read the general, scheme and KDE
  settings from the kpowersave/KDE configuration file(s)
- added functions for 'lock screen' and 'blank only screen'
- integrated screensaver and lock settings to kpowersave.cpp
* Fri Feb 25 2005 - dkukawka@suse.de
- fixed configure dialog for better look with bigger fonts
- fix/workaround for the kpowersave related part of bug #66502 on
  Workstations
- fixed dialog bug, now the user can open only one configure
  dialog at the same time
- changed displayed application name from kpowersave to KPowersave
- added function to load the general settings in the dialog
- added 'user-inactivity-actions' to dialog, configfiles and menu.
  This is atm only 'dummy' and not visible for the user.
- added autostart options to dialog and a new option to prevent the
  dialog on exit kpowersave
- updated the default config file
- updated strings for translation
* Tue Feb 22 2005 - dkukawka@suse.de
- updated configure dialog
- changed configure dialog, renamed widgets, integrated schemes and
  general config section
- changed call of the configure dialog, now kpowersave not blocked
  while dialog is open
- added different slots and logic to disable/enable widgets
- added load and store the configuration
- added configoptions and funtions to make 'lock screen'
  configureable by user
- added default configfile
- updated documentation
* Mon Feb 21 2005 - trenn@suse.de
- enable notification popup through daemon
* Tue Feb 15 2005 - dkukawka@suse.de
- update to 0.3.10:
- added configure dialog to make user specific configuration
  possible
* Sat Jan 22 2005 - ro@suse.de
- added resmgr to neededforbuild
* Mon Jan 17 2005 - dkukawka@suse.de
- remove some xscreensaver related (unneeded) code in screen.cpp
- remove some unused variables and function declaration in
  pdaemon.cpp
- added full code documentation for doxygen and changed the settings
  in the Doxyfile
- fixed bug #49844 user selected 'disable screensaver' prefered if
  the AC adapter is plugged out
- fixed bug #49845 now XScreensaver also detected under KDE
- fixed bug #49632 in po-files (correct a wrong path in translation
  files)
* Tue Dec 21 2004 - dkukawka@suse.de
- added new cs-translation. File was empty (since SUSE 9.2final)
  in the cvs-tree (unknown why) Bug #49445
* Wed Dec 15 2004 - dkukawka@suse.de
- added new icons to the applet for stand-by, suspend* and
  the different schemes
- modified kpowersave desktop icon
- changed some code in kpowersave, fixed some little bugs
  (not reported), removed some unneeded or unreachable code
* Mon Dec 13 2004 - dkukawka@suse.de
- implemented new icons/iconfunctions for better better user
  interaction if the battery is in the different states WARNING,
  LOW, CRITICAL. Now the icon background flashes every second
  orange [WARNING,LOW] or red [CRITICAL]
- changed Icons (removed some white pixel)
* Sat Dec 11 2004 - dkukawka@suse.de
- fixed Bug #48202
* Tue Oct 12 2004 - dkukawka@suse.de
- fix Bugzilla #47113 (hopefully), remove some debug messages,
  change version
- fix problem from Bugzilla #46685, now kpowersave check really if
  scheme is successfully set by powersaved
* Mon Oct 04 2004 - dkukawka@suse.de
- fixed bug in screensaver menuentry, now only checked on start if
  screensaver and dpms off or if screensaver off and no dpms
  support by machine -> see: Bugzilla #46728
* Sat Oct 02 2004 - dkukawka@suse.de
- fixed bug (Bugzilla #46685): now the real scheme names (not i18n
  version) are sent to powersaved
* Fri Oct 01 2004 - dkukawka@suse.de
- added new an revised translationfiles
- make a workaround to reduce systemload if powersaved not present
  and kpowersave need to get systeminformations from /proc/
* Wed Sep 29 2004 - dkukawka@suse.de
- correct redrawPixmap so that now kpowersave correctly func under
  GNOME
- added new translations (jp, sk), added revised translations (bg,
  cs,es,nb)
* Mon Sep 27 2004 - dkukawka@suse.de
- added 2 lines in update() were falsely removed by last changes
* Mon Sep 27 2004 - trenn@suse.de
- correct charging state, when requesting daemon
  initialise has_DPMS
  xscreensaver enable/disable support
  update translations
* Wed Sep 22 2004 - dkukawka@suse.de
- added screensaver options (disable screensaver and DPMS) to menu
  do not poll for scheme changes -> only update on right mouse clck
* Mon Sep 20 2004 - trenn@suse.de
- changes from l.lunak@suse.cz to faster start kpowersave through
  kdeinit
* Tue Aug 31 2004 - trenn@suse.de
- disk<->ram typo which prevented suspend2ram to be enabled
  correctly
* Mon Aug 23 2004 - trenn@suse.de
- renamed suspend/standby to suspend2disk and suspend2ram
  introduced new sleep state standby
* Tue Jun 29 2004 - trenn@suse.de
- switch schemes, enable/disable screensaver and dpms
  proper update functions
* Mon May 17 2004 - trenn@suse.de
- color of remaining capacity always green when on ac power
  (Version 0.2.2)
* Fri May 14 2004 - trenn@suse.de
- modified message:
  system group is not mentioned in popup any more (#40473)
- introduced sub-version nr. (Version 0.2.1)
* Thu May 06 2004 - trenn@suse.de
- added battery charge information to Tooltip
  fixed fd leak
* Thu Apr 29 2004 - trenn@suse.de
- added cpufreq speed to Tooltip
  corrected color when on low level and recharged (was red, should be green)
  merged diffs after 9.1
* Wed Apr 07 2004 - trenn@suse.de
- changed Autostart to AutoStart (#38075)
* Mon Apr 05 2004 - seife@suse.de
- increase AC adapter polling interval to 2.5 seconds
* Sat Apr 03 2004 - coolo@suse.de
- do not rely on daemon but read AC infos right away
- cleanly fixing double start
- disabling suspend/standby menu entries if not available
* Fri Apr 02 2004 - trenn@suse.de
- avoid double start of kpowersave
  added italian and russian translation
* Wed Mar 31 2004 - trenn@suse.de
- delay window that daemon is not running (possible restart of daemon)
  no battery capacity on workstations
* Mon Mar 29 2004 - trenn@suse.de
- rcpowersave to rcpowersaved
  open notification window when on low battery and when requesting info from daemon
  fixed 0:02 mins remaining bug
  ask user to restart on next login when exiting
* Mon Mar 15 2004 - trenn@suse.de
- added several languages
* Thu Mar 11 2004 - trenn@suse.de
- a lot of little fixes for usability
- corrections of translators and some translations
  by adrian@suse.de :
- fix linking (no non-mt qt needed anymore)
- fix multiple packaging of files
* Tue Mar 09 2004 - ro@suse.de
- do not use non-mt
* Wed Mar 03 2004 - ro@suse.de
- call correct yast2 module
* Wed Feb 25 2004 - trenn@suse.de
- use bz2 instead of gz archive
* Mon Feb 23 2004 - trenn@suse.de
- corrected .spec -> file inconsistence
* Mon Feb 23 2004 - trenn@suse.de
- cleaned up
* Mon Feb 16 2004 - trenn@suse.de
- initial build
