Summary: Twm based window manager for the X Window System
Summary(ru_RU.KOI8-R): Основанный на twm оконный менеджер для X Window System
Name: ctwm
%define rcfile ctwmrc
%define start startctwm
Version: 3.9devel
Release: alt2
# Initialise database
#  mtn --db=YOUR_DATABASE_DIRECTORY/ctwm.mtn db init
# Pull the repository
#  mtn  --db=YOUR_DATABASE_DIRECTORYI/ctwm.mtn pull guardian.lp.se free.lp.se:X.ctwm
# Check out the source 
#  mtn --db=YOUR_DATABASE_DIRECTORY/ctwm.mtn --branch=free.lp.se:X.ctwm co CTWM_WORK_DIRECTORY

Source: %name-%version.tar.gz
URL: http://ctwm.free.lp.se
Packager: Fr. Br. George <george@altlinux.ru>

#Source1: http://slhp1.epfl.ch/public/ctwm/ctwm-images.tar.gz
Source1: %start
Source2: %name.wmsession
Source3: %name.icon64x64.xpm
#Source4: ctwm-3.7-Imakefile.local-additional

Patch0: %name-patches-aa
Patch1: %name-3.8-m4exec.patch
#Patch2: %name-3.7.patch1
Patch3: %name-3.7-dirs-patch
Patch4: %name-strlen.patch
Patch5: %name-MAX_BUTTONS.patch
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
Ctwm -- оконный менеждер для X Windows System, основанный на одном из старейших  оконных менеджеров для X11 -- twm (Tab Window Manager) из дистрибутива Mit X11. Под влиянием vuewm от Hewlett-Packard в ctwm добавлена поддержка "трёхмерных" заголовков, рамоки меню, виртуальные экраны и многое другое. Ctwm поддерживает макросы в настройках, разнообразные стили перемещения фокуса, заливку фона и т. д., а также имеет несколько уникальных функций, например movepush, когда окно, перемещаемое по экрану, расталкивает прочие окна в стороны.

%prep
%setup
#%setup -T -D -a 1
%patch -p0
%patch1 -p0
#patch2 -p0
%patch3 -p0
%patch4 -p0
#patch5 -p0
#cat Imakefile.local-template %%SOURCE4 > Imakefile.local
cp Imakefile.local-template Imakefile.local

%build
xmkmf
%make

%install
mkdir -p %buildroot/%_sysconfdir/X11/wmsession.d
mkdir -p %buildroot/%_sysconfdir/X11/%name
mkdir -p %buildroot/%_iconsdir
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_mandir/man1
%make install DESTDIR=%buildroot
install %name.man %buildroot/%_mandir/man1/%name.1x
#convert -crop 680x280+28+4 xpm/welcome.xpm -resize 64x64! %buildroot/%_niconsdir/%name.xpm
install -pD -m644 %SOURCE3 %buildroot/%_iconsdir/hicolor/64x64/apps/%name.xpm
install -pD -m644 %SOURCE2 %buildroot/%_sysconfdir/X11/wmsession.d/07%name
install -m 755 %SOURCE1 %buildroot/%_bindir/%start

%files
%doc README CHANGES PROBLEMS
%_iconsdir/hicolor/64x64/apps/*
%_bindir/*
%_mandir/man1/*
%config(noreplace) %_sysconfdir/X11/%name/system.%rcfile
%_sysconfdir/X11/wmsession.d/*
%_datadir/X11/%name/

%changelog
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

