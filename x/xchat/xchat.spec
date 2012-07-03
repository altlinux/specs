%define ver_major 2.8

Name: xchat
Version: %ver_major.6
Release: alt2.3

Summary: Graphical IRC client
Summary(ru_RU.UTF-8): Графический IRC клиент

Group: Networking/IRC

License: %gpl2plus
URL: http://www.xchat.org/

Packager: Egor Vyscrebentsov <evyscr@altlinux.org>

Source: http://www.xchat.org/files/source/%ver_major/%name-%version.tar

Provides: xchat2 = %version-%release
Obsoletes: xchat2

# Upstream patches
Patch0: %name-2.8.6-alt1.patch
Patch1: %name-2.8.6-sf-gtk.patch
Patch2: %name-2.8.6-alt-desktop.patch
Patch3: %name-2.8.6-enable_deprecated.patch
Patch4: %name-2.8.6-alt-glib2-2.32.3.patch

Source2: %name.xpm
Source4: %name-wmconfig
Source5: %name-16.png
Source6: %name-32.png
Source7: %name-48.png

Source9: xchat-README.ALT.utf-8

%define xchatlibdir %_libdir/%name
%define xchatpluginsdir %xchatlibdir/plugins

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: GConf libXext-devel libsexy-devel libssl-devel perl-devel python-devel tcl-devel

%description
X-Chat is yet another IRC client for the X Window System, using the Gtk2+
toolkit. It is pretty easy to use compared to the other Gtk2+ IRC clients and
the interface is quite nicely designed.

%description -l ru_RU.UTF-8
X-Chat - это отличный IRC клиент для системы X Window, использующий набор
инструментов GTK2+. Прекрасный дизайн интерфейса, удобные функции и легкие
настройки являются отличительной особенностью этого приложения для общения.

%prep
%setup -n %name-%version

%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p2
%patch4 -p2

touch NEWS
touch ABOUT-NLS

%autoreconf

%build
%configure \
    --disable-gnome \
    --disable-dbus \
    --enable-tcl=%_libdir \
    --enable-shm \
    --enable-spell=libsexy \
    xchatlibdir=%xchatlibdir
%make

%install
%makeinstall

# plugins
mkdir -p %buildroot%xchatpluginsdir
for i in python.so perl.so tcl.so; do
	mv %buildroot%_libdir/$i %buildroot%xchatpluginsdir/
done
rm -f %buildroot%_libdir/*.la

# wmconfig
mkdir -p %buildroot/etc/X11/wmconfig
install -m 644 %SOURCE4 %buildroot/etc/X11/wmconfig/%name

# icons
mkdir -p %buildroot{%_miconsdir,%_niconsdir,%_liconsdir}/
install -m 644 %SOURCE5 %buildroot%_miconsdir/%name.png
install -m 644 %SOURCE6 %buildroot%_niconsdir/%name.png
install -m 644 %SOURCE7 %buildroot%_liconsdir/%name.png

cp -a %SOURCE9 ./README.ALT.utf-8

%find_lang %name

%files -f %name.lang
%doc README ChangeLog HACKING INSTALL faq.html README.ALT.utf-8 plugins/plugin20.html
%_bindir/%name
/etc/X11/wmconfig/xchat
%_datadir/pixmaps/%name.*
%_desktopdir/*.desktop
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%dir %xchatlibdir
%dir %xchatpluginsdir
%xchatpluginsdir/*.so

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.6-alt2.3
- Fixed build with new glib2 2.32.3

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.8.6-alt2.2.1
- Rebuild with Python-2.7

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 2.8.6-alt2.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.8.6-alt2.1
- fixed build with recent gtk
- rebuilt with perl 5.12

* Sat May 01 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 2.8.6-alt2
- Fixes for changes in GTK API
- Fixed xchat.desktop

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.6-alt1.1
- Rebuilt with python 2.6

* Tue Dec 02 2008 Anton Farygin <rider@altlinux.ru> 2.8.6-alt1
- new version
- removed included to mainstream patches:
    Patch0: xc284-fix-scrollbfdleak.patch
    Patch1: xc284-improvescrollback.patch
    Patch2: xc284-scrollbmkdir.patch
- really added debian patches

* Thu Apr 24 2008 Egor Vyscrebentsov <evyscr@altlinux.ru> 2.8.4-alt1
- new version: 2.8.4
- enabled tcl plugin
- fixed tcl plugin build for x86_64

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 2.6.6-alt1.1.1
- Rebuilt with python-2.5.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.6.6-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Jul 22 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.6-alt1
- 2.6.6

* Thu Jun 15 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.4-alt2
- add various patches from upstream, Debian and PLD

* Sat Jun 10 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Sun Apr 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.2-alt1
- 2.6.2
- fix icons directories
- set default encoding for FreeNode and RusNet to KOI8-R (#7564)
- disable dbus plugin

* Fri Jan 20 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.1-alt1
- NMU:
  + 2.6.1, update Patch10, Patch14
  + package %%xchatlibdir and %%xchatpluginsdir (#8728)
  + package desktop file, do not package menu file

* Tue Apr 05 2005 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.4.3-alt1
- 2.4.3 

* Wed Jan 19 2005 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.4.1-alt1
- 2.4.1 
- translation by Dmitry Alexeyev <dmi@qnx.org.ru>
- xc241-fix-fetext.diff

* Wed Jul 14 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.10-alt3
- *.la removed (plugins work without it)
- New browser probe order: $XCHAT_BROWSER, mozilla -remote 'openURL(url),new-tab , gnome-open, $BROWSER
- See README.ALT.koi8-r for details
- xc2010-fixtabcomp2.diff
- xc2010-fixfocus.diff 
- Some buildreq fixes

* Wed Jul 14 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.10-alt2
- *.la removed (plugins work without it)
- New browser probe order: $XCHAT_BROWSER, mozilla -remote 'openURL(url),new-tab , gnome-open, $BROWSER
- See README.ALT.koi8-r for details
- xc2010-fixtabcomp2.diff
- xc2010-fixfocus.diff 

* Tue Jul 06 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.10-alt1
- 2.0.10
- xc2010-fixtabcomp.diff mainstream patch applied

* Sat Jul 03 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.9-alt3
- Special for Master 2.4 default font changed to "Sans 10"

* Wed Jun 09 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.9-alt2
- xc209-fixbidi.diff applied 

* Mon Jun 07 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.9-alt1
- 2.0.9
- startup scripts removed
- now xchat doesn't stop when recieve SIGHUP
- for more see mainstream Changelog

* Fri Apr 23 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.8-alt2
- Provides, Obsoletes fix (thanx Voins) 

* Thu Apr 15 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.8-alt1
- replaced by xchat2
- 2.0.8
- xc208-fixsocks5.diff
- Default font fixed 12
- ~/.xchatrc per user setup file

* Sun Oct 12 2003 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.5-alt5
- add patch for nick autocompletion suffix character (changed to ':') 

* Sat Oct 11 2003 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.5-alt4
- By default xchat is startup with GDK_USE_XFT=0 (AntiAliasing off)
- README.ALT.koi8-r added
- Note that default nick autocompletion char is now ',' if you want to use it stop xchat remove ~/.xchat2 and restart xchat or simply change completion_suffix variable in ~/.xchat2/xchat.conf
- xchat2.spec: %files section fixed

* Thu Oct 09 2003 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.5-alt3
- 2.0.5 version
- localization
- FreeNode:#altlinux and RusNet:#lrn is added to servlist

* Sat Jun 28 2003 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.2-alt3
- some changes in spec
- rename xchat.spec to xchat2.spec
- first upload to incoming

* Sat Jun 21 2003 Sergey V Turchin <zerg at altlinux dot org> 2.0.2-alt2
- patch to $BROWSER execution
- patch to xvt execution
- patch to don't conflict with xchat-1.x.x package
- build without gnome (this is only extra requires to gnome-libs)

* Fri Jun 20 2003 Pavel S. Khmelinsky <hmepas@altlinux.ru> 2.0.2-alt1
- First builded xchat for GTK2

* Wed Jan 15 2003 Rider <rider@altlinux.ru> 1.8.11-alt2
- updated server list
- added requires to translation-tables

* Sat Jan 04 2003 Rider <rider@altlinux.ru> 1.8.11-alt1
- 1.8.11
- specfile cleunup
- bulrequires fix
- cool png icons

* Thu Oct 31 2002 Rider <rider@altlinux.ru> 1.8.10-alt4
- rebuild (new perl)

* Wed Sep 25 2002 Rider <rider@altlinux.ru> 1.8.10-alt3
- gcc 3.2 rebuild

* Mon Aug 12 2002 Rider <rider@altlinux.ru> 1.8.10-alt2
- spec bugfix

* Thu Aug 08 2002 Rider <rider@altlinux.ru> 1.8.10-alt1
- 1.8.10

* Fri May 31 2002 Rider <rider@altlinux.ru> 1.8.9-alt1
- 1.8.9
- small ru.po updated
- irc.yauza.ru added to default servers list

* Sun Mar 10 2002 Rider <rider@altlinux.ru> 1.8.8-alt1
- 1.8.8
- build without gnome-libs
- updated russian po file
- added russian summary and description
- enable socks support

* Fri Jan 18 2002 Rider <rider@altlinux.ru> 1.8.7-alt2
- fix history buffer

* Thu Jan 10 2002 Rider <rider@altlinux.ru> 1.8.7-alt1
- 1.8.7

* Fri Dec 14 2001 Rider <rider@altlinux.ru> 1.8.6-alt1
- 1.8.6

* Sat Nov 03 2001 Rider <rider@altlinux.ru> 1.8.5-alt1
- 1.8.5

* Fri Sep 28 2001 Rider <rider@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Mon Sep 10 2001 Rider <rider@altlinux.ru> 1.8.3-alt1
- russian translation updated from Valek <frob@df.ru>
- 1.8.3
- default font fix.

* Wed Aug 22 2001 Rider <rider@lrn.ru> 1.8.2-alt2
- russian translation updated

* Fri Aug 17 2001 Rider <rider@lrn.ru> 1.8.2-alt1
- 1.8.2

* Thu Jul 26 2001 Stanislav Ievlev <inger@altlinux.ru> 1.8.0-alt2
- Rebuilt with new perl. Cleanup spec.

* Fri Jun 29 2001 AEN <aen@logic.ru> 1.8.0-alt1
- 1.8.0 release

* Mon Jun 25 2001 AEN <aen@logic.ru> 1.7.3-alt1
- sync with mdk
- built with new perl
- disable python

* Fri Feb 16 2001 Rider <rider@linux.ru.net> 1.6.4-ipl1mdk
- new release (1.6.3)

* Thu Jan 20 2001 Anton B. Farygin <rider@linux.ru.net> 1.6.3-ipl3mdk
- removed text-mode xchat
- enable gnome support
- enable python scripts support

* Mon Jan 15 2001 Anton B. Farygin <rider@linux.ru.net> 1.6.3-ipl2mdk
- add text-mode xchat
- add openssl support
- disable gnome

* Sun Jan 14 2001 Anton B. Farygin <rider@linux.ru.net> 1.6.3-ipl1mdk
- new version: 1.6.3
- add RusNet server list to default servers
- add russian package description
- disabled python support

* Mon Jan  1 2001 Stefan van der Eijk <s.vandereijk@chello.nl> 1.6.2-1mdk
- shiny new version: 1.6.2
- add configure option --disable-textfe ; because of nasty python2 problem

* Wed Nov 15 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.6.0-1mdk
- new and shiny source bumped into cooker.

* Wed Nov 08 2000 Daouda Lo <daouda@mandrakesoft.com> 1.5.11-1mdk
- release

* Mon Nov 06 2000 Daouda Lo <daouda@mandrakesoft.com> 1.5.10-1mdk
- new release (gcc2.96 build)
- repatch fontset

* Thu Sep 07 2000 Alexandre Dussart <adussart@mandrakesoft.com> 1.4.3-2m
- Use find_lang.

* Mon Aug 28 2000 Geoffrey Lee <snailtalk@mandrakesoft.com. 1.4.3-1mdk
- rebuild for new version (security fix.)
- macrosifications.
- fix the installation of LC_MESSAGES.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4.2-2mdk
- automatically added BuildRequires

* Tue Jun 13 2000 Alexandre Dussart <adussart@mandrakesoft.com> 1.4.2-1mdk
- 1.4.2

* Thu Apr 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.4.1-3mdk
- fixed larger icon
- fixed menu postun
- removed useless gnome desktop entry

* Fri Apr 14 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.4.1-2mdk
- add menu entry with icon

* Sat Apr 1  2000 Jerome Dumonteil <jd@mandrakesoft.com>
- fix group
- add menu
- version 1.4.1

* Fri Feb 11 2000 Geoffrey Lee <snailtalk@linux-mandrake.com>
- 1.4

* Sun Feb 06 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.3.12-2mdk
- added patch for fontset support (asiatic languages use fontsets)
- added the language catalogs to the %files section

* Thu Jan 27 2000 Alexandre Dussart <adussart@mandrakesoft.com>
- 1.3.12

* Fri Jan 14 2000 Alexandre Dussart <adussart@mandrakesoft.com>
- 1.3.10

* Wed Dec 08 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- 1.3.8(official now ;)

* Fri Nov 26 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- 1.3.8
- Updated source URL.

* Wed Nov 10 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- 1.3.7(fix many bugs)

* Fri Oct  29 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- 1.3.5
- Updated URL.
- Updated doc section(added AUTHORS and xchat.sgml)
- Added fr description.

* Thu Oct  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.3.4.

* Wed Sep 15 1999 Daouda LO <daouda@mandrakesoft.com>
- 1.2.0

* Mon Aug 16 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.1.8

* Fri Aug 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.1.7

* Tue Aug 03 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Why --disable-perl? (Removed)
- --enable-socks
- Icon for rpm
- 1.1.6 :
    * lots see /usr/doc/xchat-1.1.6/Changelog

* Mon Jul 26 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Rebuild (2mdk)

* Sat Jul 17 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 1.1.2 :
    - Swedish translation update (Joel Rosdahl).
    - A better default popup menu (rm ~/.xchat/popup.conf if you want it)
    - Conference mode button - doesn't display join/parts.
    - Email addresses are clickable (in the main text area).
    - Hostnames and IP numbers are clickable (right click only).
    - If you joined two channels with the same people in them, userhost
      would mess up a bit - fixed.
    - Added /UNIGNORE
    - Added reverse ignore flag, eg:
      /ignore *!*@*.aol.com ALL
      /ignore myfriend!myfriend@*.aol.com ALL UNIGNORE
      (Would ignore everyone on AOL except myfriend).
    - Added Sort and Cancel buttons to ignore GUI.
    - Function Keys removed - "Edit Key Bindings" replaces it.
    - "Announce away messages" option (Sean 'Shaleh' Perry).
    - IRC::print takes multiple args (Bruce Ide).
    - Sending USERHOSTs on join are throttled so you don't excess flood
      on big channels.
    - Misc touchups.
    1.1.0 -> 1.1.1:
    - Text Events are hookable through perl (Matthias Urlichs).
      ( IRC::add_print_handler() )
    - A few palette stuff ups fixed (affected only non-zvt windows).
    - Major cleanups in text.c (TextEvents) (AGL).
    - Ignore GUI/Load/Save added (David H.rdeman).
    - USERHOST is issued on joining channels to find people's hostname.
    - Added perl command IRC::user_list (see perl.c).
    - Palette is saved in palatte.conf instead of xchat.conf.

* Mon Jul 05 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.1.0.
	 - Serbian translation (Zoltan Csala).
	 - URLs and nicknames are clickable (right click), still a bit
	   dodgy in zvt.
	 - Added IRC::print_with_channel( text, channel, servername )
	   (3rd arg is optional).
	 - Size/Pos/CPS are right justified in DCC windows.
	 - Updated French translations (Gissehel).
	 - Palette editor.
	 - 'Auto Open DCC CHAT window' option added (Javier Kohen).
	 - /Ignore added (no GUI yet).
	 - SaveBuffer in ZVT windows now works (Javier Kohen).
	 - Wildcard match in Channel List.
	 - DNS Program setting (use host, nslookup, or similar)
	 - "New Shell Tab" feature (requires GNOME).
	 - "Edit Key Bindings" feature (AGL).
	 - Dialog windows have a 'Chat' button (Fredrik Berglund).
	 - Trailing dots in url's are chopped.
	 - se.po renamed to sv.po
	 - Ran *.c and *.h through indent, should be nice and consistant now.
	 - Added recognition of WALLOPS from server.
	 - Updated Russian translation (Volosenkov Dmitry).
	 - Fixed a lockup bug (Affected FreeBSD and possibly others).

* Thu May  6 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 28 1999 Michael Fulbright <drmike@redhat.com>
- version 0.9.4

* Thu Mar 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.9.3

* Mon Mar 8 1999 Michael Fulbright <drmike@redhat.com>
- version 0.9.2

