%define oname Products.FiveSite
Name: python-module-%oname
Version: 1.0
Release: alt1
Summary: FiveSite utility for EEA
License: GPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/products.fivesite/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.app.component

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore zope.app.component

%description
This is a small product that makes sure that the Plone Site provides
ISite and that getSite() works.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

