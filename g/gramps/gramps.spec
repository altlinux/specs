Name: gramps
Version: 3.3.1
Release: alt1

Summary: Genealogical Research and Analysis Management Programming System
Summary(ru_RU.UTF-8): Программная система анализирования и управления генеалогическими изысканиями

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL
Group: Databases
Url: http://gramps.sourceforge.net/

Source: http://prdownloads.sf.net/%name/%name-%version.tar

# temporarely
Requires: python%__python_version(libglade)
Requires: python%__python_version(bonobo)
Requires: python%__python_version(gnomecanvas)
Requires: python%__python_version(gconf)

# Typical environment for GNOME program
Requires(post): GConf
Requires(post,postun): scrollkeeper
Requires(post,postun): desktop-file-utils
BuildPreReq: libGConf-devel
BuildPreReq: desktop-file-utils

BuildArch: noarch

# manually removed: eric esound
# Automatically added by buildreq on Mon Aug 07 2006
BuildRequires: docbook-dtds esound GConf gnome-doc-utils gnome-vfs libavahi-glib perl-XML-Parser pkg-config python-devel python-module-pygnome-gconf python-module-pygobject python-module-pygtk-libglade python-modules python-modules-encodings intltool

# Skipped all internal modules
%add_python_req_skip grampslib AddMedia AutoComp BaseDoc Calendar Date Filter FrenchRepublic GedcomInfo GenericFilter GrampsCfg GraphLayout Gregorian Hebrew HtmlDoc ImgManip Julian ListModel MergeData OpenSpreadSheet Plugins QuestionDialog ReadXML RelLib Relationship Report SelectObject SelectPerson SpreadSheetDoc StyleEditor SubstKeywords TarFile WriteXML ansel_utf8 const latin_utf8 sort soundex Utils Errors DateDisplay DateHandler DateParser FontScale GrampsGconfKeys GrampsMime Sort
%add_python_req_skip TreeTips DdTargets GrampsKeys MergePeople NameDisplay PeopleModel PluginMgr ReportOptions ReportUtils TreeTips Merge _winreg Lru PlaceUtils
%add_python_req_skip GrampsDisplay Tool TransUtils Assistant BasicUtils Bookmarks Config DisplayModels DisplayTabs Editors Filters GrampsDb GrampsLocale GrampsWidgets LdsUtils ManagedWindow Mime Models ODSDoc PageView PluginUtils ReportBase Selectors Spell ToolTips TreeViews

# TODO: need build python-module-osmgpsmap
%add_python_req_skip osmgpsmap

AutoProv: yes, nopython

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
%configure --disable-schemas-install --disable-scrollkeeper --disable-mime-install
#sed -i "s,/usr/bin/python,/usr/bin/env python," %name.sh
%make_build

%install
%makeinstall
install -D -m644 %buildroot%_datadir/gramps/images/gramps.png %buildroot%_liconsdir/gramps.png
%find_lang %name --with-gnome

%files -f %name.lang
%doc AUTHORS FAQ NEWS README TODO
%_bindir/%name
%_man1dir/*
%_datadir/%name/
%_desktopdir/*
#%_datadir/gnome/help/*
%_datadir/mime-info/*
%_liconsdir/*
%_datadir/application-registry/*
#%config %_sysconfdir/gconf/schemas/*
%_datadir/mime/packages/*
%_pixmapsdir/%name.png
%_datadir/icons/gnome/*/mimetypes/*

%changelog
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
* Mon May 20 2003 Donald Peterson <dpeterson@sigmaxi.org>
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
