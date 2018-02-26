%define ver_major 1.10
%define build_cvs 0
%def_without gda
%def_with python
%def_with perl
%def_without gnome
%def_without new_translation
%define abiversion 1.10

%define _unpackaged_files_terminate_build 1

Name: gnumeric
Version: 1.10.17
Release: alt4

Summary: A full-featured spreadsheet for GNOME
License: GPL
Group: Office
Url: http://www.gnome.org/gnumeric/

Source: %name-%version.tar
Patch0: gnumeric-desktop-alt.patch

%if_without gnome
Obsoletes: %name-light
Provides:  %name-light = %version-%release
%endif

%if_with python
# Provided by python_loader.so
Provides: python%__python_version(Gnumeric)
Provides: python%__python_version(gsf)
%endif

%define scrollkeeper_ver 0.3.14
%define gsf_ver 1.14.23
%define gda_ver 4.0
%define desktop_file_utils_ver 0.10
%define goffice_ver 0.8.17

PreReq: scrollkeeper >= %scrollkeeper_ver
PreReq: libgda4 >= %gda_ver
Requires(post,postun): desktop-file-utils >= %desktop_file_utils_ver
Requires: libspreadsheet%{abiversion} = %version-%release
Requires: libgnomeoffice >= %goffice_ver
Requires: %_bindir/evince

BuildRequires: flex libgnomeoffice-devel >= %goffice_ver libgsf-devel >= %gsf_ver
BuildRequires: intltool gnome-doc-utils zlib-devel librarian
%{?_with_perl:BuildRequires: perl-devel}
%{?_with_python:BuildRequires: python-module-pygobject-devel}
%{?_with_gda:BuildRequires: libgda4-devel >= %gda_ver libgnomedb4-devel}
%{?_with_gnome:BuildRequires: libgnomeui-devel libgsf-gnome-devel}

%description
Gnumeric is a modern full-featured spreadsheet program.  Gnumeric
contains built-in functions help system, analysis tools and plotting
interface.
There are nearly 95 percents of all Excel functions implemented in
Gnumeric besides a possibility to write your own functions in Python
and Perl.  There are Lotus 1-2-3, MS Excel 95/98/2000/XP, SYLK among
supported third party formats.

%description -l ru_RU.UTF8
Gnumeric - это современная полнофункциональная программа для работы с
электронными таблицами.  Gnumeric содержит встроенную систему подсказки
к функциям, средства анализа и умеет строить графики.  Программа
поддерживает приблизительно 95 процентов функций, имеющихся в MS Excel,
дополнить которые можно своими собственными функциями, написанными на
языке Python и Perl.  Среди поддерживаемых форматов - Lotus 1-2-3,
MS Excel 95/98/2000/XP, SYLK.

%package -n libspreadsheet%{abiversion}
Summary: libspreadsheet library
Group: System/Libraries
Requires: libgnomeoffice >= %goffice_ver
Obsoletes: libspreadsheet <= 1.8.1-alt1

%description -n libspreadsheet%{abiversion}
This package provide libspreadsheet library

%package -n libspreadsheet-devel
Summary: libspreadsheet library headers
Group: Development/C
Provides: libspreadsheet%{abiversion}-devel = %version-%release
Requires: libspreadsheet%{abiversion} = %version-%release

%description -n libspreadsheet-devel
This package provide libspreadsheet library headers

%set_perl_req_method relaxed

%prep
%if %build_cvs
%setup -q -n %name
%else
%setup -q
%endif

rm -f schemas/*.schemas

%if_with new_translation
pushd po
# already merged po
bzcat %SOURCE4 > ru.po
#bzcat %SOURCE4 > ru.po.new
#msgmerge ru.po.new gnumeric.pot |bzip2 > ../../../SOURCES/%name-%version-ru.po.bz2
popd
%endif

%patch0 -p1

sed -i 's|@LIBGOFFICE@|libgoffice-0.8|g' libspreadsheet.pc.in

%build
gnome-doc-prepare --copy --force
%autoreconf
%configure --disable-schemas-install \
	--disable-schemas-compile \
	--enable-ssindex \
	%{subst_with gnome} \
	%{subst_with gda} \
	%{subst_with python} \
	%{subst_with perl} \

# SMP build
%make_build

%install
%makeinstall_std

# remove none-packaged files
rm -rf %buildroot%_var

%find_lang --with-gnome %name %name-functions
cat %name-functions.lang >> %name.lang

%files -f %name.lang
%_bindir/*
%_libdir/%name/
%_libdir/goffice/%goffice_ver/plugins/gnumeric/gnumeric.so
%_libdir/goffice/%goffice_ver/plugins/gnumeric/plugin.xml
%dir %_datadir/%name
%_datadir/%name/%version
%_datadir/applications/*
%_datadir/pixmaps/*
%_iconsdir/hicolor/*/apps/gnumeric.*
%_man1dir/*
%doc AUTHORS ChangeLog NEWS BUGS README COPYING HACKING
%config %_datadir/glib-2.0/schemas/org.gnome.gnumeric.dialogs.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gnumeric.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gnumeric.plugin.gschema.xml

%exclude %_libdir/%name/%version/plugins/*/*.la
%exclude %_libdir/goffice/%goffice_ver/plugins/gnumeric/gnumeric.la

%files -n libspreadsheet-devel
%_includedir/libspreadsheet-%{abiversion}
%_pkgconfigdir/*

%files -n libspreadsheet%{abiversion}
%_libdir/libspreadsheet*

%changelog
* Tue Jun 19 2012 Yuri N. Sedunov <aris@altlinux.org> 1.10.17-alt4
- used GSettings instead GConf as in libgnomeoffice-0.8.17-alt2

* Tue Jun 19 2012 Yuri N. Sedunov <aris@altlinux.org> 1.10.17-alt3
- removed obsoletes configure options (guile, gb)
- build without obsolete gnome (bonobo, libgnomeui) support
- and as a consequence -- obsoletes/provides gnumeric-light
- updated buildreqs
- removed useless icons and pregenerated omf-file
- fixed %%files section and set %%_unpackaged_files_terminate_build to 1

* Fri Apr 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.17-alt2.2
- Fixed build

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.17-alt2.1
- Rebuild with Python-2.7

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 1.10.17-alt2
- rebuilt for perl-5.14

* Mon Sep 12 2011 Alexey Morsov <swi@altlinux.ru> 1.10.17-alt1
- new version (ALT #16960)

* Sun Mar 20 2011 Alexey Morsov <swi@altlinux.ru> 1.10.13-alt1
- new version
- add zlib-devel

* Sun Dec 19 2010 Alexey Morsov <swi@altlinux.ru> 1.10.12-alt1
- new version

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.10.11-alt1.1
- rebuilt with perl 5.12

* Tue Oct 12 2010 Alexey Morsov <swi@altlinux.ru> 1.10.11-alt1
- new version

* Sat Jul 03 2010 Alexey Morsov <swi@altlinux.ru> 1.10.7-alt1
- new version

* Tue Jun 01 2010 Alexey Morsov <swi@altlinux.ru> 1.10.5-alt1
- new version

* Wed Apr 21 2010 Alexey Morsov <swi@altlinux.ru> 1.10.2-alt1
- new version

* Tue Apr 20 2010 Alexey Morsov <swi@altlinux.ru> 1.10.0-alt2
- fix build (add intltool)

* Wed Feb 17 2010 Alexey Morsov <swi@altlinux.ru> 1.10.0-alt1
- new version

* Sat Dec 19 2009 Alexey Morsov <swi@altlinux.ru> 1.9.17-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.15-alt1.1
- Rebuilt with python 2.6

* Tue Nov 03 2009 Alexey Morsov <swi@altlinux.ru> 1.9.15-alt1
- new version

* Mon Sep 07 2009 Alexey Morsov <swi@altlinux.ru> 1.9.10-alt3
- Cleanup build dependencies using buildreq (ldv)
- Remove libgnomedb-devel from BuildPreReq, cleanup interpackage
  deps (ldv)

* Tue Sep 01 2009 Alexey Morsov <swi@altlinux.ru> 1.9.10-alt2
- rebuild with libgda4

* Sun Aug 30 2009 Alexey Morsov <swi@altlinux.ru> 1.9.10-alt1
- new version

* Thu Aug 06 2009 Alexey Morsov <swi@altlinux.ru> 1.9.9-alt2
- slightly fix russian translation
- fix desktop file (20972)

* Thu Jul 23 2009 Alexey Morsov <swi@altlinux.ru> 1.9.9-alt1
- new version

* Wed Jun 17 2009 Alexey Morsov <swi@altlinux.ru> 1.9.8-alt1
- new version

* Sat Mar 21 2009 Alexey Morsov <swi@altlinux.ru> 1.9.4-alt1
- new version

* Wed Nov 26 2008 Alexey Morsov <swi@altlinux.ru> 1.9.3-alt1
- new version
- fix spec
  + clean deprecated call in post/postun

* Sun Sep 14 2008 Alexey Morsov <swi@altlinux.org> 1.9.2-alt2
- fix requires

* Wed Sep 10 2008 Alexey Morsov <swi@altlinux.org> 1.9.2-alt1
- new version
- remove abiversion from name of libspreadsheet devel package

* Sat Jul 19 2008 Alexey Morsov <swi@altlinux.ru> 1.9.1-alt1
- new version (development)
- fix spec file
  + pursue ChangeLog policy
  + add goffice macro to libspreadsheet sub-package
  + change libgnomeoffice to libgnomeoffice0.8 (due dso policy)
  + rename libspreadsheet to libspreadsheet<abiversion> 
    (due dso policy)

* Wed May 14 2008 Alexey Morsov <swi@altlinux.ru> 1.8.2-alt1
- up to 1.8.2
- fix iconsdir

* Sun Feb 17 2008 Alexey Morsov <swi@altlinux.ru> 1.8.1-alt1
- up to 1.8.1
- Fix graph paste.
- Fix cell comment positioning problem.
- Fix NPV doc problem.
- Fix DSUM crash.
- Fix insert-current-date locale problem.
- Fix xls read crash.
- Fix inter-sheet cut problem.

* Thu Jan 03 2008 Alexey Morsov <swi@altlinux.ru> 1.8.0-alt1
- 1.8.0
- support for MS OOXML
- many improvements and bug fixes.

* Thu Nov 08 2007 Alexey Morsov <swi@altlinux.ru> 1.7.14-alt1
- 1.7.14
- A large number of crashes were identified, primarily by Sum1, 
and promptly fixed
- a few of the feature regressions for printing were fixed
- ODF import saw improvements

* Sat Sep 15 2007 Alexey Morsov <swi@altlinux.ru> 1.7.12-alt1
- version 1.7.12
- menu file deprecated

* Tue Jul 31 2007 Alexey Morsov <swi@altlinux.ru> 1.7.11-alt1
- version 1.7.11
- bug fixes include https://bugzilla.altlinux.org/show_bug.cgi?id=12430

* Sat Jun 02 2007 Alexey Morsov <swi@altlinux.ru> 1.7.10-alt1
- new tsa plugin
- Begin generalizing the conventions to properly support ODF-1.2 output

* Wed Apr 25 2007 Alexey Morsov <swi@altlinux.ru> 1.7.9-alt1
- new version
- remove Science from .desktop file (patch)
- remove _menudir from files (unneeded, empty file)

* Tue Mar 06 2007 Alexey Morsov <swi@altlinux.ru> 1.7.8-alt1
- new version (req libgoffice >= 0.3.7)

* Mon Feb 19 2007 Alexey Morsov <swi@altlinux.ru> 1.7.7-alt1
- New version (bug fixed, fix crash on OO import, see ChangeLog)
- clean spec a bit

* Tue Jan 16 2007 Alexey Morsov <swi@altlinux.ru> 1.7.6-alt2
- fix spec (remove _libdir/lib*.so from package gnumeric,
	clean some files)

* Tue Dec 19 2006 Alexey Morsov <swi@altlinux.ru> 1.7.6-alt1
- Major bugfixes

* Thu Dec 14 2006 Alexey Morsov <swi@altlinux.ru> 1.7.5-alt1
- New version 1.7.5
- fix requires versions
- fix spec (remove unused files)
- separate libspreadsheet

* Fri Mar 31 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1:1.6.1-alt1.1
- Rebuild with libgsf-1.so.114 .

* Wed Nov 09 2005 Vital Khilko <vk@altlinux.ru> 1:1.6.1-alt1
- 1.6.1

* Mon Mar 14 2005 Yuri N. Sedunov <aris@altlinux.ru> 1:1.4.3-alt1
- 1.4.3

* Thu Jan 20 2005 Yuri N. Sedunov <aris@altlinux.ru> 1:1.4.2-alt1
- 1.4.2
- updated russian translation by avp@.

* Wed Dec 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:1.4.1-alt1
- 1.4.1

* Mon Nov 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Sat Nov 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:1.3.93-alt1
- 1.3.93

* Thu Sep 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:1.2.13-alt1.1
- do not intltoolize, probably intltool has bug since 0.31 (fix #4995).

* Thu Jul 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:1.2.13-alt1
- 1.2.13

* Wed May 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:1.2.12-alt1
- 1.2.12

* Thu Apr 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:1.2.10-alt1.1
- new version.

* Sat Feb 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:1.2.6-alt1.1
- more translations.
- remove *.schemas from sources so to merge translations to it.
- fixed Gnome_Gnumeric.server
- fixed menu.

* Thu Feb 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:1.2.6-alt1
- 1.2.6

* Tue Jan 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:1.2.5-alt1
- 1.2.5

* Mon Dec 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 1:1.2.4-alt1
- 1.2.4

* Wed Dec 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 1:1.2.3-alt1
- 1.2.3

* Sun Dec 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 1:1.2.2-alt1
- 1.2.2.

* Thu Sep 18 2003 AEN <aen@altlinux.ru> 1:1.2.0-alt1
- new release

* Tue Aug 26 2003 AEN <aen@altlinux.ru> 1:1.1.90-alt1
- release

* Mon Aug 25 2003 AEN <aen@altlinux.ru> 1:1.1.90-alt0.1
- sources from CVS

* Fri Aug 08 2003 AEN <aen@altlinux.ru> 1:1.1.20-alt0.5
- updated sources

* Wed Jul 30 2003 AEN <aen@altlinux.ru> 1:1.1.20-alt0.4
- updated sources

* Thu Jul 10 2003 AEN <aen@altlinux.ru> 1:1.1.20-alt0.3
- updated sources

* Tue Jul 08 2003 AEN <aen@altlinux.ru> 1:1.1.20-alt0.2
- new source frm cvs

* Thu Jul 03 2003 AEN <aen@altlinux.ru> 1:1.1.20-alt0.1
- build from cvs source

* Mon Jun 09 2003 AEN <aen@altlinux.ru> 1:1.1.19-alt1
- new version

* Sat Mar 15 2003 AEN <aen@altlinux.ru> 1:1.1.17-alt3
- build new sources from CVS with gal2-1.99.2

* Sat Mar 15 2003 AEN <aen@altlinux.ru> 1:1.1.17-alt2
- build from CVS

* Tue Feb 25 2003 AEN <aen@altlinux.ru> 1.1.17-alt1
- build from CVS

* Thu Oct 03 2002 AEN <aen@altlinux.ru> 1.1.9-alt1
- new version for Gnome2

* Mon Jul 01 2002 AEN <aen@logic.ru> 1.0.8-alt1
- new version

* Tue May 21 2002 AEN <aen@logic.ru> 1.0.6-alt2
- add russian docs

* Mon May 13 2002 AEN <aen@logic.ru> 1.0.6-alt1
- new version

* Tue Mar 12 2002 AEN <aen@logic.ru> 1.0.5-alt1
- new version

* Mon Feb 04 2002 AEN <aen@logic.ru> 1.0.4-alt1
- new version

* Tue Jan 29 2002 AEN <aen@logic.ru> 1.0.3-alt2
- rebuilt with python-2.2

* Tue Jan 22 2002 AEN <aen@logic.ru> 1.0.3-alt1
- new release
- requires: libbonobo >= 1.0.9

* Wed Jan 16 2002 AEN <aen@logic.ru> 1.0.2-alt1
- new release

* Mon Jan 14 2002 AEN <aen@logic.ru> 1.0.1-alt2
- rebuild with gal-0.19

* Tue Jan 08 2002 AEN <aen@logic.ru> 1.0.1-alt1
- new version

* Mon Dec 31 2001 AEN <aen@logic.ru> 1.0.0-alt1
- release

* Wed Dec 26 2001 AEN <aen@logic.ru> 0.99.1-alt1
- new version

* Mon Dec 17 2001 AEN <aen@logic.ru> 0.99-alt1
- new version

* Tue Nov 20 2001 AEN <aen@logic.ru> 0.76-alt1
- new version

* Mon Nov 12 2001 AEN <aen@logic.ru> 0.75-alt3
- built with evo support

* Fri Nov 09 2001 AEN <aen@logic.ru> 0.75-alt2
- rebuilt with new gal

* Tue  Nov 06 2001 AEN <aen@logic.ru> 0.75-alt1
- new version

* Tue  Oct 30 2001 AEN <aen@logic.ru> 0.74-alt1
- new version

* Mon  Oct 29 2001 AEN <aen@logic.ru> 0.72-alt1
- new version

* Tue Oct 09 2001 AEN <aen@logic.ru> 0.71-alt1
- new version

* Fri Sep 07 2001 AEN <aen@logic.ru> 0.70-alt3
- remove gnome-core from Requires
* Wed Sep 05 2001 AEN <aen@logic.ru> 0.70-alt2
- rebuild with new gal
- oaf-slay in %pre
* Wed Aug 22 2001 AEN <aen@logic.ru> 0.70-alt1
- new version
* Wed Aug 15 2001 AEN <aen@logic.ru> 0.69-alt2
- rebuild with new libgda
* Mon Aug 13 2001 AEN <aen@logic.ru> 0.69-alt1
- new version
* Thu Aug 09 2001 AEN <aen@logic.ru> 0.68-alt2
- rebuilt with new libgal
* Wed Jul 18 2001 AEN <aen@logic.ru> 0.68-alt1
- new version
- w/o gb
* Mon Jul 9 2001 AEN <aen@logic.ru> 0.67-alt2
- rebuild with libgal-0.9
* Fri Jun 29 2001 AEN <aen@logic.ru> 0.66-alt1
- new version

* Wed May 23 2001 AEN <aen@logic.ru> 0.65-alt2
- rebuild with gb

* Tue May 22 2001 AEN <aen@logic.ru> 0.65-alt1
- new version

* Mon May 21 2001 AEN <aen@logic.ru> 0.64-alt4
- rebuild with libgal-0.8

* Tue May 15 2001 AEN <aen@logic.ru> 0.64-alt3
- rebuild with new gal

* Mon Apr 9 2001 AEN <aen@logic.ru> 0.64-alt2
- cleanup spec

* Sat Apr 7 2001 AEN <aen@logic.ru> 0.64-alt1
- 0.64
- hvv patch

* Tue Mar 13 2001 AEN <aen@logic.ru> 0.63-ipl2mdk
- rebuild in release environment

* Wed Feb 28 2001 AEN <aen@logic.ru> 0.63-ipl1mdk
- 0.63 with new libraries and gnome-db
* Mon Jan 08 2001 AEN <aen@logic.ru>
- 0.61
* Sat Dec 16 2000 AEN <aen@logic.ru>
- rebuild with gal-0.4.1

* Thu Dec 14 2000 AEN <aen@logic.ru>
- 0.60
- adopted for RE

* Tue Nov 14 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.58-1mdk
- new and shiny source.
- requires gnome-print >= 0.25
- requires gal >= 0.2.2
- buildrequires gnome-print-devel >= 0.25
- buildrequires gal >= 0.2.2

* Fri Oct 13 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.57-1mdk
- new version (needs gal)
- corrected install and added some files

* Tue Aug 29 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.56-4mdk
- added icons
- menu entry in spec file
- packager tag

* Tue Aug 22 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.56-3mdk
- BM (help by Damien)
- more macros

* Tue Jun 27 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.56-2mdk
- fix URL
- spec simplification through new chmou toys

* Wed Jun 21 2000 dam's <damien@mandrakesoft.com> 0.56-1mdk
- updated to 0.56

* Thu Jun  8 2000 dam's <damien@mandrakesoft.com> 0.54-1mdk
- updated to helix version.

* Sat May 27 2000 dam's <damien@mandrakesoft.com> 0.53-1mdk
- took new version from Helix.

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.52-3mdk
- BuildRequires: gnome-print-devel.

* Mon Apr 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.52-2mdk
- added a 32x32 icon for a better-looking KDE docking
- removed gnumeric.desktop because we don't need it, we have menu for that
- fixed /usr/share/locale/.. directory owns

* Fri Apr 14 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.52-1mdk
- took srpm from Helix [grrr.. they don't provide changelog, why?]
- add menu entry, with icon
