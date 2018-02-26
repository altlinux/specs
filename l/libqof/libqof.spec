Name: libqof
Version: 0.8.4
Release: alt1

Summary: QOF - Query Object Framework

License: GPL
Group: System/Libraries
Url: http://qof.alioth.debian.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://alioth.debian.org/frs/download.php/3029/qof-%version.tar

# Automatically added by buildreq on Sat Jan 21 2012
# optimized out: libgpg-error libstdc++-devel pkg-config tzdata
BuildRequires: doxygen gcc-c++ glib2-devel graphviz libsqlite-devel libxml2-devel xsltproc

BuildRequires: intltool

%description
QOF - Query Object Framework is a library for adding a query engine
to C applications.  An SQL database is not needed; any collection
of C/C++ objects can act as 'tables' which can be 'joined' using
an SQL-like programming interface.

%package devel
Summary: Header files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contain header files for %name

%prep
%setup -n qof-%version

%build
# with autoreconf got error: m4_divert_push: cannot change diversion to `GROW' inside m4_expand
#autoreconf
%configure --disable-static --enable-sqlite --disable-error-on-warning --disable-rpath

# fix rpath in libs
%__subst 's|^\(hardcode_into_libs\)=.*$|\1=no|' libtool
# FIXME: stranges with --docdir=%_docdir/%name-%version
# hack to fix smp build (i forget correct line for makefile)
make -C lib/libsql libqofsql.la
%make_build

%install
%makeinstall_std

%find_lang qof

%files -f qof.lang
%doc README NEWS ChangeLog
%_libdir/*.so.*
%_datadir/xml/qof/
%dir %_libdir/qof2/
%_libdir/qof2/*.so
%_libdir/qof2/%name-backend-*.la

%files devel
#%_docdir/%name-%version/
%_docdir/qof/
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Sat Jan 21 2012 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt1
- new version 0.8.4 (with rpmrb script)

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)
- update buildreq

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.5-alt1
- new version 0.7.5 (with rpmrb script)
- cleanup spec

* Sat Apr 21 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt1
- new version 0.7.2 (with rpmrb script)

* Thu Dec 28 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt0.1
- new version 0.7.1 (with rpmrb script)
- fix build, update as-needed patch

* Wed May 17 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt0.1
- new version 0.6.4, update patch
- add some docs files

* Sat Mar 25 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version, with patches for --as-needed
- disable internal libsql
- update buildreqs

* Wed Mar 01 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- release

* Mon Jan 23 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt0.1cvs20060123
- cvs version (according to svn version from gnucash repository)

* Mon Jan 09 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version

* Sun Dec 04 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version

* Sat Mar 19 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt0.1pre1
- initial build for ALT Linux Sisyphus

