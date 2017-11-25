# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# API version for libpreludedb
%global major                   7
# API version for libpreludedb c++ binding
%global cppmajor                2

Name:           libpreludedb
Version:        4.0.0
Release:        alt1_1
Summary:        Framework for easy access to the IDMEF database
# Prelude is GPL-2.0+
# libmissing is LGPL-2.1+
License:        GPLv2+
URL:            https://www.prelude-siem.org/
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
# https://www.prelude-siem.org/issues/866
Patch0:         libpreludedb-4.0.0-manpages.patch
# https://www.prelude-siem.org/issues/867
Patch1:         libpreludedb-4.0.0-undefined_non_weak_symbol.patch
# https://www.prelude-siem.org/issues/908
Patch2:         libpreludedb-4.0.0-fix-gtk-doc.patch
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  gtk-doc gtk-doc-mkpdf
BuildRequires:  glib2-devel libgio libgio-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  libgpg-error-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libecpg-devel libpq-devel postgresql-devel
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libprelude) >= %{version}
BuildRequires:  pkgconfig(openssl)
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  python-devel
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(zlib)

%ifnarch s390
BuildRequires:  valgrind
%endif

#Requires: preludedb-mysql
#Requires: preludedb-pgsql
#Requires: preludedb-sqlite3

# Upstream do not use explicit version of gnulib, just checkout
# and update files. In libprelude 4.0.0, the checkout has been done
# on 2017-01-05
Provides:       bundled(gnulib) = 20170105
Source44: import.info

%description
The PreludeDB Library provides an abstraction layer upon the type and the
format of the database used to store IDMEF alerts. It allows developers to use
the Prelude IDMEF database easily and efficiently without worrying about SQL,
and to access the database independently of the type/format of the database.

%description -l ru_RU.UTF-8
PreludeDB библиотека предоставляет несколько уровеней абстракции и форматов
баз данных для хранения IDMEF алертов. Она позволяет разработчикам
использовать базу данных Prelude IDMEF легко и эффективно не беспокоясь
о SQL, и получать доступ к базе данных независимо от ее формата.

%package devel
Group: Development/C
Summary:        Libraries and headers for PreludeDB
Requires:       %{name} = %{version}-%{release}

%description devel
Libraries and headers you can use to access Prelude database using the Prelude
Library. The PreludeDB Library provides an abstraction layer upon the type and
the format of the database used to store IDMEF alerts. It allows developers to
use the Prelude IDMEF database easily and efficiently without worrying about
SQL, and to access the database independently of the type/format of the
database.

%package -n preludedb-tools
Group: System/Libraries
Summary:        Command-line tools for %{name}
Requires:       %{name} = %{version}-%{release}

%description -n preludedb-tools
Provides a convenient interface for accessing Prelude alerts.

%package -n python-module-preludedb
Group: System/Libraries
Summary:        Python 2 bindings for preludedb
Requires:       %{name} = %{version}-%{release}
%{?python_provide:%python_provide python2-preludedb}

%description -n python-module-preludedb
Provides python 2 bindings for preludedb.

%package -n python3-module-preludedb
Group: System/Libraries
Summary:        Python 3 bindings for preludedb
Requires:       %{name} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-preludedb}

%description -n python3-module-preludedb
Provides python 3 bindings for preludedb.

%package -n preludedb-mysql
Group: System/Libraries
Summary:        Plugin to use prelude with a MySQL database
Requires:       %{name} = %{version}-%{release}

%description -n preludedb-mysql
This plugin authorize prelude to store alerts into a MySQL
database.

%package -n preludedb-pgsql
Group: System/Libraries
Summary:        Plugin to use prelude with a PostgreSQL database
Requires:       %{name} = %{version}-%{release}

%description -n preludedb-pgsql
This plugin authorize prelude to store alerts into a PostgreSQL
database.

%package -n preludedb-sqlite3
Group: System/Libraries
Summary:        Plugin to use prelude with a SQLite3 database
Requires:       %{name} = %{version}-%{release}

%description -n preludedb-sqlite3
This plugin authorize prelude to store alerts into a SQLite3
database.

%package doc
Group: System/Libraries
Summary:        Documentation for preludedb
BuildArch:      noarch

%description doc
Provides documentation for preludedb generated by gtk-doc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure \
    --disable-rpath \
    --disable-static \
    --enable-shared \
    --includedir=%{_includedir}/%{name} \
    --with-swig \
    --with-perl-installdirs=vendor \
    --with-python2 \
    --with-python3 \
    --enable-gtk-doc \
    --with-html-dir=%{_docdir}/%{name}-devel
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%makeinstall_std

chrpath -d %{buildroot}%{_libdir}/*.so.*

find %{buildroot} -name '*.la' -delete
find %{buildroot} -name 'perllocal.pod' -delete
find %{buildroot} -name '.packlist' -delete

chmod +x %{buildroot}%{_datadir}/%{name}/classic/mysql2pgsql.sh
chmod +x %{buildroot}%{_datadir}/%{name}/classic/mysql2sqlite.sh

%check
#%make_build check

%files
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*
%{_libdir}/%{name}cpp.so.%{cppmajor}
%{_libdir}/%{name}cpp.so.%{cppmajor}.*
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/formats
%dir %{_libdir}/%{name}/plugins/sql
%{_libdir}/%{name}/plugins/formats/classic.so
%doc COPYING LICENSE.README HACKING.README
%doc README NEWS

%files devel
%{_datadir}/%{name}
%{_bindir}/%{name}-config
%{_libdir}/%{name}.so
%{_libdir}/%{name}cpp.so
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man1/%{name}-config.1*

%files -n preludedb-tools
%{_bindir}/preludedb-admin
%{_mandir}/man1/preludedb-admin.1*

%files -n python-module-preludedb
%{python_sitelibdir}/_preludedb.*so
%{python_sitelibdir}/preludedb-%{version}-py?.?.egg-info
%{python_sitelibdir}/preludedb.py
%{python_sitelibdir}/preludedb.pyc
%{python_sitelibdir}/preludedb.pyo

%files -n python3-module-preludedb
%{python3_sitelibdir}/_preludedb.*so
%{python3_sitelibdir}/__pycache__/preludedb.cpython-??.*pyc
%{python3_sitelibdir}/preludedb-%{version}-py?.?.egg-info
%{python3_sitelibdir}/preludedb.py

%files -n preludedb-mysql
%{_libdir}/%{name}/plugins/sql/mysql.so
%dir %{_datadir}/%{name}/classic
%{_datadir}/%{name}/classic/mysql*.sql

%files -n preludedb-pgsql
%{_libdir}/%{name}/plugins/sql/pgsql.so
%dir %{_datadir}/%{name}/classic
%{_datadir}/%{name}/classic/pgsql*.sql

%files -n preludedb-sqlite3
%{_libdir}/%{name}/plugins/sql/sqlite3.so
%dir %{_datadir}/%{name}/classic
%{_datadir}/%{name}/classic/sqlite*.sql

%files doc
%{_docdir}/%{name}-devel
%doc COPYING LICENSE.README HACKING.README
%doc ChangeLog README NEWS

%changelog
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_1
- new version

* Thu Feb 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_1
- new version

* Thu Sep 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.rc2.git20140916
- Version 1.2.6rc2

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.rc1.git20140916
- Version 1.2.6rc1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt3
- built for perl 5.18

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.0-alt2.qa1
- NMU: rebuilt with libmysqlclient.so.18.

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt2
- rebuilt for perl-5.16

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.4
- Fixed build with new glibc

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
