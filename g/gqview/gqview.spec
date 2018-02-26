Name: gqview
Version: 2.1.5
Release: alt7

Summary: Image viewer and browser utility
License: GPLv2+
Group: Graphics

Url: http://gqview.sourceforge.net/
Source: http://dl.sourceforge.net/gqview/gqview-%version.tar.gz
Patch0: gqview-2.1.5-editors.patch
Patch1: gqview-1.5.8-zoom-defaults.patch
Patch2: gqview-enable_dng.patch
Patch3: gqview-2.1.5-alt-freedesktop.patch
Patch4: gqview-native-icons.patch
Patch5: gqview-2.1.5-alt-histfile_perms.patch
Patch6: gqview-pixbuf-renderer-use-gdk_region.patch
Patch7: gqview-pixbuf-renderer-use-gdk_window_scroll.patch

# Automatically added by buildreq on Mon Feb 25 2008
BuildRequires: libgtk+2-devel liblcms-devel

%description
GQview is an image viewer for browsing through graphics files.
Features include single click file viewing, support for external
editors, previewing images using thumbnails, and zoom.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p2
%patch7 -p2

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -pD -m644 gqview.png %buildroot%_liconsdir/gqview.png

%find_lang %name

%files -f %name.lang
%doc README
%_bindir/*
%_desktopdir/*
%_pixmapsdir/*
%_liconsdir/*
%_man1dir/*

%changelog
* Thu Jul 15 2010 Vladislav Zavjalov <slazav@altlinux.org> 2.1.5-alt7
- enhance image scrolling (closes #23770)

* Tue Jun 16 2010 Sergey Kurakin <kurakin@altlinux.org> 2.1.5-alt6
- fixed bug with directory icons not presented in theme (closes #23625)

* Tue Jun  3 2010 Sergey Kurakin <kurakin@altlinux.org> 2.1.5-alt5
- system pictogramms in the folders browsing area (closes #18172)
- default permissions for histfile are 0600 (closes #17307)

* Tue Jun  1 2010 Sergey Kurakin <kurakin@altlinux.org> 2.1.5-alt4
- corrected default external editors entries to prefer lossless
  JPEG transformation (closes #21640)
- added default external command: Exif auto-transform
- fixed repocop issue: desktop-file-validate

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.1.5-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * desktop-mime-entry for gqview
  * update_menus for gqview
  * postclean-05-filetriggers for spec file

* Fri Apr 11 2008 Victor Forsyuk <force@altlinux.org> 2.1.5-alt3
- Desktop mime entry fix.

* Mon Feb 25 2008 Victor Forsyuk <force@altlinux.org> 2.1.5-alt2
- Added .dng to list of supported extensions.
- Fix ALT bug #13464 (broken call of Gimp).

* Fri Dec 22 2006 Victor Forsyuk <force@altlinux.org> 2.1.5-alt1
- 2.1.5
- Updated buildrequires.

* Wed Sep 14 2005 Anton Farygin <rider@altlinux.ru> 2.0.1-alt2
- package fixed for x86_64 (mouse@)

* Thu Sep 08 2005 Anton Farygin <rider@altlinux.ru> 2.0.1-alt1
- 2.0.1
- updated russian translation by lav@
- Freedesktop.org menu added

* Thu Mar 03 2005 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Wed Feb 09 2005 Anton Farygin <rider@altlinux.ru> 1.5.8-alt1
- 1.5.8

* Fri Oct 29 2004 Anton Farygin <rider@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Mon Sep 20 2004 Anton Farygin <rider@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Tue Sep 07 2004 Anton Farygin <rider@altlinux.ru> 1.4.3-alt2
- changed default zoom properties (#5029)

* Tue May 11 2004 Anton Farygin <rider@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Tue Apr 13 2004 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Tue Mar 02 2004 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Sat Feb 28 2004 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Mar 10 2003 Rider <rider@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Fri Jan 24 2003 Rider <rider@altlinux.ru> 1.2.1-alt1
- new version

* Fri Dec 13 2002 Rider <rider@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Oct 05 2002 Rider <rider@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Wed Jan 30 2002 Rider <rider@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sat Jan 05 2002 Rider <rider@altlinux.ru> 1.0.1-alt2
- fix default HELP path
- removed XV from default config file

* Thu Jan 03 2002 Rider <rider@altlinux.ru> 1.0.1-alt1
- 1.0.1
- russian summary and description

* Thu Dec 27 2001 Stanislav Ievlev <inger@altlinux.ru> 0.12.0-alt2
- spec cleanup.
- added Belarusian translation

* Sat Nov 13 2001 Rider <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Fri Oct 12 2001 AEN <aen@logic.ru> 0.11.0-alt2
- rebuilt with libpng.so.3

* Fri Jun 08 2001 Rider <rider@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Sun Jan 14 2001 AEN <aen@logic.ru>
- RE adaptation

* Mon Sep 25 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.8.2-6mdk
- changed icon

* Tue Sep  5 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.8.2-5mdk
- icons
- further macroszification

* Thu Aug 24 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.8.2-4mdk
- macros
- added %%lang

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.8.2-3mdk
- automatically added BuildRequires

* Thu Jun 22 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.8.2-2mdk
- change url, thanks Jan.

* Thu Jun 22 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.8.2-1mdk
- v0.8.2
- add locale
- fix install & files section

* Fri Apr 28 2000 Daouda Lo <daouda@mandrakesoft.com> 0.7.0-10mdk
- add icon (32*32 and 16*16)
- cleanup spec file

* Wed Apr 05 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.7.0-9mdk
- merge menu file with spec
- clean spec

* Thu Mar 21 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.7.0-8mdk
- fix rpmlint warnings

* Mon Mar 20 2000 Lenny Cartier <lenny@mandrakesoft.com>
- clean specfile
- add menu entry

* Wed Nov 10 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- Updated URL
- Added icon
* Thu Jul 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 0.7.0.
* Tue May 11 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions
* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)
* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- strip binaries
* Sat Mar 6 1999 Michael Fulbright <drmike@redhat.com>
- version 0.6.0
* Wed Oct 7 1998 John Ellis <gqview@geocities.com>
- updated for version 0.4.2
* Fri Sep 11 1998 John Ellis <gqview@geocities.com>
- updated for version 0.4.1
* Sat Aug 15 1998 John Ellis <gqview@geocities.com>
- updated for version 0.4.0
* Wed Aug 5 1998 Joel Young <jyoung@erols.com>
- enhanced rpm .spec file
