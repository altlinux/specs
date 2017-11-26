%def_enable snapshot

%define _name libgda
%define ver_major 5.2
%define abi_ver 5.0
# to avoid conflict with old libgda
%def_disable default_binary

%def_disable static
%def_disable gtk_doc

%def_with mysql
%def_with postgres
%def_without odbc
%def_with mdb
%def_with bdb
%def_with ldap
%def_without oracle
%def_without tds
%def_without sybase
%def_with sqlite
%def_enable system_sqlite
%def_without interbase
%def_without java
%def_disable crypto
%def_enable introspection
%def_enable vala
%def_with ui
%def_with gtksourceview

%define _libexecdir %_prefix/libexec
# openerp provides this
%add_python_req_skip rml2html

Name: %{_name}5
Version: %ver_major.4
Release: alt6

Summary: Library for writing gnome database programs
Group: System/Libraries
License: LGPL
Url: http://www.gnome-db.org/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif
Patch: libgda-5.2.4-alt-utf-8.patch

Obsoletes: libgda2 < %version
Provides: libgda2 = %version-%release

%define mysql_ver 5.0.50
%define mdbtools_ver 0.7
%define ldap_ver 2.2.27-alt1.1
%define freetds_ver 0.63
%define vala_ver 0.38

BuildPreReq: intltool >= 0.35.5
BuildPreReq: gnome-common >= 2.8.0
BuildPreReq: perl-XML-Parser
BuildPreReq: glib2-devel >= 2.12.0
BuildPreReq: libgio-devel >= 2.12.0
BuildPreReq: libxslt-devel >= 1.0.9
BuildPreReq: gtk-doc >= 1.0
BuildPreReq: libldap-devel >= %ldap_ver libsasl2-devel
BuildRequires: libjson-glib-devel libunixODBC-devel libssl-devel
BuildRequires: libgnome-keyring-devel libsecret-devel iso-codes-devel
BuildRequires: gcc-c++ libncurses-devel libreadline-devel libsoup-devel libgcrypt-devel
%{?_enable_vala:BuildRequires: vala-tools >= %vala_ver}
BuildRequires: yelp-tools
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.6.7}
%{?_with_ui:BuildRequires: libgtk+3-devel libgtk+3-gir-devel}
%{?_with_gtksourceview:BuildRequires: libgtksourceview3-devel}

%if_with postgres
BuildPreReq: libpq-devel
BuildPreReq: postgresql-devel
%endif

%if_with mysql
BuildPreReq: libMySQL-devel >= %mysql_ver
%endif

%if_with odbc
BuildPreReq: libunixODBC-devel
%endif

%if_with mdb
BuildPreReq: libmdbtools-devel >= %mdbtools_ver
%endif

%if_with interbase
#BuildPreReq: interbase
BuildPreReq: FirebirdCS
%endif

%if_with sqlite
BuildPreReq: libsqlite3-devel
%endif

%if_with ldap
BuildPreReq: libldap-devel >= %ldap_ver
# while libldap-devel doesn't requires libsasl2-devel
BuildPreReq: libsasl2-devel
%endif

%if_with tds
BuildPreReq: libfreetds-devel >= %freetds_ver
%endif

%if_with bdb
BuildPreReq: libdb4.7-devel
%endif

%if_with java
BuildRequires: java-devel
#BuildRequires: java-devel-openjdk
BuildRequires: /proc
%endif

%description
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome.org/projects/gnome-db), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

%package providers
Summary: GDA service providers for %_name
Group: System/Libraries
%if_with mysql
Requires: %name-mysql = %version-%release
%endif
%if_with postgres
Requires: %name-postgresql = %version-%release
%endif
%if_with odbc
Requires: %name-odbc = %version-%release
%endif
%if_with mdb
Requires: %name-mdb = %version-%release
%endif
%if_with interbase
Requires: %name-interbase = %version-%release
%endif
%if_with ldap
Requires: %name-ldap = %version-%release
%endif
%if_with tds
Requires: %name-tds = %version-%release
%endif
%if_with sqlite
Requires: %name-sqlite = %version-%release
%endif
%if_with bdb
Requires: %name-bdb = %version-%release
%endif
%if_with java
Requires: %name-jdbc = %version-%release
%endif

%description providers
This package includes:
%if_with ldap
GDA LDAP provider.
%endif
%if_with mysql
GDA MySQL provider.
%endif
%if_with postgres
GDA PostgreSQL provider.
%endif
%if_with odbc
GDA ODBC provider.
%endif
%if_with interbase
GDA Interbase provider.
%endif
%if_with ldap
GDA LDAP provider.
%endif
%if_with tds
Provider for TDS-based databases (using FreeTDS)
%endif
%if_with sqlite
GDA SQLite provider.
%endif
%if_with bdb
GDA BerkleyDB provider.
%endif
%if_with jdbs
JDBC provider.
%endif

%package mysql
Summary: GDA MySQL Provider
Group: System/Libraries
Requires: %name = %version-%release

%description mysql
This package includes the GDA MySQL provider.

%package bdb
Summary: GDA BerkleyDB Provider
Group: System/Libraries
Requires: %name = %version-%release

%description bdb
This package includes the GDA BerkleyDB provider.

%package postgresql
Summary: GDA PostgreSQL Provider
Group: System/Libraries
Requires: %name = %version-%release

%description postgresql
This package includes the GDA PostgreSQL provider.

%package odbc
Summary: GDA ODBC Provider
Group: System/Libraries
Requires: %name = %version-%release

%description odbc
This package includes the GDA ODBC provider.

%package mdb
Summary: GDA MS Access Provider
Group: System/Libraries
Requires: %name = %version-%release

%description mdb
This package includes the GDA MS Access provider.

%package interbase
Summary: GDA Interbase Provider
Group: System/Libraries
Requires: %name = %version-%release
#Requires: interbase

%description interbase
This package includes the GDA Intebase provider

%package ldap
Summary: GDA LDAP Provider
Group: System/Libraries
Requires: %name = %version-%release

%description ldap
This package includes the GDA LDAP provider

%package tds
Summary: CDA Provider for TDS-based databases
Group: System/Libraries
Requires: %name = %version-%release

%description tds
This package includes the GDA provider for TDS-based databases (using
FreeTDS).

%package sqlite
Summary: GDA SQLite Provider
Group: System/Libraries
Requires: %name = %version-%release

%description sqlite
This package includes the GDA SQLite provider

%package jdbc
Summary: GDA JDBC Provider
Group: System/Libraries
Requires: %name = %version-%release

%description jdbc
This package includes the GDA JDBC provider

%package devel
Summary: Development libraries and header files for libgda
Group: Development/C
Requires: %name = %version-%release
Obsoletes: libgda2-devel < %version
Provides: libgda2-devel = %version-%release

%if 0
Requires: %name-providers = %version-%release

%if_with openldap
Requires: libldap-devel >= %ldap_ver
# while libldap-devel doesn't requires libsasl2-devel
Requires: libsasl2-devel
%endif
%if_with mysql
Requires: libMySQL-devel >= %mysql_ver
%endif
%if_with postgres
Requires: postgresql-devel
%endif
%if_with odbc
Requires: libunixODBC-devel
%endif
%if_with interbase
Requires: interbase
%endif
%if_with tds
Requires: libfreetds-devel >= %freetds_ver
%endif
%{?_with_sqlite:Requires: libsqlite3-devel}

%if_with bdb
Requires: libdb4.7-devel
%endif
%endif

%description devel
This package contains the header files and libraries needed to write
or compile programs that use libgda.

%package devel-doc
Summary: Development libraries and header files for libgda
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package provides documentation needed to write programs that use libgda.

%package gir
Summary: GObject introspection data for the GDA library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GNU Data Access library.

%package gir-devel
Summary: GObject introspection devel data for the GDA library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GNU Data Access library.

%package -n libgdaui5
Summary: GNU Data Access user interface library
Group: System/Libraries
Requires: %name = %version-%release

%description -n libgdaui5
This package provides GNU Data Access user interface library.

%package -n libgdaui5-devel
Summary: Development libraries and header files for GDAUI library
Group: Development/C
Requires: libgdaui5 = %version-%release

%description -n libgdaui5-devel
This package contains the header files and libraries needed to write or
compile programs that use GNU Data Access user interface library.

%package -n libgdaui5-gir
Summary: GObject introspection data for the GDAUI library
Group: System/Libraries
Requires: libgdaui5 = %version-%release

%description -n libgdaui5-gir
GObject introspection data for the GNU Data Access user interface
library.

%package -n libgdaui5-gir-devel
Summary: GObject introspection devel data for the GDAUI library
Group: System/Libraries
BuildArch: noarch
Requires: libgdaui5-devel = %version-%release
Requires: libgdaui5-gir = %version-%release

%description -n libgdaui5-gir-devel
GObject introspection devel data for the GNU Data Access user interface
library.

%package devel-static
Summary: Static libraries for libgda
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains the static version of %name libraries.

%package -n gda-browser
Summary: GDA Browser
Group: Databases
Requires: %name = %version-%release

%description -n gda-browser
GDA Browser is a tool for database administrators: they can analyse
database's schemas to understand how data is organized, run SQL commands
interactively, and in a broader way manage the data contained in the
databases.

%prep
%setup -n %_name-%version
# convert headers from ISO-8559 to UTF-8
%patch -p1
touch config.rpath

%if_enabled crypto
sed -e 's/^[[:blank:]]//' libgda/libgda.symbols |grep '^_' > libgda/private.sym
%define private_sym _gda_server_operation_new_from_string|_split_identifier_string|_gda_vconnection_change_working_obj|_gda_vconnection_set_working_obj
%endif

%build
%autoreconf
export ac_cv_path_VAPIGEN=%_bindir/vapigen
export VALA_API_VERSION=%vala_ver
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{?_disable_default_binary:--disable-default-binary} \
%if_with bdb
    --with-bdb=%_prefix \
    --with-bdb-libdir-name=%_lib \
%endif
%if_with mysql
	--with-mysql=%prefix \
%endif
%if_with postgres
	--with-postgres=%prefix \
%endif
%if_with odbc
	--with-odbc \
%endif
%if_with mdb
	--with-mdb \
%endif
%if_with oracle
	--with-oracle \
%endif
%if_with sqlite
	%{?_enable_system_sqlite:--enable-system-sqlite} \
%endif
	%{subst_enable crypto} \
	%{?_without_java:--with-java=no} \
	%{subst_enable vala} \
%if_enabled introspection
	--enable-gda-gi \
	--enable-gdaui-gi
%endif

# SMP-incompatible build
%if_enabled crypto
%make LIBTOOL_EXPORT_OPTIONS='-export-symbols-regex "^(gda_|fnYM49765777344607__gda|%private_sym).*"'
%else
%make
%endif

%install
%makeinstall_std

%find_lang --with-gnome %_name-%abi_ver gda-browser

%files -f %_name-%abi_ver.lang
%_bindir/gda-list-config-%abi_ver
%_bindir/gda-list-server-op-%abi_ver
%_bindir/gda-sql-%abi_ver
%_bindir/gda-test-connection-%abi_ver
%_bindir/gdaui-demo-%abi_ver
%_libdir/libgda-%abi_ver.so.*
%_libdir/libgda-report-%abi_ver.so.*
%_libdir/libgda-xslt-%abi_ver.so.*
%dir %_libdir/%_name-%abi_ver
%dir %_libdir/%_name-%abi_ver/providers
%dir %_libdir/%_name-%abi_ver/plugins
%{?_enable_crypto:%_libdir/%_name-%abi_ver/providers/libgda-sqlcipher.so}
%_libdir/%_name-%abi_ver/providers/libgda-web.so
%dir %_datadir/%_name-%abi_ver/
%_datadir/%_name-%abi_ver/dtd/
%exclude %_datadir/%_name-%abi_ver/dtd/gdaui-layout.dtd
%_datadir/%_name-%abi_ver/language-specs/
%_datadir/%_name-%abi_ver/gda_trml2*
%_datadir/%_name-%abi_ver/web/
%_datadir/%_name-%abi_ver/information_schema.xml
%_datadir/%_name-%abi_ver/web_specs*.xml
%_man1dir/gda-sql*
%dir %_sysconfdir/%_name-%abi_ver
%config(noreplace) %_sysconfdir/%_name-%abi_ver/config
%doc AUTHORS ChangeLog README NEWS

%files providers

%if_with mysql
%files mysql
%_libdir/%_name-%abi_ver/*/*-mysql.so
%_datadir/%_name-%abi_ver/mysql_*.xml
%endif

%if_with postgres
%files postgresql
%_libdir/%_name-%abi_ver/*/*-postgres.so
%_datadir/%_name-%abi_ver/postgres_*.xml
%endif

%if_with mdb
%files mdb
%_libdir/%_name-%abi_ver/*/*-mdb.so
%_datadir/%_name-%abi_ver/mdb_*.xml
%endif

%if_with bdb
%files bdb
%_libdir/%_name-%abi_ver/*/*-bdb.so
%_datadir/%_name-%abi_ver/bdb_*.xml
%endif

%if_with odbc
%files odbc
%_libdir/%_name-%abi_ver/*/*-odbc.so
%endif

%if_with interbase
%files interbase
%_libdir/%_name-%abi_ver/*/*-firebird.so
%endif

%if_with ldap
%files ldap
%_libdir/%_name-%abi_ver/*/*-ldap.so
%_datadir/%_name-%abi_ver/ldap_*.xml
%endif

%if_with tds
%files tds
%_libdir/%_name-%abi_ver/*/*-freetds.so
%endif

%if_with sqlite
%files sqlite
%_libdir/%_name-%abi_ver/*/*-sqlite.so
%_datadir/%_name-%abi_ver/sqlite_*.xml
%endif

%if_with jdbc
%files jdbc
%_libdir/%_name-%abi_ver/*/gdaprovider-%abi_ver.0.jar
%_libdir/%_name-%abi_ver/*/libgda-jdbc.so
%endif

%files devel
%dir %_includedir/libgda-%abi_ver
%_includedir/libgda-%abi_ver/libgda
%_includedir/libgda-%abi_ver/libgda-report
%_includedir/libgda-%abi_ver/libgda-xslt
%_libdir/libgda-%abi_ver.so
%_libdir/libgda-report-%abi_ver.so
%_libdir/libgda-xslt-%abi_ver.so
%_pkgconfigdir/libgda-%abi_ver.pc
%_pkgconfigdir/libgda-report-%abi_ver.pc
%_pkgconfigdir/libgda-xslt-%abi_ver.pc
# .pc files for providers
%{?_enable_crypto:%_pkgconfigdir/libgda-sqlcipher-%abi_ver.pc}
%_pkgconfigdir/libgda-web-%abi_ver.pc
%{?_with_mdb:%_pkgconfigdir/*mdb*}
%{?_with_mysql:%_pkgconfigdir/*mysql*}
%{?_with_postgres:%_pkgconfigdir/*postgres*}
%{?_with_bdb:%_pkgconfigdir/*bdb*}
%{?_with_sqlite:%_pkgconfigdir/*sqlite*}
%{?_with_jdbc:%_pkgconfigdir/libgda-jdbc-%abi_ver.pc}
%{?_with_ldap:%_pkgconfigdir/libgda-ldap-%abi_ver.pc}
%{?_enable_vala:%_vapidir/*.vapi}

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%files -n libgdaui5
%_libdir/libgda-ui-%abi_ver.so.*
%_libdir/%_name-%abi_ver/plugins/libgda-ui*.so
%_libdir/%_name-%abi_ver/plugins/gdaui*.xml
%_datadir/%_name-%abi_ver/dtd/gdaui-layout.dtd
%_datadir/%_name-%abi_ver/ui/
%_datadir/%_name-%abi_ver/server_operation.glade
%dir %_datadir/%_name-%abi_ver/pixmaps
%_datadir/%_name-%abi_ver/pixmaps/bin-attachment*.png
%_datadir/%_name-%abi_ver/pixmaps/gdaui-generic.png

%exclude %_libdir/%_name-%abi_ver/plugins/libgda-ui*.la

%files -n libgdaui5-devel
%_includedir/libgda-%abi_ver/libgda-ui
%_libdir/libgda-ui-%abi_ver.so
%_pkgconfigdir/libgda-ui-%abi_ver.pc

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/Gda-%abi_ver.typelib

%files gir-devel
%_datadir/gir-1.0/Gda-%abi_ver.gir

%files -n libgdaui5-gir
%_libdir/girepository-1.0/Gdaui-%abi_ver.typelib

%files -n libgdaui5-gir-devel
%_datadir/gir-1.0/Gdaui-%abi_ver.gir
%endif

%if_enabled static
%files devel-static
%_libdir/*.a
%_libdir/%_name-%abi_ver/*/*.a
%endif

%files -n gda-browser -f gda-browser.lang
%_bindir/gda-browser-%abi_ver
%_bindir/gda-control-center-%abi_ver
%_datadir/applications/gda-browser-%abi_ver.desktop
%_datadir/applications/gda-control-center-%abi_ver.desktop
%_iconsdir/hicolor/*x*/apps/gda-control-center.png
%_datadir/%_name-%abi_ver/import_encodings.xml
%_datadir/%_name-%abi_ver/icons/hicolor/*/actions/*
%_datadir/%_name-%abi_ver/pixmaps/gda-browser*.png
%_datadir/%_name-%abi_ver/pixmaps/gda-control-center*.png
%_datadir/pixmaps/gda-browser*.png
%_datadir/appdata/gda-browser-%abi_ver.appdata.xml

%exclude %_libdir/%_name-%abi_ver/providers/*.la
%exclude %_sysconfdir/%_name-%abi_ver/sales_test.db
%exclude %_datadir/%_name-%abi_ver/demo
%exclude %_datadir/%_name-%abi_ver/php

%changelog
* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 5.2.4-alt6
- updated to LIBGDA_5_2_4-41-g7945516
- fixed build with recent glib-mkenums
- built with vala-0.38

* Fri Mar 31 2017 Yuri N. Sedunov <aris@altlinux.org> 5.2.4-alt5
- rebuilt with vala-0.36

* Tue Jan 10 2017 Yuri N. Sedunov <aris@altlinux.org> 5.2.4-alt4
- updated to 5_2_4-37-gebe3b20

* Sun May 08 2016 Yuri N. Sedunov <aris@altlinux.org> 5.2.4-alt3
- updated to 5_2_4-32-g03de66c

* Wed Oct 28 2015 Yuri N. Sedunov <aris@altlinux.org> 5.2.4-alt2
- 5.2.4_bc89eb08

* Mon Jul 06 2015 Yuri N. Sedunov <aris@altlinux.org> 5.2.4-alt1
- 5.2.4

* Sat Mar 16 2013 Yuri N. Sedunov <aris@altlinux.org> 5.1.2-alt1
- 5.1.2 release

* Mon Dec 03 2012 Yuri N. Sedunov <aris@altlinux.org> 5.1.2-alt0.1
- libgda4->libgda5 (5.1.2 snapshot (670276bca4c))
- disabled crypto (SQLCipher database provider)

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 4.2.13-alt1
- 4.2.13 snapshot (7a3e641)

* Wed Jun 01 2011 Yuri N. Sedunov <aris@altlinux.org> 4.2.7-alt1
- 4.2.7

* Wed Feb 16 2011 Yuri N. Sedunov <aris@altlinux.org> 4.2.4-alt1
- 4.2.4

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Fri Oct 08 2010 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sat Jun 12 2010 Yuri N. Sedunov <aris@altlinux.org> 4.0.9-alt1
- 4.0.9

* Thu Apr 01 2010 Yuri N. Sedunov <aris@altlinux.org> 4.0.8-alt2
- rebuild with new rpm-build-gir

* Sat Mar 06 2010 Yuri N. Sedunov <aris@altlinux.org> 4.0.8-alt1
- 4.0.8
- introspection support

* Mon Jul 20 2009 Yuri N. Sedunov <aris@altlinux.org> 4.0.2-alt2
- fixed build

* Sat Apr 18 2009 Yuri N. Sedunov <aris@altlinux.org> 4.0.2-alt1
- 4.0.2
- use --disable-default-binary to fix ALT #19662

* Sun Mar 29 2009 Yuri N. Sedunov <aris@altlinux.org> 4.0.1-alt1
- new version

* Thu Mar 19 2009 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0
- JDBC provider

* Tue Jan 20 2009 Yuri N. Sedunov <aris@altlinux.org> 3.99.9-alt1
- 3.99.9
- removed obsolete %%post{,un}_ldconfig

* Mon Nov 10 2008 Yuri N. Sedunov <aris@altlinux.org> 3.99.6-alt1
- rename libgda to libgda4
- disable freetds, LDAP, ODBC providers (not implemented yet)
- updated buildreqs

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.9.103-alt1.0
- Fixed postgresql build dependencies.
- Rebuilt due to libpq.so.4 -> libpq.so.5 soname change.

* Fri Sep 15 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.9.103-alt1
- renamed libgda2 -> libgda
- newer version of libdb(4.4) for providers
- xml provider not exist any more
- no mSQL, IBM DB2, Xbase support
- mono support preparing

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.91-alt1.1.1.1
- Rebuilt with libldap-2.3.so.0.

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.91-alt1.1.1
- Rebuilt for new pkg-config dependencies.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.91-alt1.1
- Rebuilt with libreadline.so.5.

* Mon Nov 28 2005 Vital Khilko <vk@altlinux.ru> 1.3.91-alt1
- 1.3.91

* Mon Oct 31 2005 Vital Khilko <vk@altlinux.ru> 1.2.2-alt2
- fixed postgres dependencies

* Fri Oct 28 2005 Vital Khilko <vk@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Mon Nov 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.99-alt1
- 1.1.99
- mdb provider temporarily disabled (not ready for 0.6).

* Fri Jun 25 2004 Vital Khilko <vk@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Fri May 28 2004 Vital Khilko <vk@altlinux.ru> 1.1.2-alt2
- rebuilded with sqlite and without interbase providers

* Mon Apr 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Thu Apr 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.1-alt2
- gda-export.h provided by libgda2-devel subpackage.

* Tue Apr 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Tue Dec 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.2-alt1
- 1.0.2
- do not package .la files.
- do not build devel-static subpackage by default.

* Mon Sep 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt2
- rebuild with new mysql.
- removed unusual dependencies (fix #3012).

* Mon Sep 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Thu Jul 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.90.0-alt1
- 0.90.0

* Mon Jun 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.12.1-alt1
- interbase support disabled. !!!

* Thu May 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.12.0-alt1
- 0.12.0
- new tds provider package.

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Sun Feb 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.10.0-alt2
- fixed buildreqs (close #2181).

* Tue Jan 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Thu Dec 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt1
- new version.
- mdb provider.

* Wed Dec 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.8.199-alt2
- Removed wrong dependence on postgresql-libs for main package (#1660)

* Mon Oct 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.8.199-alt1
- 0.8.199

* Sun Sep 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.8.192-alt1
- Adopted for Sisyphus.
- devel-static package.
- providers moved in separate packages.

* Tue Feb 26 2002 Chris Chabot <chabotc@reviewboard.com>
- Added defines and configure flags for all supported DB types

* Mon Feb 25 2002 Chris Chabot <chabotc@reviewboard.com>
- Cleaned up formatting
- Added Requirements
- Added defines for postgres, mysql, odbc support

* Thu Feb 21 2002 Chris Chabot <chabotc@reviewboard.com>
- Initial spec file
