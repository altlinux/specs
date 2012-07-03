Name:         xfig
Version:      3.2.5b
Release:      alt5

Summary:      An X Window System tool for drawing basic vector graphics.
Group:        Graphics
URL:          http://epb.lbl.gov/xfig/
License:      Freeware

Packager:     Vladislav Zavjalov <slazav@altlinux.org>
Source:       %name-%version.tar.gz
Patch1:       %name-%version-alt.patch

Requires:     transfig >= 3.2.5 fonts-type1-urw

BuildPreReq:  imake xorg-cf-files
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
%patch1 -p1

%build
CDEBUGFLAGS=OptimizedCDebugFlags
# Optimization can break xfig on x86_64?
#%ifarch x86_64
#CDEBUGFLAGS=NoOpCDebugFlags
#%endif
# Uncomment to build with -g flag:
# CDEBUGFLAGS=DebuggableCDebugFlags
xmkmf -DXAW3D -DXAW3D1_5E -DDefaultCDebugFlags=$CDEBUGFLAGS
ln -nfs Doc/xfig.man xfig.man
make DESTDIR=%buildroot

%install
make DESTDIR=%buildroot install.all

install -D -m 755 xfig.sh %buildroot/%_bindir/xfig.sh
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

