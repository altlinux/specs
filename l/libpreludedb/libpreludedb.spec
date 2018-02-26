Name: libpreludedb
Version: 1.0.0
Release: alt1.3.1.1
Summary: Provide the framework for easy access to the Prelude database
Group: System/Libraries
License: GPLv2
Url: http://prelude-ids.org/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

%define username _prelude
%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}
%def_enable gtk_doc
%define _gtk_docdir %_datadir/gtk-doc/html
%{?_enable_gtk_doc:BuildPreReq: gtk-doc}

# Automatically added by buildreq on Mon Oct 17 2011
BuildRequires: gcc-c++ libgcrypt-devel libgnutls-devel libmysqlclient-devel libprelude-devel libsqlite3-devel perl-devel postgresql-devel python-devel swig glib2-devel

%description
The PreludeDB Library provides an abstraction layer upon the type and the
format of the database used to store IDMEF alerts. It allows developers
to use the Prelude IDMEF database easily and efficiently without
worrying about SQL, and to access the database independently of the
type/format of the database.

%description -l ru_RU.UTF-8
PreludeDB библиотека предоставляет несколько уровеней абстракции и форматов
баз данных для хранения IDMEF алертов. Она позволяет разработчикам
использовать базу данных Prelude IDMEF легко и эффективно не беспокоясь
о SQL, и получать доступ к базе данных независимо от ее формата.

%package devel
Summary: Libraries and headers for PreludeDB
Group: Development/C
Requires: %name = %version-%release, libprelude-devel

%description devel
The PreludeDB Library provides an abstraction layer upon the type
and the format of the database used to store IDMEF alerts. It
allows developers to use the Prelude IDMEF database easily and
efficiently wi thout worrying about SQL, and to access the
database independently of the type/format of the database.

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
Conflicts: %name-devel < %version-%release
BuildArch: noarch

%description devel-doc
The PreludeDB Library provides an abstraction layer upon the type
and the format of the database used to store IDMEF alerts. It
allows developers to use the Prelude IDMEF database easily and
efficiently wi thout worrying about SQL, and to access the
database independently of the type/format of the database.

This package contains development documentation for the library.

%package mysql
Summary: Plugin to use prelude with a mysql database
Group: System/Libraries
Requires: %name = %version-%release, mysql, mysql-server
Provides: libprelude-db

%description mysql
This plugin authorise prelude to store alerts into a mysql database.

%package pgsql
Summary: Plugin to use prelude with a pgsql database
Group: System/Libraries
Requires: %name = %version-%release, postgresql-server
Provides: libprelude-db

%description pgsql
This plugin authorise prelude to store alerts into a pgsql database.

%package sqlite
Summary: Plugin to use prelude with a sqlite database
Group: System/Libraries
Requires: %name = %version-%release, sqlite3
Provides: libprelude-db

%description sqlite
This plugin authorise prelude to store alerts into a sqlite database.

%package -n python-module-%name
Summary: Python bindings for libpreludedb
Group: Development/Python
Requires: %name = %version-%release
Obsoletes: python-modules-%name <= 0.9.15.1-alt2

%description -n python-module-%name
Python bindings for libpreludedb.

%package -n perl-%name
Summary: Perl bindings for libpreludedb
Group: Development/Perl
Requires: %name = %version-%release

%description -n perl-%name
Perl bindings for libpreludedb.


%prep
%setup -q
%patch -p1
%__subst "s|\$dir\/lib\/|%_libdir/|g" configure.in

%build
%autoreconf
%configure %{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--with-perl-installdirs=vendor 

#	--with-html-dir=%_defaultdocdir/%name-%version/html \

%make

%install
%make DESTDIR=%buildroot install

%__mkdir_p %buildroot%_var/lib/preludedb

rm -f %buildroot%_libdir/%name/plugins/sql/mysql.la
rm -f %buildroot%_libdir/%name/plugins/sql/pgsql.la
rm -f %buildroot%_libdir/%name/plugins/sql/sqlite3.la
rm -fr %buildroot%_defaultdocdir/%name-%version/html

%pre sqlite
/usr/sbin/groupadd -r -f %username &> /dev/null ||:
/usr/sbin/useradd -r -g %username -d %_datadir/%name -c 'Prelude Hybrid Intrusion Detection System Manager' -s /dev/null -n %username &> /dev/null ||:

%post sqlite
echo "For database setup execute: 'sqlite3 %_var/lib/preludedb/idmef-db.sqlite < /usr/share/libpreludedb/classic/sqlite.sql'"
touch %_var/lib/preludedb/idmef-db.sqlite
chown -R root:%username %_var/lib/preludedb/* &> /dev/null ||:
chmod 660 %_var/lib/preludedb/idmef-db.sqlite &> /dev/null ||:

%files
%doc README LICENSE.README AUTHORS COPYING NEWS HACKING.README
%_bindir/preludedb-admin
%_libdir/%{name}*.so.*
%_libdir/%name/plugins/formats/*
%dir %_libdir/%name/
%dir %_libdir/%name/plugins/
%dir %_libdir/%name/plugins/formats/
%dir %_libdir/%name/plugins/sql/
%dir %_datadir/%name
%dir %_datadir/%name/classic/
%_man1dir/preludedb-admin.*

%files devel
%_bindir/%name-config
%_libdir/%{name}*.so
%dir %_includedir/%name/
%_includedir/%name/*
%_datadir/aclocal/libpreludedb.m4

%files devel-doc
%_gtk_docdir/*

%files -n python-module-%name
%python_sitelibdir/*

%files -n perl-%name
%perl_vendor_archlib/Prelude*
%perl_vendor_autolib/Prelude*

%files mysql
%_libdir/%name/plugins/sql/mysql.so
%_datadir/%name/classic/mysql*.sql
%_datadir/%name/classic/*.sh

%files sqlite
%_libdir/%name/plugins/sql/sqlite3.so
%_datadir/%name/classic/sqlite*
%dir %attr(0770,root,%username) %_var/lib/preludedb

%files pgsql
%_libdir/%name/plugins/sql/pgsql.so
%_datadir/%name/classic/pgsql*

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.3.1
- Rebuild with Python-2.7

* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt1.3
- Rebuilt for perl-5.14

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.2
- Rebuilt for debuginfo

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt1.1
- rebuilt with perl 5.12

* Tue Jul 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- New version

* Wed Jan 13 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.15.3-alt1
- New version

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.15.1-alt3.1
- Rebuilt with python 2.6

* Mon Mar 09 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.15.1-alt3
- Rename python-modules-%name to python-module-%name
- Add Obsoletes: python-modules-%name <= 0.9.15.1-alt2

* Sun Jan 11 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.15.1-alt2
- Change requires from sqlite to sqlite3 in sqlite subpackage
- Add instruction for setup sqlite database in post
- Add groupadd  and useradd in pre for sqlite subpackage

* Sat Oct 18 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.15.1-alt1
- New version
- Add description on ru_RU.UTF-8
- Add subpackage %name-devel-doc

* Sat Jun 28 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.14.1-alt1
- Build for ALT
