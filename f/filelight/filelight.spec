Name: filelight
Version: 1.0
Release: alt11.3

Summary: Graphical disk usage display
License: GPLv2
Group: Graphical desktop/KDE

Url: http://www.methylblue.com/filelight
Source: %name-%version.tar.bz2
Patch0: filelight-1.0-alt-sparsefiles.patch
Patch1: filelight-1.0-alt-desktop.patch
Patch2: filelight-1.0-fix-autoconf-2.64.patch
Patch3: filelight-1.0-buffer.patch
Patch4: filelight-1.0-alt-DSO.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(de): Eine grafische Anzeige der Festplattenbelegung
Summary(ru_RU.KOI8-R): Графическая визуализация занимаемого места на диске
Summary(uk_UA.KOI8-U): Граф╕чна в╕зуал╕зац╕я зайнятого м╕сця на диску

# Automatically added by buildreq on Wed Jul 29 2009
BuildRequires: gcc-c++ imake kdelibs-devel libXt-devel libjpeg-devel qt3-designer xml-utils xorg-cf-files
BuildRequires: libtqt-devel

%set_automake_version 1.9

%description
Filelight creates a complex, but data-rich graphical representation
of the files and directories on your computer.

For KDE4, see also filelight-kde4 package.
For GNOME, see also gdmap package.

%description -l de
Filelight zeigt eine aufwДndige grafische Darstellung der Dateien
und Verzeichnisse.

%description -l ru_RU.KOI8-R
Filelight создает графическое представление места, занимаемого
файлами и каталогами на вашем диске.

Для KDE4 см. тж. пакет filelight-kde4.
Для GNOME см. тж. пакет gdmap.

%description -l uk_UA.KOI8-U
Filelight створю╓ граф╕чне уявлення м╕сця, яке займають файли
та теки на вашому диску.

Для KDE4 див. також пакунок filelight-kde4.
Для GNOME див. також пакунок gdmap.

%add_optflags %optflags_shared

%prep
%setup
%patch0 -p2
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p2
subst 's,\.la,\.so,' configure
subst 's,\.la\>,.so,' admin/acinclude.m4.in
make -f admin/Makefile.common

%build
%configure \
	--without-arts \
	--enable-closure \
	--disable-rpath \
	--disable-debug
%make_build CXXFLAGS="-g -I%_includedir/tqtinterface"

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%_bindir/*
%_iconsdir/*/*/*/*.png
%_datadir/apps/*
%_datadir/config/%{name}rc
%_datadir/applications/kde/*.desktop
%_datadir/services/*.desktop
%_libdir/kde3/lib%name.*

%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt11.3
- Fixed build

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt11.2
- Rebuilt without arts

* Sun Jan 23 2011 Michael Shigorin <mike@altlinux.org> 1.0-alt11.1
- fixed FTBFS (BR:/flags tweak)

* Fri Oct 15 2010 Michael Shigorin <mike@altlinux.org> 1.0-alt11
- applied patch from https://bugs.kde.org/167549
  to fix stack smashing (closes: #22584)

* Tue Jan 12 2010 Michael Shigorin <mike@altlinux.org> 1.0-alt10
- fixed FTBFS with autoconf-2.64 (ender@)

* Wed Jul 29 2009 Michael Shigorin <mike@altlinux.org> 1.0-alt9
- added desktop file patch (repocop)
- added reference to gdmap
- spec cleanup
- buildreq

* Wed Dec 03 2008 Michael Shigorin <mike@altlinux.org> 1.0-alt8
- applied repocop patch

* Sat Oct 18 2008 Michael Shigorin <mike@altlinux.org> 1.0-alt7
- rebuilt

* Sat Oct 18 2008 Michael Shigorin <mike@altlinux.org> 1.0-alt6
- removed Debian menufile (#17597)
- minor spec cleanup

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for filelight
 * update_menus for filelight

* Wed Dec 26 2007 Michael Shigorin <mike@altlinux.org> 1.0-alt5
- set automake version to 1.9

* Sat Nov 03 2007 Michael Shigorin <mike@altlinux.org> 1.0-alt4
- added patch by avm@ to fix sparse file handling
- buildreq

* Mon Oct 22 2007 Michael Shigorin <mike@altlinux.org> 1.0-alt3
- fixed intersections with current filesystem package

* Sat Sep 09 2006 Michael Shigorin <mike@altlinux.org> 1.0-alt2
- *1.0* (forgot to nilify %%define, shame on me)
- fixes #9973 (crash on exit)

* Tue Sep 05 2006 Michael Shigorin <mike@altlinux.org> 1.0-alt1
- 1.0
- macro abuse cleanup
- adjusted configure args

* Tue Jun 20 2006 Michael Shigorin <mike@altlinux.org> 1.0-alt0beta6.1
- rebuild (to get into x86_64)

* Fri Dec 02 2005 Michael Shigorin <mike@altlinux.org> 1.0-alt0beta6
- 1.0-beta6
- adopted an orphan
- fixed TEXTREL
- updated %%files
  + removed COPYING after checking License: tag accordance
  + removed applnk file
  + added lib%name, desktop files
- sanitized translations handling (thanks php-coder@)

* Fri Feb 06 2004 Egor S. Orlov <oes@altlinux.ru> 0.6.4-alt1
- 0.6.4
- fixed la-file search

* Fri Oct 03 2003 Egor S. Orlov <oes@altlinux.ru> 0.6.2-alt2
- Hasher build 

* Thu Sep 18 2003 Egor S. Orlov <oes@altlinux.ru> 0.6.2-alt1
- New version 

* Sun Sep 07 2003 Egor S. Orlov <oes@altlinux.ru> 0.6.1-alt0.1
- Initial build bor ALT 


* Thu Sep 2 2003 - herbert@links2linux.de

- added the doc files
