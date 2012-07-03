%def_disable gnome
%def_without gnomevfs
%def_without gucharmap

Name: abiword-light
Summary: Lean and fast full-featured word processor
Version: 2.8.4
Release: alt1.1
Group: Office
License: GPL
Url: http://www.abisource.com/

Packager: Damir Shayhutdinov <damir@altlinux.ru>

Source: http://www.abisource.com/downloads/abiword/%version/source/abiword-%version.tar.gz
Source1: abiword.desktop
Source6: abiword-48.png.bz2
Source7: abiword-32.png.bz2
Source8: abiword-16.png.bz2
Source10: abiword.keys
Source11: abiword.mime

Patch: abiword-2.8.1-headers.patch

#AutoReq: yes, noshell
Obsoletes: abisuite, abisuite-koi8, abisuite-cp1251, abisuite-iso8859-8

BuildRequires: bzlib-devel gcc-c++ libaiksaurus-gtk-devel libenchant-devel libfribidi-devel
BuildRequires: libots-devel libreadline-devel libgtkmathview-devel librsvg-devel libwmf-devel
BuildRequires: liblink-grammar-devel >= 4.2.1
BuildRequires: libwpd-devel libwpg-devel perl-HTML-Tree t1lib-devel
BuildRequires: libwv-devel boost-devel libdbus-glib-devel libtidy-devel

%if_enabled gnome
BuildRequires: libgnomeoffice-devel libgsf-gnome-devel
%endif
%{?_with_gnomevfs:BuildRequires: gnome-vfs-devel}
%{?_with_gucharmap:BuildRequires: libgucharmap-devel}

Provides: abiword = %version-%release
Conflicts: abiword < %version-%release
Conflicts: abiword > %version-%release
Obsoletes: abiword < 2.6.8-alt3

%description
AbiWord is a cross-platform, Open Source Word Processor developed
by the people at AbiSource, Inc. and by developers from around the world.
(http://www.abisource.com)
It is a lean and fast full-featured word processor. It works on Microsoft
Windows and most Unix Systems. Features include:

   * Basic character formatting (bold, underline, italics, etc.)
   * Paragraph alignment
   * Spell-check
   * Import of Word97 and RTF documents
   * Export to RTF, Text, HTML, and LaTeX formats
   * Document Templates
   * Interactive rulers and tabs
   * Styles
   * Unlimited undo/redo
   * Multiple column control
   * Widow/orphan control
   * Find/Replace
   * Images
   and much more...

%package devel
Group: Development/C++
Summary: Headers for Abiword plugins
Requires: %name = %version-%release
Requires: libfribidi-devel >= 0.10.4

%description devel
Headers and pkgconfig support for  Abiword plugin building.

%prep
%setup -q -n abiword-%version
%patch -p1 -b .headers

%build

%configure %{subst_with gnomevfs} \
	%{subst_with gucharmap} \
	%{subst_enable gnome} \
	--enable-print \
	--enable-plugins \
	--enable-templates \
	--enable-clipart \
	--enable-dynamic \
	--disable-static

%make_build

%install
%make_install DESTDIR=%buildroot install

mkdir -p $RPM_BUILD_ROOT%_datadir/mime-info
mkdir -p $RPM_BUILD_ROOT%_libdir/abiword-2.8/plugins
install -m 644 %SOURCE10 %SOURCE11  $RPM_BUILD_ROOT%_datadir/mime-info

sed -i 's/fribidi >= 0.10.4//g' %buildroot%_pkgconfigdir/abiword-2.8.pc
# (fg) Icons
mkdir -p $RPM_BUILD_ROOT%_liconsdir
mkdir -p $RPM_BUILD_ROOT%_niconsdir
mkdir -p $RPM_BUILD_ROOT%_miconsdir
mkdir -p $RPM_BUILD_ROOT%_datadir/pixmaps
bzcat %SOURCE6 > $RPM_BUILD_ROOT%_liconsdir/abiword.png
bzcat %SOURCE7 > $RPM_BUILD_ROOT%_niconsdir/abiword.png
bzcat %SOURCE8 > $RPM_BUILD_ROOT%_miconsdir/abiword.png

mv $RPM_BUILD_ROOT%_iconsdir/abiword_48.png $RPM_BUILD_ROOT%_datadir/pixmaps/

install -D %SOURCE1 %buildroot%_desktopdir/

%files
#_bindir/AbiWord-2.6
%_bindir/abiword
%dir %_libdir/abiword-2.8
%dir %_libdir/abiword-2.8/plugins
%_miconsdir/*
%_liconsdir/*
%_niconsdir/abiword.png
%_datadir/pixmaps/abiword_48.png
%_datadir/abiword-2.8
%_datadir/mime-info/*
%_desktopdir/abiword.desktop
%_libdir/abiword-2.8/plugins/*.so
%_libdir/libabiword-2.8.so
%exclude %_libdir/abiword-2.8/plugins/*.la
%_man1dir/*

%files devel
%_includedir/*
%_pkgconfigdir/*

#TODO: apply %%lang tags to localized files /usr/share/abiword-2.8/strings/*.strings (5 Mb)

%changelog
* Tue Oct 11 2011 Michael Shigorin <mike@altlinux.org> 2.8.4-alt1.1
- NMU: rebuilt against current libwv

* Mon Apr 19 2010 Damir Shayhutdinov <damir@altlinux.ru> 2.8.4-alt1
- Updated to 2.8.4 (light version)
  + Fixed problem with multiple deletion of cyrillic symbols

* Tue Apr 06 2010 Damir Shayhutdinov <damir@altlinux.ru> 2.8.2-alt2
- Link plugins against libabiword (Closes #23288)

* Thu Feb 18 2010 Damir Shayhutdinov <damir@altlinux.ru> 2.8.2-alt1
- Updated to 2.8.2
- Fix icondir repocop warning
- Built with new libgnomeoffice

* Sat Jan 02 2010 Damir Shayhutdinov <damir@altlinux.ru> 2.8.1-alt3
- Added fixes by Yuri Sedunov <aris@>

* Wed Nov 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt2
- updated buildreqs
- removed/replaced obsolete configure options
- build goffice, grammar, wpg plugins
- libtidy support
- patched for build against our libwmf and libtidy
- fixed MimeType in abiword.desktop
- packaged additional templates and clipart

* Sat Nov 14 2009 Damir Shayhutdinov <damir@altlinux.ru> 2.8.1-alt1
- Updated to 2.8.1

* Sat Sep 19 2009 Damir Shayhutdinov <damir@altlinux.ru> 2.6.8-alt4
- Packaged no-gnome build into abiword-light (without devel)

* Mon Sep 14 2009 Damir Shayhutdinov <damir@altlinux.ru> 2.6.8-alt3
- Removed libgda-devel from BuildRequires
- Built with gnome

* Wed May 06 2009 Damir Shayhutdinov <damir@altlinux.ru> 2.6.8-alt2
- Fix building with gcc4.4

* Sun Apr 26 2009 Damir Shayhutdinov <damir@altlinux.ru> 2.6.8-alt1
- Updated to 2.6.8

* Fri Dec 05 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.6.5-alt1
- Updated to 2.6.5
- Removed update/clean desktopdb macros

* Sat Nov 22 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.6.4-alt2
- Enabled libabiword building

* Sun Oct 12 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.6.4-alt1
- New stable version

* Tue May 13 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.6.3-alt1
- New stable version 

* Sat Mar 29 2008 Damir Shayhutdinov <damir@altlinux.ru> 2.5.2-alt3
- Synced desktop file with upstream's one (#14985)
- Added update/clean desktopdb macros to post/postun

* Mon Oct 29 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.5.2-alt2
- Disable more GNOME components (gucharmap) 

* Sun Sep 16 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.5.2-alt1
- 2.5.2 development version.

* Mon Apr 16 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.5.1-alt1
- 2.5.1 development version. 

* Fri Mar 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.4.6-alt2
- Built with system libwv.

* Thu Nov 16 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.4.6-alt1
- New version: 2.4.6

* Wed Oct 04 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.4.5-alt5
- Bumped release to build with new gucharmap

* Sat Sep 23 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.4.5-alt4
- Updated build requires.

* Tue Jul 11 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.4.5-alt3
- New version

* Tue Jun 20 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.4.4-alt3
- Repackaged for x86_64

* Sun May 28 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.4.4-alt2
- New version

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.4.1-alt3.1
- Rebuilt with libreadline.so.5.

* Fri Dec 09 2005 Vital Khilko <vk@altlinux.ru> 2.4.1-alt3
- build with libgtkmathview
- #8643

* Thu Dec 01 2005 Vital Khilko <vk@altlinux.ru> 2.4.1-alt2
- fix #8170

* Wed Nov 23 2005 Vital Khilko <vk@altlinux.ru> 2.4.1-alt1
- 2.4.1
- patch for new libgda2 
- patch for new libgnomedb
- patch for new libgnomeoffice
- enable link-grammar

* Tue Nov 08 2005 Vital Khilko <vk@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Thu Sep 15 2005 Vital Khilko <vk@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Tue Jul 26 2005 Vital Khilko <vk@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Wed Apr 06 2005 Vital Khilko <vk@altlinux.ru> 2.2.7-alt1
- 2.2.7

* Tue Feb 22 2005 Vital Khilko <vk@altlinux.ru> 2.2.4-alt1
- 2.2.4

* Fri Jan 21 2005 Vital Khilko <vk@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Thu Jan 20 2005 Vital Khilko <vk@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Sep 21 2004 Vital Khilko <vk@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Thu Jun 24 2004 Vital Khilko <vk@altlinux.ru> 2.1.3-alt1
- bugfix release

* Thu May 13 2004 Vital Khilko <vk@altlinux.ru> 2.1.2-alt2
- fixed #4132
- added belarusian templates
- added be_SU locale support

* Tue Apr 27 2004 Vital Khilko <vk@altlinux.ru> 2.1.2-alt1
- new version
- builded with enchant support

* Wed Jul 30 2003 AEN <aen@altlinux.ru> 1.99.3-alt1
- new version

* Thu Jul 10 2003 AEN <aen@altlinux.ru> 1.9.2-alt1
- new version

* Tue Jul 08 2003 AEN <aen@altlinux.ru> 1.9.1-alt1
- new gtk2/gnome2 version
- build cvs post-1.9.1 source

* Wed Sep 25 2002 AEN <aen@altlinux.ru> 1.0.3-alt1
- new version
- built w/o gnome

* Thu Jun 06 2002 AEN <aen@logic.ru> 1.0.2-alt1
- new version

* Sun Jun 02 2002 AEN <aen@logic.ru> 1.0.1-alt1
- new version

* Mon Mar 18 2002 AEN <aen@logic.ru> 0.99.3-alt1
- new version

* Mon Jan 14 2002 AEN <aen@logic.ru> 0.9.4.1-alt6
- rebuilt with gal-0.19

* Wed Nov 22 2001 AEN <aen@logic.ru> 0.9.4.1-alt5
- print patch

* Fri Nov 09 2001 AEN <aen@logic.ru> 0.9.4.1-alt4
- rebuild with new libgal

* Fri Oct 25 2001 AEN <aen@logic.ru> 0.9.4.1-alt3
- rebuild with new libgal

* Thu Oct 11 2001 AEN <aen@logic.ru> 0.9.4.1-alt2
- rebuilt with libpng.so.3

* Tue Oct 9 2001 AEN <aen@logic.ru> 0.9.4.1-alt1
- new version
- build w/o bidi (temporary)

* Wed Sep 05 2001 AEN <aen@logic.ru> 0.9.2-alt2
- rebuild with new libgal
* Thu Aug 16 2001 AEN <aen@logic.ru> 0.9.2-alt1
* Wed Aug 15 2001 AEN <aen@logic.ru> 0.9-alt4
- don't add  Abisource fonts to fontpath!
* Mon Aug 13 2001 AEN <aen@logic.ru> 0.9-alt3
- s/666/644/g
* Fri Aug 10 2001 AEN <aen@logic.ru> 0.9-alt2
- direct print enabled
* Thu Aug 09 2001 AEN <aen@logic.ru> 0.9-alt1
- 0.9
* Tue Jul 17 2001 AEN <aen@logic.ru> 0.9-alt0.4
- new snapshot
- cp1251 added to encodettf

* Wed Jul 11 2001 AEN <aen@logic.ru> 0.9-alt0.3
- i18n patch (belarusian, hebrew & ukrainian support)
* Wed Jul 11 2001 AEN <aen@logic.ru> 0.9-alt0.2
- ABI_USE_100_ISPELL
- use ispell american dictionary

* Wed Jul 11 2001 AEN <aen@logic.ru> 0.9-alt0.1
- snapshot 010709

* Mon Jul 9 2001 AEN <aen@logic.ru> 0.7.14-alt3
- rebuild with libgal-0.9
- new wrapper patch

* Sat Jun 9 2001 AEN <aen@logic.ru> 0.7.14-alt2
- bidi enabled

* Fri May 25 2001 AEN <aen@logic.ru> 0.7.14-alt1
- sync with MDK
- build with gnome
- unichar patch

* Tue Feb 27 2001 AEN <aen@logic.ru>
- 0.7.13

* Thu Nov 30 2000 AEN <aen@logic.ru>
- gcc296 patch
- build for 7.2RE

* Tue Oct 10 2000 AEN <aen@logic.ru>
- two small patches

* Sun Oct 8 2000 AEN <aen@logic.ru>
- New patch from hvv

* Mon Oct 2 2000 AEN <aen@logic.ru>
- build for RE with i18n patch from Vlad Harchev (hvv@hyppo.ru)

* Mon Sep 18 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.7.11-1mdk
- new version
- updated menus patch
- added toolbars patch

* Thu Sep  7 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.7.10-2mdk
- macroszification
- added liconsdir

* Wed Jul 19 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.10-1mdk
- Update to 0.7.10 (from Helix)
- change menu update
- move doc to standard location
- BM

* Sun May 21 2000 David BAUDENS <baudens@mandrakesoft.com> 0.7.9-1mdk
- Fix descriptions (RPM & menu)

* Tue May  2 2000 Vincent Saugey <vince@mandrakesoft.com> 0.7.9-1mdk
- Update to 0.7.9
- Nothing sucks :)

* Sat Apr 15 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.7.8-7mdk
- fg sucks - menu entry really really added this time :-)
- fixed sources location

* Fri Apr 14 2000 David BAUDENS <baudens@mandrakesoft.com> 0.7.8-6mdk
- Real description

* Tue Apr 11 2000 Francis Galiegue <fg@mandrakesoft.com> 0.7.8-5mdk
- Titi sucks - menu entry really added this time
- Titi sucks - %post and %postun were incorrect
- Titi sucks - there were no icons, now there are
- Removed SMP cruft

* Wed Apr 05 2000 Jerome Martin <jerome@mandrakesoft.com> 0.7.8-4mdk
- Fixing distribution tag

* Thu Mar 30 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.7.8-3mdk
- add menu entry

* Thu Mar 30 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.7.8-2mdk
- clean spec: remove last garbages of file lists
- now compliant to the new naming scheme
- fix /usr/share/abisuite/bin/abiword incorectely linked on
  /var/tmp/abisuite-buildroot/usr/share/abisuite/AbiSuite/bin/AbiWord
  This bug is present at least since 0.7.7-3mdk!!

* Sun Mar 19 2000 John Buswell <johnb@mandrakesoft.com> 0.7.8-1mdk
- 0.7.8
- PPC Support

* Tue Jan 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.7.7-2mdk
- Fix alpha/sparc compilation.

* Thu Jan 13 2000 Saugey Vincent <vince@mandrakesoft.com>
- update to 0.7.7

* Thu Oct 21 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- update to 0.7.6

* Thu Sep 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build for cooker.

* Fri Sep 10 1999 Daouda LO <daouda@mandrakesoft.com>
- Mandrake adaptations
- bzipped the sources
- Make the package relocatable

* Sun Sep 05 1999 Vu Hung Quan <binaire@videotron.ca>
- update to 0.7.5 ; redhat adaptation

* Sat Jun 26 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- create (more or less) generic spec file...


