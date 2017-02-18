Name:         xfig
Version:      3.2.6a
Release:      alt1

Summary:      An X Window System tool for drawing basic vector graphics.
Group:        Graphics
URL:          http://epb.lbl.gov/xfig/
License:      Freeware

Packager:     Vladislav Zavjalov <slazav@altlinux.org>
Source:       %name-%version.tar.gz

Requires:     transfig >= 3.2.5 fonts-type1-urw

BuildPreReq:  libXpm-devel libXt-devel libXmu-devel libXaw-devel
BuildPreReq:  libpng-devel libjpeg-devel libXi-devel libXp-devel
BuildPreReq:  libXaw3d-devel >= 1.5e

%description
Xfig is an X Window System tool for creating basic vector graphics,
including arcs, ellipses, bezier curves, lines, rulers and more.
The resulting graphics can be saved, printed on PostScript printers 
or converted to a variety of other formats (e.g., X11 bitmaps, CGM,
Encapsulated PostScript, LaTeX).

You should install xfig if you need a program to create vector graphics.

%package -n xfig-libs
Summary:  XFig image libraries
Group:    Graphics
BuildArch: noarch

%description -n xfig-libs
Library of FIG images

%package -n xfig-docs
Summary:  XFig documentation
Group:    Graphics
BuildArch: noarch

%description -n xfig-docs
XFig documentation

%prep
%setup -q

%build
%autoreconf
%configure --with-appdefaultdir=%_x11appconfdir
%make install DESTDIR=%buildroot

install -D -m 755 xfig.sh      %buildroot/%_bindir/xfig.sh
install -D -m 644 xfig48.png   %buildroot/%_liconsdir/xfig.png
install -D -m 644 xfig32.png   %buildroot/%_niconsdir/xfig.png
install -D -m 644 xfig16.png   %buildroot/%_miconsdir/xfig.png
install -D -m 644 xfig.desktop %buildroot/%_desktopdir/xfig.desktop

%files
%_bindir/xfig
%_bindir/xfig.sh
%_man1dir/*
%_x11appconfdir/*
%_desktopdir/xfig.desktop
%_liconsdir/xfig.png
%_niconsdir/xfig.png
%_miconsdir/xfig.png
%dir /usr/share/xfig/
/usr/share/xfig/CompKeyDB

%files -n xfig-libs
/usr/share/xfig/Libraries

%files -n xfig-docs
/usr/share/doc/xfig

%changelog
* Sat Feb 18 2017 Vladislav Zavjalov <slazav@altlinux.org> 3.2.6a-alt1
- update 3.2.6-beta -> 3.2.6a

* Sun May 15 2016 Vladislav Zavjalov <slazav@altlinux.org> 3.2.6-alt1
- 3.2.6

* Sun Feb 28 2016 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5c-alt3
- fix reading png files with libpng16
  See: https://bugzilla.redhat.com/show_bug.cgi?id=1150330

* Sat Feb 27 2016 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5c-alt2
- a few patches from Roland Rosenfeld (debian):
  - Fix problems with creating PS, EPS and PDF
    when using a locale that uses "," as decimal separator.
  - Revert the change of X-Spline parameter made in 3.2.5c.
  - Fix a hack in arcs and ellipses editing wich does not work with
    position independent executables (PIE).

* Sat Nov 29 2014 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5c-alt1
- 3.2.5c

* Mon Nov 11 2013 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5b-alt9
- fix error with filled objects in new xlib

* Wed May 29 2013 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5b-alt8
- Don't use local SimpleMenu.c with XAW3D1_5E (closes #26956)
- add -DDXAW_INTERNATIONALIZATION for new libXaw3d-1.6.2
- f_read.c: delete comments when deleting objects
- rebuild with libXaw3d-1.6.2

* Sun Oct 14 2012 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5b-alt7
- restore colors and figure comments after delete_all + undo
- fix scrollbar on indpanel after mode change
- fix some build warnings

* Tue Sep 18 2012 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5b-alt6
- fix for libpng15

* Mon Nov 14 2011 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5b-alt5
- add xfig.sh wrapper to avoid utf8 charsets
  and use it in the desktop file (see #26579)
- add save8bit appres to allow saving 8-bit symbols without converting
  into \ooo form
- small fix to the previous commit

* Mon Nov 14 2011 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5b-alt4
- don't use fontsets for symbols and dingbats fonts (closes #26579)

* Sat Feb 19 2011 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5b-alt3
- revert 10pt search tolerance back to 4pt (as in < 3.2.5 )
- bugfixes (see git-log for details):
  - swap depths in undo_load()
  - don't restore filenames in F_ADD/F_DELETE actions
  - restore user colors in new_xfig_request()
  - fix depth handling in undo_join_split()
  - fix xfontlist->fset initialization

* Mon Dec 13 2010 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5b-alt2
- fix errors with help viewer calls
- more accurate fix of wrong cur_mode after zooming

* Mon Dec 13 2010 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5b-alt1
- 3.2.5b

* Wed Nov 03 2010 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt13
- fix xfig.desktop
- rebuild with set-versioned libXaw3d

* Thu Sep 24 2009 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt12
- xfig.desktop: add Categories
- xfig.spec: remove unsupported Vendor tag

* Tue Jun 23 2009 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt11
- rebuild with new libpng

* Tue Jun 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt10
- replace incomplete mkstemp patch from Fedora with one from SUSE (CVE-2009-1962)

* Fri Mar 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt9
- Fig.ad: use 9x18bold for bold fonts
  (7x14bold has no proper alias in bitmap-cyrillic-misc)
- build with xaw3d + increase msg_panel height 18->24 
  (there is no text shown when height is too small for used font;
   xaw3d makes this height smaller)

* Thu Nov 20 2008 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt8
- move directories from spec to Imakefile
- don't use libXaw3d (it breaks msg_panel)
- fix typo in w_msgpanel.c
- fix xfig.desktop

* Wed Nov 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt7
- make libs and docs to be noarch

* Wed Nov 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt6
- fix xfig.desktop according to freedesktop.org policy
- add icons according to altlinux policy

* Mon Nov 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt5
- add BuildPreReq: libXp-devel

* Thu Oct 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt4
- rename "utf8_encoding" option to "locale_encoding" (it must work with any encoding)
- fix null function crash
- do not specify font charsets in international mode

* Tue Sep 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt3
- add utf8 support:
  Fig.eucEncoding: false
  Fig.utf8Encoding: true
  (default settings)

* Fri Sep 26 2008 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt2
- apply some Alt, Fedora and Debian patches
- split into three packages: xfig, xfig-docs, xfig-libs
- problem: only latin characters are ok in text objects...

* Wed Sep 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 3.2.5_alpha5-alt1
- first build

