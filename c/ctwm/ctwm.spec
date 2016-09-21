Summary: Twm based window manager for the X Window System
Summary(ru_RU.KOI8-R): Основанный на twm оконный менеджер для X Window System
Name: ctwm
Version: 3.8.2
Epoch: 1
Release: alt2

Source: %name-%version.tar.xz
Url: http://ctwm.free.lp.se
Packager: Fr. Br. George <george@altlinux.ru>

#Source1: http://slhp1.epfl.ch/public/ctwm/ctwm-images.tar.gz
Source1: startctwm
Source2: %name.wmsession
Source3: %name.icon64x64.xpm
#Source4: ctwm-3.7-Imakefile.local-additional

Patch: ctwm-3.8-dirs.patch
Patch1: ctwm-strlen.patch
Patch2: ctwm-3.8.2-GetFont.patch
License: BSD
Group: Graphical desktop/Other

# Automatically added by buildreq on Mon Mar 14 2011
BuildRequires: flex imake libXext-devel libXmu-devel libXpm-devel libjpeg-devel xorg-cf-files

%description
Ctwm is a window manager for the X Window System.  It provides
titlebars, shaped windows, virtual screens (workspaces), several forms
of icon management, user-defined macro functions, click-to-type and
pointer-driven keyboard focus, and user-specified key and pointer
button bindings.  It is actually twm (Tab Window Manager) from the MIT
X11 distribution slightly modified to accommodate the use of several
virtual screens (workspaces). It is heavily inspired from the
Hewlett-Packard vuewm window manager.  In addition, ctwm can use
coloured, shaped icons and background root pixmaps in XPM format [from
Arnaud Le Hors], any format understood by the imconv package [from the
San Diego Supercomputer Center] and xwd files.  Ctwm can be compiled
to use both, either or none of the above icon/pixmap formats.

%description -l ru-RU.KOI8-R
Ctwm -- оконный менеждер для X Windows System, основанный на одном из
старейших  оконных менеджеров для X11 -- twm (Tab Window Manager) из
дистрибутива Mit X11. Под влиянием vuewm от Hewlett-Packard в ctwm
добавлена поддержка "трёхмерных" заголовков, рамоки меню, виртуальные
экраны и многое другое. Ctwm поддерживает макросы в настройках,
разнообразные стили перемещения фокуса, заливку фона и т. д., а также
имеет несколько уникальных функций, например movepush, когда окно,
перемещаемое по экрану, расталкивает прочие окна в стороны.

%prep
%setup
%patch -p1
%patch1 -p0
%patch2 -p1
cp Imakefile.local-template Imakefile.local
sed -ri 's/(#define[[:space:]]+MAX_BUTTONS[[:space:]]+).*/\1 24/' twm.h

%build
xmkmf
%make_build CDEBUGFLAGS="-g -Og"

%install
%make install DESTDIR=%buildroot
install -D %name.man %buildroot/%_mandir/man1/%name.1x
install -pD -m644 %SOURCE3 %buildroot/%_iconsdir/hicolor/64x64/apps/%name.xpm
install -pD -m644 %SOURCE2 %buildroot/%_sysconfdir/X11/wmsession.d/07%name
install -Dm 755 %SOURCE1 %buildroot/%_bindir/startctwm

%files
%doc README CHANGES PROBLEMS TODO*
%_iconsdir/hicolor/64x64/apps/*
%_bindir/*
%_mandir/man1/*
%config(noreplace) %_sysconfdir/X11/%name/system.ctwmrc
%_sysconfdir/X11/wmsession.d/*
%_datadir/X11/%name/

%changelog
* Wed Sep 21 2016 Fr. Br. George <george@altlinux.ru> 1:3.8.2-alt2
- Fix fonset usage

* Mon Jul 14 2014 Fr. Br. George <george@altlinux.ru> 1:3.8.2-alt1
- Autobuild version bump to 3.8.2
- Clean up spec

* Thu Aug 29 2013 Fr. Br. George <george@altlinux.ru> 1:3.8.1-alt1
- Update to current mtn
- Introducing epoch (version switched back to 3.8.*)

* Mon Mar 14 2011 Fr. Br. George <george@altlinux.ru> 3.9devel-alt2
- Buildreq regenerated

* Mon Feb 14 2011 Fr. Br. George <george@altlinux.ru> 3.9devel-alt1
- Version up to MTN development

* Sat Nov 21 2009 Repocop Q. A. Robot <repocop@altlinux.org> 3.8a-alt1.qa2
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for ctwm
  * postclean-05-filetriggers for spec file

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.8a-alt1.qa1.1
- NMU:
  * updated build dependencies
  * removed obsolete %%update_wms/%%clean_wms calls

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 3.8a-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_wms for ctwm

* Wed Apr 18 2007 Fr. Br. George <george@altlinux.ru> 3.8a-alt1
- version up
- another strcpy() without \0 fix
- MAX_BUTTONS is 24 now

* Mon Dec 11 2006 Fr. Br. George <george@altlinux.ru> 3.7-alt5
- Poor strcpy() bugfix

* Thu Nov 16 2006 Fr. Br. George <george@altlinux.ru> 3.7-alt4
- Bug 10256 closed (/usr/X11R6 -> /usr)

* Thu Sep 14 2006 Fr. Br. George <george@altlinux.ru> 3.7-alt3
- GEAR tuning

* Sun Oct 09 2005 Fr. Br. George <george@altlinux.ru> 3.7-alt2
- Trivial description bugs fixed, russian description added

* Thu Aug 25 2005 Fr. Br. George <george@altlinux.ru> 3.7-alt1
- Version upping
- Upstream changed

* Fri Jul 01 2005 Fr. Br. George <george@altlinux.ru> 3.6-alt3
- Change startctwm to be used both with or without m4

* Mon Jul 26 2004 Fr. Br. George <george@altlinux.ru> 3.6-alt2
- Add startctwm simple script, move pixmaps out of /etc/X11

* Fri Oct 17 2003 Fr. Br. George <george@altlinux.ru> 3.6-alt1
- First time ported under ALT Linux

