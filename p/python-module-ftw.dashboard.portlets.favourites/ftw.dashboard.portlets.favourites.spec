%define m1name dashboard
%define m2name portlets
%define mname ftw.%m1name.%m2name
%define oname %mname.favourites
Name: python-module-%oname
Version: 3.2.1
Release: alt1.dev0.git20141216
Summary: A favourite Portlet, which shows your favourites on the dashboard
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.dashboard.portlets.favourites/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.dashboard.portlets.favourites.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-argparse
BuildPreReq: python-module-ftw.dashboard.dragndrop
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires ftw.dashboard.dragndrop ftw.upgrade Products.CMFCore
%py_requires Products.statusmessages plone.app.portlets plone.i18n
%py_requires plone.registry plone.portlets plone.memoize zope.component
%py_requires zope.interface zope.i18nmessageid

%description
ftw.dashboard.portlets.favourites provides a favorites portlet for your
dashboard.

The favorite portlet shows links for all your favorites in your Home
Folder. In the edit mode you have also the possibility to remove a
single favorite. Additionaly it implements the site action "add to
favorites", which add a current section to your favorites Folder.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing ftw.testing zope.configuration

%description tests
ftw.dashboard.portlets.favourites provides a favorites portlet for your
dashboard.

The favorite portlet shows links for all your favorites in your Home
Folder. In the edit mode you have also the possibility to remove a
single favorite. Additionaly it implements the site action "add to
favorites", which add a current section to your favorites Folder.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires ftw.%m1name

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

install -p -m644 ftw/%m1name/%m2name/__init__.py \
	%buildroot%python_sitelibdir/ftw/%m1name/%m2name/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/ftw/%m1name/%m2name/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/ftw/%m1name/%m2name/*/test*
%exclude %python_sitelibdir/ftw/%m1name/%m2name/__init__.py*

%files tests
%python_sitelibdir/ftw/%m1name/%m2name/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/ftw/%m1name/%m2name
%python_sitelibdir/ftw/%m1name/%m2name/__init__.py*

%changelog
* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.dev0.git20141216
- Initial build for Sisyphus

