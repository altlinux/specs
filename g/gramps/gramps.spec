Name: gramps
Version: 5.1.4
Release: alt2

Summary: Genealogical Research and Analysis Management Programming System
Summary(ru_RU.UTF-8): Программная система анализирования и управления генеалогическими изысканиями

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPLv2
Group: Databases
Url: http://gramps.sourceforge.net/

Source: http://prdownloads.sf.net/%name/%name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-gir rpm-build-python3

BuildRequires: intltool

#Requires: typelib(GConf) typelib(GExiv2) typelib(OsmGpsMap) typelib(GLib) typelib(GObject) typelib(Gdk) typelib(GdkPixbuf) typelib(Gtk) typelib(GtkSpell) typelib(Pango) typelib(PangoCairo)

AutoReq:yes,nopython
AutoProv:no

%add_typelib_req_skiplist typelib(GtkosxApplication) typelib(Gtkspell)

%add_python3_req_skip winreg
%add_python3_req_skip gi.repository.GLib
%add_python3_req_skip gi.repository.Gio

# TODO: need build python-module-osmgpsmap
%add_python3_req_skip osmgpsmap

%py3_requires PyICU

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%description -l ru_RU.UTF-8
GRAMPS (Программная система управления генеалогическими
изысканиями и анализом) - основанная на GNOME генеалогическая
программа, поддерживающая подключаемые модули на Питоне.

%prep
%setup

%build
%python3_build
# TODO: python3_build --server

%install
%python3_install --resourcepath=%_datadir

mkdir -p %buildroot%_datadir/locale
cp -pr build/mo/* %buildroot%_datadir/locale/
#Remove duplicate doc
rm -f %buildroot%_datadir/%name/COPYING

mkdir -p %buildroot%_desktopdir/
cp -p build/data/gramps.desktop %buildroot%_desktopdir/

mkdir -p %buildroot%_datadir/mime/packages/
cp -p build/data/gramps.xml %buildroot%_datadir/mime/packages/

mkdir -p %buildroot%_datadir/application-registry/
cp -p data/gramps.applications %buildroot%_datadir/application-registry/

mkdir -p %buildroot%_datadir/appdata/
cp -p build/data/gramps.appdata.xml %buildroot%_datadir/appdata/

mkdir -p %buildroot%_man1dir/
cp -p build/data/man/gramps.1.gz %buildroot%_man1dir/gramps.1.gz

mkdir -p %buildroot%_pixmapsdir/
cp -p images/gramps.png %buildroot%_pixmapsdir/

rm -rf %buildroot%_docdir/gramps/
#rm -rf %buildroot%_iconsdir/

mkdir -p %buildroot%_iconsdir/hicolor/48x48/apps/
cp -p %buildroot%_datadir/%name/images/%name.png %buildroot%_iconsdir/hicolor/48x48/apps/

echo -n "%_datadir" > %buildroot%python3_sitelibdir/gramps/gen/utils/resource-path

# Bug? 'from .test import test_util as tu' resolved as python3(gramps.test.test)
rm -rv %buildroot%python3_sitelibdir/gramps/test/

#install -D -m644 %buildroot%_datadir/gramps/images/gramps.png %buildroot%_liconsdir/gramps.png
%find_lang %name

%files -f %name.lang
%doc AUTHORS FAQ NEWS README.md TODO
%_bindir/%name
%python3_sitelibdir/gramps/
%python3_sitelibdir/gramps-*.egg-info
%_man1dir/*
%_datadir/%name/
%_desktopdir/*
%_datadir/mime-info/*
%_iconsdir/hicolor/48x48/apps/*
%_datadir/application-registry/*
%_datadir/appdata/*
#%config %_sysconfdir/gconf/schemas/*
%_datadir/mime/packages/*
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/apps/gramps.*
%_iconsdir/hicolor/*/mimetypes/*

%changelog
* Fri Dec 22 2023 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt2
- remove unused tests (getting rid of gramps.test.test and unittest reqs)

* Wed Dec 22 2021 Andrey Cherepanov <cas@altlinux.org> 5.1.4-alt1
- NMU: new version 5.1.4 (ALT bug #37029)

* Mon Aug 16 2021 Vitaly Lipatov <lav@altlinux.ru> 4.2.8-alt2
- drop obsoleted BR

* Mon Feb 26 2018 Vitaly Lipatov <lav@altlinux.ru> 4.2.8-alt1
- new version 4.2.8 (with rpmrb script)

* Sat Jan 30 2016 Vitaly Lipatov <lav@altlinux.ru> 3.4.9-alt1
- new version 3.4.9 (with rpmrb script)
- final maintenance release with gtk2

* Mon Sep 02 2013 Vitaly Lipatov <lav@altlinux.ru> 3.4.5-alt1
- new version 3.4.5 (with rpmrb script)

* Mon Apr 09 2012 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt1
- new version 3.3.1 (with rpmrb script) (ALT bug #27180)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.5-alt1.qa1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 3.2.5-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for gramps
  * postclean-03-private-rpm-macros for the spec file

* Thu Apr 07 2011 Vitaly Lipatov <lav@altlinux.ru> 3.2.5-alt1
- new version 3.2.5 (with rpmrb script) (ALT bug #23865)
- build as noarch

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.1
- Rebuilt with python 2.6

* Sun Jun 21 2009 Vitaly Lipatov <lav@altlinux.ru> 3.1.2-alt1
- new version 3.1.2 (with rpmrb script)

* Sun Apr 19 2009 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt1
- new version 3.1.1 (with rpmrb script)
- fix build on x86_64 (bug #19676)

* Sat Jan 03 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt1
- new version 3.0.4 (with rpmrb script)
- remove post/postun sections

* Sun May 04 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version 3.0.0 (with rpmrb script)

* Mon Feb 18 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.10-alt2
- rebuild with python 2.5

* Tue Jan 22 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.10-alt1
- new version 2.2.10 (with rpmrb script)

* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.9-alt1
- new version 2.2.9 (with rpmrb script)

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.8-alt1
- new version 2.2.8 (with rpmrb script)

* Sun Apr 29 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.7-alt1
- new version 2.2.7 (with rpmrb script)

* Sun Mar 25 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.6-alt1
- new version 2.2.6 (with rpmrb script)

* Fri Dec 29 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt0.1
- new version 2.2.4 (with rpmrb script)
- enable smp build

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.95-alt0.1
- new version 2.1.95
- remove debian menu
- add icon (fix bug #9856 again)

* Mon Aug 07 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.90-alt0.1
- new version (2.1.90) 
- cleanup spec, update buildreqs
- remove ALT menu (fix bug #9856)

* Wed Jun 14 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.5-alt0.1
- new version 2.1.5 (with rpmrb script)

* Wed Mar 08 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.10-alt1
- new version (2.0.10)

* Fri Dec 23 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.9-alt1
- new version
- fix macros in preun
- fix doc macros using

* Sun Sep 25 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.8-alt1
- new version
- tested with my own base

* Tue Aug 02 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt2.1
- really fix Zope (ZODB) dependences

* Sat Mar 26 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt2
- fix require gnomecanvas

* Mon Mar 21 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt1
- new stable version
- rebuild with python 2.4

* Sat Dec 11 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- new unstable version
- spec file comformed to GNOME program packaging policy

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt1
- new version
- remove Zope(ZODB) dependences
- remove unneeded requires and provides

* Sun Aug 01 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version
- fix description

* Tue Jul 20 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt3
- add russian description and summary
- add requires for pygtk-libglade

* Tue Jul 13 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt2
- rebuild with new python-module-pygtk/gnome

* Fri Jul 09 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- first build for Sisyphus

* Tue Dec  2 2003 Tim Waugh <twaugh@redhat.com>
- More docs.
- Change Copyright: to License:.

* Fri Sep 19 2003 Tim Waugh <twaugh@redhat.com>
- Own %%{_datadir/gramps directory.
- Ship %%{_libdir}/gramps.
* Tue May 20 2003 Donald Peterson <dpeterson@sigmaxi.org>
- Override RPMs default of localstatedir to /var/lib..
  This is done in accordance with GNOME and FHS compliance guidelines
  (http://fedora.mplug.org/docs/rpm-packaging-guidelines.html)
- Use %find_lang macro to get NLS files
- Set %%doc tags on appropriate files
- Remove temporary scrollkeeper-created files from install before packaging
  to avoid rpm 4.1 complaints.  (These aren't needed in the distribution.)
- Use default scrollkeeper-update scripts
* Mon Mar 24 2003 Alex Roitman <shura@alex.neuro.umn.edu>
- update scrollkeeper dependencies and add post and postun to enable install on a machine without scrollkeeper
* Fri Jun 14 2002 Donald Peterson <dpeterso@engr.ors.edu>
- add scrollkeeper dependencies and some file cleanup
