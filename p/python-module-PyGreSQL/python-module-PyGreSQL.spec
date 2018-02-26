%define version 4.0
%define release alt3
%setup_python_module PyGreSQL

Summary: Python PostgreSQL Interfaces
Name: %packagename
Version: %version
Release: %release.1
Source0: %modulename-%version.tgz
License: Python
Group: Development/Python
URL: http://www.pygresql.org/
Packager: Python Development Team <python@packages.altlinux.org>

BuildPreReq: postgresql-devel libpq-devel libssl-devel

%description
PyGreSQL is a python module that interfaces to a PostgreSQL database. It
embeds the PostgreSQL query library to allow easy use of the powerful
PostgreSQL features from a Python script.

%prep
%setup -n %modulename-%version

%build
%python_build_debug

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc docs/* tutorial

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0-alt3.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt3
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt2
- Rebuilt with PostgreSQL 9

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1
- Version 4.0

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt3
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 3.6.2-alt2.0.1
- Rebuilt with python-2.5.

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 3.6.2-alt2.0
- Rebuilt due to libpq.so.4 -> libpq.so.5 soname change.

* Mon Jan 02 2006 Ivan Fedorov <ns@altlinux.ru> 3.6.2-alt2
- fix buildreq's

* Mon May 23 2005 Ivan Fedorov <ns@altlinux.ru> 3.6.2-alt1
- Initial build for ALT Linux.
