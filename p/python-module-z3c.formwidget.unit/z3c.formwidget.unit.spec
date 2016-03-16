%define mname z3c.formwidget
%define oname %mname.unit

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3
Release: alt2.dev.git20141114.1
Summary: A multi unit widget for z3c.form
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/z3c.formwidget.unit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tmassman/z3c.formwidget.unit.git
Source: %name-%version.tar
BuildRequires: python-module-js.bootstrap_select python-module-nose python-module-pint python-module-pytest python-module-z3c.coverage python-module-z3c.form python-module-z3c.template python-module-zc.recipe.egg python-module-zc.sourcefactory python-module-zope.app.testing python-module-zope.testrunner

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-js.bootstrap_select python-module-pint
#BuildPreReq: python-module-unittest2 python-module-zc.buildout
#BuildPreReq: python-module-zope.browserpage python-module-nose
#BuildPreReq: python-module-zope.publisher
#BuildPreReq: python-module-zope.testing
#BuildPreReq: python-module-zope.traversing-tests
#BuildPreReq: python-module-z3c.form-tests
#BuildPreReq: python-module-zope.i18nmessageid
#BuildPreReq: python-module-zope.annotation
#BuildPreReq: python-module-zope.component-tests
#BuildPreReq: python-module-zope.i18n
#BuildPreReq: python-module-zope.security
#BuildPreReq: python-module-zope.interface
#BuildPreReq: python-module-zope.schema
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-js.bootstrap_select python3-module-nose python3-module-pint python3-module-pytest python3-module-sphinx python3-module-z3c.coverage python3-module-z3c.form python3-module-z3c.template python3-module-zc.recipe.egg python3-module-zc.sourcefactory python3-module-zope.app.testing python3-module-zope.testrunner
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-js.bootstrap_select python3-module-pint
#BuildPreReq: python3-module-unittest2 python3-module-zc.buildout
#BuildPreReq: python3-module-zope.browserpage python3-module-nose
#BuildPreReq: python3-module-zope.publisher
#BuildPreReq: python3-module-zope.testing
#BuildPreReq: python3-module-zope.traversing-tests
#BuildPreReq: python3-module-z3c.form-tests
#BuildPreReq: python3-module-zope.i18nmessageid
#BuildPreReq: python3-module-zope.annotation
#BuildPreReq: python3-module-zope.component-tests
#BuildPreReq: python3-module-zope.i18n
#BuildPreReq: python3-module-zope.security
#BuildPreReq: python3-module-zope.interface
#BuildPreReq: python3-module-zope.schema
%endif

%py_provides %oname
#%py_requires %mname js.bootstrap_select z3c.form zope.i18nmessageid
#%py_requires zope.annotation zope.component zope.i18n zope.security
#%py_requires zope.interface zope.schema

%description
This package provides a unit widget for the z3c.form library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#%py_requires zope.browserpage zope.publisher zope.testing
#%py_requires zope.traversing.testing z3c.form.testing
#%py_requires zope.component.testing

%description tests
This package provides a unit widget for the z3c.form library.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A multi unit widget for z3c.form
Group: Development/Python3
%py3_provides %oname
#%py3_requires %mname js.bootstrap_select z3c.form zope.i18nmessageid
#%py3_requires zope.annotation zope.component zope.i18n zope.security
#%py3_requires zope.interface zope.schema

%description -n python3-module-%oname
This package provides a unit widget for the z3c.form library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
#%py3_requires zope.browserpage zope.publisher zope.testing
#%py3_requires zope.traversing.testing z3c.form.testing
#%py3_requires zope.component.testing

%description -n python3-module-%oname-tests
This package provides a unit widget for the z3c.form library.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
#nosetests3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/z3c/formwidget/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/z3c/formwidget/*/tests.*

%files tests
%python_sitelibdir/z3c/formwidget/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/z3c/formwidget/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/z3c/formwidget/*/tests.*
%exclude %python3_sitelibdir/z3c/formwidget/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/z3c/formwidget/*/tests.*
%python3_sitelibdir/z3c/formwidget/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt2.dev.git20141114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.3-alt2.dev.git20141114
- Rebuild with "def_disable check"
- Cleanup buildreq

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev.git20141114
- Initial build for Sisyphus

