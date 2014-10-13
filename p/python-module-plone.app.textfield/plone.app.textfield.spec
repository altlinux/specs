%define oname plone.app.textfield
Name: python-module-%oname
Version: 1.2.4
Release: alt1.dev0.git20140925
Summary: Text field with MIME type support
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.textfield/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.textfield.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-plone.supermodel-tests
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-plone.schemaeditor
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
%py_requires plone.app ZODB3 zope.schema zope.interface zope.component
%py_requires Products.PortalTransforms plone.supermodel z3c.form
%py_requires plone.rfc822 plone.schemaeditor

%description
This package provides a zope.schema style field type called RichText
which can be used to store a value with a related MIME type. The value
can be transformed to an output MIME type, for example to transform from
structured text to HTML.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing
Requires: python-module-plone.supermodel-tests

%description tests
This package provides a zope.schema style field type called RichText
which can be used to store a value with a related MIME type. The value
can be transformed to an output MIME type, for example to transform from
structured text to HTML.

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

%files
%doc *.rst docs/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/tests.*

%files tests
%python_sitelibdir/plone/app/*/tests.*

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.dev0.git20140925
- Initial build for Sisyphus

