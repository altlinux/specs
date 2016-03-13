%define oname peewee

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.6.0
Release: alt2.git20150421.1.1
Summary: A small, expressive orm -- supports postgresql, mysql and sqlite
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/peewee/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/coleifer/peewee.git
Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest python-modules-sqlite3 python3-module-pytest python3-modules-sqlite3 rpm-build-python3 time

#BuildRequires: python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest python-modules-sqlite3

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-modules-sqlite3
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-modules-sqlite3
#BuildRequires: python3-module-pytest python3-modules-sqlite3
%endif

%py_provides %oname
#%py_requires sqlite3

%description
Peewee is a simple and small ORM. It has few (but expressive) concepts,
making it easy to learn and intuitive to use.

* A small, expressive ORM
* Written in python with support for versions 2.6+ and 3.2+.
* built-in support for sqlite, mysql and postgresql
* tons of extensions available in the playhouse
  (postgres hstore/json/arrays, sqlite full-text-search, schema
  migrations, and much more).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Peewee is a simple and small ORM. It has few (but expressive) concepts,
making it easy to learn and intuitive to use.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A small, expressive orm -- supports postgresql, mysql and sqlite
Group: Development/Python3
%py3_provides %oname
#%py3_requires sqlite3 pysqlcipher3
%add_python3_req_skip pysqlcipher

%description -n python3-module-%oname
Peewee is a simple and small ORM. It has few (but expressive) concepts,
making it easy to learn and intuitive to use.

* A small, expressive ORM
* Written in python with support for versions 2.6+ and 3.2+.
* built-in support for sqlite, mysql and postgresql
* tons of extensions available in the playhouse
  (postgres hstore/json/arrays, sqlite full-text-search, schema
  migrations, and much more).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Peewee is a simple and small ORM. It has few (but expressive) concepts,
making it easy to learn and intuitive to use.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Peewee is a simple and small ORM. It has few (but expressive) concepts,
making it easy to learn and intuitive to use.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Peewee is a simple and small ORM. It has few (but expressive) concepts,
making it easy to learn and intuitive to use.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_install

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
python runtests.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py
popd
%endif

%files
%doc *.md *.rst examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst ../python3/examples
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/berkeley_build.sh
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.0-alt2.git20150421.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt2.git20150421.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 2.6.0-alt2.git20150421
- Rebuild with "def_disable check"
- Cleanup buildreq

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.git20150421
- Version 2.6.0

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.7-alt1.git20150212
- Version 2.4.7

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt1.git20150108
- New snapshot
- Added module for Python 3

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt1.git20141231
- Initial build for Sisyphus

