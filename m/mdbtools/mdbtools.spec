%define pre %nil
%def_disable static
%def_disable gmdb2

Name: mdbtools
Version: 0.6
Release: alt8cvs20051217%pre

Summary: Utilities for use M$ Access databases under Linux

Group: Databases
License: GPL/LGPL
Url: http://mdbtools.sourceforge.net/
Source: http://dl.sourceforge.net/%name/%name-%version%pre.tar.bz2

Patch0: %name-as-needed.patch
Patch1: %name-0.6-alt-sql.patch

Requires: lib%name = %version-%release

BuildRequires: flex libreadline-devel libunixODBC-devel glib2-devel
%{?_enable_gmdb2:BuildRequires: libglade-devel libgnomeui-devel librarian}

%description
MDB Tools is a set of libraries and programs to help you use Microsoft
Access file in various settings.

This package provides:
Several command line utilities to list tables, export schema, and data,
show the version of the files, and other useful stuff.
mdb-sql - a command line SQL tool that allows one to type sql queries
and get results.

%package -n gmdb
Summary: MS Access MDB File Viewer
Group: Databases
Requires: lib%name = %version-%release

%description -n gmdb
gmdb - The GTK2 MDB File Viewer and debugger. Still alpha, but making
great progress.

%package -n lib%name
Summary: MDB Tools shared libraries
Group: System/Libraries

%description -n lib%name
MDB Tools is a set of libraries and programs to help you use Microsoft
Access file in various settings.

This package contains:
libmdb		the core library that allows access to MDB files programatically.
libmdbsql	builds on libmdb to provide a SQL engine (ala Jet)
libmdbodbc	an ODBC driver for use with unixODBC driver manager. Allows
		one to use MDB files with PHP for example.

%package -n lib%name-devel
Summary: MDB Tools development files and libraries
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the files needed to build packages that depend on
MDB Tools.

%package -n lib%name-devel-static
Summary: MDB Tools static libraries
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains the libraries needed to build applications
statically linked with MDB Tools.

%prep
%setup -q -n %name-%version%pre
%patch0 -p0
%patch1 -p1
subst "s|.*<config\.h>.*||" include/mdbtools.h

%build
%autoreconf
%configure \
    %{subst_enable static} \
    --with-unixodbc=%_prefix \
    %{subst_enable gmdb2}

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*
%{?_enable_gmdb2:%exclude %_bindir/gmdb2}
%_man1dir/*
%doc AUTHORS NEWS README TODO ChangeLog doc/faq.html

%if_enabled gmdb2
%files -n gmdb
%_bindir/gmdb2
%_datadir/gmdb
%doc %_datadir/gnome/help/gmdb
%endif

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Mon Apr 09 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt8cvs20051217
- don't build gmdb

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt7cvs20051217
- rebuild for soname set-versions

* Mon Dec 29 2008 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt6cvs20051217
- updated buildreqs
- removed obsolete %%post{,un}_ldconfig

* Sat Apr 15 2006 Igor Zubkov <icesik@altlinux.ru> 0.6-alt5cvs20051217
- fix changelog
- buildreq

* Fri Apr 07 2006 Igor Zubkov <icesik@altlinux.ru> 0.6-alt4cvs20051217
- update from cvs
- add fix for export to sql

* Wed Apr 05 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt4cvs20050908
- fix build with ld --as-needed

* Mon Oct 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt3cvs20050908
- fix release (2.1cvs < 2cvs)

* Mon Sep 19 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2.1cvs20050908
- fix bug #8007 (config.h in system wide headers)
- Note: you have to define HAVE_ICONV _before_include mdbtools.h

* Thu Sep 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2cvs20050908
- come back to Sisyphus :) CVS version

* Fri Aug 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6-alt1pre1
- 0.6pre1

* Mon Dec 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt3
- do not package .la files.
- do not build devel-static subpackage by default. 

* Wed Oct 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt2
- fixed buildreqs.

* Sun Jan 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt1
- new version.

* Thu Dec 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4-alt1
- First build for Sisyphus.

