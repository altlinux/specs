%define mname plonehrm
%define oname %mname.notifications
Name: python-module-%oname
Version: 1.2
Release: alt1
Summary: Notifications for Plone HRM
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/plonehrm.notifications/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.testing
#BuildPreReq: python-module-Products.plonehrm

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires Products.CMFPlone Products.CMFCore zope.component zope.i18n
%py_requires zope.interface zope.annotation zope.event
#py_requires Products.plonehrm

%description
Base package for adding notifications in Plone HRM. For example you can
send an email when a contract nears its ending. Or you can add a note to
an Employee when his birthday draws near. For more info see the
Products.plonehrm package.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
Base package for adding notifications in Plone HRM. For example you can
send an email when a contract nears its ending. Or you can add a note to
an Employee when his birthday draws near. For more info see the
Products.plonehrm package.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

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

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test
rm -fR build
py.test

%files
%doc PKG-INFO docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

