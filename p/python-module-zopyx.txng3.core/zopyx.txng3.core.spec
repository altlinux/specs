%define mname zopyx.txng3
%define oname %mname.core

%def_disable check

Name: python-module-%oname
Version: 3.6.1.1
Release: alt1.git20141102
Summary: TextIndexNG3 core implementation
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zopyx.txng3.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopyx/zopyx.txng3.core.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-nose python-module-zope.testing
BuildPreReq: python-module-zope.componentvocabulary
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.app.catalog
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-grok
#BuildPreReq: python-module-zopyx.txng3.ext

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires ZODB3 zope.component zope.componentvocabulary zope.schema
%py_requires zope.interface Products.ZCatalog zope.i18nmessageid
%py_requires zope.app.catalog grok
#py_requires zopyx.txng3.ext

%description
TextIndexNG3 core implementation.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.component.testing

%description tests
TextIndexNG3 core implementation.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
Requires: python-module-zopyx = %EVR

%description -n python-module-%mname
Core files of %mname.

%package -n python-module-zopyx
Summary: Core files of zopyx
Group: Development/Python
%py_provides zopyx

%description -n python-module-zopyx
Core files of zopyx.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

pushd zopyx/txng3/core
cp -fR converters data interfaces parsers src tests \
	%buildroot%python_sitelibdir/zopyx/txng3/core/
popd

install -p -m644 zopyx/__init__.py \
	%buildroot%python_sitelibdir/zopyx/
install -p -m644 zopyx/txng3/__init__.py \
	%buildroot%python_sitelibdir/zopyx/txng3/

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/zopyx/txng3/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/zopyx/txng3/*/tests
%exclude %python_sitelibdir/zopyx/txng3/*/*/tests
%exclude %python_sitelibdir/zopyx/txng3/__init__.py*

%files tests
%python_sitelibdir/zopyx/txng3/*/tests
%python_sitelibdir/zopyx/txng3/*/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/zopyx/txng3
%python_sitelibdir/zopyx/txng3/__init__.py*

%files -n python-module-zopyx
%dir %python_sitelibdir/zopyx
%python_sitelibdir/zopyx/__init__.py*

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1.1-alt1.git20141102
- Initial build for Sisyphus

