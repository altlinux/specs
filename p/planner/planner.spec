Name: planner
Version: 0.14.6
Release: alt1

Summary: Planner - project management application
Summary(ru_RU.KOI8-R): Программа управления проектами Planner

License: GPL
Group: Office
Url: http://live.gnome.org/Planner
#http://ftp.gnome.org/pub/GNOME/sources/planner/0.14

Packager: Pavel Vainerman <pv@altlinux.ru>

#Source: http://ftp.gnome.org/pub/GNOME/sources/planner/%version/%name-%version.tar.bz2
Source: http://ftp.gnome.org/pub/GNOME/sources/planner/0.14/%name-%version.tar.bz2
Source1: %name-%version.ru.po
#Patch: %name-%version.patch

# Automatically added by buildreq on Sat Jun 26 2010
BuildRequires: desktop-file-utils glibc-devel-static gtk-doc intltool libglade-devel libgnomeui-devel librarian libxslt-devel libgsf-devel

# python-base python-dev python-module-pygtk-devel python-modules-compiler python-modules-encodings esound

Obsoletes: mrproject
Provides: mrproject

Requires: lib%name = %version-%release

%add_findprov_lib_path %_libdir/%name

%description
Planner, a project management application for GNOME.

%description -l ru_RU.KOI8-R
Программа управления проектами Planner для GNOME.

%package -n lib%name
Summary: Libraries for planner
Group: System/Libraries
Obsoletes: libmrproject

%description -n lib%name
This package provides libraries to use planner.
%description -n lib%name -l ru_RU.KOI8-R
Пакет предоставляет библиотеки, используемые planner.

%package -n lib%name-devel
Group: Development/C
Summary: Libraries needed to develop for planner
Summary(ru_RU.KOI8-R): Библиотеки, требуемые для разработки с planner
Requires: lib%name = %version-%release libxml2-devel 
Obsoletes: libmrproject-devel

%description -n lib%name-devel
Libraries needed to develop for planner.
%description -n lib%name-devel -l ru_RU.KOI8-R
Библиотеки, требуемые для разработки с planner.


%prep
%setup -q
#%patch -p0
cp -f %SOURCE1 po/ru.po

%build
#autoreconf -fisv
%__subst "s| install-data-hook||" data/mime/Makefile.in
%configure --disable-postgres --disable-python --enable-simple-priority-scheduling
#%make_build
%make

%install
%makeinstall

%find_lang %name --with-gnome

mkdir -p $RPM_BUILD_ROOT%_datadir/doc/%name-%version

#DOCS="README.sql sample-1.planner kitchen.planner"

DOCS=$( ls $RPM_BUILD_ROOT%_datadir/doc/%name )
for i in $DOCS
do
	cd $RPM_BUILD_ROOT%_datadir/doc/%name-%version/
	%__mv ../%name/$i $i
done


%files -n lib%name-devel
%_includedir/%name-1.0
%_libdir/pkgconfig/*
%_libdir/libplanner-1.so

%files -n lib%name
%_libdir/%name
%_libdir/*.so.*
%_libdir/%name/*/*.so

%exclude %_libdir/%name/*/*.la
#%exclude %_libdir/%name/*.la

#%_libdir/%name/file-modules/*.so
#%_libdir/%name/plugins/*.so
#%_libdir/%name/storage-modules/*.so
#%_libdir/%name/views/*.so


%files -f %name.lang
# %doc ChangeLog README
%_bindir/*
%_sysconfdir/gconf/schemas/%name.schemas
#%_datadir/application-registry/*
%_datadir/applications/*
#%_datadir/mime-info/*
%_datadir/mime/packages/*
%_datadir/gnome/help/%name
# %_datadir/gtk-doc/html/lib%name
%_datadir/doc/%name-%version/*
%_datadir/omf/%name
%_datadir/pixmaps/*
%_datadir/%name
%_datadir/icons/hicolor/48x48/mimetypes/*
%_man1dir/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/planner-%version 


%changelog
* Tue Jan 31 2012 Pavel Vainerman <pv@altlinux.ru> 0.14.6-alt1
- new version (0.14.6)

* Thu Sep 29 2011 Pavel Vainerman <pv@altlinux.ru> 0.14.5-alt1
- new version (0.14.5)

* Sat Jun 26 2010 Pavel Vainerman <pv@altlinux.ru> 0.14.4-alt2
- update version (closes: #22116)
- update ru.po 

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.14.3-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for planner
  * postclean-05-filetriggers for spec file

* Sun Feb 08 2009 Pavel Vainerman <pv@altlinux.ru> 0.14.3-alt4
- update build depends

* Tue Dec 30 2008 Pavel Vainerman <pv@altlinux.ru> 0.14.3-alt3
- bug fixes (add libplanner for devel package)

* Mon Dec 29 2008 Pavel Vainerman <pv@altlinux.ru> 0.14.3-alt2
- add libglade-devel for build depends

* Mon Dec 29 2008 Pavel Vainerman <pv@altlinux.ru> 0.14.3-alt1
- new version (0.14.3)

* Sun Oct 14 2007 Pavel Vainerman <pv@altlinux.ru> 0.14.2-alt5
- remove menu file
- add man pages

* Tue Oct 09 2007 Pavel Vainerman <pv@altlinux.ru> 0.14.2-alt4
- fixed for new rpmbuild: find-provides

* Tue Aug 07 2007 Pavel Vainerman <pv@altlinux.ru> 0.14.2-alt3
- update build requires

* Fri Apr 13 2007 Pavel Vainerman <pv@altlinux.ru> 0.14.2-alt2
- fixed bug: undefined reference to `floor'

* Wed Nov 29 2006 Pavel Vainerman <pv@altlinux.ru> 0.14.2-alt1
- new version (0.14.2)

* Tue Sep 26 2006 Pavel Vainerman <pv@altlinux.ru> 0.14.1-alt1
- new version (0.14.1)

* Tue Aug 01 2006 Pavel Vainerman <pv@altlinux.ru> 0.14-alt1
- new version (0.14)

* Mon Sep 19 2005 Pavel Vainerman <pv@altlinux.ru> 0.13-alt9
- corrected package requires

* Sat Sep 17 2005 Pavel Vainerman <pv@altlinux.ru> 0.13-alt8
- fixed unment dependency libplanner-1.so.0 again... :)

* Wed Sep 14 2005 Pavel Vainerman <pv@altlinux.ru> 0.13-alt7
- fixed unment dependency libplanner-1.so.0

* Sat Sep 10 2005 Pavel Vainerman <pv@altlinux.ru> 0.13-alt6
- spec fixed (include %_libdir)
- update BuildRequires

* Mon Jun 20 2005 Pavel Vainerman <pv@altlinux.ru> 0.13-alt5
- update ru.po
- add patch for russian language

* Wed Jun 08 2005 Pavel Vainerman <pv@altlinux.ru> 0.13-alt4
- remove empty directory (gtk-doc/html/libplanner) from package

* Mon Mar 28 2005 Pavel Vainerman <pv@altlinux.ru> 0.13-alt3
- fixed bug: not build documentation

* Thu Mar 24 2005 Pavel Vainerman <pv@altlinux.ru> 0.13-alt2
- disable python

* Wed Mar 23 2005 Pavel Vainerman <pv@altlinux.ru> 0.13-alt1
- build new version
- update spec-file

* Mon Nov 08 2004 Pavel Vainerman <pv@altlinux.ru> 0.12.1-alt2
- change docdir

* Mon Sep 20 2004 Pavel Vainerman <pv@altlinux.ru> 0.12.1-alt1
- build new version

* Sun Jul 11 2004 Pavel Vainerman <pv@altlinux.ru> 0.12-alt1
- build new version
- update ru.po

* Mon Jun 14 2004 Pavel Vainerman <pv@altlinux.ru> 0.11-alt4
- fix bug #4353 (wrong pkgconfig depends)

* Mon Jun 07 2004 Pavel Vainerman <pv@altlinux.ru> 0.11-alt3
- build with N proc fixed

* Sun Jun 06 2004 Pavel Vainerman <pv@altlinux.ru> 0.11-alt2
- rebuild with new libs
- update requires

* Sun May 23 2004 Pavel Vainerman <pv@altlinux.ru> 0.11-alt1
- new version with new name of project
- remove COPYING from doc

* Mon Sep 22 2003 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- new version

* Mon Mar 17 2003 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version
- update russian translation

* Tue Jan 07 2003 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1pre
- new version (0.8pre)
- add post & postun sections (thanks to Yuri N. Sedunov <aris@altlinux.ru>)
- add requires on libmproject version
- update russian translation

* Sun Dec 01 2002 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt2
- add missed omf, gnome/help to files

* Thu Nov 28 2002 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- new version

* Sat Nov 02 2002 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2
- add genericname
- new version
- spec cleanup and messages translated in russian
- add ru.po

* Wed Oct 09 2002 AEN <aen@altlinux.ru> 0.6-alt1
- new version (Gnome2)

* Thu Mar 14 2002 AEN <aen@linux.ru> 0.5.1-alt2
- rebuilt win conv_deskfiles.pl

* Wed Jan 23 2002 AEN <aen@logic.ru> 0.5.1-alt1
- new version

* Mon Jan 14 2002 AEN <aen@logic.ru> 0.5.0-alt2
- rebuilt with libgal-0.19

* Thu Dec 20 2001 AEN <aen@logic.ru> 0.5.0-alt1
- new version

* Fri Nov 09 2001 AEN <aen@logic.ru> 0.4.1-alt2
- rebuilt with new gal

* Fri Oct 25 2001 AEN <aen@logic.ru> 0.4.1-alt1
- new version
- rebuild with new libgal

* Tue Oct 09 2001 AEN <aen@logic.ru> 0.4.0-alt1
- new version
- patch to build with new bonobo

* Wed Sep 05 2001 AEN <aen@logic.ru> 0.3.2-alt4
- rebuild with libgal-0.11.2
- oaf-slay added in %pre
* Thu Aug 09 2001 AEN <aen@logic.ru> 0.3.2-alt3
- rebuild with libgal-0.10
* Mon Jul 9 2001 AEN <aen@logic.ru> 0.3.2-alt2
- rebuild with libgal-0.9
* Fri Jul 6 2001 AEN <aen@logic.ru> 0.3.2-alt1
- first Spring package
