Name: logjam
Version: 4.5.3
Release: alt9.qa2

Summary: LogJam is a client for LiveJournal.com
Summary(ru_RU.UTF-8): LogJam - клиент для LiveJournal.com

License: GPL
Group: Networking/Other
Url: http://logjam.danga.com

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://logjam.danga.com/download/%name-%version.tar
Source1: ru_RU.po

# Patches from Fedora package
Patch2:		logjam-4.4.1-backdated.patch
Patch3:		logjam-4.4.1-cleanups.patch
Patch4:		logjam-4.4.1-fedora-desktop.patch
Patch5:		logjam-4.5-patch8-manfix.patch
Patch6:		logjam-4.5.3-gtkhtml314.patch
Patch7:		logjam-4.4.1-ru.po.asp.patch
Patch8:		logjam-4.5.3-gtkspell.patch
Patch9:		http://people.freebsd.org/~novel/patches/non-freebsd/logjam_docklet_context_menu.diff
Patch10:	logjam-4.5.3-rhythmbox-fix.patch
Patch11:	logjam-libsoup24.patch
Patch12:	logjam-4.5.3-disable-threads.patch
Patch13:	logjam-title.patch
Patch14:	logjam-4.5.3-tags.patch
Patch15:	logjam-4.5.3-default-spelllang-en-US.patch

# Additional patches (see bug #15821)
Patch20:	logjam-4.5.3-close_when_send.patch
Patch21:	logjam-4.5.3-start_in_dock2.patch
Patch22:	logjam-4.5.3-no_quit_when_docked2.patch

# Bug #21193
Patch23:	logjam-4.5.3-useragent.patch

Patch24:	logjam-4.5.3-localequotes.patch
Patch25:	logjam-4.5.3-potfiles.patch

# Bug #19768
Patch26:	logjam-4.5.3-mpris.patch

# Bug #19776
Patch27:	logjam-4.5.3-tagsdialog.patch

# Bug #9516
Patch28:	logjam-4.5.3-docname.patch

# Automatically added by buildreq on Sun Oct 24 2010
BuildRequires: glibc-devel intltool libdbus-glib-devel libgtkhtml3-devel libgtkspell-devel librsvg-devel libsoup-devel libsqlite3-devel libxml2-devel
BuildRequires: desktop-file-utils

%description
"LiveJournal.com... because you like to think other people care."
LogJam is a client for LiveJournal.  It sits unobtrusively in the
corner of your screen, waiting for you to have something worthwhile to
tell the world.

%prep
%setup -q
#%patch0 -p1
%patch2 -p1 -b .backdated
%patch3 -p1 -b .cleanups
%patch4 -p1 -b .desktop
%patch5 -p1 -b .manfix
%patch6 -p1 -b .gtkhtml318
#%patch7 -p1 -b .ru.po
%patch8 -p1 -b .bz186906
%patch9 -p1 -b .docklet-context-menu
%patch10 -p1 -b .rhythmboxfix
%patch11 -p1 -b .libsoup
%patch12 -p1 -b .disable-threads
%patch13 -p1 -b .title
%patch14 -p1 -b .tags
%patch15 -p1 -b .default-spelllang-en-US
%patch20 -p1 -b .close

%patch21 -p1 -b .dock
%patch22 -p1 -b .no_quit
%patch23 -p1 -b .useragent
%patch24 -p2 -b .localquotes
%patch25 -p2 -b .potfiles

%patch26 -p1 -b .mpris
%patch27 -p1 -b .tagsdialog
%patch28 -p2 -b .docname

cp -f %SOURCE1 po/ru_RU.po

%build
#sed -i 's,\.la,.so,' configure
touch protocol/liblivejournal/NEWS protocol/liblivejournal/AUTHORS NEWS AUTHORS README
%autoreconf

# Fixing locale files
sed -i 's,ru_RU,ru,'  configure
sed -i 's,uk_UA,uk,'  configure
mv po/ru_RU.po po/ru.po
mv po/uk_UA.po po/uk.po

%configure --with-gtkhtml314

%make_build

%install
%makeinstall_std
install -pD -m644 images/logjam_pencil.png %buildroot%_iconsdir/%{name}.png
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=WebDevelopment \
	%buildroot%_desktopdir/logjam.desktop

%files -f %name.lang
%_bindir/logjam
%_datadir/pixmaps/*
%_man1dir/*
%_datadir/applications/*
%_iconsdir/%{name}.png
%doc doc/TODO doc/README COPYING ChangeLog

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.3-alt9.qa2
- Fixed build

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 4.5.3-alt9.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for logjam
  * postclean-03-private-rpm-macros for the spec file

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 4.5.3-alt9
- update buildreqs (libxml2-devel was missed)

* Sat Mar 20 2010 Vitaly Lipatov <lav@altlinux.ru> 4.5.3-alt8
- add MPRIS support (bug #19768)
- impove tags dialogue (bug #19776)
- add support for locale dependent quotes
- update russian translation
- fix window title from filename (bug #9516)
- update buildreqs

* Mon Aug 24 2009 Vitaly Lipatov <lav@altlinux.ru> 4.5.3-alt7
- fix User-Agent string (bug #21193)
- drop obsoleted entries from spec, drop xmms support

* Sat Jul 26 2008 Vitaly Lipatov <lav@altlinux.ru> 4.5.3-alt6
- do not quit in docklet mode (fix bug #15658)

* Mon Jun 30 2008 Vitaly Lipatov <lav@altlinux.ru> 4.5.3-alt5
- change packager, cleanup spec
- add patches from Fedora (also bug #15821, thanks to Andy Shevchenko)
- build with libgtkhtml3.14 (bug #15811)

* Mon Jul 23 2007 Eugene V. Horohorin <genix@altlinux.ru> 4.5.3-alt4
- buildreq updated

* Sun Jan 07 2007 Eugene V. Horohorin <genix@altlinux.ru> 4.5.3-alt3
- disable xmms helper (rebuild with --enable xmms option if you need)

* Tue May 02 2006 Eugene Suchkov <cityhawk@altlinux.ru> 4.5.3-alt2
- libenchant-devel build dependecy added

* Tue Mar 07 2006 Eugene Suchkov <cityhawk@altlinux.ru> 4.5.3-alt1
- New version build
- Now using sqlite 

* Mon Feb 13 2006 Eugene Suchkov <cityhawk@altlinux.ru> 4.5.2-alt2
- Added build dependency on libpopt-devel 

* Tue Jan 03 2006 Eugene Suchkov <cityhawk@altlinux.ru> 4.5.2-alt1
- New version build

* Mon Dec 05 2005 Eugene Suchkov <cityhawk@altlinux.ru> 4.5.1-alt2
- libgtkhtml-3.8 support
- menu entry icon added

* Tue Sep 06 2005 Eugene Suchkov <cityhawk@altlinux.ru> 4.5.1-alt1
- New version build

* Sat Apr 02 2005 Ivan Evtuhovich <brun@altlinux.ru> 4.4.1-alt2
- New build because of Sisyhpus changes

* Sun Jan 16 2005 Ivan Evtuhovich <brun@altlinux.ru> 4.4.1-alt1
- Logjam 4.4.1 released
- Enable libgtkhtml3 -- version 3.1 works just fine, appropriate patch
  added

* Sun May 16 2004 Ivan Evtuhovich <brun@altlinux.ru> 4.4.0-alt1
- Logjam 4.4.0 released
- Enable libgtkhtml3 -- version 3.1 works just fine

* Tue Feb 09 2004 Sergey Degtyaryov <maga@altlinux.ru> 4.3.0-alt2
- Logjam 4.3.0 release. 
- Disabled libgtkhtml3 -- problem with libgnomeui-2.la
- Added protocol docs to /usr/share/gtk-doc/

* Tue Feb 04 2004 Sergey Degtyaryov <maga@altlinux.ru> 4.3.0-alt1.pre2
- Logjam 4.3.0pre2

* Sat Sep 20 2003 Ivan Evtuhovich <brun@altlinux.ru> 4.2.4-alt1
- 

* Sun Jun 08 2003 Artem K. Jouravsky <ujo@altlinux.ru> 4.2.0-alt1
-  New version

* Fri May 16 2003 Artem K. Jouravsky <ujo@altlinux.ru> 4.1.2-alt1
- Initial revision.
