%define oname pysqlite2
%define version 2.6.0
%define release alt3
%setup_python_module %oname

Summary: Python interface to SQLite 3.0
Name: python-module-%oname
Version: %version
Release: %release.1
URL: http://pypi.python.org/pypi/pysqlite/
Source0: pysqlite.tar
License: zlib/libpng license
Group: Development/Python
BuildRequires: libsqlite3-devel
Packager: Python Development Team <python@packages.altlinux.org>

BuildPreReq: python-module-sphinx-devel texlive-latex-recommended

%description
Pysqlite is an interface to the SQLite 3.0  database server for Python.
It aims to be fully compliant with Python database API version 2.0
while also exploiting the unique features of SQLite 3.0.

%package docs
Summary: Documentation for pysqlite2
Group: Development/Documentation
BuildArch: noarch

%description docs
Pysqlite is an interface to the SQLite 3.0  database server for Python.
It aims to be fully compliant with Python database API version 2.0
while also exploiting the unique features of SQLite 3.0.

This package contains documentation for pysqlite2.

%package pickles
Summary: Pickles for pysqlite2
Group: Development/Python

%description pickles
Pysqlite is an interface to the SQLite 3.0  database server for Python.
It aims to be fully compliant with Python database API version 2.0
while also exploiting the unique features of SQLite 3.0.

This package contains pickles for pysqlite2.

%package tests
Summary: Tests for pysqlite2
Group: Development/Python
Requires: %name = %version-%release

%description tests
Pysqlite is an interface to the SQLite 3.0  database server for Python.
It aims to be fully compliant with Python database API version 2.0
while also exploiting the unique features of SQLite 3.0.

This package contains tests for pysqlite2.

%prep
%setup -n pysqlite

%prepare_sphinx doc/sphinx

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%make -C doc/sphinx html

%install
%python_install --optimize=2

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/sphinx/.build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc LICENSE PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test
%exclude %python_sitelibdir/%oname/pickle

%files docs
%doc doc/sphinx/.build/html

%files pickles
%python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/%oname/test
%exclude %python_sitelibdir/%oname/test/py25

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6.0-alt3.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt3
- Rebuilt with python-module-sphinx-devel

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt2
- Rebuilt for debuginfo

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1
- Version 2.6.0

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.1
- Rebuilt with python 2.6

* Tue Mar 18 2008 Grigory Batalov <bga@altlinux.ru> 2.4.1-alt1
- 2.4.1 (fix #14959)

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.4.0-alt2
- Use package name without python version

* Tue Jan 01 2008 Ivan Fedorov <ns@altlinux.org> 2.4.0-alt1
- 2.4.0

* Sun Jul 08 2007 Ivan Fedorov <ns@altlinux.org> 2.3.4-alt1
- 2.3.4

* Sun Apr 22 2007 Ivan Fedorov <ns@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Sat Jul 01 2006 Ivan Fedorov <ns@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sat Apr 15 2006 Ivan Fedorov <ns@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sun Feb 12 2006 Ivan Fedorov <ns@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Sun Jan 22 2006 Ivan Fedorov <ns@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Thu Nov 10 2005 Ivan Fedorov <ns@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Mon Oct 03 2005 Ivan Fedorov <ns@altlinux.ru> 2.0.4-alt1
- switch to 2.0 branch
- module renamed to pysqlite2

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.4-alt1.1
- Rebuilt with python-2.4.

* Thu Nov 25 2004 Konstantin Klimchev <koka@altlinux.ru> 1.1.4-alt1
- Initial build for Sisyphus
