%def_disable snapshot
%def_disable static
%def_enable man

Name: mdbtools
Version: 1.0.0
Release: alt1.1

Summary: Utilities for use M$ Access databases under Linux
Group: Databases
License: GPL-2.0 and LGPL-2.0
Url: https://github.com/mdbtools/mdbtools

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

Requires: lib%name = %EVR

%define glib_ver 2.68

BuildRequires: bison flex glib2-devel >= %glib_ver libreadline-devel libunixODBC-devel
BuildRequires: bash-completion
%{?_enable_man:BuildRequires: txt2man}
%{?_enable_static:BuildRequires: glibc-devel-static glib2-devel-static}

%description
MDB Tools is a set of libraries and programs to help you use Microsoft
Access file in various settings.

%package -n lib%name
Summary: MDB Tools shared libraries
Group: System/Libraries
License: LGPL-2.0
Requires: glib2 >= %glib_ver

%description -n lib%name
MDB Tools is a set of libraries and programs to help you use Microsoft
Access file in various settings.
This package provides MDB Tools shared libraries.

%package -n lib%name-devel
Summary: MDB Tools development files and libraries
Group: Development/C
License: LGPL-2.0
Requires: lib%name = %EVR
Requires: glib2-devel >= %glib_ver

%description -n lib%name-devel
This package contains the files needed to build packages that depend on
MDB Tools libraries.

%package -n lib%name-devel-static
Summary: MDB Tools static libraries
Group: Development/C
License: LGPL-2.0
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
This package contains the libraries needed to build applications
statically linked with MDB Tools.

%prep
%setup
# always use system GLIB:
sed -i 's|\(Cflags:.*\)$|\1 -DHAVE_GLIB=1|' *.pc.in

%build
%add_optflags %(getconf LFS_CFLAGS)
%ifarch %e2k
# lcc 1.25.20 ftbfs workaround (cf. mcst#6021)
%add_optflags -Wno-error=maybe-uninitialized
%endif
%autoreconf
%configure \
    %{subst_enable static} \
    --with-unixodbc=%_prefix \
    %{subst_enable man}
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%{?_enable_man:%_man1dir/*}
%_datadir/bash-completion/completions/mdb-*
%doc AUTHORS NEWS README* TODO*

%files -n lib%name
%_libdir/*.so.*
%dir %_libdir/odbc/
%_libdir/odbc/libmdbodbc*.so

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Fri Jan 14 2022 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1.1
- E2K: lcc 1.25 ftbfs workaround

* Sat Nov 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Fri Aug 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1
- 0.9.4

* Fri Dec 18 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0 (moved gmdb2 to its own project)

* Sat Jul 04 2020 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- updated to 0.8.2-4-ga6c3fa2 from new %%url

* Thu Jun 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt2
- updated to 0.7.1-82-gd6f5745
- enabled gmdb build
- updated buildreqs

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Fri Jun 07 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- go to new upstream: https://github.com/brianb/mdbtools
- build against libodbcinst.so.2

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

