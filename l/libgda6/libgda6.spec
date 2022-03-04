%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define _name libgda
%define ver_major 6.0
%define abi_ver_major 6
%define abi_ver 6.0
%def_disable doc
%def_with mysql
%def_with postgres
%def_with sqlite
%def_with sqlcipher
%def_enable system_sqlite
# experimental
%def_without ldap
%def_without web
# not supported in 6.0
%def_without odbc
%def_without mdb
%def_without bdb
%def_without interbase
%def_without oracle
%def_without tds
%def_without sybase
%def_without java

%def_enable introspection
%def_enable vala
# experimental would be defined for ui
%def_enable experimental
%def_enable ui
%def_with gtksourceview
%def_enable glade
%def_enable tools

%add_python3_path %_datadir/%_name-%abi_ver
# openerp provides this
%add_python3_req_skip rml2html

Name: %{_name}%abi_ver_major
Version: %ver_major.0
Release: alt1

Summary: Library for writing gnome database programs
Group: System/Libraries
License: GPL-2.0 and LGPL-2.0
Url: http://www.gnome-db.org/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif
Patch: libgda-6.0.0-alt-meson.patch

Obsoletes: libgda2 < %version
Provides: libgda2 = %EVR

%define mysql_ver 8.0
%define mdbtools_ver 0.7
%define ldap_ver 2.2.27-alt1.1
%define freetds_ver 0.63
%define vala_ver 0.54
%define sqlite_ver 3.10.2

BuildRequires(pre): meson rpm-build-gir rpm-build-vala rpm-build-python3
BuildRequires: intltool gcc-c++
BuildRequires: glib2-devel >= 2.12.0
BuildRequires: libgio-devel >= 2.12.0
BuildRequires: libxslt-devel >= 1.0.9
BuildRequires: libgee0.8-devel
BuildRequires: libjson-glib-devel libunixODBC-devel libssl-devel
BuildRequires: libgnome-keyring-devel libsecret-devel iso-codes-devel
BuildRequires: libncurses-devel libreadline-devel libsoup-devel libgcrypt-devel
%{?_with_ldap:BuildRequires: libldap-devel >= %ldap_ver libsasl2-devel}
%{?_enable_glade:BuildRequires: libgladeui2.0-devel}
%{?_enable_vala:BuildRequires: vala-tools >= %vala_ver}
BuildRequires: yelp-tools valadoc
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.6.7}
%{?_enable_ui:BuildRequires: libgtk+3-devel libgtk+3-gir-devel libgoocanvas2-devel}
%{?_with_gtksourceview:BuildRequires: libgtksourceview3-devel}

%if_with postgres
BuildRequires: postgresql-devel
%endif

%if_with mysql
BuildRequires: libMySQL-devel >= %mysql_ver
%endif

%if_with odbc
BuildRequires: libunixODBC-devel
%endif

%if_with mdb
BuildRequires: libmdbtools-devel >= %mdbtools_ver
%endif

%if_with interbase
#BuildPreReq: interbase
BuildRequires: FirebirdCS
%endif

%if_with sqlite
BuildRequires: libsqlite3-devel >= %sqlite_ver
%endif

%if_with sqlcipher
BuildRequires: libsqlcipher-devel
%endif

%if_with ldap
BuildRequires: libldap-devel >= %ldap_ver
# while libldap-devel doesn't requires libsasl2-devel
BuildRequires: libsasl2-devel
%endif

%if_with tds
BuildRequires: libfreetds-devel >= %freetds_ver
%endif

%if_with bdb
BuildRequires: libdb4.7-devel
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
Requires: %name-mysql = %EVR
%endif
%if_with postgres
Requires: %name-postgresql = %EVR
%endif
%if_with odbc
Requires: %name-odbc = %EVR
%endif
%if_with mdb
Requires: %name-mdb = %EVR
%endif
%if_with interbase
Requires: %name-interbase = %EVR
%endif
%if_with ldap
Requires: %name-ldap = %EVR
%endif
%if_with tds
Requires: %name-tds = %EVR
%endif
%if_with sqlite
Requires: %name-sqlite = %EVR
%endif
%if_with bdb
Requires: %name-bdb = %EVR
%endif
%if_with java
Requires: %name-jdbc = %EVR
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
Requires: %name = %EVR

%description mysql
This package includes the GDA MySQL provider.

%package bdb
Summary: GDA BerkleyDB Provider
Group: System/Libraries
Requires: %name = %EVR

%description bdb
This package includes the GDA BerkleyDB provider.

%package postgresql
Summary: GDA PostgreSQL Provider
Group: System/Libraries
Requires: %name = %EVR

%description postgresql
This package includes the GDA PostgreSQL provider.

%package odbc
Summary: GDA ODBC Provider
Group: System/Libraries
Requires: %name = %EVR

%description odbc
This package includes the GDA ODBC provider.

%package mdb
Summary: GDA MS Access Provider
Group: System/Libraries
Requires: %name = %EVR

%description mdb
This package includes the GDA MS Access provider.

%package interbase
Summary: GDA Interbase Provider
Group: System/Libraries
Requires: %name = %EVR
#Requires: interbase

%description interbase
This package includes the GDA Intebase provider

%package ldap
Summary: GDA LDAP Provider
Group: System/Libraries
Requires: %name = %EVR

%description ldap
This package includes the GDA LDAP provider

%package tds
Summary: CDA Provider for TDS-based databases
Group: System/Libraries
Requires: %name = %EVR

%description tds
This package includes the GDA provider for TDS-based databases (using
FreeTDS).

%package sqlite
Summary: GDA SQLite Provider
Group: System/Libraries
Requires: %name = %EVR

%description sqlite
This package includes the GDA SQLite provider

%package jdbc
Summary: GDA JDBC Provider
Group: System/Libraries
Requires: %name = %EVR

%description jdbc
This package includes the GDA JDBC provider

%package devel
Summary: Development libraries and header files for libgda
Group: Development/C
Requires: %name = %EVR
Obsoletes: libgda2-devel < %version
Provides: libgda2-devel = %EVR


Requires: %name-providers = %EVR

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
Requires: %name = %EVR

%description gir
GObject introspection data for the GNU Data Access library.

%package gir-devel
Summary: GObject introspection devel data for the GDA library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the GNU Data Access library.

%package -n libgdaui%abi_ver_major
Summary: GNU Data Access user interface library
Group: System/Libraries
Requires: %name = %EVR

%description -n libgdaui%abi_ver_major
This package provides GNU Data Access user interface library.

%package -n libgdaui%abi_ver_major-devel
Summary: Development libraries and header files for GDAUI library
Group: Development/C
Requires: libgdaui%abi_ver_major = %EVR

%description -n libgdaui%abi_ver_major-devel
This package contains the header files and libraries needed to write or
compile programs that use GNU Data Access user interface library.

%package -n libgdaui%abi_ver_major-gir
Summary: GObject introspection data for the GDAUI library
Group: System/Libraries
Requires: libgdaui%abi_ver_major = %EVR

%description -n libgdaui%abi_ver_major-gir
GObject introspection data for the GNU Data Access user interface
library.

%package -n libgdaui%abi_ver_major-gir-devel
Summary: GObject introspection devel data for the GDAUI library
Group: System/Libraries
BuildArch: noarch
Requires: libgdaui%abi_ver_major-devel = %EVR
Requires: libgdaui%abi_ver_major-gir = %EVR

%description -n libgdaui%abi_ver_major-gir-devel
GObject introspection devel data for the GNU Data Access user interface
library.

%package devel-static
Summary: Static libraries for libgda
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
This package contains the static version of %name libraries.

%package -n gda-browser
Summary: GDA Browser
Group: Databases
Requires: %name = %EVR

%description -n gda-browser
GDA Browser is a tool for database administrators: they can analyse
database's schemas to understand how data is organized, run SQL commands
interactively, and in a broader way manage the data contained in the
databases.

%package demo
Summary: GDA Demo
Group: Databases
Requires: %name = %EVR

%description demo
This package provides GDA Demo Applications.

%package report-engine
Summary: GDA Report Engine
Group: Databases
Requires: %name = %EVR
BuildArch: noarch
%add_python3_path %_datadir/%_name-%abi_ver

%description report-engine
This package provides GDA Python-based report engine.


%prep
%setup -n %_name-%version
%patch

%build
export VALA_VERSION=%vala_ver
%meson \
    %{?_with_ldap:-Dldap=true} \
    %{?_with_web:-Dweb=true} \
    %{?_enable_experimental:-Dexperimental=true} \
    %{?_disable_ui:-Dui=false} \
    %{?_enable_tools:-Dtools=true}
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name-%abi_ver gda-browser

%files -f %_name-%abi_ver.lang
%_libdir/libgda-%abi_ver.so.*
%_libdir/libgda-report-%abi_ver.so.*
%_libdir/libgda-xslt-%abi_ver.so.*
%dir %_libdir/%_name-%abi_ver
%dir %_libdir/%_name-%abi_ver/providers
%{?_with_sqlcipher:%_libdir/%_name-%abi_ver/providers/libgda-sqlcipher-%abi_ver.so}
%{?_with_web:%_libdir/%_name-%abi_ver/providers/libgda-web-%abi_ver.so}
%dir %_datadir/%_name-%abi_ver/
%_datadir/%_name-%abi_ver/dtd/
%{?_enable_crypto:%_datadir/%_name-%abi_ver/sqlcipher_*}
%doc AUTHORS ChangeLog README NEWS


%files providers

%if_with mysql
%files mysql
%_libdir/%_name-%abi_ver/*/*-mysql-%abi_ver.so
%endif

%if_with postgres
%files postgresql
%_libdir/%_name-%abi_ver/*/*-postgres-%abi_ver.so
%endif

%if_with mdb
%files mdb
%_libdir/%_name-%abi_ver/*/*-mdb-%abi_ver.so
%endif

%if_with bdb
%files bdb
%_libdir/%_name-%abi_ver/*/*-bdb-%abi_ver.so
%endif

%if_with odbc
%files odbc
%_libdir/%_name-%abi_ver/*/*-odbc-%abi_ver.so
%endif

%if_with interbase
%files interbase
%_libdir/%_name-%abi_ver/*/*-firebird-%abi_ver.so
%endif

%if_with ldap
%files ldap
%_libdir/%_name-%abi_ver/*/*-ldap-%abi_ver.so
%endif

%if_with tds
%files tds
%_libdir/%_name-%abi_ver/*/*-freetds-%abi_ver.so
%endif

%if_with sqlite
%files sqlite
%_libdir/%_name-%abi_ver/*/*-sqlite-%abi_ver.so
%endif

%if_with jdbc
%files jdbc
%_libdir/%_name-%abi_ver/*/gdaprovider-%abi_ver.0.jar
%_libdir/%_name-%abi_ver/*/libgda-jdbc.so
%endif

%files devel
%dir %_includedir/libgda-%abi_ver
%_includedir/libgda-%abi_ver/libgda
%_includedir/%_name-%abi_ver/libgda-report/
%dir %_includedir/%_name-%abi_ver/providers/
%_includedir/%_name-%abi_ver/providers/sqlcipher/
%_libdir/libgda-report-%abi_ver.so
%_libdir/libgda-xslt-%abi_ver.so
%_pkgconfigdir/libgda-report-%abi_ver.pc
%_pkgconfigdir/libgda-xslt-%abi_ver.pc
%_libdir/libgda-%abi_ver.so
%_pkgconfigdir/libgda-%abi_ver.pc
%_pkgconfigdir/libgda-capi-6.0.pc
%_pkgconfigdir/libgda-models-6.0.pc
# .pc files for providers
%{?_with_sqlcipher:%_pkgconfigdir/libgda-sqlcipher-%abi_ver.pc}
%{?_with_web:%_pkgconfigdir/libgda-web-%abi_ver.pc}
%{?_with_mdb:%_pkgconfigdir/*mdb*}
%{?_with_mysql:%_pkgconfigdir/*mysql*}
%{?_with_postgres:%_pkgconfigdir/*postgres*}
%{?_with_bdb:%_pkgconfigdir/*bdb*}
%{?_with_sqlite:%_pkgconfigdir/*sqlite*}
%{?_with_jdbc:%_pkgconfigdir/libgda-jdbc-%abi_ver.pc}
%{?_with_ldap:%_pkgconfigdir/libgda-ldap-%abi_ver.pc}
%{?_enable_vala:
%_vapidir/*.vapi
%_vapidir/*.deps}

%if_enabled doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled ui
%files -n libgdaui%abi_ver_major
%_libdir/libgda-ui-%abi_ver.so.*
%_libdir/%_name-%abi_ver/plugins/libgda-ui*.so
%_datadir/%_name-%abi_ver/ui/

%files -n libgdaui%abi_ver_major-devel
%_includedir/libgda-%abi_ver/libgda-ui
%_libdir/libgda-ui-%abi_ver.so
%{?_enable_glade:%_datadir/glade/catalogs/gdaui-catalog.xml
%_datadir/glade/pixmaps/widget-gdaui-*.png}
%_pkgconfigdir/libgda-ui-%abi_ver.pc
%endif

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/Gda-%abi_ver.typelib

%files gir-devel
%_datadir/gir-1.0/Gda-%abi_ver.gir

%if_enabled ui
%files -n libgdaui%abi_ver_major-gir
%_typelibdir/Gdaui-%abi_ver.typelib

%files -n libgdaui%abi_ver_major-gir-devel
%_girdir/Gdaui-%abi_ver.gir
%endif
%endif

%if_enabled static
%files devel-static
%_libdir/*.a
%_libdir/%_name-%abi_ver/*/*.a
%endif

%if_enabled tools
%files -n gda-browser -f gda-browser.lang
%_bindir/gda-list-config-%abi_ver
%_bindir/gda-list-server-op-%abi_ver
%_bindir/gda-sql-%abi_ver
%_bindir/gda-control-center-%abi_ver
%_bindir/org.gnome.gda.Browser
%_desktopdir/org.gnome.gda.Browser.desktop
%_iconsdir/hicolor/*/*/org.gnome.gda.Browser.*
%_datadir/pixmaps/org.gnome.gda.Browser.png
%_datadir/%_name-%abi_ver/information_schema.xml
%_datadir/%_name-%abi_ver/gda-sql/
%_man1dir/gda-sql.1*
%_datadir/metainfo/org.gnome.gda.Browser.appdata.xml
%endif

%files demo
%_bindir/org.gnome.gda.Demoui
%_datadir/%_name-%abi_ver/demo/

%files report-engine
%_bindir/trml2html.py
%_bindir/trml2pdf.py
%_datadir/%_name-%abi_ver/gda_trml2html/
%_datadir/%_name-%abi_ver/gda_trml2pdf/

%changelog
* Tue Mar 01 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.0-alt1
- updated to LIBGDA_6_0_0-72-g9a89053d5

* Mon Nov 09 2020 Yuri N. Sedunov <aris@altlinux.org> 5.2.10-alt1
- 5.2.10 release

* Sun Mar 22 2020 Yuri N. Sedunov <aris@altlinux.org> 5.2.10-alt0.1
- updated to LIBGDA_5_2_9-17-g08342b7f8
- built glade catalog for gdaui
- fixed License tag

* Wed May 08 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.9-alt1
- 5.2.9

* Fri Apr 05 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.8-alt2
- updated buildreqs for pgsql

* Wed Dec 26 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.8-alt1
- updated to LIBGDA_5_2_8-7-ga5355eb42

* Fri Sep 14 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.4-alt8
- rebuilt with vala-0.42

* Mon Mar 19 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.4-alt7
- updated to LIBGDA_5_2_4-44-gb9f0a9e
- built with vala-0.40

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
