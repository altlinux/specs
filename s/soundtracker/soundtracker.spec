Name: soundtracker
Version: 0.6.8
Release: alt5.qa2

Summary: Sound modules editor/player
License: GPL
Group: Sound
Packager: Yury Aliaev <mutabor@altlinux.ru>

Url: http://www.soundtracker.org/
Source: ftp://ftp.soundtracker.org/pub/soundtracker/v0.6/soundtracker-%version.tar.gz
Source2: %name-icon.png
Source3: %name.control
Source4: %name.1

Patch0: %name-0.6.7-desktop-alt.patch
Patch1: %name-0.6.8-fixjack-up.patch
Patch2: %name-0.6.8-translation-alt.patch
Patch3: %name-0.6.8-gccwarnings-up.patch.bz2
Patch4: %name-0.6.8-utf8overflow-alt.patch.bz2
Patch5: %name-0.6.8-fixjack-alt.patch

Summary(ru_RU.KOI8-R): Редактор/проигрыватель модулей
Summary(uk_UA.KOI8-U): Редактор/трекер модул╕в

# Automatically added by buildreq on Sat Jan 22 2005
#BuildRequires: esound-devel gdk-pixbuf-devel glib-devel glib2 gnome-libs-devel gtk+-devel imlib-devel jackit-devel libaudiofile-devel libdb1-devel libsndfile-devel pkgconfig xorg-x11-devel xorg-x11-libs
BuildRequires: esound-devel gdk-pixbuf-devel glib-devel gtk+-devel imlib-devel jackit-devel libaudiofile-devel libdb1-devel libsndfile-devel pkgconfig libX11-devel
BuildRequires: gnome-libs-devel >= 1.4.2-alt7

%description
Soundtracker is a module tracker for the X Window System similar to
the DOS program `FastTracker'. Soundtracker is based on the XM file
format.  The user interface makes use of GTK+, and, optionally, GNOME.

%description -l ru_RU.KOI8-R
Soundtraker -- графический редактор модулей, похожий на FastTracker и
использующий формат XM. Пользовательский интерфейс на основе библиотек GTK+ и
GNOME (по желанию).

%description -l uk_UA.KOI8-U
Soundtraker -- граф╕чний редактор модул╕в, що схожий на FastTracker та
використову╓ формат XM. ╤нтерфейс користувача на основ╕ б╕бл╕отек GTK+ та
GNOME (опц╕онально).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
unset CC CXX
sed -i 's,chown,echo &,g' `find -name 'Makefile*'`
%configure
%make_build

%install
%makeinstall
install -pD -m644 %SOURCE2 $RPM_BUILD_ROOT%_niconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT%_datadir/pixmaps
ln -s %_niconsdir/%name.png $RPM_BUILD_ROOT%_datadir/pixmaps/%name.png
install -pD -m755 %SOURCE3 %buildroot%_controldir/%name
mkdir -p $RPM_BUILD_ROOT%_datadir/applications
install -pD -m644 %name.desktop $RPM_BUILD_ROOT%_datadir/applications
install -pD -m755 %SOURCE4 %buildroot%_man1dir/%name.1


%find_lang %name

%pre
%pre_control %name

%post
%post_control -s normal %name

%files -f %name.lang
%_bindir/*
%_datadir/pixmaps/*
%_niconsdir/*
%dir %_datadir/%name
%_datadir/%name/*
%config(noreplace) %_controldir/%name
%_man1dir/*
%_desktopdir/*

%doc AUTHORS ChangeLog FAQ NEWS README TODO doc/*.txt


%changelog
* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.8-alt5.qa2
- NMU: converted debian menu to freedesktop

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.8-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * desktop-mime-entry for soundtracker
  * update_menus for soundtracker
  * postclean-05-filetriggers for spec file

* Mon Aug 4 2008 Yury Aliaev <mutabor@altlinux.ru> 0.6.8-alt5
- possible jack driver crash fix
- small desktop entry bug fixed

* Wed Jul 23 2008 Yury Aliaev <mutabor@altlinux.ru> 0.6.8-alt4
- crash when running under UTF-8 locale fixed (#12697 at bugzilla.altlinux.org)
- spec and desktop entry cleanups according to repocop messages

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.6.8-alt3.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for soundtracker

* Tue May 1 2007 Yury Aliaev <mutabor@altlinux.ru> 0.6.8-alt3
- spec file cleanup
- added man page from Debian
- added fix from upstream (less warnings)
- icons issue adjusted one more time according modern requirements
- fixed desktop/menu issue

* Sun Nov 12 2006 Yury Aliaev <mutabor@altlinux.ru> 0.6.8-alt2
- one little fix rtom upstream (jack driver compilation warning)
- Russian translation updated
- icon file name in %name.menu fixed

* Sun Apr 30 2006 Yury Aliaev <mutabor@altlinux.ru> 0.6.8-alt1
- 0.6.8
- adjusted icons/pixmaps issue

* Wed May 18 2005 Yury Aliaev <mutabor@altlinux.ru> 0.6.7-alt7
- added two patches from upstream (midi and xm bugfixes)
- Russian translation updated
- desktop entry updated and now it is packed

* Sat Jan 22 2005 Yury Aliaev <mutabor@altlinux.ru> 0.6.7-alt6
- added patches for extra functionality: permanent channels (see
  ChangeLog), improvements in keyboard recording, extra fucntions
  in sample editor

* Wed Jan 19 2005 Yury Aliaev <mutabor@altlinux.ru> 0.6.7-alt5
- removed malicious patch 1 (which works nowhere except my home)
- fixed control(8) issue
- added some extra fixes

* Tue Mar 23 2004 Michael Shigorin <mike@altlinux.ru> 0.6.7-alt4
- worked around #3759, thanks to Yury Aliaev (mutabor@)

* Sun Feb 08 2004 Yury Aliaev <mutabor@altlinux.ru> 0.6.7-alt3
- fixed "mimetype" menu entry

* Wed Jan 21 2004 Michael Shigorin <mike@altlinux.ru> 0.6.7-alt2
- updated buildrequires; hasher build on behalf of Yury Aliaev
- implemented control(8) support (non-privileged by default)
- libtoolize & co 

* Sun Jan 18 2004 Yury Aliaev <mutabor@altlinux.ru> 0.6.7-alt1
- new version + post-release fixes and additions

* Fri Sep 06 2002 Michael Shigorin <mike@altlinux.ru> 0.6.6-alt1
- largely updated ru.po (thanks to Yury Aliaev <mutabor @ catholic org>)

* Wed Jun 05 2002 Michael Shigorin <mike@altlinux.ru> 0.6.6-alt0.2
- new version
- updated ru.po
- removed --disable-alsa from configure

* Thu Dec 27 2001 Michael Shigorin <mike@altlinux.ru> 0.6.4-alt2
- ru.po cleanup

* Fri Oct 12 2001 Michael Shigorin <mike@altlinux.ru> 0.6.4-alt1
- alt1
- spec cleanup
- soundtracker binary no longer suid root by default
- updated ru.po
