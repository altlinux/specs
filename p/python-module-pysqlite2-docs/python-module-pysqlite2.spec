%define oname pysqlite2
%define fname python-module-%oname
%define descr \
Pysqlite is an interface to the SQLite 3.0  database server for Python. \
It aims to be fully compliant with Python database API version 2.0 \
while also exploiting the unique features of SQLite 3.0.

Name: %fname-docs
Version: 2.8.3
Release: alt1

%if "-docs"==""
Summary: Python interface to SQLite 3.0
Group: Development/Python
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License: zlib/libpng license
Url: http://pypi.python.org/pypi/pysqlite/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-sphinx
BuildPreReq: python-module-sphinx-devel texlive-latex-recommended
BuildRequires: libsqlite3-devel

%if "-docs"!=""
Conflicts: %fname < %EVR
Conflicts: %fname > %EVR
%endif

%description
%descr
%if "-docs"!=""

This package contains documentation for %oname.

%package -n %fname-pickles
Summary: Pickles for %oname
Group: Development/Python

%description -n %fname-pickles
%descr

This package contains pickles for %oname.
%else

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
%descr

This package contains tests for %oname.
%endif

%prep
%setup
%patch -p1
%if "-docs"!=""
%prepare_sphinx doc/sphinx
%endif

%build
%add_optflags -fno-strict-aliasing
%if "-docs"==""
%python_build
%else
%make -C doc/sphinx html
%endif

%install
%if "-docs"==""
%python_install
%else
mkdir -p %buildroot%python_sitelibdir/%oname
cp -fR doc/sphinx/.build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%if "-docs"==""
%files
%doc LICENSE PKG-INFO doc/default.css doc/docutils.css
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%else

%files
%doc doc/sphinx/.build/html

%files -n %fname-pickles
%python_sitelibdir/%oname/pickle
%endif

%changelog
* Fri Mar 23 2018 Grigory Ustinov <grenka@altlinux.org> 2.8.3-alt1
- Build new version.
- Tranfer package to subst-packaging system.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1
- Version 2.7.0

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.3-alt1
- Version 2.6.3

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
