%define mname ps.zope
%define oname %mname.i18nfield

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.dev.git20141114
Summary: A zope.schema field for inline translations
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ps.zope.i18nfield/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/propertyshelf/ps.zope.i18nfield.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-ZODB3 python-module-z3c.indexer
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-z3c.form-tests
BuildPreReq: python-module-zc.buildout
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zodbpickle
BuildPreReq: python-module-plone.memoize
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-ZODB3 python3-module-z3c.indexer
BuildPreReq: python3-module-unittest2
BuildPreReq: python3-module-zope.globalrequest
BuildPreReq: python3-module-zope.i18n
BuildPreReq: python3-module-zope.interface
BuildPreReq: python3-module-zope.schema
BuildPreReq: python3-module-z3c.form-tests
BuildPreReq: python3-module-zc.buildout
BuildPreReq: python3-module-zope.browserpage
BuildPreReq: python3-module-zope.publisher
BuildPreReq: python3-module-zope.testing
BuildPreReq: python3-module-zope.traversing
BuildPreReq: python3-module-zope.i18nmessageid
BuildPreReq: python3-module-zope.component
BuildPreReq: python3-module-zope.security
BuildPreReq: python3-module-zodbpickle
BuildPreReq: python3-module-plone.memoize
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires ZODB3 z3c.indexer zope.globalrequest zope.i18n
%py_requires zope.interface zope.schema z3c.form zope.i18nmessageid
%py_requires zope.component zope.publisher zope.security plone.memoize

%description
This package provides a zope.schema based field which allows multiple
translations within the field. It uses a custom dictionary class for the
storage. There is also a widget available for the z3c.form library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires z3c.form.testing zope.browserpage
%py_requires zope.testing zope.traversing

%description tests
This package provides a zope.schema based field which allows multiple
translations within the field. It uses a custom dictionary class for the
storage. There is also a widget available for the z3c.form library.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A zope.schema field for inline translations
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires ZODB3 z3c.indexer zope.globalrequest zope.i18n
%py3_requires zope.interface zope.schema z3c.form zope.i18nmessageid
%py3_requires zope.component zope.publisher zope.security plone.memoize

%description -n python3-module-%oname
This package provides a zope.schema based field which allows multiple
translations within the field. It uses a custom dictionary class for the
storage. There is also a widget available for the z3c.form library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires z3c.form.testing zope.browserpage
%py3_requires zope.testing zope.traversing

%description -n python3-module-%oname-tests
This package provides a zope.schema based field which allows multiple
translations within the field. It uses a custom dictionary class for the
storage. There is also a widget available for the z3c.form library.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
Requires: python-module-ps = %EVR

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname
Requires: python3-module-ps = %EVR

%description -n python3-module-%mname
Core files of %mname.

%package -n python-module-ps
Summary: Core files of ps
Group: Development/Python
%py_provides ps

%description -n python-module-ps
Core files of ps.

%package -n python3-module-ps
Summary: Core files of ps
Group: Development/Python3
%py3_provides ps

%description -n python3-module-ps
Core files of ps.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/ps/__init__.py \
	%buildroot%python_sitelibdir/ps/
install -p -m644 src/ps/zope/__init__.py \
	%buildroot%python_sitelibdir/ps/zope/
%if_with python3
pushd ../python3
install -p -m644 src/ps/__init__.py \
	%buildroot%python3_sitelibdir/ps/
install -p -m644 src/ps/zope/__init__.py \
	%buildroot%python3_sitelibdir/ps/zope/
popd
%endif

%check
python setup.py test
rm -fR build
py.test
%if_with python3
pushd ../python3
python3 setup.py test
#rm -fR build
#py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/ps/zope/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/ps/zope/__init__.py*
%exclude %python_sitelibdir/ps/zope/*/tests

%files tests
%python_sitelibdir/ps/zope/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/ps/zope
%python_sitelibdir/ps/zope/__init__.py*

%files -n python-module-ps
%dir %python_sitelibdir/ps
%python_sitelibdir/ps/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/ps/zope/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/ps/zope/__init__.py
%exclude %python3_sitelibdir/ps/zope/__pycache__/__init__.*
%exclude %python3_sitelibdir/ps/zope/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/ps/zope/*/tests

%files -n python3-module-%mname
%dir %python3_sitelibdir/ps/zope
%dir %python3_sitelibdir/ps/zope/__pycache__
%python3_sitelibdir/ps/zope/__init__.py
%python3_sitelibdir/ps/zope/__pycache__/__init__.*

%files -n python3-module-ps
%dir %python3_sitelibdir/ps
%dir %python3_sitelibdir/ps/__pycache__
%python3_sitelibdir/ps/__init__.py
%python3_sitelibdir/ps/__pycache__/__init__.*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev.git20141114
- Initial build for Sisyphus

