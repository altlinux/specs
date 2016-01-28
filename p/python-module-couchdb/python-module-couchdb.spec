%define sname couchdb

%def_with python3
%def_disable check

Summary: Python library for working with CouchDB. 
Name: python-module-%sname
Version: 1.0.1
Release: alt1.git20141116.1
# https://github.com/djc/couchdb-python.git
Source0: %name-%version.tar
License: BSD
Group: Development/Python
URL: http://code.google.com/p/couchdb-python/
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest python3-module-pytest rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools-tests
#BuildPreReq: python-module-sphinx-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

%add_findreq_skiplist %python_sitelibdir/%sname/util3.py

%description
A Python library for CouchDB. It provides a convenient high level
interface for the CouchDB server.

%package tests
Summary: Tests for %sname
Group: Development/Python
Requires: %name = %EVR

%description tests
A Python library for CouchDB. It provides a convenient high level
interface for the CouchDB server.

This package contains tests for %sname.

%package -n python3-module-%sname
Summary: Python library for working with CouchDB
Group: Development/Python3
%add_findreq_skiplist %python3_sitelibdir/%sname/util2.py

%description -n python3-module-%sname
A Python library for CouchDB. It provides a convenient high level
interface for the CouchDB server.

%package -n python3-module-%sname-tests
Summary: Tests for %sname
Group: Development/Python3
Requires: python3-module-%sname = %EVR

%description -n python3-module-%sname-tests
A Python library for CouchDB. It provides a convenient high level
interface for the CouchDB server.

This package contains tests for %sname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv doc/

%if_with python3
cp -fR . ../python3
#for i in $(find ../python3 -type f -name '*.py'); do
#	2to3 -w -n $i ||:
#done
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%make -C doc html

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst doc/build/html
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%sname
%doc *.rst doc/build/html
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%sname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.git20141116.1
- NMU: Use buildreq for BR.

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20141116
- Version 1.0.1
- Extracted tests into separate packages

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt2.hg20140707
- Added module for Python 3

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.hg20140707
- New snapshot

* Thu Dec 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1
- Version 0.10

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.1
- Rebuild with Python-2.7

* Wed Dec 01 2010 Mikhail Pokidko <pma@altlinux.org> 0.8-alt1
- v0.8

* Fri Jul 16 2010 Mikhail Pokidko <pma@altlinux.org> 0.7-alt1
- v0.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.1
- Rebuilt with python 2.6

* Mon Oct 12 2009 Mikhail Pokidko <pma@altlinux.org> 0.6-alt1
- Initial ALT build



