%define version 2.5.1
%define release alt2
%setup_python_module pyPgSQL

Summary: pyPgSQL - A Python DB-API 2.0 compliant interface to PostgreSQL.
Name: %packagename
Version: %version
Release: %release.1.2.1
Source0: %modulename.tar
License: Python
Group: Development/Python
URL: http://pypgsql.sourceforge.net/
Packager: Python Development Team <python@packages.altlinux.org>

BuildPreReq: python-devel

# Automatically added by buildreq on Thu Mar 22 2007
BuildRequires: postgresql-devel 

%description
pyPgSQL is a package of two (2) modules that provide a Python DB-API 2.0
compliant interface to PostgreSQL databases.  The first module, libpq,
exports the PostgreSQL C API to Python.  This module is written in C and
can be compiled into Python or can be dynamically loaded on demand.  The
second module, PgSQL, provides the DB-API 2.0 compliant interface and
support for various PostgreSQL data types, such as INT8, NUMERIC, MONEY,
BOOL, ARRAYS, etc.  This module is written in Python.  This version works
with PostgreSQL 7.0 or later and Python 2.1 or later.

%prep
%setup -n %modulename

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_build_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc examples README README.html

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.1-alt2.1.2.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2.1.2
- Rebuilt for debuginfo

* Wed Dec 16 2009 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt2.1.1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-pyPgSQL
  * postclean-05-filetriggers for spec file

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2.1.1
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 2.5.1-alt2.1
- Rebuilt with python-2.5.

* Tue Jan 22 2008 Grigory Batalov <bga@altlinux.ru> 2.5.1-alt2
- Remove python version from BuildPreReq.

* Wed Mar 21 2007 Ivan Fedorov <ns@altlinux.ru> 2.5.1-alt1
- Initial build for Sisyphus
