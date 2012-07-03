# ./rdf_init_internal.h:142: error: expected specifier-qualifier-list before 'rasqal_world'

# Conditional build:
%def_without	threestore	# with 3store
%define oname redland

Name: libredland
Version: 1.0.15
Release: alt1

Summary: Redland - a library that provides a high-level interface for RDF

License: LGPL v2.1+ or GPL v2+ or Apache v2
Group: System/Libraries
Url: http://librdf.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.librdf.org/source/%oname-%version.tar.bz2
Patch: %oname-link.patch
Patch1: %oname-sqlite.patch

BuildPreReq: rpm-build-intro

# Automatically added by buildreq on Thu Sep 01 2011 (-bi)
# optimized out: elfutils libpq-devel pkg-config raptor2-devel
#BuildRequires: glibc-devel-static gtk-doc libdb4-devel libiodbc-devel libltdl7-devel libmysqlclient-devel libredland-devel libsqlite-devel libsqlite3-devel postgresql-devel rasqal-devel
BuildRequires: glibc-devel gtk-doc libdb4-devel libiodbc-devel libltdl-devel glib2-devel
BuildRequires: libmysqlclient-devel libredland-devel libsqlite3-devel postgresql-devel rasqal-devel

%if_with threestore
BuildRequires: 3store-devel >= 2.0
BuildRequires: 3store-devel < 3.0
%endif

%description
Redland is a library that provides a high-level interface for RDF
allowing the RDF graph to be parsed from XML, stored, queried and
manipulated. Redland implements each of the RDF concepts in its own
class via an object based API, reflected into the other language APIs:
Perl, Python, Tcl, Java and Ruby. Some of the classes providing the
parsers, storage mechanisms and other elements are built as modules
that can be added or removed as required.

%package devel
Summary: Headers for Redland RDF library
Group: Development/C
Requires: %name = %version-%release
%if_with threestore
Requires: 3store-devel >= 2.0
Requires: 3store-devel < 3.0
%endif

%description devel
Headers for Redland RDF library.

%package -n python-module-redland
Summary: Python bindings for Redland RDF library
Group: System/Libraries/Python
Requires: %name = %version-%release

%description -n python-module-redland
Python bindings for Redland RDF library

%prep
%setup -q -n %oname-%version
#patch1 -p2

#__autoreconf
./autogen.sh

%build
%configure \
	--disable-static \
	--enable-release \
	--with-html-dir=%_gtkdocdir \
	--with-threestore=%{!?with_threestore:no}%{?with_threestore:yes} \
	--with-raptor=system \
	--with-rasqal=system

%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog* FAQS.html LICENSE.html NEWS.html README.html RELEASE.html TODO.html
%_bindir/rdfproc
%_bindir/redland-db-upgrade
%_libdir/librdf.so.*
%dir %_libdir/redland/
%_libdir/redland/librdf_storage_mysql.so
%_libdir/redland/librdf_storage_postgresql.so
%_libdir/redland/librdf_storage_sqlite.so
%_libdir/redland/librdf_storage_virtuoso.so
%dir %_datadir/redland/
%_datadir/redland/mysql-v*.ttl
%_man1dir/rdfproc.1*
%_man1dir/redland-db-upgrade.1*


%files devel
%doc docs/{README.html,storage.html}
%_bindir/redland-config
%_libdir/librdf.so
%_includedir/librdf.h
%_includedir/rdf_*.h
%_includedir/redland.h
%_datadir/redland/Redland.i
%_pkgconfigdir/redland.pc
%_man1dir/redland-config.1*
%_man3dir/redland.3*
%_gtkdocdir/redland/

%changelog
* Thu May 24 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.15-alt1
- new version

* Tue Oct 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.14-alt2
- fix build requires

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.14-alt0.M60P.1
- built for M60P

* Mon Sep 05 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.14-alt1
- new version (ALT#26213)

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.12-alt1
- new version 1.0.12 (with rpmrb script)

* Fri Nov 20 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt2
- fix build (thanks, kas@)

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt1
- new version 1.0.8 (with rpmrb script)
- remove post/postun scripts

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.7-alt1
- new version 1.0.7 (with rpmrb script)
- update buildreq

* Sun Oct 21 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- initial build for ALT Linux Sisyphus

