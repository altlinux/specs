%define mname uwosh.pfg
%define oname %mname.d2c
Name: python-module-%oname
Version: 2.4.7
Release: alt1.git20141112
Summary: Content adapter for ploneformgen
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/uwosh.pfg.d2c/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/uwosh.pfg.d2c.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.PloneFormGen
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-Products.TALESField
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-unittest2 python-module-nose
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires Products.PloneFormGen archetypes.schemaextender
%py_requires Products.TALESField

%description
This product provides a dynamic content type to store PloneFormGen form
data into. It leverages schemaextenders ability to dynamically add extra
fields on a content type so that you essentially get a persistent copy
of your form.

The product adds a "Save Data to Content Adapter" item to the "Add
new.." drop down for the PloneFormGen Form. Once enabled, when a user
submits a form, a new content item is created with that data and located
in the adapter.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.component.testing zope.security.testing
%py_requires Products.PloneTestCase

%description tests
This product provides a dynamic content type to store PloneFormGen form
data into. It leverages schemaextenders ability to dynamically add extra
fields on a content type so that you essentially get a persistent copy
of your form.

The product adds a "Save Data to Content Adapter" item to the "Add
new.." drop down for the PloneFormGen Form. Once enabled, when a user
submits a form, a new content item is created with that data and located
in the adapter.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
Requires: python-module-uwosh = %EVR

%description -n python-module-%mname
Core files of %mname.

%package -n python-module-uwosh
Summary: Core files of uwosh
Group: Development/Python
%py_provides uwosh

%description -n python-module-uwosh
Core files of uwosh.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 uwosh/__init__.py \
	%buildroot%python_sitelibdir/uwosh/
install -p -m644 uwosh/pfg/__init__.py \
	%buildroot%python_sitelibdir/uwosh/pfg/

%check
python setup.py test
nosetests

%files
%doc *.txt *.rst docs/*
%python_sitelibdir/uwosh/pfg/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/uwosh/__init__.py*
%exclude %python_sitelibdir/uwosh/pfg/__init__.py*
%exclude %python_sitelibdir/uwosh/pfg/*/tests.*

%files tests
%python_sitelibdir/uwosh/pfg/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/uwosh/pfg
%python_sitelibdir/uwosh/pfg/__init__.py*

%files -n python-module-uwosh
%dir %python_sitelibdir/uwosh
%python_sitelibdir/uwosh/__init__.py*

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.7-alt1.git20141112
- Version 2.4.7

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.6-alt1.dev.git20140918
- Initial build for Sisyphus

