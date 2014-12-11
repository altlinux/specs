%define mname plonehrm
%define oname %mname.personaldata
Name: python-module-%oname
Version: 2.0.2
Release: alt2.dev.svn20091125
Summary: Personal data for Plone HRM
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plonehrm.personaldata/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/plonehrm.personaldata/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-collective.autopermission
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.plonehrm

%py_provides %oname
%py_requires %mname collective.autopermission Products.CMFCore
%py_requires Products.Archetypes zope.interface zope.i18nmessageid
%py_requires Products.plonehrm

%description
This package adds extended personal data for Employees in Plone HRM. For
more info see the Products.plonehrm package.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

pushd %mname/personaldata
cp -fR ChangeLog *.txt *.zcml profiles \
	%buildroot%python_sitelibdir/%mname/personaldata/
popd

%check
python setup.py test

%files
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt2.dev.svn20091125
- Added necessary requirements

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.dev.svn20091125
- Initial build for Sisyphus

