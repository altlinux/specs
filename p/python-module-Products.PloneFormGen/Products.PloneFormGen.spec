%define oname Products.PloneFormGen
Name: python-module-%oname
Version: 1.7.17
Release: alt1.dev0.git20140926
Summary: A through-the-web form generator for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PloneFormGen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/smcmahon/Products.PloneFormGen.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.TALESField
BuildPreReq: python-module-Products.TemplateFields
BuildPreReq: python-module-Products.PythonField
BuildPreReq: python-module-plone.app.jquerytools
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-collective.funkload
BuildPreReq: python-module-unittest2

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.Archetypes Products.CMFPlone Products.TALESField
%py_requires Products.TemplateFields Products.PythonField
%py_requires plone.app.jquerytools collective.js.jqueryui

%description
This package provides a generic Plone form generator. Use it to build
simple, one-of-a-kind, web forms that save or mail form input.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase collective.funkload

%description tests
This package provides a generic Plone form generator. Use it to build
simple, one-of-a-kind, web forms that save or mail form input.

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
python setup.py test
rm -fR build
py.test

%files
%doc *.txt *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests
%exclude %python_sitelibdir/Products/*/*/loadtest

%files tests
%python_sitelibdir/Products/*/tests
%python_sitelibdir/Products/*/*/loadtest

%changelog
* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.17-alt1.dev0.git20140926
- Initial build for Sisyphus

