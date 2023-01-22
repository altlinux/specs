%define major 1.2

# pack shared libinkscape library
%def_with shared

%def_without gnome_vfs
%def_without dbus
%def_disable check

# some reasons to prefer GraphicsMagick over ImageMagick: http://www.graphicsmagick.org/
%def_with graphicsmagick

Name: inkscape
Version: %major.2
Release: alt1

Summary: A Vector Drawing Application

License: GPLv2
Group: Graphics
Url: http://inkscape.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://media.inkscape.org/dl/resources/file/inkscape-%version.tar.xz
Source: %name-%version.tar

Source1: inkview.desktop

Patch: poppler-22.03.0.patch

# a program package can't have any provides
AutoProv:no

BuildRequires(pre): rpm-build-python3

BuildRequires: cmake gcc-c++ intltool
BuildRequires: boost-devel-headers boost-filesystem-devel
BuildRequires: libgc-devel libgsl-devel libpopt-devel libxslt-devel zlib-devel libsoup-devel libaspell-devel libdbus-devel libgspell-devel libreadline-devel
BuildRequires: lib2geom-devel >= 1.2.2

# Checking for modules 'gtkmm-3.0>=3.24;gdkmm-3.0>=3.24;gtk+-3.0>=3.24;gdk-3.0>=3.24'
BuildRequires: pkgconfig(gtkmm-3.0) >= 3.24
BuildRequires: pkgconfig(gdkmm-3.0) >= 3.24
BuildRequires: pkgconfig(gtk+-3.0) >= 3.24
BuildRequires: pkgconfig(gdk-3.0) >= 3.24

%{?_with_gnome_vfs:BuildRequires: gnome-vfs-devel}
%{?_with_dbus: BuildRequires: libdbus-devel}
BuildRequires: libwpg-devel librevenge-devel libcdr-devel libvisio-devel
BuildRequires: libpng-devel libexif-devel libjpeg-devel
BuildRequires: libpoppler-devel libpoppler-glib-devel
BuildRequires: libpotrace-devel liblcms2-devel
%if_with graphicsmagick
BuildRequires: libGraphicsMagick-c++-devel
%else
BuildRequires: libImageMagick-devel
%endif
BuildRequires: libgomp-devel
BuildRequires: libdouble-conversion-devel
BuildRequires: perl-podlators

%add_python3_lib_path %_datadir/%name/extensions

Requires: icc-profiles
Requires: python3-module-appdirs

# For extensions
# https://bugzilla.altlinux.org/21626
Requires: wmf-utils
# Recommends: skencil pstoedit

# mike: work around https://bugzilla.altlinux.org/24586
#Requires: gnome-icon-theme

# to support svg in libgdk-pixbuf
Requires: librsvg

Requires: %name-data = %EVR
Requires: inkscape-tutorial
Requires: lib%name = %EVR

# due $ORIGIN using
Requires: /proc

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
Requires: lib%name = %EVR
# TODO: uses
# /usr/share/inkscape/ui/menus.xml
# /usr/share/inkscape/ui/style.css
# /usr/share/inkscape/fonts
#Requires: %name-data = %EVR

%description viewer
inkview is standalone viewer for Inkscape files (SVG).

%package data
Summary: Inkscape common data files
Group: Graphics
BuildArch: noarch
Requires: icon-theme-hicolor

# a data package can't have any provides
AutoProv:no

%description data
Inkview tutorial.

%package -n lib%name
Summary: Inkscape shared library
Group: System/Libraries

%description -n lib%name
Inkscape shared library.


%package tutorial
Summary: Inkscape tutorial
Group: Graphics
BuildArch: noarch

%description tutorial
Inkview tutorial.

%package checkinstall
Summary: Checkinstall for %name
Group: Development/Other
BuildArch: noarch
#Requires(pre): %name = %EVR
Conflicts: python3(setuptools)

%description checkinstall
Run checkinstall tests for %name.

%prep
%setup
#patch -p1

%ifarch %e2k
# missing typeinfo fix
cat >> src/inkscape-version.cpp.in << "EOF"
#include <typeinfo>
namespace Geom { struct Curve { };
	__attribute__((visibility("hidden")))
	auto Curve_typeinfo_ptr = &typeid(Curve); }
EOF
# LCC cannot work with expressions inside openmp pragmas
sed -i "s|limit > OPENMP_THRESHOLD|limit_gt_thr|;s|limit = w \\* h|&, limit_gt_thr = limit > OPENMP_THRESHOLD|" src/display/{cairo-templates.h,nr-filter-morphology.cpp}
%endif
rm -rv src/3rdparty/2geom/

%build
%cmake_insource \
%if_with shared
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_SKIP_RPATH=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH=OFF \
    -DWITH_GNU_READLINE=ON \
    -DWITH_INTERNAL_2GEOM=OFF \
%else
    -DBUILD_SHARED_LIBS=OFF \
%endif
%if_with graphicsmagick
    -DWITH_IMAGE_MAGICK=OFF \
    -DWITH_GRAPHICS_MAGICK=ON \
%else
    -DWITH_IMAGE_MAGICK=ON \
    -DWITH_GRAPHICS_MAGICK=OFF \
%endif
    %nil
# FIXME: ppc64le (make -j132):
# No rule to make target 'po/bn.gmo', needed by 'share/templates/default_templates.timestamp
%make_build || %make_build -j2

%install
%makeinstall_std

# remove unneeded man
rm -rv %buildroot%_mandir/??/
rm -rv %buildroot%_mandir/??_??/

subst "s|/usr/bin/env python$|%__python3|" %buildroot%_datadir/%name/extensions/*.py
subst "s|/usr/bin/env python$|%__python3|" %buildroot%_datadir/%name/extensions/*/*.py
subst "s|/usr/bin/env python$|%__python3|" %buildroot%_datadir/%name/extensions/*/*/*.py
subst "s|/usr/bin/env python$|%__python3|" %buildroot%_datadir/%name/extensions/*/*/*/*.py



# remove tests
rm -rv %buildroot%_datadir/%name/extensions/inkex/tester/

%find_lang %name

install -m644 %SOURCE1 %buildroot%_desktopdir/inkview.desktop

%check
$(INKSCAPE) -z -f $< --export-eps=$@
$(INKSCAPE) -z -f $< --export-png=$@
true

%files -f %name.lang
%doc AUTHORS CONTRIBUTING.md NEWS.md COPYING README.md doc
%_bindir/inkscape
%_desktopdir/org.inkscape.Inkscape.desktop
%_man1dir/inkscape*
#_mandir/??/man1/inkscape.??.1.*
%_datadir/metainfo/org.inkscape.Inkscape.appdata.xml
/usr/share/bash-completion/completions/inkscape

%files data
%_datadir/%name/
%exclude %_datadir/inkscape/tutorials/
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg

%files viewer
%_bindir/inkview
%_man1dir/inkview*
%_desktopdir/inkview.desktop

%if_with shared
%files -n lib%name
%dir %_libdir/inkscape/
%_libdir/inkscape/libinkscape_base.so
%endif

%files tutorial
%dir %_datadir/%name/
%_datadir/inkscape/tutorials/

%files checkinstall

%changelog
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)
- set BR: lib2geom-devel >= 1.2.2

* Mon Apr 25 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.1.2-alt1
- NMU:
    + new version (1.1.2) with rpmgs script
    + fix build with poppler-22.03.0
    + add python3-module-appdirs to Requires

* Sat Dec 04 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt8
- fix build with poppler 21.11.0 (thanks, zerg@) (ALT bug 41503)

* Fri Aug 20 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt7
- move add noarch files to data subpackage
- rearrange build requires and requires
- drop gnome icons requirement (see https://bugzilla.altlinux.org/24586)
- add librsvg require to support svg in libgdk-pixbuf

* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt6
- update build requires

* Wed Aug 11 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.1-alt5
- e2k: fixed OpenMP pragmas for LCC

* Tue Aug 10 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.1-alt4
- e2k: workaround for compiler bug

* Thu Jul 08 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt3
- fix build with gcc-7.5 and lcc (e2k)

* Thu Jul 01 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- add desktop file for inkview (ALT bug 34135)

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version 1.1 (with rpmrb script) (ALT bug 40171)

* Wed Mar 31 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- fix build with glib >= 2.67.3

* Fri Feb 05 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt7
- add Requires: /proc (ALT bug 39230)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt6
- build libinkscape to share code between inkscape and inkview
- enable build shared lib
- pack bash-completion file

* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt5
- build with GraphicsMagick instead of ImageMagick (all reasons of fork in 2002)

* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt4
- pack tutorial in separate noach package

* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt3
- add checkinstall, drop setuptools require

* Fri Oct 16 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- cleanup spec, add search requires in extensions dir (ALT bug 39052)

* Wed Sep 16 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Wed May 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version (1.0) with rpmgs script

* Tue Apr 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt0.beta2.1
- FIxed build with python2.

* Wed Jan 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt0.beta2
- drop python using (ALT bug 37290)
- add patch against poppler >= 0.83.0 build

* Thu Oct 24 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt0.beta1
- new version (1.0) with rpmgs script
- update buildreqs, switch to cmake

* Mon Jul 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.92.4-alt4
- fix build with poppler 0.76 and above

* Wed May 29 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.92.4-alt3
- spec: BR: replaced libgomp6-devel -> libgomp-devel.

* Mon May 06 2019 Michael Shigorin <mike@altlinux.org> 0.92.4-alt2
- E2K: disable openmp and -Werror=return-type
- uncomment check section but disable it by default
- minor spec cleanup
- leave de/fr manpages in just in case

* Sun Feb 10 2019 Vitaly Lipatov <lav@altlinux.ru> 0.92.4-alt1
- new version 0.92.4 (with rpmrb script)

* Wed Nov 21 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.92.3-alt4
- Fixed build with poppler >= 0.71.

* Tue Sep 04 2018 Vitaly Lipatov <lav@altlinux.ru> 0.92.3-alt3
- fix build with poppler 0.65

* Mon Jun 25 2018 Vitaly Lipatov <lav@altlinux.ru> 0.92.3-alt2
- don't override tutorial with obsoleted one (ALT bug 35081)

* Sun Apr 22 2018 Vitaly Lipatov <lav@altlinux.ru> 0.92.3-alt1
- new version 0.92.3 (with rpmrb script)

* Mon Dec 04 2017 Vitaly Lipatov <lav@altlinux.ru> 0.92.2-alt2
- fix build with libpoppler >= 0.58

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 0.92.2-alt1
- new version 0.92.2 (with rpmrb script)

* Fri Aug 18 2017 Anton Farygin <rider@altlinux.ru> 0.92.1-alt3
- rebuild with new ImageMagick

* Wed Mar 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.92.1-alt2
- build with potrace (ALT bug #33147)
- fix man build

* Sat Feb 18 2017 Vitaly Lipatov <lav@altlinux.ru> 0.92.1-alt1
- new version 0.92.1 (with rpmrb script)

* Sun Jan 29 2017 Vitaly Lipatov <lav@altlinux.ru> 0.92-alt1
- new version 0.92 (with rpmrb script)

* Mon Apr 11 2016 Denis Medvedev <nbr@altlinux.org> 0.91-alt5
- Changed obsoleted ScopedPtr to make_unique_ptr_gfree
hinted by https://mail.gnome.org/archives/commits-list/2016-January/msg04404.html

* Mon Mar 21 2016 Vitaly Lipatov <lav@altlinux.ru> 0.91-alt4
- rebuild with latest libpoppler58

* Fri Oct 09 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.91-alt3
- build fixed

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 0.91-alt2
- build with libcdr and libvisio

* Mon Jun 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.91-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Feb 18 2015 Vitaly Lipatov <lav@altlinux.ru> 0.91-alt1
- new version 0.91 (with rpmrb script)

* Thu Oct 23 2014 Anton Farygin <rider@altlinux.ru> 0.48.5-alt2
- Rebuild with new libImageMagick

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.48.5-alt1
- new version 0.48.5 (with rpmrb script)

* Fri Jun 06 2014 Alexey Shabalin <shaba@altlinux.ru> 0.48.4-alt6
- switch to librevenge
- build without gnome-vfs support

* Thu Sep 26 2013 Anton Farygin <rider@altlinux.ru> 0.48.4-alt5
- Rebuild with new libImageMagick

* Tue Apr 23 2013 Anton Farygin <rider@altlinux.ru> 0.48.4-alt4
- rebuild with libpoppler35

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 0.48.4-alt3
- Rebuild with new libImageMagick

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.48.4-alt2
- rebuild with libpoppler35

* Mon Feb 11 2013 Vitaly Lipatov <lav@altlinux.ru> 0.48.4-alt1
- new version 0.48.4 (with rpmrb script) (ALT bug #28530)
- drop all patches

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.48.2-alt4.1
- Rebuilt with libpng15

* Sat Aug 04 2012 Vitaly Lipatov <lav@altlinux.ru> 0.48.2-alt4
- fix build (thanks, Fedora!)
- update buildreq

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

