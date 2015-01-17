%define mname quintagroup
%define oname %mname.megamenu
Name: python-module-%oname
Version: 1.5
Release: alt1.git20150116
Summary: Mega menu for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/quintagroup.megamenu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/quintagroup/quintagroup.megamenu.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.panels
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-plone.app.layout

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.panels plone.app.layout zope.interface

%description
Clean and professional fully responsive Mega Menu solution for Plone.
This product allows Plone website to display panel added to portal top
as drop-down menu for navigation tabs.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Clean and professional fully responsive Mega Menu solution for Plone.
This product allows Plone website to display panel added to portal top
as drop-down menu for navigation tabs.

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

pushd %mname/megamenu
cp -fR *.zcml locales profiles \
	%buildroot%python_sitelibdir/%mname/megamenu/
pushd browser
cp -fR *.zcml *.css resources templates \
	%buildroot%python_sitelibdir/%mname/megamenu/browser/
popd
popd

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20150116
- Initial build for Sisyphus

