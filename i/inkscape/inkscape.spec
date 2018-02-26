%define pre %nil
Name: inkscape
Version: 0.48.2
Release: alt3.1.1

Summary: A Vector Drawing Application

License: GPL
Group: Graphics
Url: http://inkscape.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version%pre.tar

Source1: %name-%version.ru.po
Source2: tutorial-%version.tar

Patch: %name.patch
# https://bugs.launchpad.net/inkscape/+bug/487038
Patch5: inkscape-0.47-poppler-GfxColorSpace.patch
Patch6: inkscape-0.48.0-spell.patch
Patch7: inkscape-0.48.0-poppler-0.16.patch
Patch8: inkscape-0.48.2-alt-glib2-2.32.0.patch

# Typical environment for GTK program
Requires(post,postun): desktop-file-utils
#BuildPreReq: menu-devel
BuildPreReq: desktop-file-utils

%add_findreq_skiplist %_datadir/%name/extensions/*

# Automatically added by buildreq on Mon Jul 06 2009 (-bi)
BuildRequires: boost-devel gcc-c++ gnome-vfs-devel intltool libImageMagick-devel libaspell-devel libgc-devel libgsl-devel libgtkmm2-devel libgtkspell-devel liblcms-devel libpoppler-glib-devel libpopt-devel libssl-devel libwpg2-devel libxslt-devel perl-devel python-devel rpm-build-ruby subversion
BuildRequires: libpng-devel
BuildRequires: libpoppler-devel

Requires: icc-profiles

# For extensions
# It is recommended to install skencil, pstoedit also
# https://bugzilla.altlinux.org/21626
Requires: wmf-utils python-module-lxml

# mike: work around https://bugzilla.altlinux.org/24586
Requires: gnome-icon-theme

%description
Inkscape is a SVG based generic vector-drawing program for Linux/Unix
and Windows.  It uses an advanced imaging engine with anti-aliased
display, alpha transparency, and vector fonts.

%description -l ru_RU.UTF-8
Inkscape -- это программа векторного рисования общего назначения,
использующая формат SVG, работающая на платформах Linux/Unix/Windows
и имеющая мощный движок для отображения графики со сглаживанием,
альфа-каналом и векторными шрифтами.

%package viewer
Summary: Viewer for Inkscape files
Group: Graphics

%description viewer
inkview is standalone viewer for Inkscape files (SVG)

%prep
%setup -n %name-%version%pre
#patch5
%patch6 -p1
#patch7 -p0
%patch8 -p2
cat %SOURCE1 >po/ru.po

%build
#autoreconf
subst "s|.*\(checkPYTHON_LIBS\)=.*|\1=-lpython%__python_version|" ./configure
%add_optflags -fno-strict-aliasing
%configure --with-python --with-perl --enable-inkboard
%make_build

%install
%makeinstall_std

# use tango by default (bug #13994)
#cp share/icons/tango_icons.svg %buildroot%_datadir/%name/icons/icons.svg

tar xvf %SOURCE2 -C %buildroot%_datadir/inkscape/tutorials/

# remove unneeded man
rm -rf %buildroot%_mandir/fr/
%find_lang %name

#%check
#$(INKSCAPE) -z -f $< --export-eps=$@
#$(INKSCAPE) -z -f $< --export-png=$@
#true

%files -f %name.lang
%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README doc
%_bindir/inkscape
%_datadir/%name/
%_desktopdir/inkscape.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/inkscape*

%files viewer
%_bindir/inkview
%_man1dir/inkview*

%changelog
* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 0.48.2-alt3.1.1
- Rebuild with new libImageMagick

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.48.2-alt3.1
- Rebuilt with libwpg2
- Fixed build with new glib2

* Fri Feb 10 2012 Vitaly Lipatov <lav@altlinux.ru> 0.48.2-alt3
- add updated russian tutorial (ALT bug #26857)

* Mon Jan 09 2012 Vitaly Lipatov <lav@altlinux.ru> 0.48.2-alt2
- add updated ru.po (ALT bug #26753)

* Tue Sep 13 2011 Vitaly Lipatov <lav@altlinux.ru> 0.48.2-alt1
- new version 0.48.2 (with rpmrb script) (ALT bug #26274)

* Mon Apr 25 2011 Vitaly Lipatov <lav@altlinux.ru> 0.48.1-alt1
- new version 0.48.1 (with rpmrb script)

* Sun Mar 27 2011 Michael Shigorin <mike@altlinux.org> 0.48.0-alt3
- re-added lost BR:

* Tue Mar 15 2011 Michael Shigorin <mike@altlinux.org> 0.48.0-alt2
- added startup problems workaround (closes: #24586)
- fixed FTBFS:
  + libcairo-devel requires libpng-devel no more)
  + added gentoo patches (fix build with poppler-0.16, gtkspell)
- tweaked package description a bit

* Sun Jan 30 2011 Vitaly Lipatov <lav@altlinux.ru> 0.48.0-alt1
- new version 0.48.0 (with rpmrb script)

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 0.47-alt7
- rebuild with new libImageMagick

* Fri Jul 30 2010 Vitaly Lipatov <lav@altlinux.ru> 0.47-alt6
- reenable python-module-lxml require (ALT bug #21626)

* Wed Mar 10 2010 Vitaly Lipatov <lav@altlinux.ru> 0.47-alt5
- fix build with libpoppler 0.12 (thanks, Ubuntu)

* Fri Oct 09 2009 Vitaly Lipatov <lav@altlinux.ru> 0.47-alt4
- build via git

* Tue Oct 06 2009 Vitaly Lipatov <lav@altlinux.ru> 0.47-alt3
- new version (0.47pre3)

* Mon Sep 14 2009 Vitaly Lipatov <lav@altlinux.ru> 0.47-alt2
- new version (0.47pre2)

* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 0.47-alt1
- new version (0.47pre1)
- remove external tango icons
- enable build with python
- build with new ImageMagick (remove perl-Magick requires) (ALT#19982)

* Thu Dec 18 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt6
- replace external CFLAGS with correct ImageMagick patch (thanks, Valery Inozemtsev)

* Wed Dec 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt5
- fix build with ImageMagick
- remote post/postun macros

* Wed Nov 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt4
- fix build with new libgtk (thanks, Mandriva)

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt3
- fix build with libpoppler 0.8.3 (thanks, Gentoo)

* Wed May 14 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt2
- really 0.46 release
- fix Magick++ detecting

* Sat Mar 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt1
- release (0.46)

* Wed Feb 27 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt0.8svn
- SVN revision 17522 (about 0.46 beta 2) from branch 0.46

* Wed Jan 30 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt0.7svn
- SVN revision 17202

* Fri Jan 18 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt0.6svn
- SVN revision 17126

* Mon Jan 14 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt0.5svn
- use internal tango icons (fix bug #13994)

* Sat Jan 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt0.4svn
- SVN revision 17024
- cleanup spec, update
- fix lcms lib using (bug #182170 in launchpad)
- rebuild with new libgc-0.7

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt0.3svn
- SVN revision 16905
- reenabled poppler-cairo
- disable python scripting (due broken include to CXX dir)

* Wed Dec 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt0.2svn
- SVN revision 16668

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt0.1svn
- SVN revision 16411
- disable popple-cairo preview due missed CairoOutputDev.h in headers

* Fri Jul 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.45.1-alt4
- fix icons.svg (bug #12399)

* Thu Jun 28 2007 Vitaly Lipatov <lav@altlinux.ru> 0.45.1-alt3
- add updated russian translation from Alexandre Prokoudine

* Thu May 17 2007 Vitaly Lipatov <lav@altlinux.ru> 0.45.1-alt2
- added Tango icons by defaults (thanks to Valery Inozemtsev shrek@)

* Sat Mar 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.45.1-alt1
- new version 0.45.1 (with rpmrb script)
- fix bug #11205: CVE-2007-1463, CVE-2007-1464 (thanks icesik@)

* Thu Mar 01 2007 Vitaly Lipatov <lav@altlinux.ru> 0.45-alt1
- split inkview to standalone package
- remove dia and skencil from build requires
- add patch for detect dia (remove it from install requires)

* Tue Feb 06 2007 Vitaly Lipatov <lav@altlinux.ru> 0.45-alt0.1
- new version 0.45 (with rpmrb script)
- remove debian menu

* Mon Sep 18 2006 Vitaly Lipatov <lav@altlinux.ru> 0.44.1-alt0.1
- new version 0.44.1 (with rpmrb script)

* Sat Jun 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.44-alt0.1
- new version 0.44
- enable inkboard

* Tue Nov 22 2005 Vitaly Lipatov <lav@altlinux.ru> 0.43-alt1
- new version

* Tue Sep 20 2005 Vitaly Lipatov <lav@altlinux.ru> 0.42.2-alt0.1
- new version

* Fri Sep 09 2005 Vitaly Lipatov <lav@altlinux.ru> 0.42-alt0.2
- try again

* Mon Aug 01 2005 Vitaly Lipatov <lav@altlinux.ru> 0.42-alt0.1z
- new version (release)
- update buildrequires

* Sun Jul 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.42-alt0.1cvs20050716
- add require perl-Magick
- add perl && python extensions

* Thu Apr 14 2005 Vitaly Lipatov <lav@altlinux.ru> 0.41-alt2cvs20050320
- add some requires needed by extensions

* Mon Apr 04 2005 Vitaly Lipatov <lav@altlinux.ru> 0.41-alt1cvs20050320
- CVS version

* Mon Feb 21 2005 Vitaly Lipatov <lav@altlinux.ru> 0.41-alt1
- release 0.41
- disable gnome-print

* Tue Jan 25 2005 Vitaly Lipatov <lav@altlinux.ru> 0.41-alt0.2cvs20050125
- fix buildreq

* Mon Jan 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.41-alt0.1cvs20050125
- CVS version
- rebuild with gcc3.4
- disable requires for extensions

* Tue Nov 30 2004 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt1
- 0.40 release

* Sun Nov 28 2004 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt0.1cvs20041128
- about 0.40 pre4 release

* Wed Nov 10 2004 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt0.1cvs20041110
- about 0.40 pre2 release
- spec file comformed to GTK program packaging policy

* Tue Oct 26 2004 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt0.1cvs20041021
- 0.40 pre release

* Tue Apr 13 2004 Egor S. Orlov <oes@altlinux.ru> 0.38.1-alt1
- 0.38.1

* Thu Apr 01 2004 Egor S. Orlov <oes@altlinux.ru> 0.37-alt2
- Added menu

* Wed Feb 11 2004 Egor S. Orlov <oes@altlinux.ru> 0.37-alt1
- initial build for Sisyphus

* Thu May 01 2003 Christian Schaller <uraeus@gnome.org>
- Fix up the spec file for current release

* Mon Sep 23 2002 Dag Wieers <dag@wieers.com>
- Update to 0.2.6

* Thu Sep 12 2002 Dag Wieers <dag@wieers.com>
- Update to 0.2.5
- Changed SPEC to benefit from macros

