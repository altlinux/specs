%define oname Products.ZCatalog

Name: python-module-%oname
Version: 3.0.3
Release: alt1.dev.git20140304
Summary: Zope 2's indexing and search solution
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ZCatalog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ZODB3

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.ZCTextIndex zope.dottedname zope.interface
%py_requires zope.schema zope.testing ZODB3

%description
The ZCatalog is Zope's built in search engine. It allows you to
categorize and search all kinds of Zope objects.

It comes with a variety of indexes for different types of data.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The ZCatalog is Zope's built in search engine. It allows you to
categorize and search all kinds of Zope objects.

It comes with a variety of indexes for different types of data.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
export PYTHONPATH=$PWD/src
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests
%exclude %python_sitelibdir/Products/*/*/tests*

%files tests
%python_sitelibdir/Products/*/tests
%python_sitelibdir/Products/*/*/tests*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1.dev.git20140304
- Version 3.0.3dev
- Enabled testing

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1
- Initial build for Sisyphus

