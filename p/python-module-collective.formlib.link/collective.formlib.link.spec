%define mname collective.formlib
%define oname %mname.link
Name: python-module-%oname
Version: 0.2
Release: alt1
Summary: A link schema type representing an internal or external link
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.formlib.link/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.dublincore
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.app.form
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.BTreeFolder2

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires Products.CMFCore zope.i18nmessageid zope.dublincore
%py_requires zope.schema zope.interface zope.app.form zope.app.component
%py_requires zope.component

%description
This package provides a schema field that combines an internal and
external link representation. It's relatively low-tech.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.testing

%description tests
This package provides a schema field that combines an internal and
external link representation. It's relatively low-tech.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires collective

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 collective/formlib/__init__.py \
	%buildroot%python_sitelibdir/collective/formlib/

%check
export PYTHONPATH=$PWD
python setup.py test
python collective/formlib/link/tests.py

%files
%doc *.txt
%python_sitelibdir/collective/formlib/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/formlib/*/tests.*
%exclude %python_sitelibdir/collective/formlib/__init__.py*

%files tests
%python_sitelibdir/collective/formlib/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/collective/formlib
%python_sitelibdir/collective/formlib/__init__.py*

%changelog
* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

