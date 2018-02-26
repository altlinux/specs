# be ready to change gnustepdir to /usr/lib/GNUstep
%define gnustepdir %_prefix/libexec/GNUstep
%define wmdatadir /usr/share/WindowMaker

%define WINGs_SOVER 2
%define WUtil_SOVER 2
%define wraster_SOVER 3

%def_disable debug

%define frame_border   navy

Name: WindowMaker
Version: 0.95.3
Release: alt1
Packager: %packager

Summary: A window manager for the X Window System
Group: Graphical desktop/Window Maker
License: GPL
URL: http://www.windowmaker.info/

Source0: %name-%version.tar
Source1: altlinux.tar

Patch0: delete_pl.patch
Patch1: wmgenmenu.patch
Patch2: WindowMaker-0.95.0-configure.ac.patch
Patch3: WindowMaker-alt-Makefile.patch

Requires: xvt, wmsetbg = %version-%release, libWINGs = %version-%release, cpp
Requires: design-graphics
Obsoletes: windowmaker, windowmaker-devel, windowmaker-libs
Obsoletes: wmakerconf <= 2.5

# Automatically added by buildreq on Sun Mar 22 2009
BuildRequires: libICE-devel libXext-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libgif-devel libjpeg-devel libpng-devel libtiff-devel

%description
Window Maker is an X11 window manager which emulates the look and feel of the
NeXTSTEP (TM) graphical user interface. It is relatively fast, feature rich and
easy to configure and use. Window Maker is part of the official GNU project,
which means that Window Maker can interoperate with other GNU projects, such as
GNOME.

Window Maker allows users to switch themes 'on the fly,' to place favorite
applications on either an application dock, similar to AfterStep's Wharf or on
a workspace dock, a 'clip' which extends the application dock's usefulness.

%description -l ru_RU.UTF-8
Window Maker - это менеджер окон системы X11, эмулирующий графический
интерфейс системы NeXTSTEP (TM). Отличается высоким быстродействием,
лёгкой настраиваемостью и удобством использования. Window Maker позволяет
менять темы без перезапуска, размещать часто используемые приложения на
док, прообраз дока Mac OSX, аналогичный Wharf'у оконного менеджера
AfterStep, или же на 'скрепку' - переключатель рабочих столов.

%package -n libWINGs
Summary: WINGs - WINGs Is Not GNUstep
Group: System/Libraries
Requires: libwraster = %version-%release
Provides: libwings = %version-%release

%description -n libWINGs
WINGs is a small widget set with the N*XTSTEP look and feel. It's API
is inspired in OpenStep and it's implementation borrows some ideas
from Tk. It has a reasonable set of widgets, sufficient for building
small applications (like a CDPlayer or hacking something like rxvt). It
also has other functions that are usefull for applications, like a
User Defaults alike configuration manager and a notification system.

%description -l ru_RU.UTF-8 -n libWINGs
WINGs - небольшая библиотека компонент для системы X11, эмулирующая NeXTSTEP.
API библиотеки навеен OpenStep, в реализации использовались идеи
из Tk. Библиотека реализует небольшой набор виджетов, вполне достаточный
для разработки интерфейсов небольших программ (таких как CDPlayer или rxvt).
Кроме того, библиотека содержит дополнительные функции, полезные для
разработки приложений, такие как система уведомлений и менеджер настроек.


%package -n libWINGs-devel
Summary: Development files for WINGs library
Group: Development/C
Requires: libWINGs = %version-%release
Requires: libwraster-devel = %version-%release
Provides: libwings-devel = %version-%release
Provides: WindowMaker-devel = %version-%release
Obsoletes: WindowMaker-devel

%description -n libWINGs-devel
This package contains files needed for developing programs with
WINGs.

%description -l ru_RU.UTF-8 -n libWINGs-devel
В этом пакете содержатся файлы, необходимые для разработки программ,
использующих библиотеку WINGs.

%package -n libwraster
Summary: WindowMaker raster graphics library
Group: System/Libraries

%description -n libwraster
This library is used to manipulate images and convert them to
a format that can be displayed through the X window system.
Read the wraster.h header for an idea of what is available

%description -l ru_RU.UTF-8 -n libwraster
Эта библиотека используется для различных манипуляций с изображениями
и конвертирования их в форматы, подходящие для отображения средствами
X11.

%package -n libwraster-devel
Summary: Development files for wraster library
Group: Development/C
Requires: libwraster = %version-%release

%description -n libwraster-devel
This package contains files needed for developing programs
which manipulate images.

%description -l ru_RU.UTF-8 -n libwraster-devel
В этом пакете содержатся файлы, необходимые для разработки программ,
использующих библиотеку libwraster.

%package -n libWMaker
Summary: WindowMaker library
Group: System/Libraries

%description -n libWMaker
This library is used to provide api to WindowMaker.
Currently only FSViewer is using it.

%description -l ru_RU.UTF-8 -n libWMaker
Эта библиотека предоставляет интерфейс для сторонних
приложений. В настоящий момент используется только
программой FSViewer.

%package -n libWMaker-devel
Summary: Development files for WMaker library
Group: Development/C
Requires: libWMaker = %version-%release

%description -n libWMaker-devel
This package contains files needed for developing programs
which manipulate images.

%description -l ru_RU.UTF-8 -n libwraster-devel
В этом пакете содержатся файлы, необходимые для разработки программ,
использующих библиотеку libWMaker.

%package -n wmsetbg
Summary: Utility for root window image setting
Group: Graphical desktop/Window Maker

%description -n wmsetbg
Utility for root window image setting

%description -l ru_RU.UTF-8 -n wmsetbg
Утилита, позволяющая размещать изображения на рабочий стол.

%prep
%setup -n %name-%version
%setup -a 1 
#%%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

GNUSTEP_LOCAL_ROOT=%gnustepdir
LINGUAS="bg cs da de el es et fi fr gl hr hu it ja ko nl no pl pt ro ru sk sv tr zh_CN zh_TW"
export LINGUAS GNUSTEP_LOCAL_ROOT

%add_optflags -DNEWAPPICON
%autoreconf
%configure \
	--bindir=%_bindir \
	--sysconfdir=%_sysconfdir/X11 \
	--datadir=%_datadir \
	--libdir=%_libdir \
	--includedir=%_includedir \
	--mandir=%_mandir \
	--enable-shared \
	--disable-static \
	--with-pixmapdir=%_datadir \
	--with-appspath=%gnustepdir/Apps \
	--with-menu-textdomain=menu-messages \
                            --with-nlsdir=%_datadir/locale \
	--with-gnustepdir=%gnustepdir \
	--enable-modelock \
	--enable-xinerama \
	--enable-usermenu \

# Меняем цвет бордюра окон на более светлый по просьбе Михаила Шигорина.
subst 's,^\(#define FRAME_BORDER_COLOR \)"black",\1"%frame_border",' \
       src/wconfig.h

%make_build

%install
%makeinstall_std
pushd altlinux
tar cf - . | tar xf - -C "%buildroot"
popd
sed -e 's@#wmdatadir#@%wmdatadir@' <$RPM_BUILD_ROOT/%wmdatadir/wmmacros \
	>$RPM_BUILD_ROOT/%wmdatadir/wmmacros.t
mv $RPM_BUILD_ROOT/%wmdatadir/wmmacros.t $RPM_BUILD_ROOT/%wmdatadir/wmmacros

sed -i -e 's@#wmdatadir#@%wmdatadir@' %buildroot%wmdatadir/wmmacros 

rm -f %buildroot%wmdatadir/menu*
rm -f %buildroot%wmdatadir/plmenu*
rm -f %buildroot%wmdatadir/autostart.sh
rm -f %buildroot%wmdatadir/exitscript.sh
rm -rf %buildroot/usr/share/man/sk/

%find_lang WPrefs
%find_lang WindowMaker
%find_lang WINGs

cat WPrefs.lang >> WindowMaker.lang
#cat WINGs.lang >> WindowMaker.lang

#find_lang name WPrefs geticonset getstyle seticons setstyle wdwrite wmaker wmsetbg wxcopy wxpaste
#find_lang --output=WINGs.lang WINGs

# Подчищаем ненужные языки документации.
rm -rf %buildroot%_mandir/cs

%files -f %name.lang
%doc AUTHORS BUGFORM BUGS COPYING COPYING.WTFPL FAQ FAQ.I18N INSTALL-WMAKER README* TODO
%config(noreplace) %_sysconfdir/X11/WindowMaker
%config(noreplace) %_sysconfdir/menu-methods/WindowMaker
%config(noreplace) %_sysconfdir/X11/wmsession.d/*
%_bindir/convertfonts
%_bindir/geticonset
%_bindir/getstyle
%_bindir/seticons
%_bindir/setstyle
%_bindir/wdread
%_bindir/wdwrite
%_bindir/wmagnify
%_bindir/wmaker
%_bindir/wmaker.inst
%_bindir/wmgenmenu
%_bindir/wmmenugen
%_bindir/wxcopy
%_bindir/wxpaste

%_bindir/startwindowmaker
%_bindir/WindowMaker-Terminal
%_bindir/WindowMaker-Lock

%_man1dir/*
%_mandir/ru/man1/*
%_menudir/*
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%_liconsdir/*.xpm

%gnustepdir/Applications/WPrefs.app
%dir %wmdatadir
%wmdatadir/*
%dir %_datadir/WINGs
%_datadir/WINGs/*

%files -n libWINGs -f WINGs.lang
%doc WINGs/NEWS WINGs/README
%_libdir/libWINGs.so.%WINGs_SOVER
%_libdir/libWINGs.so.%WINGs_SOVER.*
%_libdir/libWUtil.so.%WUtil_SOVER
%_libdir/libWUtil.so.%WUtil_SOVER.*

%files -n libWINGs-devel
%_bindir/get-wings-flags
%_bindir/get-wutil-flags
%_includedir/WINGs
%_libdir/libWINGs.so
%_libdir/libWUtil.so
%_libdir/pkgconfig/WINGs.pc

%files -n libwraster
%_libdir/libwraster.so.%wraster_SOVER
%_libdir/libwraster.so.%wraster_SOVER.*

%files -n libwraster-devel
%_bindir/get-wraster-flags
%_includedir/wraster.h
%_libdir/libwraster.so
%_libdir/pkgconfig/wrlib.pc

%files -n libWMaker
%_libdir/libWMaker.so.*

%files -n libWMaker-devel
%_includedir/WMaker.h
%_libdir/libWMaker.so

%files -n wmsetbg
%_bindir/wmsetbg

%changelog
* Thu May 17 2012 Andrey Bergman <vkni@altlinux.org> 0.95.3-alt1
- Update to a new version.

* Thu May 17 2012 Andrey Bergman <vkni@altlinux.org> 0.95.2-alt3
- Corrected frame border color.

* Sun May 13 2012 Andrey Bergman <vkni@altlinux.org> 0.95.2-alt2
- Reimport to Sisyphus.

* Sat Mar 17 2012 Konstantin Kogan <kostyalamet@yandex.ru 0.95.2-alt1
- WindowMaker 0.95.2 for branch 5.1

* Tue Jan 24 2012 Konstantin Kogan <kostyalamet@yandex.ru 0.95.0-alt1
- First version for Alt Linux Users Club

* Wed Nov 17 2010 Alexey I. Froloff <raorn@altlinux.org> 0.94.0-alt2
- Apply forgotten title height patch

* Sun Oct 31 2010 Alexey I. Froloff <raorn@altlinux.org> 0.94.0-alt1
- [0.94.0-crm-292-g5ff0272]
- Pixmaps and icons moved from /usr/share/pixmaps to Pixmaps and Icons
  WindowMaker data directories
- Dropped wkdemenu.pl and wm-oldmenu2new scripts
- Added /usr/share/design/current/backgrounds and
  /usr/share/design/current/icons to default PixmapPath and IconPath

* Tue Jun 23 2009 Alexey I. Froloff <raorn@altlinux.org> 0.92.0-alt6
- Rebuilt with new libpng12

* Sun Mar 29 2009 Sir Raorn <raorn@altlinux.ru> 0.92.0-alt5
- Dropped useless use of alloca(3) [#18514]
- Workaround for Composite problems.
  (patch from http://repo.or.cz/w/wmaker-crm.git?a=commitdiff;h=e4800e84)
- Ignore workspace change when chaning workspaces. [#7230]
- Atomic saves for history and session. [#3394]
- Turn anti-aliasing in libWINGs on by default.

* Sun Mar 22 2009 Sir Raorn <raorn@altlinux.ru> 0.92.0-alt4
- Fixed typos in WindowMaker-Terminal script. [#15693]
- Slightly rewritten WindowMaker-Lock script. [#15694]
- Updated URL. [#19126]
- Fixed periodic focus bug. [#9520]
  (patch from http://repo.or.cz/w/wmaker-crm.git?a=commitdiff;h=c91bb1ba)
- Fixed segfault when sending messages to backgroung helper. [#18353]
- Dropped obsolete menu/wms/ldconfig updates.
- Sanitized icon search paths.
- Updated BuildRequires.

* Thu May 15 2008 Alexey Voinov <voins@altlinux.ru> 0.92.0-alt3
- WPrefs.app moved to /usr/libexec. [#8414]
  Don't forget to update your local settings!
- Fixed fallback fonts when there's no ttf-fonts-ms installed [#13015]
- Fixed hiding of app-switching panel [#7352]
- Fixed environment corruption resulting in losing managed heads on restart [#9519]
- Fixed autostart/exitscript scripts [#13904]
- Shadowed window frames are raised on unhide now [#9237]
  (patch by Artem Delendik <u2u at nm dot ru>)
- little spec cleanup

* Sun Feb 19 2006 Alexey Voinov <voins@altlinux.ru> 0.92.0-alt2
- weird change to changelog... ^( ( %% -> %%%%)
- chrismas bug fixed [#3480]
- rebuilt with new xorg
- sowings patch updated, 'undefined symbol' warnings removed
- all configs and paths updated (/usr/X11R6 -> /usr)


* Sat Sep 03 2005 Alexey Voinov <voins@altlinux.ru> 0.92.0-alt1
- new version (0.92.0, cvs snapshot 20050903)
- fixed menu file [#6951]
- autostart script fixed (thanks thresh@ :) ) [#7337]
- swpanel-customization patch added (by Gleb Stiblo <g.stiblo@sam-solutions.net>)
- ukrainian po added (by Victor Forsyuk <victor@ksi-linux.com>)


* Sat May 21 2005 Alexey Voinov <voins@altlinux.ru> 0.91.0-alt1
- new version (0.91.0, cvs snapshot 20050517)
- xinerama support enabled [#5649]
- dockhotkeys patch updated and combined with dockhotkeys-fix patch,
  settings window positioning fixed
- sowings, singleclick, session, restartscrpt, menutrans, trance, newbuttons
  titlebar, clipnotext, mmx, adialog, minimizeall, swmenu_rclick, moving-add,
  focus patches were updated
- ancient fonts, ac25, nousrscripts, appsdir, nimbus, transopt
  patches were removed
- peter's patches: newappicon, mouse-placement, appicon-bouncer2
  were updated
- peter's patches: wmmisc, xinerama_arrangeicons, virtual-desktop,
  nomovable, action-fullscreen, netwm2, info-panel-update, netwm-skip-taskbar,
  netwm-focus-fix, placement-fixes were removed
- system autostart and exitscript scripts were updated
- convertfonts utility was added
- default configs were updated
- README.ALT updated
- using default .po file (temporarily :) )
- buildreqs updated


* Fri Oct 22 2004 Alexey Voinov <voins@altlinux.ru> 0.80.2-alt24
- fixed bug in dockhotkeys patch

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.80.2-alt23.1
- Rebuilt with libtiff.so.4.

* Tue Aug 03 2004 Alexey Voinov <voins@altlinux.ru> 0.80.2-alt23
- call ldconfig in proper subpackages [fix for #4926]

* Wed Jun 09 2004 Alexey Voinov <voins@altlinux.ru> 0.80.2-alt22
- peter's appicon bouncer patch added
- peter's netwm focus fix patch added
- adialog patch updated [thanks to dfo]
- changed default font for WindowMaker-Terminal [fix for #3949]

* Wed Mar 24 2004 Alexey Voinov <voins@altlinux.ru> 0.80.2-alt21
- peter's patches updated (netwm)

* Wed Dec 29 2003 Alexey Voinov <voins@altlinux.ru> 0.80.2-alt20
- fixed dependency on libWINGs
- removed *.la
- fixed compilation of WINGs examples [.sowings patch updated]

* Thu Oct 16 2003 Alexey Voinov <voins@altlinux.ru> 0.80.2-alt19
- updated to cvs snapshot 06-Aug-2003
- peter's netwm patches updated
- textfield patch added [WMGetTextFieldCursorPosition function]
- adialog now supports completion
- sga-moving-add updated

* Mon Jul 14 2003 Alexey Voinov <voins@altlinux.ru> 0.80.2-alt18
- adialog patch added. adds history to some dialogs.
  replace %%a with %%A to activate it.
- default WMRootMenu changed to use dialogs with history.
- sowings patch updated [libWMaker is also shared library]
- moving-add patch that uses home/end/pgup/pgdn keys to move/resize
  windows to various parts of the screen
  [by Gleb Stiblo <g.stiblo@sam-solutions.net>]

* Thu Jul 10 2003 Alexey Voinov <voins@altlinux.ru> 0.80.2-alt17
- fixed deps for libWINGs* on libwraster*
- virtual_desktop disabled by default.
  set VirtualEdgeThickness to 1 to enable it.

* Mon Jul 07 2003 Alexey Voinov <voins@altlinux.ru> 0.80.2-alt16
- new cvs snapshot (07-Jul-2003)
- dynamic libWINGs and libWUtil (sowings patch)
- repackaging.
- virtual desktop patch updated [by peter]
- netwm patch updated [by peter]
- fixes patch replaced xinerama-usablearea-fix and xinerama-arrange-icons 
  patches [by peter]
- no-movable patch updated [by peter]
- mouse-placement patch updated [by peter]
- mouse-placement-wprefs patch added [by peter]
- newappicon patch updated but still disabled (it still doesn't support
  alt-tab switching) [by peter]
- buildreqs fixed

* Tue Jul 03 2003 Alexey Voinov <voins@altlinux.ru> 0.80.2-alt15
- titlebar patch. Adds WindowTitleMinHeight, WindowTitleMaxHeight,
  MenuTitleMinHeight and MenuTitleMaxHeight options, that provides
  more control over titlebar look.
- clipnotext patch. Adds ShowClipTitle that allows hiding
  workspace name in clip
- --enable-kde removed form configure. This fixes bug with omnipresent
  windows, that eats cpu.
- LeetWM theme removed. It is provided by largo-themes package.

* Fri Jun 27 2003 Alexey Voinov <voins@altlinux.ru> 0.80.2-alt14
- typo in WPrefs.ru-po fixed.
- transopt patch added (translation of strings in %%a());
- menutrans patch fixed (translation of submenu titles)
- README.ALT updated

* Sat Jun 14 2003 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt13
- new cvs snapshot (14-Jun-2003)
- xft2 patch no longer needed.
- patches reordered
- netwm patches updated
- virtual-desktop patch added and enabled.
- newappicon patch removed. (too many bugs.)
- buildreqs updated

* Fri Jun 06 2003 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt12
- added swmenu_rclick patch (by "Pavel S. Khmelinsky" <hmepas@yauza.ru>)
- README.ALT updated

* Mon Jun 02 2003 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt11
- newappicon patch (by Peter Zijlstra <a.p.zijlstra@chello.nl>)
- xft2 patch fixed, now it builds correctly even with latest XFree86.

* Wed May 14 2003 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt10
- new cvs snapshot (11-May-2003)
- fixed bug in Peter's patch [gimp2 crashes wmaker to segfault]
- fixed problem with lost focus by single window with iconify/deiconify
- pkgconfig files added to -devel
- fake items added to menu file to prevent translation disappear from
  .mo in menu package

* Sat Mar 08 2003 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt9
- netwm patch added  (by Peter Zijlstra <a.p.zijlstra@chello.nl>)
  [this should add kde3.1 and gnome2 support]
- sloppyback patch added (by Peter Zijlstra <a.p.zijlstra@chello.nl>)

* Sun Mar 02 2003 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt8
- new cvs snapshot (01-Mar-2003)
- wmsetbg and swmsetbg patches no longer needed.
- trance patch by vlaad updated.
- mmx patch updated. --disable-mmx added to configure.
- minimizeall patch added (by "Pavel S. Khmelinsky" <hmepas@yauza.ru>)

* Fri Feb 28 2003 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt7
- swmsetbg patch added.
- default theme fixed (uses design-graphics)

* Thu Feb 06 2003 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt6
- BuildRequires fixed

* Wed Jan 29 2003 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt5
- translations spellchecked (bug #2101)
- Default focus mode set to manual (it's better for GNUstep)
- s/_x11prefix/_x11dir/

* Thu Jan 23 2003 Stanislav Ievlev <inger@altlinux.ru> 0.80.2-alt4
- remove deps on mandrake_desk

* Sun Dec 29 2002 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt3
- new cvs snapshot (29-Dec-2002)
- "--enable debug" option added (build with debug info)
- ALTLinux theme (sadist@altlinux.ru) added and made default
  for new users.
- fixed bug in wmsetbg with tpixmap (#1794)

* Mon Dec 07 2002 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt2
- new cvs snapshot (02-Dec-2002)
- wfrabebug patch no longer needed
- listview patch no longer needed
- aafont patch no longer needed
- nimbus patch updated
- gettext patch no longer needed
- singleclick patch updated
- WPrefs.app russian translation updated
- patches renumbered

* Thu Nov 20 2002 Alexey Voinov <voins@voins.program.ru> 0.80.2-alt1
- cvs snapshot (17-Nov-2002)
- bas tarball changed to 0.80.2 (libwraster buffer overrun fixed)
- more accurate xft2 patch.
- nimbus patch updated.
- wframebug patch added (fixes bug in WINGs/wframe.c)
- listview patch added (adds method to access bg color of WMList
  [needed to fix synaptic and FSViewer.app])

* Mon Nov 04 2002 Alexey Voinov <voins@voins.program.ru> 0.80.1-alt10
- fallback fonts changed from arial to nimbus sans l (nimbus patch)
- default WMGLOBAL updated (Antialiasing by default is turned off)
- README.ALT updated
- global exitscript fixed
- removed directory /usr/share/icons/mini from filelist

* Sat Oct 19 2002 Alexey Voinov <voins@voins.program.ru> 0.80.1-alt9.1
- cvs snapshot (19-Oct-2002) [Xft support]
- singleclick patch updated and renamed
- nousrscrpt patch updated and renamed
- menutrans patch updated and renamed
- trance patch updated and renamed
- newbuttons patch updated and renamed
- mmx patch added (dirty hack to disable mmx inline asm)
- xft2 patch added (dirty hack from aen to allow WM use Xft2)

* Tue Oct 08 2002 Alexey Voinov <voins@voins.program.ru> 0.80.1-alt9
- fixed bug #1366 (change in WindoMaker-alt.tar.bz2/usr/X11R6/bin/startwindowmaker)

* Mon Sep 16 2002 Alexey Voinov <voins@voins.program.ru> 0.80.1-alt8.1
- newbuttons patch fixed, so it have all used buttons 
  (including xkb group indicators)
- (inger) update buildreq(XFree86-static-libs)

* Sat Sep 14 2002 Alexey Voinov <voins@voins.program.ru> 0.80.1-alt7
- cvs snapshot (20020914)
- wtblbug patch no longer needed
- trance patch (transparent menus by Carlos Torres <vlaadbrain@operamail.com>
  [sent to me by Axel <axel@technoserv.ru>])
- newbuttons patch (buttons in window titles by Carlos Torres <vlaadbrain@operamail.com>)

* Tue Sep 03 2002 Alexey Voinov <voins@voins.program.ru> 0.80.1-alt6
- WindowMaker-Lock added to filelist
- /usr/share/locale/*/WINGs.mo added to filelist

* Sat Aug 31 2002 Alexey Voinov <voins@voins.program.ru> 0.80.1-alt5
- WMRootMenu added.
- WindowMaker-Lock script added (called from menu to lock screen)
- WindowMaker-Terminal now runs xvt by default
- Requires xvt instead of aterm
- Better patch to support .../Gs/Applications directory
  (thanks to Sir Raorn <raorn@binec.ru>)
- /usr/lib/menu/WindowMaker updated. most users should delete their 
  ~/Gs/D/WMRootMenu to get full functionality now.
- /etc/menu-methods/WindowMaker doesn't do translation, it is performed by
  WindowMaker itself
- patches renamed according to policy
- menutrans patch added (translate root menu on-the-fly)
- README.ALT updated
- ru.po updated

* Wed Jul 31 2002 Alexey Voinov <voins@voins.program.ru> 0.80.1-alt4
- reverted back to .../Gs/Apps, helper scripts is not installed
- README.ALT downdated :)

* Mon Jul 25 2002 Alexey Voinov <voins@voins.program.ru> 0.80.1-alt3 (unpublished)
- restartscrpt patch added. It allows wmaker to run exit script when
  restarting.
- nousrscrpt patch added. It starts systemwide init/exit script before
  user defined scripts. Additionally it adds two options in ~/G/D/WindowMaker:
  ExecuteUserScript & ExecuteSystemScript, to finetune running of scripts.
- apps patch added. It provides ability to load resources from .../Apps and from 
  .../Applications directory. Needed for compatibility.
- changed .../GNUstep/Apps to .../GNUstep/Appliactions as Sir Raorn suggested.
- README.ALT added
- gsappswarn.sh startup script added, which informs user about possible "bad" links 
  to application in ~/Gs/D/
- fixgsapps script added, which tries to fix "bad" links in  ~/Gs/D/

* Thu Jul 11 2002 Alexey Voinov <voins@voins.program.ru> 0.80.1-alt2
- fixed bug in WINGs/Extra/wtableview.c
- fixed bug #1061 

* Fri Jul 05 2002 Alexey Voinov <voins@voins.program.ru> 0.80.1-alt1
- new release (+ cvs snapshot)
- updated -session patch.
- ac25 patch. now autogen.sh uses autoconf_2.5 directly
- ru.po updated

* Wed Jun 19 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.80.0-alt0.9
- Removed requires to glibc-locales (removed wmchlocale)

* Sat Jun 01 2002 Alexey Voinov <vns@altlinux.ru> 0.80.0-alt0.8
- '--enable-gnome' option re-enabled
- cpp added to required packages (BUG#0000968)
- spec cleanup

* Fri May 31 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.80.0-alt0.7
- Removed requires for binutils (moved some scripts to devel package)

* Sun Mar 31 2002 Alexey Voinov <voins@voins.program.ru> 0.80.0-alt0.6
- session patch added (fix a bug with not saving all windows in session 
  when SharedAppIcon is enabled)

* Mon Jan 21 2002 AEN <aen@logic.ru> 0.80.0-alt0.5
- s/Mandrake/ALT Linux/g menu-methods

* Wed Jan 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.80.0-alt0.4
- Updated wmsession.d and startup scripts.

* Sun Jan 06 2002 Alexey Voinov <voins@voins.program.ru> 0.80.0-alt0.3
- cvs version
- gettext patch added (zh_TW.Big5.po corrupted, make it at least compile)

* Fri Dec 28 2001 Alexey Voinov <voins@voins.program.ru> 0.80.0-alt0.2
- directories rearranged
- removed all references to '/home/voins' from default config files
- default configuration files updated to 0.80.0
- ru.po updated to 0.80.0 and fixed a little

* Sun Dec 23 2001 Alexey Voinov <voins@voins.program.ru> 0.80.0-alt0.1
- 0.80.0

* Sat Oct 27 2001 Alexey Voinov <voins@voins.program.ru> 0.70.0-alt6
- cvs version 

* Mon Oct 22 2001 Alexey Voinov <voins@voins.program.ru> 0.70.0-alt6
- dockhotkeys patch updated (fixed BUG#103)

* Thu Oct 18 2001 Alexey Voinov <voins@voins.program.ru> 0.70.0-alt5
- WindowMaker-devel removed from BuildRequires

* Mon Oct 15 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.70.0-alt4
- Rebuilt with libpng.so.3

* Wed Oct 11 2001 Alexey Voinov <voins@voins.program.ru> 0.70.0-alt3
- uncollapse patch added
- dockhotkeys patch added (now we can setup docked appicons to launch
  on keypress(not only mouse click))

* Sun Oct  7 2001 Alexey Voinov <voins@voins.program.ru> 0.70.0-alt2
- forget to mention: wm now compiled with gcc instead of kgcc(!)
- fixed BuildRequires

* Sun Oct  7 2001 Alexey Voinov <voins@voins.program.ru> 0.70.0-alt1
- .po files updated (but not finished :( )

* Fri Oct  5 2001 Alexey Voinov <voins@voins.program.ru> 0.70.0-alt0.1
- new version
- spec cleanup
- WindowMaker-Terminal now passess all commandline options to underlying term.
- all extra files put into WindowMaker-alt.tar.bz2

* Thu Sep 13 2001 Alexey Voinov <voins@voins.program.ru> 0.66.0-alt0.3
- 2001-09-13 cvs version

* Thu Aug 14 2001 Alexey Voinov <voins@voins.program.ru> 0.66.0-alt0.2
- 2001-08-14 cvs version
- cyrenter patch removed
- BuildRequires corrected

* Thu Jul 05 2001 Alexey Voinov <voins@voins.program.ru> 0.66.0-alt0.1
- cvs version
- plmenu.ja added (Kojima marks wrong files as release-0_65_0 in cvs)

* Fri Jun 08 2001 Alexey Voinov <voins@voins.program.ru> 0.65.0-alt2	
- corrected dependance on wmsetbg
- better WindowMaker-Terminal
- menu rearranged
- now BuildRequires gettext > 0.38.1 because it'll not compile
  with earlier versions

* Sat May 12 2001 Alexey Voinov <voins@voins.program.ru> 0.65.0-alt1
- 0.65.0
- patches reordered

* Sun Apr 29 2001 Alexey Voinov <voins@voins.program.ru>
- fixed problems with new gettext
- conditional NoSource. use --define 'nosource 1' to build nosrc.rpm

* Tue Apr 17 2001 Alexey Voinov <voins@voins.program.ru>
- WPrefs's menu section fixed, no more SIGSEGV

* Mon Apr 16 2001 Alexey Voinov <voins@voins.program.ru>
- WPrefs translations updated

* Sat Apr 14 2001 Alexey Voinov <voins@voins.program.ru>
- translation updated
- configuration updated
- utils/wm-oldmenu2new fixed

* Thu Apr 12 2001 Alexey Voinov <voins@voins.program.ru>
- fixed problem with WPrefs translations
- fixed problem with menu
- all files in /usr/X11R6/bin added
- wsfont patch (display cyrillic workspcae name correctly)
- extras now included
- wmCalClock and WMMail.app now in separate packages
- single_click patch adapted and applied

* Sat Feb 17 2001 AEN <aen@logic.ru>
- patches from Alexey Voinov

* Thu Feb 15 2001 AEN <aen@logic.ru>
- 0.64

* Thu Feb 1 2001 AEN <aen@logic.ru>
- build from cvs

* Tue Jan 11 2001 AEN <aen@logic.ru>
- new version
- small spec cleanup

* Sun Dec 24 2000 AEN <aen@logic.ru>
- correct packager name :-)

* Tue Dec 05 2000 AEN <aen@logic.ru>
- rebuild for RE
- fonts & kbdlock patches
- moved wmsetbg & libwraster in separate package
- ru.po  patch
- mo files -> /usr/share/locale

* Fri Nov 10 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-19mdk
- Build with glibc-2.2 & gcc-2.96

* Tue Sep 19 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-18mdk
- Make auto-login happy

* Thu Aug 31 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-17mdk
- Fix wmsession

* Wed Aug 30 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-16mdk
- Fix "I kill the X server"

* Sun Aug 13 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-15mdk
- New clock (wmCalClock)
- New config files
- Modify Window Maker specific menu entries
- Spec clean up
- Patch for wmsetbg
- Add Packager tag
- New wmsession support

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.62.1-14mdk
- automatically added BuildRequires

* Fri May 12 2000 dam's <damien@mandrakesoft.com> 0.62.1-13mdk
- corrected workspace menus.

* Wed May 10 2000 dam's <damien@mandrakesoft.com> 0.62.1-12mdk
- corrected wmaker.inst text script

* Tue May 09 2000 dam's <damien@mandrakesoft.com> 0.62.1-11mdk
- corrected wmaker test script.

* Mon May  8 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.62.1-10mdk
- remove asclock which conflicts with AfterStep-APPS
- added url

* Tue May  2 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.62.1-9mdk
- really add menu support

* Fri Apr 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.62.1-8mdk
- added fndSession call

* Thu Apr 27 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix wmconfig crash

* Fri Apr 21 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-6mdk
- Requires mandrake_desk >= 1.0.3-9mdk

* Fri Apr 21 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-5mdk
- Add the binary :/ and put it in the right PATH

* Fri Apr 21 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-4mdk
- Relocate in /usr/X11R6
- Menu support
- Fix crazy obsoletes

* Thu Apr 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.62.1-3mdk
- fix a very old bug : when ~/GNUstep doesn't exists, exec wmaker.inst
  else the end user won't be able to launch WindowMaker

* Tue Apr 04 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-2mdk
- Split in 2 packages (devel & normal)
- Fix Group

* Tue Apr 04 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-1mdk
- 0.62.1

* Fri Mar 31 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.0-1mdk
- 0.62.0
- Release for impatients
- Use new Groups
- Use %%{_tmppath} for BuildRoot

* Sun Mar 05 2000 David BAUDENS 0.61.1-17mdk
- Fix duplicate screen saver
- French translations and adapatations

* Wed Jan 05 2000 - David BAUDENS <baudens@mandrakesoft.com>
- 0.61.1-16mdk: new icon
- 0.61.1-15mdk: back to /usr for some directories 
- 0.61.1-14mdk: fix PATH in /etc/X11/WindowMaker 
- 0.61.1-13mdk: fix a typo in WMDrake
- 0.61.1-12mdk: requires mandrake_desk >= 1.0.1-11mdk

* Tue Jan 04 2000 - David BAUDENS <baudens@mandrakesoft.com>
- 0.61.1-11mdk: new icon
- 0.61.1-10mdk: better MandrakeSoft customization

* Mon Jan 03 2000 - David BAUDENS <baudens@mandrakesoft.com>
- Enable WMDrake
- Fix typos

* Mon Dec 27 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Fix display version

* Tue Dec 21 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Fix WMDrake

* Wed Dec 15 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Cleanup spec
- Back to original sources
- (Re) Fix cpp problem

* Wed Dec 09 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Build release

* Tue Dec 08 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Add some apps in wmdrake

* Fri Dec 04 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Initial wmdrake

* Fri Nov 20 1999 - David BAUDENS <baudens@mandrakesoft.com>
- 0.61
- Add some patches from package of Ryan Weaver <ryanw@infohwy.com>

* Wed Sep 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Various patch syncronised with package from Ryan Weaver <ryanw@infohwy.com>
- Added diff from cvs 'WindowMaker-0.61.0-19990922cvs.diff.bz2'
- fixes seg fault at exit among other things including the following.
- fixed problem with window shortcut assignment from the menu
- fixed problem with fonts in WINGs (Masahide -mac- NODA
- WindowMaker-0.61.0-po.patch.bz2

* Tue Sep 21 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 0.61.0
- fix compilation
- redo Mandrake adaptions

* Tue Jul 20 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- add french description from Gregus <gregus@etudiant.net>
- fix a typo

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Update URL.

* Mon May 17 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix include problem with /usr/bin/cpp (need /lib/cpp).

* Sat May 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake Adaptations.

* Mon Apr 19 1999 Preston Brown <pbrown@redhat.com>
- fixed up default config (dock was empty...)

* Thu Apr 15 1999 Cristian Gafton <gafton@redhat.com>
- version 0.52.0

* Wed Apr 14 1999 Preston Brown <pbrown@redhat.com>
- fixed problem with running wmaker.inst in batch mode (forgot comma)

* Mon Apr 12 1999 Preston Brown <pbrown@redhat.com>
- fixed icon problems
- run wmaker.inst in batch mode if no ~/GNUstep/Library/WindowMaker dir exists

* Mon Apr 05 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Thu Apr 01 1999 Cristian Gafton <gafton@redhat.com>
- requires cpp

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Wed Mar 17 1999 Cristian Gafton <gafton@redhat.com>
- make sure we get the full distribution
- run ldconfig in the post script

* Mon Feb 15 1999 The Rasterman <raster@redhat.com>
- added gnome winhints areas support fix.

* Tue Feb 02 1999 Cristian Gafton <gafton@redhat.com>
- version 0.51.0
