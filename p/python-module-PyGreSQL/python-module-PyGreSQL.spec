%define version 4.1.1
%define release alt1.svn20140730
%setup_python_module PyGreSQL

Summary: Python PostgreSQL Interfaces
Name: %packagename
Version: %version
Release: %release
# svn://svn.PyGreSQL.org/pygresql/trunk
Source0: %modulename-%version.tgz
License: Python
Group: Development/Python
URL: http://www.pygresql.org/

BuildPreReq: postgresql-devel libpq-devel libssl-devel
BuildPreReq: python-module-sphinx-devel python-module-cloud_sptheme

%description
PyGreSQL is a python module that interfaces to a PostgreSQL database. It
embeds the PostgreSQL query library to allow easy use of the powerful
PostgreSQL features from a Python script.

%package pickles
Summary: Pickles for %modulename
Group: Development/Python

%description pickles
PyGreSQL is a python module that interfaces to a PostgreSQL database. It
embeds the PostgreSQL query library to allow easy use of the powerful
PostgreSQL features from a Python script.

This package contains pickles for %modulename.

%prep
%setup -n %modulename-%version

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
pushd module
%python_build_debug
popd

%install
pushd module
%python_install --record=INSTALLED_FILES
popd

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%modulename
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%modulename/

%files -f module/INSTALLED_FILES
%doc docs/*.txt docs/_build/html tutorial

%files pickles
%python_sitelibdir/*/pickle

%changelog
* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.svn20140730
- Version 4.1.1

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
