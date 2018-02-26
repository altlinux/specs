Name: gtk+
Version: 1.2.10
Release: alt20

Summary: The GIMP ToolKit (GTK+), a library for creating GUIs for X
License: LGPL
Group: System/Libraries
Url: http://www.gtk.org/

Source0: ftp://ftp.gimp.org/pub/gtk/v1.2/gtk+-%version.tar
Source1: gtkrc_utf8.tar
Patch1: gtk+-1.2.9-be.patch
Patch2: gtk+-1.2.9-rc.patch
Patch3: gtk+-1.2.9-rc2.patch
Patch4: gtk+-1.2.8-advanced-gtkfilesel.patch
Patch5: gtk+-1.2.10-rh-encoding.patch
Patch6: gtk+-1.2.10-alt-linkage.patch
Patch7: gtk+-1.2.10-rh-m4.patch
Patch8: gtk+-1.2.10-rh-clistfocusrow.patch
Patch9: gtk+-1.2.10-rh-bellvolume.patch

# (fc) 1.2.10-2mdk ximian patch changing drawing when no shadow is set for menubar
Patch102: gtk+-1.2.6-ximian-noborder.patch
# (pablo) better gtkrc definitions
Patch103: gtk+-1.2.10-mdk-gtkrc_files.patch
# (fc) 1.2.10-8mdk GNOME CVS patch correcting bad focus (seen in Evolution and gnomecc)
Patch104: gtk+-1.2.10-cvs-focus.patch
# (pablo) load locale based gtkrc (GNOME CVS)
Patch105: gtk+-1.2.10-cvs-rclocale.patch
# (fc) 1.2.10-10mdk fix alignement warning on ia64 (Rawhide)
Patch106: gtk+-1.2.10-rh-alignment.patch
# (fc) 1.2.10-10mdk Improve exposure compression (GNOME CVS)
Patch107: gtk+-1.2.10-cvs-expose.patch
# (fc) 1.2.10-10mdk Don't screw up CTEXT encoding for UTF-8 (Rawhide)
Patch108: gtk+-1.2.10-rh-ctext.patch
# (fc) 1.2.10-10mdk Accept KP_Enter as a synonym for Return everywhere (Rawhide)
Patch109: gtk+-1.2.10-rh-kpenter.patch
# (fc) 1.2.10-10mdk Allow theme switching to work properly when no windows are realized (Rawhide)
Patch110: gtk+-1.2.10-mdk-themeswitch.patch
# (fc) 1.2.10-10mdk Fix crash when switching themes (Rawhide)
Patch111: gtk+-1.2.10-rh-pixmapref.patch
# (fc) 1.2.10-10mdk Fix computation of width of missing characters (Rawhide)
Patch112: gtk+-1.2.10-rh-missingchar.patch
# (fc) 1.2.10-20mdk set _NET_WM_PID on gdkwindow (GNOME CVS)
Patch115: gtk+-1.2.10-cvs-netwmpid.patch
# (fc) 1.2.10-22mdk fix Fix check of wrong variable on gtklabel (GNOME CVS)
Patch116: gtk+-1.2.10-cvs-labelvariable.patch
# (fc) 1.2.10-22mdk fix GtkCombo occasionally segfaults after content is changed and list shown (GNOME CVS) Bugzilla 58024
Patch117: gtk+-1.2.10-mdk-gtklist.patch
# (fc) 1.2.10-22mdk option menu doesn't appear centered when applied a border (GNOME CVS) Bugzilla 54585
Patch118: gtk+-1.2.10-cvs-border.patch
# (fc) 1.2.10-22mdk DnD code doesn't notice new windows (GNOME CVS) Bugzilla 56349
Patch119: gtk+-1.2.10-cvs-dndnewwindow.patch
# (fc) 1.2.10-26mdk don't set -L/usr/lib in gtk-config
Patch120: gtk+-1.2.10-mdk-libdir.patch
# (fc) 1.2.10-27mdk Fix file selection delete-dir when changing directory problem
# also, fix memory corruption problem when changing directories. (Rawhide)
Patch121: gtk+-1.2.10-rh-deletedir.patch 
# fc) 1.2.10-27mdk Improve warning for missing fonts (Rawhide)
Patch122: gtk+-1.2.10-rh-fontwarning.patch
# (fc) 1.2.10-27mdk Allow themes to make scrollbar trough always repaint (rawhide)
Patch123: gtk+-1.2.10-rh-troughpaint.patch
# (fc) 1.2.10-28mdk Fix a crash that can happen in some apps when the current
# locale is not supported by XLib. (rawhide)
Patch124: gtk+-1.2.10-rh-localecrash.patch
# (fc) 1.2.10-29mdk fix loop and crash in file selector when / is not readable (bug #90)
Patch125: gtk+-1.2.10-mdk-fileselectorfallback.patch
# (fc) 1.2.10-30mdk change default colors to match GTK2 2.2 colors
Patch126: gtk+-1.2.10-mdk-defaultcolor.patch
# (fc) 1.2.10-45mdv ugly hack to skip argb visuals
Patch128: gtk+-1.2.10-mdk-argb.patch
# (fc) CJK polish
Patch129: gtk+-1.2.10-ahiguti.patch
# (fc) PPC64
Patch130: gtk+-1.2.10-rh-ppc64.patch

%set_autoconf_version 2.13
%set_automake_version 1.4
%set_libtool_version  1.5

BuildPreReq: libtool_1.5 >= 3:1.5-alt10

# Automatically added by buildreq on Thu Feb 22 2007
BuildRequires: glib-devel glibc-devel-static imake libXi-devel libXt-devel xorg-cf-files

# it's also currently required by xorg-server-common
# but let's be explicit just in case
Requires: fonts-bitmap-misc

%package devel
Summary: Development tools for GTK+ (GIMP ToolKit) applications
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Requires: glib-devel libX11-devel

%package devel-static
Summary: Static libraries for GTK+ (GIMP ToolKit) applications
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release

%description
This package contains the GIMP ToolKit (GTK+), a library for creating
graphical user interfaces for the X Window System.  GTK+ was originally
written for the GIMP (GNU Image Manipulation Program) image processing
program, but is now used by several other programs as well.

To use GTK1 in UTF-8 locales, you are advised to install these packages:
* fonts-bitmap-75dpi
* fonts-bitmap-cyrillic (for Cyrillic glyphs)

%description devel
The %name-devel package contains the header and support files needed for
developing GTK+ (GIMP ToolKit) applications.  The %name-devel package
contains GDK (the General Drawing Kit, which simplifies the interface for
writing GTK+ widgets and using GTK+ widgets in applications), and GTK+
(the widget set).

%description devel-static
This package contains the static libraries needed for developing
GTK+ (GIMP ToolKit) statically linked applications.

%prep
%setup

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p0
%patch9 -p1

subst -p 's/az /az be /g' configure*

%patch102 -p1 -b .noshadow
#patch103 -p1 -b .gtkrc -- conflicts with rc.patch
%patch104 -p1 -b .focus
#patch105 -p1 -b .rclocale -- superseded by rh-encoding.patch
%patch106 -p1 -b .ia64
%patch107 -p1 -b .expose
%patch108 -p1 -b .ctext
%patch109 -p1 -b .kpenter
%patch110 -p1 -b .themeswitch
%patch111 -p1 -b .pixmapref
%patch112 -p1 -b .missingchar
%patch115 -p1 -b .netwmpid
%patch116 -p1 -b .labelvariable
%patch117 -p1 -b .gtklist
%patch118 -p1 -b .border
%patch119 -p1 -b .dndnewwindow
%patch120 -p1 -b .libdir
#patch121 -p1 -b .deletedir -- conflicts with advanced-gtkfilesel.patch
%patch122 -p1 -b .fontwarning
%patch123 -p1 -b .troughpaint
%patch124 -p1 -b .localecrash
%patch125 -p1 -b .fileselectorfallback
%patch126 -p1 -b .defaultcolor
%patch128 -p1 -b .argb
%patch129 -p1 -b .ahiguchi
%patch130 -p1 -b .ppc64

%build
%def_disable static
export ac_cv_prog_INDENT=indent
libtoolize --copy --force
automake --foreign --include-deps --add-missing --copy
autoconf
autoheader
%configure %{subst_enable static} --with-xinput=xfree
%make_build

%install
%makeinstall

cd %buildroot%_sysconfdir/gtk
mv gtkrc.uk gtkrc.uk_UA.koi8u
ln -s gtkrc.ru_RU.cp1251 gtkrc.uk_UA.cp1251
ln -s gtkrc.uk_UA.koi8u gtkrc.ru_UA.koi8u
subst -p 's/14/12/g' gtkrc.uk_UA.koi8u
tar xf %SOURCE1
cd -

%define pkgdocdir %_docdir/%name-%version
mkdir -p %buildroot%pkgdocdir/devel
install -p -m644 AUTHORS NEWS README TODO %buildroot%pkgdocdir
cp -a docs/{*.txt,html,text} %buildroot%pkgdocdir/devel

%find_lang %name

%files -f %name.lang
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/NEWS
%pkgdocdir/README
%pkgdocdir/TODO
%_libdir/lib*.so.*
%_datadir/themes/Default
%config(noreplace) %_sysconfdir/gtk/

%files devel
%dir %pkgdocdir
%pkgdocdir/devel/
%_libdir/lib*.so
%_libdir/pkgconfig/*
#_libdir/lib*.la
%_man1dir/*.*
%_infodir/*.info*
%_includedir/*
%_datadir/aclocal/*
%_bindir/*

%if_enabled static
%files devel-static
%_libdir/lib*.a
%endif

%changelog
* Sat Feb 26 2011 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt20
- Rebuilt for debuginfo.

* Fri Dec 17 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt19
- Fixed "gtk-config --libs" output.

* Sat Oct 23 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt18
- Rebuilt for soname set-versions.

* Sun May 31 2009 Michael Shigorin <mike@altlinux.org> 1.2.10-alt17
- added font dependency and hints
  (actually fonts-bitmap-misc is enough)

* Sun May 31 2009 Michael Shigorin <mike@altlinux.org> 1.2.10-alt16
- fixed FTBFS with current toolchain
- added patches from Fedora-devel:
  + CJK enhancements patch by Akira Higuchi
  + ppc64 patch

* Thu Feb 22 2007 Alexey Tourbin <at@altlinux.ru> 1.2.10-alt15
- mdk-argb.patch (Frederic Crozat): in gdk_init(), set XLIB_SKIP_ARGB_VISUALS=1
  environment before calling XOpenDisplay(), so as to prevent crashes when
  composite is enabled (#8225, #8354)

* Tue Sep 05 2006 Alexey Tourbin <at@altlinux.ru> 1.2.10-alt14
- merged in Michael Shigorin's changes:
  * Mon Dec 26 2005 Michael Shigorin <mike@altlinux.org> 1.2.10-alt13.M30.1
  - fixed gtkrc_utf8.tar.bz2:
    + added support for "fixed" and "terminus" iso10646 fonts
    + added ru_UA.utf8
  - added unicode font package suggestion to description
- updated dependencies for modular X
- changelog not packaged
- specfile cosmetics

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.10-alt13.1
- Rebuilt for new pkg-config dependencies.

* Sun Apr 17 2005 Alexey Tourbin <at@altlinux.ru> 1.2.10-alt13
- in sync with 1.2.10-40mdk (some 20 more patches)
- added gtkrc.ru_UA.koi8u (#1642)

* Fri Aug 27 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt12
- Relaxed fix made in previous package release,
  to support broken packages.

* Thu Aug 26 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt11
- Fixed library linkage.
- Relocated documentation.
- Fixed underquoted m4 definition (Tim Waugh).

* Tue Dec 02 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt10
- Do not even build static library by default.
- Require libtool_1.5 >= 3:1.5-alt10 for build.

* Thu Nov 27 2003 Alexey Tourbin <at@altlinux.ru> 1.2.10-alt9
- Do not package .la files.
- Do package pkgconfig files.
- Do not package devel-static by default.

* Thu Oct 31 2002 AEN <aen@altlinux.ru> 1.2.10-alt8
- gtkfilesel patch from Aleksey Morozov
- RH encoding patches

* Tue Sep 17 2002 AEN <aen@altlinux.ru> 1.2.10-alt7
- rebuilt with gcc-3.2

* Sun Jun 12 2002 AEN <aen@logic.ru> 1.2.10-alt6
- set default font size in gtkrc.koi8u to 12

* Thu May 23 2002 AEN <aen@logic.ru> 1.2.10-alt5
- really fixed ...

* Wed May 22 2002 AEN <aen@logic.ru> 1.2.10-alt4
- ukrainian gtkrc fixed

* Thu Mar 21 2002 AEN <aen@logic.ru> 1.2.10-alt3
- back to old gdkselection (bug #547)

* Fri Jul 06 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.10-alt2
- spec cleanup
- turned info on, swept garbage from docs
- devel-static subpackage

* Wed Apr 4 2001 AEN <aen@logic.ru> 1.2.10-alt1
- 1.2.10

* Sun Mar 4 2001 AEN <aen@logic.ru> 1.2.9-ipl4mdk
- new gdkselelection.c back, fixed

* Sun Mar 4 2001 AEN <aen@logic.ru> 1.2.9-ipl3mdk
- back to old gdkfont

* Sat Mar 3 2001 AEN <aen@logic.ru> 1.2.9-ipl2mdk
- back to old gdkselect

* Sat Mar 3 2001 AEN <aen@logic.ru> 1.2.9-ipl1mdk
- 1.2.9
- new be & rc patches

* Wed Feb 21 2001 AEN <aen@logic.ru>
- build w/o submenu patch

* Fri Jan 05 2001 AEN <aen@logic.ru>
- kk & ky added
- finally remove Pablo patches

* Sun Nov 27 2000 AEN <aen@logic.ru>
- sync with RE
- be & rc patches

* Fri Nov 03 2000 DindinX <odin@mandrakesoft.com> 1.2.8-7mdk
- rebuild with gcc-2.96

* Thu Oct 26 2000 DindinX <odin@mandrakesoft.com> 1.2.8-6mdk
- Solve show Big5(temporality) (from Andrew Lee <andrew@cle.linux.org.tw>)

* Tue Oct 24 2000 DindinX <odin@mandrakesoft.com> 1.2.8-5mdk
- Backported the submenu-navigation patch
- Added many docs to gtk+-devel

* Mon Aug 28 2000 DindinX <odin@mandrakesoft.com> 1.2.8-4mdk
- remove --enable-debug=no since some programs segfault because of this
  (reported by Frederic Crozat)

* Fri Aug 25 2000 DindinX <odin@mandrakesoft.com> 1.2.8-3mdk
- use %%lang and %%make
- add the noreplace flag for %%config

* Tue Aug 01 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.8-2mdk
- rebuild with macros
- rebuild for BM
- misc fixes

* Wed Jun 7 2000 DindinX <odin@mandrakesoft.com> 1.2.8-1mdk
- 1.2.8

* Tue Mar 21 2000 DindinX <odin@mandrakesoft.com> 1.2.7-4mdk
- corrected the paths in glib-config

* Tue Mar 21 2000 DindinX <odin@mandrakesoft.com> 1.2.7-3mdk
- Patches cleanups (now use 1.2.7 from www.gtk.org instead of 1.2.4 + patches

* Mon Mar 20 2000 DindinX <odin@mandrakesoft.com> 1.2.7-2mdk
- Group and spec fixes

* Sat Feb 19 2000 DindinX <odin@mandrakesoft.com> 1.2.7-1mdk
- 1.2.7

* Thu Jan 27 2000 DindinX <odin@mandrakesoft.com> 1.2.6-8mdk

- disable all debugging stuff by adding --enable-debug=no to the configure
  script.

* Thu Jan 20 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2.6-7mdk

- enabled XInput support

* Thu Jan  6 2000 Pixel <pixel@mandrakesoft.com>
- more stars in the fontset of et of vi_VN.tcvn

* Thu Jan  6 2000 Pixel <pixel@mandrakesoft.com>
- really 1.2.6 (and silimi)

* Fri Nov 05 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- New po files from Pablo
- Remove summary/description clutter

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Enable SMP build/check
- 1.2.6

* Wed Sep 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Real 1.2.5 (chmou sux).
- 1.2.5

* Tue Aug 31 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- a little i18n patch for gfontsel
- latest translations
- tooltip colours in /etc/gtkrc

* Thu Aug 26 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.2.4

* Tue Aug 24 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove completely the /etc/gtk/gtkrc (completely sucks :-(( )

* Sat Aug 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove style "default-text" in gtkrc (cause trouble with i18n language).

* Fri Jul 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Rebuild without glib-1.3 :-((

* Wed Jul 14 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- included latest *.po files from GNOME CVS
- and added back descriptions from RH 5.2
- added an icon for the rpm

* Thu Jul 08 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- put back --sysconfdir=/etc for config time (otherwise the files on /etc are
  never read)

* Mon Jun 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build for new environment.

* Thu May 12 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 1.2.3

* Fri Apr 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adpatations.

* Thu Apr 01 1999 Michael Fulbright <drmike@redhat.com>
- patches from owen to handle various gdk bugs

* Sun Mar 28 1999 Michael Fulbright <drmike@redhat.com>
- added XFree86-devel requirement for gtk+-devel

* Thu Mar 25 1999 Michael Fulbright <drmike@redhat.com>
- version 1.2.1

* Wed Mar 17 1999 Michael Fulbright <drmike@redhat.com>
- removed /usr/info/dir.gz file from package

* Fri Feb 26 1999 Michael Fulbright <drmike@redhat.com>
- Version 1.2.0

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- version 1.2.0pre2, patched to use --sysconfdir=/etc

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- patched in Owen's patch to fix Metal theme

* Fri Feb 05 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.15

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.14

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.13

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.12

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- added Theme directory to file list
- up to 1.1.7 for GNOME freeze

* Sun Oct 25 1998 Shawn T. Amundson <amundson@gtk.org>
- Fixed Source: to point to v1.1

* Tue Aug 04 1998 Michael Fulbright <msf@redhat.com>
- change %%postun to %%preun

* Mon Jun 27 1998 Shawn T. Amundson
- Changed version to 1.1.0

* Thu Jun 11 1998 Dick Porter <dick@cymru.net>
- Removed glib, since it is its own module now

* Mon Apr 13 1998 Marc Ewing <marc@redhat.com>
- Split out glib package

* Tue Apr  8 1998 Shawn T. Amundson <amundson@gtk.org>
- Changed version to 1.0.0

* Tue Apr  7 1998 Owen Taylor <otaylor@gtk.org>
- Changed version to 0.99.10

* Thu Mar 19 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.9
- Changed gtk home page to www.gtk.org

* Thu Mar 19 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.8

* Sun Mar 15 1998 Marc Ewing <marc@redhat.com>
- Added aclocal and bin stuff to file list.
- Added -k to the SMP make line.
- Added lib/glib to file list.

* Fri Mar 14 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.7

* Fri Mar 14 1998 Shawn T. Amundson <amundson@gimp.org>
- Updated ftp url and changed version to 0.99.6

* Thu Mar 12 1998 Marc Ewing <marc@redhat.com>
- Reworked to integrate into gtk+ source tree
- Truncated ChangeLog.  Previous Authors:
  Trond Eivind Glomsrod <teg@pvv.ntnu.no>
  Michael K. Johnson <johnsonm@redhat.com>
  Otto Hammersmith <otto@redhat.com>
