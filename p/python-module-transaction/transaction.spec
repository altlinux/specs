%define oname transaction

%def_with python3

Name: python-module-%oname
Version: 1.4.5
Release: alt1.dev0.git20150807.1.1
Summary: Transaction management for Python
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/transaction/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/transaction.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-repoze.sphinx.autointerface
#BuildPreReq: python-module-nose python-module-coverage
%py_requires zope.interface
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-repoze python-module-repoze.sphinx python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools python3-module-zope.interface
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-repoze.sphinx.autointerface python-module-setuptools-tests python3-module-coverage python3-module-nose python3-module-setuptools-tests python3-module-zope rpm-build-python3 time

#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python3-module-zope.interface
%endif

%description
This package contains a generic transaction implementation for Python.
It is mainly used by the ZODB, though.

Note that the data manager API, transaction.interfaces.IDataManager, is
syntactically simple, but semantically complex. The semantics were not
easy to express in the interface. This could probably use more work. The
semantics are presented in detail through examples of a sample data
manager in transaction.tests.test_SampleDataManager.

%if_with python3
%package -n python3-module-%oname
Summary: Transaction management for Python 3
Group: Development/Python3
%py3_requires zope.interface

%description -n python3-module-%oname
This package contains a generic transaction implementation for Python 3.
It is mainly used by the ZODB, though.

Note that the data manager API, transaction.interfaces.IDataManager, is
syntactically simple, but semantically complex. The semantics were not
easy to express in the interface. This could probably use more work. The
semantics are presented in detail through examples of a sample data
manager in transaction.tests.test_SampleDataManager.

%package -n python3-module-%oname-tests
Summary: Tests for Transaction management for Python 3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package contains a generic transaction implementation for Python 3.
It is mainly used by the ZODB, though.

Note that the data manager API, transaction.interfaces.IDataManager, is
syntactically simple, but semantically complex. The semantics were not
easy to express in the interface. This could probably use more work. The
semantics are presented in detail through examples of a sample data
manager in transaction.tests.test_SampleDataManager.

This package contains tests for Transaction management for Python 3.
%endif

%package tests
Summary: Tests for Transaction management for Python
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package contains a generic transaction implementation for Python.
It is mainly used by the ZODB, though.

Note that the data manager API, transaction.interfaces.IDataManager, is
syntactically simple, but semantically complex. The semantics were not
easy to express in the interface. This could probably use more work. The
semantics are presented in detail through examples of a sample data
manager in transaction.tests.test_SampleDataManager.

This package contains tests for Transaction management for Python.

%package pickles
Summary: Pickles for Transaction management for Python
Group: Development/Python

%description pickles
This package contains a generic transaction implementation for Python.
It is mainly used by the ZODB, though.

Note that the data manager API, transaction.interfaces.IDataManager, is
syntactically simple, but semantically complex. The semantics were not
easy to express in the interface. This could probably use more work. The
semantics are presented in detail through examples of a sample data
manager in transaction.tests.test_SampleDataManager.

This package contains pickles for Transaction management for Python.

%package docs
Summary: Documentation for Transaction management for Python
Group: Development/Documentation

%description docs
This package contains a generic transaction implementation for Python.
It is mainly used by the ZODB, though.

Note that the data manager API, transaction.interfaces.IDataManager, is
syntactically simple, but semantically complex. The semantics were not
easy to express in the interface. This could probably use more work. The
semantics are presented in detail through examples of a sample data
manager in transaction.tests.test_SampleDataManager.

This package contains documentation for Transaction management for
Python.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/%oname/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.5-alt1.dev0.git20150807.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.5-alt1.dev0.git20150807.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.5-alt1.dev0.git20150807
- Version 1.4.5.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.dev.git20140404
- Version 1.4.4dev
- Enables testing

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1
- Version 1.4.3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Version 1.4.1

* Sat Mar 23 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2.0-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Added module for Python 3

* Thu Dec 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

