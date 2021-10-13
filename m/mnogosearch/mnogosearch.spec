# Spec file for mnoGoSearch package

%def_without	static

# Database backends
%def_with	mysql
%def_with	pgsql
%def_without	sqlite
%def_with	sqlite3
%def_with	unixODBC
%def_with	cache

# Unsupported by SPEC file
%def_without	db2
%def_without	ibase
%def_without	oracle8
%def_without	oracle8i
%def_without	freetds
%def_without	ctlib
%def_without	solid
%def_without	sapdb
%def_without	monetdb

## Database definition only - support via ODBC (?)
%if_with unixODBC
	%def_without	mimer
	%def_with	mssql
	%def_with	oracle
	%def_without	sybase
	%def_without	virtuoso
%else
	%def_without	mimer
	%def_without	mssql
	%def_without	oracle
	%def_without	sybase
	%def_without	virtuoso
%endif


Name: mnogosearch
Version: 3.4.1
Release: alt2

Summary: a full-featured search engine for intranet and internet servers
Summary(ru_RU.UTF-8): поисковая машина для серверов интернет и интранет

Group: Text tools
License: %gpl2plus
URL: http://www.mnogosearch.ru/
Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %name-%version.tar
Source1: mnogosearch-dbgen
Source2: mnogosearch.png
Source3: udm-config.1
Patch0: indexer.conf.5.patch
Patch1: %name-3.3.7-alt-docbook.patch
Patch5: %name-3.3.7-debian-url_escape.patch
#Patch8: %name-3.3.14-alt-format_fix.patch
#Patch9: %name-3.3.14-alt-uninitialized_fix.patch
#Patch11: %name-3.3.14-alt-check_io_results.patch
#Patch12: %name-3.3.14-alt-fix_misc_errors.patch

Requires: %name-backend = %version

BuildRequires(pre): rpm-build-licenses rpm-macros-apache2

# Note: openjade used to re-generate docs. It needs to fix pathes to
#       the DTDs in doc/catalog and doc/Makefile.in
# Using pre-build html documentation instead rebuild it from XML files.
# BuildRequires: openjade docbook-style-dsssl-utils
BuildRequires: glibc-devel-static
BuildRequires: libssl-devel libreadline-devel libtinfo-devel zlib-devel

%if_with mysql
BuildRequires: libmysqlclient-devel
%endif
%if_with sqlite
BuildRequires: libsqlite-devel
%endif
%if_with sqlite3
BuildRequires: libsqlite3-devel
%endif
%if_with unixODBC
BuildRequires: libunixODBC-devel
%endif
%if_with pgsql
BuildRequires: postgresql-devel
%endif

%description
mnoGoSearch is a full-featured SQL based web search engine. 
mnoGoSearch consists of two parts - the indexing mechanism
(indexer) and the web CGI front-end. The indexer walks over
html hypertext references and stores found words and new
references into a database. The CGI front-end provides search
using data collected by the indexer.


%define common_summary mnoGoSearch web search engine
%define common_desc  mnoGoSearch is a full-featured SQL based web search engine.\
\
This package contains

%package doc
Summary: %common_summary HTML and PDF documentation
BuildArch: noarch
Group: Text tools
Requires: %name = %version-%release

%description doc
%common_desc mnoGoSearch HTML documentation.

%package multidb
Summary: %common_summary multi-database backend
Group: Development/C
Requires: %name = %version-%release
Provides: %name-backend = %version

%description multidb
%common_desc multi-database backend.
Install this package for full set of the supported mnoGoSearch
database backends.  Probably You should't install this but one
of the database-specfic subpackage.

%if_with mysql
%package mysql
Summary: %common_summary MySQL database backend
Group: Development/C
Requires: %name = %version-%release
Provides: %name-backend = %version

%description mysql
%common_desc MySQL database backend.

Install this package when using MySQL database backend.
%endif

%if_with pgsql
%package pgsql
Summary: %common_summary PostgreSQL database backend
Group: Development/C
Requires: %name = %version-%release
Provides: %name-backend = %version

%description pgsql
%common_desc PostgreSQL database backend.

Install this package when using PostgreSQL database backend.
%endif

%if_with sqlite
%package sqlite
Summary: %common_summary SQLite database backend
Group: Development/C
Requires: %name = %version-%release
Provides: %name-backend = %version

%description sqlite
%common_desc SQLite database backend.

Install this package when using SQLite database.
%endif

%if_with sqlite3
%package sqlite3
Summary: %common_summary SQLite3 database backend
Group: Development/C
Requires: %name = %version-%release
Provides: %name-backend = %version

%description sqlite3
%common_desc SQLite3 database backend.

Install this package when using SQLite3 database backend.
%endif

%if_with unixODBC
%package odbc
Summary: %common_summary ODBC database backend
Group: Development/C
Requires: %name = %version-%release
Provides: %name-backend = %version

%description odbc
%common_desc unixODBC database backend.

Install this package when using ODBC database backend.
%endif


%package -n lib%name-devel
Summary: Headers to develop mnogosearch application
Group: Development/C
Requires: %name = %version-%release
Requires: %name-multidb = %version-%release

%description -n lib%name-devel
%common_desc Headers to develop mnogosearch applications.

%if_with static
%package -n lib%name-devel-static
Summary: Static libraries to develop mnogosearch application
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
%common_desc static libraries to develop mnogosearch applications.
%endif

%package cgi
Summary: CGI frontend to mnogosearch
Group: Networking/Other
BuildArch: noarch
Requires: %name = %version, webserver-common

%description cgi
%common_desc CGI frontend to mnogosearch search engine.


%define	config_owner	_%name

%define bin_install	install-libLTLIBRARIES install-binPROGRAMS install-sbinPROGRAMS

%prep
%setup -n %name-%version -q
%patch0 -p0
%patch1 -p0
%patch5 -p0
#%%patch8 -p2
#%%patch9 -p2
#%%patch11 -p2
#%%patch12 -p2

mv -f -- COPYING COPYING.GPL.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
# General notes for build process:
# main goal is to build a set of mnoGoSeach binaries for every database
# backend and an additional set or binaries linked with all enabled database
# backends.
# One can install then a subpackage for a specific database backend, or a
# general subpackage with full set of database's libs.

# LTO support for static libraries
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

# Common configuration flags
CONF_FLAGS="--enable-shared \
	--enable-phrase \
	--enable-linux-pthreads \
	--with-zlib \
	--with-readline \
	--disable-rpath \
	--with-openssl=%_usr \
	--enable-syslog --enable-syslog=LOG_LOCAL6 \
	--enable-parser \
	--enable-mp3 \
	--enable-file \
	--enable-http \
	--enable-ftp \
	--enable-news \
	--with-extra-charsets=all \
	--enable-fhs-layout \
	--sysconfdir=%_sysconfdir/%name \
	--localstatedir=%_localstatedir/%name \
	--datadir=%_datadir/%name \
	--includedir=%_includedir/%name"


# Building mnoGoSearch for single database backend
# and saving binaries for use in the install section
#
# Usage: build_single_db <name> <flags>
build_single_db() {
	aname=$1
	flags=$2

# Generate clean Makefile.in files
	%autoreconf
# Renaming libraries
	sed -e "s/mnogosearch/mnogosearch-$aname/g" -i Makefile.in
	sed -e "s/mnogosearch/mnogosearch-$aname/g" -i src/Makefile.in

# Now run configure, and build mnoGoSearch:
	%configure	$CONF_FLAGS --without-docs $flags
	%make_build

# And save binaries and libraries into .$aname subdir
	DB_LIB=`pwd`/.$aname
	mkdir -p $DB_LIB
	pushd src
	make DESTDIR=$DB_LIB %{bin_install}
	popd

	# Prevent original docs to clean
	echo "clean: " > doc/Makefile
	%make clean

# Returning libmnogocharset:
	mkdir src/.libs
	cp -a $DB_LIB/%_libdir/libmnogocharset* src/.libs/
	cp -a $DB_LIB/%_libdir/libmnogocharset.la src/
}

all_db_flags=''

# One-database backend builds:
%if_with mysql
	build_single_db "mysql" "--with-mysql --program-suffix=-mysql"
	all_db_flags="$all_db_flags --with-mysql"
%endif

%if_with pgsql
	build_single_db "pgsql" "--with-pgsql --program-suffix=-pgsql"
	all_db_flags="$all_db_flags --with-pgsql"
%endif

%if_with sqlite
	build_single_db "sqlite" "--with-sqlite --program-suffix=-sqlite"
	all_db_flags="$all_db_flags --with-sqlite"
%endif

%if_with sqlite3
	build_single_db "sqlite3" "--with-sqlite3 --program-suffix=-sqlite3"
	all_db_flags="$all_db_flags --with-sqlite3"
%endif

%if_with unixODBC
	build_single_db "odbc" "--with-unixODBC --program-suffix=-odbc"
	all_db_flags="$all_db_flags --with-unixODBC"
%endif


# All-database backends build:
%autoreconf
# Renaming libraries
sed -e "s/mnogosearch/mnogosearch-multidb/g" -i Makefile.in
sed -e "s/mnogosearch/mnogosearch-multidb/g" -i src/Makefile.in
%configure	$CONF_FLAGS \
		--with-docs \
		--htmldir=%_datadir/%name/html \
		--pdfdir=%_datadir/%name/pdf \
		$all_db_flags \
		--program-suffix=-multidb \
		%nil
%make_build


%install
# Installing multidb package
%makeinstall	sysconfdir=%buildroot%_sysconfdir/%name \
		localstatedir=%buildroot%_localstatedir/%name \
		datadir=%buildroot%_datadir/%name

rm -f -- %buildroot%_sysconfdir/%name/*-dist
mkdir -p -- %buildroot%_var/www/cgi-bin
pushd %buildroot%_var/www/cgi-bin
ln -s -- ../../../%_bindir/search.cgi search.cgi
popd

for f in indexer.conf langmap.conf search.htm stopwords.conf; do
	install -m 644 -- etc/$f-dist %buildroot%_sysconfdir/%name/$f
done

install -pD -m 755 -- %SOURCE1 %buildroot%_sysconfdir/cron.daily/%name-dbgen

# HTML docs build and install are broken in 3.3.8
mkdir -p %buildroot%_prefix/doc/
cp -- doc/*.html doc/mnogo.css %buildroot%_prefix/doc/
cp -r -- doc/samples  %buildroot%_prefix/doc/
mv -- %buildroot%_prefix/doc %buildroot%_datadir/%name/html
rm -rf -- %buildroot%_datadir/doc/%name

# Moving headers into subdir
mkdir -p  %buildroot%_includedir/%name
mv -- %buildroot%_includedir/udm* %buildroot%_includedir/%name

# Install local log icon
install -pD -m 644 -- %SOURCE2 %buildroot%webserver_iconsdir/%name.png

# Install man page for udm-config
install -pD -m 644 -- %SOURCE3 %buildroot%_man1dir/udm-config.1

# Install binaries and libraries with different database bindings
mkdir -p -- %buildroot%_altdir

# Make alternatives file
#
# Usage: mk_alt_file <name> <weight>
mk_alt_file() {
    aname=$1
    weight=$2

    echo "%_bindir/indexer    %_bindir/indexer-$aname    $weight" > %buildroot%_altdir/%name-$aname
    echo "%_bindir/mguesser   %_bindir/mguesser-$aname   %_bindir/indexer-$aname" >> %buildroot%_altdir/%name-$aname
    echo "%_bindir/mconv      %_bindir/mconv-$aname      %_bindir/indexer-$aname" >> %buildroot%_altdir/%name-$aname
    echo "%_bindir/search.cgi %_bindir/search.cgi-$aname %_bindir/indexer-$aname" >> %buildroot%_altdir/%name-$aname
}

# Installing binaries and libraries for single database backends
#
# Usage: install_single_db <name> <weight>
install_single_db() {
    aname=$1
    weight=$2

    mv -- .$aname%_bindir/indexer* %buildroot%_bindir/
    mv -- .$aname%_bindir/mguesser-$aname %buildroot%_bindir/
    mv -- .$aname%_bindir/mconv-$aname %buildroot%_bindir/
    mv -- .$aname%_bindir/search.cgi-$aname %buildroot%_bindir/
    mv -- .$aname%_libdir/lib%name-$aname* %buildroot%_libdir/

    mk_alt_file $aname $weight
}

mk_alt_file  multidb 50

# Rename datebase-independant files
mv -- %buildroot%_bindir/udm-config-multidb %buildroot%_bindir/udm-config
rename -- -multidb '' %buildroot%_man1dir/*
rename -- -multidb '' %buildroot%_man5dir/*

ln -s -- mguesser-multidb %buildroot%_bindir/mguesser
ln -s -- mconv-multidb %buildroot%_bindir/mconv
ln -s -- search.cgi-multidb %buildroot%_bindir/search.cgi
ln -s -- indexer-multidb %buildroot%_bindir/indexer


%if_with mysql
    install_single_db mysql 40
%endif
%if_with pgsql
    install_single_db pgsql 30
%endif
%if_with sqlite
    install_single_db sqlite 20
%endif
%if_with sqlite3
    install_single_db sqlite3 25
%endif
%if_with unixODBC
    install_single_db odbc 10
%endif

%pre
%_sbindir/groupadd -r -f %config_owner &>/dev/null ||:

%post cgi
[ -d %_var/www/cgi-bin/ -a ! -e %_var/www/cgi-bin/search.cgi ] && /bin/ln -nsf -- %_bindir/search.cgi %_var/www/cgi-bin/search.cgi ||:

%preun cgi
if [ "$1" = "0" ] ; then # last uninstall
    [ -L %_var/www/cgi-bin/search.cgi ] && /bin/rm -f -- %_var/www/cgi-bin/search.cgi ||:
fi

%files
%doc README AUTHORS NEWS TODO ChangeLog INSTALL
%doc --no-dereference COPYING

%if_with mysql
	%_datadir/%name/create/mysql
%else
	%exclude %_datadir/%name/create/mysql
%endif
%if_with pgsql
	%_datadir/%name/create/pgsql
%else
	%exclude %_datadir/%name/create/pgsql
%endif
%if_with sqlite
	%_datadir/%name/create/sqlite
%else
	%exclude %_datadir/%name/create/sqlite
%endif
%if_with sqlite3
	%_datadir/%name/create/sqlite
%else
	%exclude %_datadir/%name/create/sqlite
%endif

%if_with cache
	%_datadir/%name/create/cache
%else
	%exclude %_datadir/%name/create/cache
%endif
%if_with db2
	%_datadir/%name/create/db2
%else
	%exclude %_datadir/%name/create/db2
%endif
%if_with ibase
	%_datadir/%name/create/ibase
%else
	%exclude %_datadir/%name/create/ibase
%endif

%if_with mimer
	%_datadir/%name/create/mimer
%else
	%exclude %_datadir/%name/create/mimer
%endif
%if_with oracle
	%_datadir/%name/create/oracle
%else
	%exclude %_datadir/%name/create/oracle
%endif
%if_with mssql
	%_datadir/%name/create/mssql
%else
	%exclude %_datadir/%name/create/mssql
%endif
%if_with sybase
	%_datadir/%name/create/sybase
%else
	%exclude %_datadir/%name/create/sybase
%endif
%if_with virtuoso
	%_datadir/%name/create/virtuoso
%else
	%exclude %_datadir/%name/create/virtuoso
%endif
%if_with monetdb
	%_datadir/%name/create/monetdb
%else
	%exclude %_datadir/%name/create/monetdb
%endif

%_man1dir/indexer*
%_man5dir/*

%dir %_localstatedir/%name

%exclude %_bindir/mguesser
%ghost %_bindir/mguesser
%exclude %_bindir/search.cgi
%ghost %_bindir/search.cgi
%exclude %_bindir/indexer
%ghost %_bindir/indexer
%exclude %_bindir/mconv
%ghost %_bindir/mconv

%attr(0770,root,%config_owner) %dir %_sysconfdir/%name
%attr(0664,root,%config_owner) %config(noreplace) %_sysconfdir/%name/indexer.conf
%attr(0664,root,%config_owner) %config(noreplace) %_sysconfdir/%name/langmap.conf
%attr(0664,root,%config_owner) %config(noreplace) %_sysconfdir/%name/stopwords.conf

%_datadir/%name/freq
%_datadir/%name/langmap
%_datadir/%name/stopwords
%_datadir/%name/synonym

%_sysconfdir/cron.daily/%name-dbgen

%_libdir/libmnogocharset-3.4.so


%files cgi
%attr(0664,root,%config_owner) %config(noreplace) %_sysconfdir/%name/search.htm
%webserver_iconsdir/%name.png
%ghost   %_var/www/cgi-bin/search.cgi
%exclude %_var/www/cgi-bin/search.cgi


%files multidb
%_libdir/lib%{name}-multidb-3.4.so
%_bindir/*-multidb
%_altdir/%name-multidb

%if_with mysql
%files mysql
%_libdir/lib%{name}-mysql-3.4.so
%_bindir/*-mysql
%_altdir/%name-mysql
%endif

%if_with pgsql
%files pgsql
%_libdir/lib%{name}-pgsql-3.4.so
%_bindir/*-pgsql
%_altdir/%name-pgsql
%endif

%if_with sqlite
%files sqlite
%_libdir/lib%{name}-sqlite-3.4.so
%_bindir/*-sqlite
%_altdir/%name-sqlite
%endif

%if_with sqlite3
%files sqlite3
%_libdir/lib%{name}-sqlite3-3.4.so
%_bindir/*-sqlite3
%_altdir/%name-sqlite3
%endif

%if_with unixODBC
%files odbc
%_libdir/lib%{name}-odbc-3.4.so
%_bindir/*-odbc
%_altdir/%name-odbc
%endif


%files doc
%_datadir/%name/html


%files -n lib%name-devel
%_bindir/udm-config
%_usr/include/%{name}*
%_libdir/libmnogocharset.so
%_libdir/libmnogosearch-multidb.so
%if_with mysql
%_libdir/libmnogosearch-mysql.so
%endif
%if_with pgsql
%_libdir/libmnogosearch-pgsql.so
%endif
%if_with sqlite
%_libdir/libmnogosearch-sqlite.so
%endif
%if_with sqlite3
%_libdir/libmnogosearch-sqlite3.so
%endif
%if_with unixODBC
%_libdir/libmnogosearch-odbc.so
%endif
%_man1dir/udm-config*

%if_with static
%files -n lib%name-devel-static
%_libdir/lib*.a
%else
%exclude %_libdir/lib*.a
%endif

%changelog
* Wed Oct 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.4.1-alt2
- Fix build with LTO flags

* Fri Jul 02 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.4.1-alt1
- New version (Closes: 32446)

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.3.14-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Mon Jun 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 3.3.14-alt2
- Rebuild with unixODBC 2.3.1

* Sun May 19 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.14-alt1
- New version 3.3.14

* Fri Apr 12 2013 Michael Shigorin <mike@altlinux.org> 3.3.12-alt1.1
- rebuilt against libmysqlclient.so.18

* Sun Aug 26 2012 Nikolay A. Fetisov <naf@altlinux.ru> 3.3.12-alt1
- Picked up from orphaned
- New version 3.3.12

* Thu Dec 09 2010 Nikolay A. Fetisov <naf@altlinux.ru> 3.3.10-alt1
- New version

* Mon Aug 24 2009 Nikolay A. Fetisov <naf@altlinux.ru> 3.3.8-alt1
- Picked up from orphaned
- New version 3.3.8

* Fri Jan 23 2004 Kachalov Anton <mouse@altlinux.ru> 3.2.13-alt2
- removed .la files

* Mon Sep 22 2003 Kachalov Anton <mouse@altlinux.ru> 3.2.13-alt1
- new version 3.2.13
- build with new libMySQL

* Fri Oct 18 2002 Kachalov Anton <mouse@altlinux.ru> 3.2.7-alt1
- 3.2.7

* Wed Mar 20 2002 Rider <rider@altlinux.ru> 3.1.19-alt2
- build fix

* Fri Nov 09 2001 Rider <rider@altlinux.ru> 3.1.19-alt1
- 3.1.19
- more libifications

* Fri Jun 15 2001 Rider <rider@altlinux.ru> 3.1.16-alt1
- 3.1.16

* Fri Jun 08 2001 Rider <rider@altlinux.ru> 3.1.15-alt1
- 3.1.15

* Wed Jun 06 2001 Rider <rider@altlinux.ru> 3.1.13-alt1
- 3.1.14

* Wed May 23 2001 Rider <rider@altlinux.ru> 3.1.13-alt1
- 3.1.13

* Tue Apr 03 2001 Rider <rider@altlinux.ru> 3.1.12-alt1
- bugfix (removed news extension)

* Thu Mar 13 2001 Rider <rider@altlinux.ru> 3.1.12-ipl3
- final (stable) 3.1.12 version from MnogoSearch developers

* Sun Mar 04 2001 Alexander Bokovoy <ab@avilink.net> 3.1.12-ipl2
- libification
- multi-threaded indexer
- Dependencies changed to follow current libMySQL state
- Shared library build added
- Group changed for mnogosearch package: 'Text tools' instead of 'Networking/Other'
- Headers are included into libmnogosearch-devel now
- Documentation about DB structure stripped down to MySQL in order
  to avoid misunderstooding

* Sun Mar 04 2001 Rider <rider@lrn.ru>
- first spec for RE
