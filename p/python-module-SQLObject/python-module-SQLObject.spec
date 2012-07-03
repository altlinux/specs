%define oname SQLObject

Name: python-module-SQLObject
Version: 0.13.0
Release: alt1.1.1

Summary: Object-Relational Manager, aka database wrapper for Python

License: LGPL
Group: Development/Python
Url: http://sqlobject.org
Packager: Sergey Bolshakov <sbolshakov@altlinux.ru>

Source: http://pypi.python.org/packages/source/S/%oname/%oname-%version.tar

BuildArch: noarch
BuildRequires: python-devel python-modules-compiler python-modules-encodings
BuildPreReq: python-module-distribute

%setup_python_module sqlobject

%add_python_req_skip py

%description
SQLObject is a popular *Object Relational Manager* for providing an
object interface to your database, with tables as classes, rows as
instances, and columns as attributes.

SQLObject includes a Python-object-based query language that makes SQL
more abstract, and provides substantial database independence for
applications.

Supports MySQL, PostgreSQL, SQLite, Firebird, Sybase, and MaxDB (SAPDB).


%package doc
Summary: This package contains documentation for SQLObject.
Group: Development/Python

%description doc
SQLObject is a popular *Object Relational Manager* for providing an
object interface to your database, with tables as classes, rows as
instances, and columns as attributes.

SQLObject includes a Python-object-based query language that makes SQL
more abstract, and provides substantial database independence for
applications.

Supports MySQL, PostgreSQL, SQLite, Firebird, Sybase, and MaxDB (SAPDB).


%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

# omit paste for a while
#__subst '/sqlobject\/manager/d' -e '/sqlobject\/wsgi_middleware.py/d' INSTALLED_FILES

%files
%doc README.txt
%_bindir/sqlobject-admin
%python_sitelibdir/%modulename/
%python_sitelibdir/%oname-*.egg-info

%files doc
%doc docs/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13.0-alt1.1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.1
- Fixed build

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- build new version 0.13.0
- cleanup spec and build rules

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1
- Rebuilt with python 2.6

* Mon Sep  1 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.2-alt0.M41.1
- 0.10.2

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.7rc1-alt1.0.1
- Rebuilt with python-2.5.

* Sun Mar 25 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.7rc1-alt1.0
- Rebuilt with rpm-build-python-0.30-alt3.

* Sun Nov 06 2005 Maxim Bodyansky <maximbo@altlinux.ru> 0.7rc1-alt1
- Initial build for Sisyphus
