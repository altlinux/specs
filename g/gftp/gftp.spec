Name: gftp
Version: 2.0.19
Release: alt2.qa1

Summary: Multithreaded FTP client for X Window
Summary(ru_RU.KOI8-R): Многопотоковый FTP-клиент для X Window
License: GPL
Group: Networking/File transfer
Url: http://www.%name.org/

Packager: Pavel Vainerman <pv@altlinux.ru>

Source: ftp://gftp.seul.org/pub/gftp/%name-%version.tar.bz2
#Source: ftp://gftp.seul.org/pub/gftp/gftp-2.0.18.tar.bz2
Source1: %name-48.xpm.bz2
Source2: %name-32.xpm.bz2
Source3: %name-16.xpm.bz2
Source4: %name-%version.ru.po
Patch: %name-%version.patch

# Automatically added by buildreq on Sun Feb 26 2006
BuildRequires: docbook-utils fontconfig freetype2 glib2-devel libatk-devel libcairo-devel libgtk+2-devel libpango-devel libssl-devel pkg-config desktop-file-utils
Requires: %name-text = %version-%release %name-gtk = %version-%release
PreReq: gtk2-ssh-askpass

%package -n %name-common
Summary: common files for gftp
Group: Networking/File transfer
Summary: common files for gftp
Summary(ru_RU.KOI8-R): Общие файлы, требуемые для gftp

%package -n %name-gtk
Summary: Multithreaded FTP client for X Window
Summary(ru_RU.KOI8-R): Многопотоковый FTP-клиент для X Window
License: GPL
Group: Networking/File transfer
Requires: %name-common = %version-%release

%package -n %name-text
Summary: gftp Console version
Group: Networking/File transfer
Summary: gftp text mode
Summary(ru_RU.KOI8-R): Текстовый вариант gftp
Requires: %name-common = %version-%release

%description
gFTP is a multithreaded FTP client

%description -n %name-gtk
gFTP is a multithreaded FTP client for X Window written using Gtk. It features
simultaneous downloads, resuming of interrupted file transfers, file transfer
queues, downloading of entire directories, ftp proxy support, remote directory
caching, passive and non-passive file transfers, drag-n-drop, bookmarks menu,
stop button, and many more features.

%description -n %name-gtk -l ru_RU.KOI8-R
gFTP -- это многопотоковый FTP-клиент для X Window, использующий Gtk2.
Он поддерживает одновременную закачку нескольких файлов, докачку
файла после обрыва соединения, очередь закачки, загрузку каталогов целиком,
ftp-прокси, кэширование удалённых каталогов, пассивный и не пассивный режимы
передачи файлов, копирование файлов переносом мышкой, меню с закладками,
кнопку останова и многие другие возможности.

%description -n %name-common
Common files for gftp
%description -n %name-common -l ru_RU.KOI8-R
Общие файлы требуемые для gftp.

%description -n %name-text
Console version gftp
%description -n %name-text -l ru_RU.KOI8-R
Консольная версия gftp.

%prep
%setup -q
%patch -p0
cp -f %SOURCE4 po/ru.po
rm -f po/ru.gmo

%build
%configure
%make_build
(cd po/; %make update-gmo)

%install
%makeinstall

# menu
# TODO: report the .desktop upstream
desktop-file-install --dir %buildroot%_desktopdir \
		      --remove-category=Application \
		      --add-category=FileTransfer \
		      %buildroot%_desktopdir/%name.desktop

sed -i -e 's,Icon=%name\.png,Icon=%name,' %buildroot%_desktopdir/%name.desktop

# icon
mkdir -p $RPM_BUILD_ROOT%_niconsdir
mkdir -p $RPM_BUILD_ROOT%_liconsdir
mkdir -p $RPM_BUILD_ROOT%_miconsdir
bzcat %SOURCE1 > $RPM_BUILD_ROOT%_liconsdir/%name.xpm
bzcat %SOURCE2 > $RPM_BUILD_ROOT%_niconsdir/%name.xpm
bzcat %SOURCE3 > $RPM_BUILD_ROOT%_miconsdir/%name.xpm

%find_lang %name

%files
%files -n %name-common -f %name.lang
%_bindir/gftp
%doc THANKS ChangeLog README TODO
%_mandir/man1/*

%files -n %name-text
%_bindir/gftp-text

%files -n %name-gtk
%_bindir/gftp-gtk
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/pixmaps/*.png
%_niconsdir/*.xpm
%_liconsdir/*.xpm
%_miconsdir/*.xpm

%changelog
* Sat Apr 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.19-alt2.qa1
- NMU: dropped obsolete menu entry

* Mon Feb 21 2011 Pavel Vainerman <pv@altlinux.ru> 2.0.19-alt2
- rebuild new version

* Sun Feb 20 2011 Pavel Vainerman <pv@altlinux.ru> 2.0.19-alt1
- new version (2.0.19) 

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.18stable-alt5.qa1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Fri Jan 15 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.18stable-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for gftp
  * update_menus for gftp-gtk
  * postclean-05-filetriggers for spec file

* Thu Nov 06 2008 Pavel Vainerman <pv@altlinux.ru> 2.0.18stable-alt5
- build for new gcc4.3

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.18stable-alt4.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Tue Jan 08 2008 Pavel Vainerman <pv@altlinux.ru> 2.0.18stable-alt4
- add patch for correct locale in gftp-text (bug #7861)

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.18stable-alt3.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Mar 04 2006 Pavel Vainerman <pv@altlinux.ru> 2.0.18stable-alt3
- corrected iconsdir in files section

* Sun Feb 26 2006 Pavel Vainerman <pv@altlinux.ru> 2.0.18stable-alt2
- rebuild BuildRequires

* Sat Feb 12 2005 Pavel Vainerman <pv@altlinux.ru> 2.0.18stable-alt1
- new version

* Tue Dec 07 2004 Pavel Vainerman <pv@altlinux.ru> 2.0.18rc1-alt1
- new version
- update ru.po
- correction package requires
- fixed bug 5388 (invalid menufile)
- add path for fixed bug 5206 (drop russian words)
- add path for fixed bug in gftp-text: utf8 --> locale

* Thu May 27 2004 Pavel Vainerman <pv@altlinux.ru> 2.0.17-alt1
- new version

* Wed Jan 28 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.16-alt2
- backported patch for date problem (bug #3550)
- update ru.po
- spec review, change packager, add man page to files

* Sun Nov 09 2003 Vitaly Lipatov <lav@altlinux.ru> 2.0.16-alt1
- new version
- update ru.po

* Sun Sep 21 2003 Vitaly Lipatov <lav@altlinux.ru> 2.0.15-alt1
- new version
- build in hasher

* Mon Mar 31 2003 Vitaly Lipatov <lav@altlinux.ru> 2.0.14-alt2
- add PreReq fpr *-ssh-askpass

* Mon Jan 06 2003 Vitaly Lipatov <lav@altlinux.ru> 2.0.14-alt1
- new version
- update russian translation
- add scrollkeeper to post/postun
- add genericname to menu

* Wed Oct  9 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.13-alt4
- rebuild with gtk 2.1

* Wed Sep 18 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.13-alt3
- rebuild with new XFree86

* Sun Sep 08 2002 Vitaly Lipatov <lav@altlinux.ru> 2.0.13-alt2
- update russian translation
- add russian description to spec

* Tue Aug 13 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.13-alt1
- 2.0.13
- cleanup spec
- TODO: to see try-mutex patch in MDK

* Tue Jun 17 2002 AEN <aen@logic.ru> 2.0.12-alt1
- new version

* Fri Jan 04 2002 AEN <aen@logic.ru> 2.0.11-alt1
- new version

* Tue Apr 24 2001 Kostya Timoshenko <kt@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation

* Mon Aug 28 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 2.0.7b-2mdk
- menu entry inside spec file
- crash with gtk+ compiled with debug=no ; backtraced and reported to
  author
- changed icon into official one and added 48x48

* Tue Aug 08 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0.7b-1mdk
- new release
- fix macros

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0.7a-2mdk
- automatically added BuildRequires

* Tue Jul 25 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0.7a-1mdk
- new release

* Mon Jul 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0.7-1mdk
- 2.0.7
- macros

* Fri Apr 28 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0.6a-5mdk
- patched menu entry, added 32x32 icon

* Tue Apr 11 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0.6a-4mdk
- added icon

* Sat Apr  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0.6a-3mdk
- added menu entry
- added url

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 2.0.6a-2mdk
- match new group structure

* Wed Dec 22 1999 Vincent Saugey <vince@mandrakesoft.com>
- 2.0.6a
	* More stable version
	* many new improvement (translation, transfert window, etc ..)

* Mon Nov 1 1999 Vincent Saugey <vincent@mandrakesoft.com>
- 2.0.5a
   *Fixed problem with gFTP forgetting your passwords
   *When you drag a file from gFTP, it will not send the password over
   *When you drop a file to gFTP, if there is no password, it will prompt you for one
   *Added Japanese and partian Korean translation and Unicode fixes
   *Fixed French and German translations. I didn't mark some strings with N_( and some strings got commented out
   *Fixed file handle leak in transfer of files (yikes!)

* Wed Sep 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.0.5
-Added gettext support. A French and German tranlsation is included with this
version. If you would like to do a translation of gFTP, please email
me first just to make sure someone else isn't already doing one.
-Ifyou right click on the log window, or in the edit bookmarks dialog, it will bring up a menu.
-Added bandwidth throttling
-Fixed problem with stopping file transfers
-Fixed problem with Use Proxy under the FTP menu not working properly with a http proxy
-Fixed problem with some file transfers not completing properly
-Fixed problem with remote editing of files sometimes not working
-Added manpage, gftp(1)
-Makefiles are now generated by automake
-Other small bug fixes and enhancements

* Thu Aug 26 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 2.0.4pre1

* Fri Jul  9 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.0.3 version :
    * Many bug fixes. I should have all known bugs fixed
    * Now parses some NT, MacOS, and Novell ftp servers output
    * Added support for logging in with the ACCOUNT command
    * Added a users guide for newbies. See USERS-GUIDE
    * You can now disable some columns in the local and remote listboxes in the
      config file. You can also set the columns to auto-resizing
    * Added debian/ directory to main distribution

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Mandrake adaptations.

* Fri Jun 25 1999 Ryan Weaver <ryanw@infohwy.com>
  [gftp-2.0.2-1]
- Removed Use same connection option. Now when you download a file, the
  remote window automagically becomes cached, and the file transfer will use
  the same connection. It will only open a second connection when it has to.
- Added support to be able to drag urls from Netscape to the Open URL button
  on the toolbar. Also cleaned up the drag and drop code.
- Added drop down history box on the local and remote directory entry widget
- HTTP Proxy fixups to make it work with squid-2.2.STABLE3. Please email me
  about how this works/doesn't work with other http proxies.
- Added option to show hidden files
- Several bookmarks bug fixes
- Various other small bug fixes
- Added .spec file to main distribution

* Wed May 19 1999 Ryan Weaver <ryanw@infohwy.com>
  [gftp-2.0.1-3]
- I have changed installation prefix to /usr instead of /usr/X11R6
  to conform more to RH installations.

* Mon May 17 1999 Ryan Weaver <ryanw@infohwy.com>
  [gftp-2.0.1-2]
- Building with gtk+-1.2.3 now because of bugs in gtk+-1.2.2

* Mon May 17 1999 Ryan Weaver <ryanw@infohwy.com>
  [gftp-2.0.1-1]
- Changes from 2.0.0 to 2.0.1
- Main screen is now more responsive during downloads
- Various small bug fixes

- Changes from 1.13 to 2.0.0
- Added toolbar with stop button
- Removed connection manager and added Bookmarks menu
- Added tree based bookmark editor
- Added option to preserve file permissions of transfered files
- Added option to use the same connection for downloads
- Added auto-retry option. If you set the number of retries to 0, it will
  keep trying until you either stop it or it logs in
- Removed read() and write() timeouts
- Fixed problem only allowing you to log in on port 21
- Fixed problem with recursively getting remote directories and files
- HTTP proxy fixups
- Many other small bug fixes and enhancements

- Note to users upgrading from a previous version: there are a few config file
  changes:
- If you are using a http proxy, set your use_proxy type in the config
  file to type 100.
- Since gFTP uses a bookmarks menu now, you will have to change your
  host= lines. A line in the old config file will have:
  host=Debian Sites:Debian:ftp.debian.org:21:/debian:anonymous:@EMAIL@:1
  You will have to change it to something like:
  host=Debian Sites/Debian:ftp.debian.org:21:/debian:anonymous:@EMAIL@:1
  The first column is the menu path. You can have
  Menu/Submenu/Submenu/Debian in order to nest items into submenus.

* Tue Apr  6 1999 Ryan Weaver <ryanw@infohwy.com>
  [gftp-1.13-2]
- Installing fixed gftprc available on the home page.

* Wed Mar 31 1999 Ryan Weaver <ryanw@infohwy.com>
  [gftp-1.13-1]
- Added graphical configuration
- Uses a lot less memory
- Separated all ftp code into gnome-ftp library
- Now prompts the user to reconnect on connect error
- Added much more efficient transfer dialog for when the files exist
- Added local and remote chmod support
- Added support for HTTP proxies
- Added another FTP proxy type
- Added support for EPLF directory listings
- Now uses a configure script to generate the makefile
- Added Save Password feature in the connection manager
- Added more keyboard shortcuts
- Various bug fixes
- Improved internal design

* Tue Feb 16 1999 Ryan Weaver <ryanw@infohwy.com>
  [gftp-1.12-1]
- Added the ability to edit local and remote files
- Added the ability to associate with a file extension a file viewer
  and the default download type (ASCII or BINARY).
- Added anti-idle tool. Please do not abuse this feature
- Better remote symlink handling
- Removed some icons from the distribution
- Added another FTP proxy type
- Several small enhancements

