Name: kamix
Version: 0.6.6
Release: alt4.1

Summary: A KDE mixer application for KDE 3 and ALSA.
License: GPL
Group: Sound
Url: http://kamix.sourceforge.net/
Packager: Ilya Mashkin <oddity at altlinux dot ru>

Source0: %name-%version.tar.bz2
Source1: %name.menu
Patch0: %name-0.6.6-alt-DSO.patch

BuildRequires: fontconfig freetype2 gcc-c++ gcc-java kde-settings kdelibs-devel libalsa-devel libjpeg-devel libpng-devel libqt3-devel libqt3-settings libstdc++-devel qt3-designer xml-utils zlib-devel

%description
Basically, because there's not a complete one. kmix is the official mixer app for KDE, but it lacks:

    * Support for enumerated items, when the control is not just a volume, but a choice between different elements
    * Support for splitted playback/record volumes: sometimes, an element can have different volumes for playing and recording: kmix doesn't show them all
    * Support for balance: one cannot adjust Left/Right volumes in an independent way
    * You cannot configure what you want to see or not; for 90%% of the people, "IEC958" item is useless and correctly hidden, but for someone it may not be

With this, I'm not stating that kmix is not good: it is, indeed, and it works in 95%% cases; but, you know, it's a matter of choice :) 

%prep
%setup -q -n %name
%patch0 -p2

%__subst 's/\(-Wl,--no-undefined\)/-Wl,--warn-unresolved-symbols \1/g' configure 
%__subst 's/\-lkdeui/-lkdeui -lpthread/g' configure
 
%build
%add_optflags -I%_includedir/tqtinterface
%set_automake_version 1.9
%set_autoconf_version 2.5


%__subst 's,\.la,\.so,' configure
%__subst 's,\.la,\.so,' admin/acinclude.m4.in
%configure --disable-rpath --disable-path-check --without-arts --disable-vumeter
%set_verify_elf_method textrel=relaxed
%make_build

%install
make DESTDIR=%buildroot install

%__mkdir_p %buildroot%_menudir
%__install -pD -m644 %SOURCE1 %buildroot%_menudir/%name

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog README
%_bindir/%name
%_menudir/%name
%_datadir/apps/%name/
%_datadir/applnk/Utilities/kamix.desktop
%doc %_docdir/HTML/en/%name
%_iconsdir/*/*/apps/%name.png

%_iconsdir/hicolor/16x16/actions/*
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/128x128/apps/%name/mute.png

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt4.1
- Fixed build

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.6.6-alt4
- Build for TDE 3.5.13 release

* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.6-alt3
- fix build

* Sun Dec 26 2010 Ilya Mashkin <oddity@altlinux.ru> 0.6.6-alt2
- update requires
- build without arts (Closes: #24820)

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.6-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for kamix
  * postclean-05-filetriggers for spec file

* Tue Mar 11 2008 Ilya Mashkin <oddity at altlinux dot ru> 0.6.6-alt1
- 0.6.6

* Fri Jan 06 2006 Ilya Mashkin <oddity at altlinux dot ru> 0.6.5-alt1
- New version 0.6.5
- cleanup spec

* Mon Oct 04 2004 Dmitriy Porollo <spider@altlinux.ru> 0.5.7-alt1
- New Version

* Tue Sep 28 2004 Dmitriy Porollo <spider@altlinux.ru> 0.5.6-alt1
- 0.5.5-alt1 kamix is now single instance, this fixes a multi-run problem seen on SuSE box
- 0.5.5-alt1 OSD has configurable font and colors
- 0.5.5-alt1 Updated de i18n (Andreas)
- 0.5.5-alt1 For those who don't have aRts, a --disable-vumeter configure parameter is available at compile time, to avoid linking to aRts libraries

* Mon Sep 20 2004 Dmitriy Porollo <spider@altlinux.ru> 0.5.5-alt1
- 0.5.5-alt1 Added an OSD-like notifier for mixer changes
- 0.5.5-alt1 When shown in systray, DCOP commands acted only on one channel
- 0.5.5-alt1 When a tab contained no sliders, the vertical label was badly shown (thanks to Andreas Arens for the fix)
- 0.5.5-alt1 Updated hu and it translations
- 0.5.5-alt1 Added de translation (thanks to Andreas)
